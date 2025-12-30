import json
import requests
from pathlib import Path
from typing import Dict, List

# ==========================================================
# Configuration
# ==========================================================
BASE_URL = "http://5.180.148.151:8000/api"

LOGIN_ENDPOINT = f"{BASE_URL}/auth/login/"

CREDENTIALS = {
    "email": "admin@alpenwegs.com",
    "password": "sfsefsef3434@!$2",
}

DATA_FILE = Path("demo_data.json")


# ==========================================================
# Core helpers
# ==========================================================
def login(credentials: Dict[str, str]) -> str:
    """Authenticate and return JWT access token."""
    response = requests.post(
        LOGIN_ENDPOINT,
        json=credentials,
        headers={"Content-Type": "application/json"},
        timeout=15,
    )
    response.raise_for_status()

    data = response.json()
    return data["page_results"]["access"]


def post_objects(
    endpoint: str,
    objects: List[Dict],
    access_token: str,
) -> None:
    """Create multiple objects using POST."""
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    for obj in objects:
        resp = requests.post(endpoint, json=obj, headers=headers, timeout=15)
        if resp.ok:
            print(f"✔ Created: {obj.get('name', 'object')}")
        else:
            print(f"✖ Failed: {obj.get('name', 'object')}")
            print(resp.status_code, resp.text)


# ==========================================================
# Files helpers
# ==========================================================
def upload_files(
    endpoint: str,
    base_dir: Path,
    access_token: str,
    *,
    format_value: str = "gpx",
) -> None:
    """
    Upload all files from base_dir recursively using multipart/form-data.
    """

    if not base_dir.exists():
        raise FileNotFoundError(f"Directory not found: {base_dir}")

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    files_found = list(base_dir.rglob("*"))
    files_found = [f for f in files_found if f.is_file()]

    if not files_found:
        print("⚠ No files found to upload")
        return

    for file_path in files_found:
        with file_path.open("rb") as f:
            multipart_data = {
                "path": (file_path.name, f),
            }

            form_data = {
                "name": file_path.stem,
                "snippet": f"Auto-imported file {file_path.name}.",
                "format": format_value,
            }

            response = requests.post(
                endpoint,
                headers=headers,
                data=form_data,
                files=multipart_data,
                timeout=30,
            )

        if response.ok:
            print(f"✔ Uploaded file: {file_path.name}")
        else:
            print(f"✖ Upload failed: {file_path.name}")
            print(response.status_code, response.text)


# ==========================================================
# Main execution
# ==========================================================
def main() -> None:
    if not DATA_FILE.exists():
        raise FileNotFoundError("demo_data.json not found")

    with DATA_FILE.open(encoding="utf-8") as f:
        demo_data = json.load(f)

    access_token = login(CREDENTIALS)

    # ---- GPX Files ----
    # upload_files(
    #     endpoint=f"{BASE_URL}/assets/photo/",
    #     base_dir=Path("media/dev/photos"),
    #     access_token=access_token,
    #     format_value="jpg",
    # )

    # # ---- Regions ----
    if "objects" in demo_data:
        post_objects(
            endpoint=f"{BASE_URL}/explorers/track/",
            objects=demo_data["objects"],
            access_token=access_token,
        )

    print("✔ Seeding completed")


if __name__ == "__main__":
    main()
