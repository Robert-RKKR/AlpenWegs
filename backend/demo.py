import json
import requests
from pathlib import Path
from typing import Dict, List

# ==========================================================
# Configuration
# ==========================================================
BASE_URL = "http://5.180.148.151:8000/api"

LOGIN_ENDPOINT = f"{BASE_URL}/auth/login/"
REGION_ENDPOINT = f"{BASE_URL}/compendiums/region/"

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
# Main execution
# ==========================================================
def main() -> None:
    if not DATA_FILE.exists():
        raise FileNotFoundError("demo_data.json not found")

    with DATA_FILE.open(encoding="utf-8") as f:
        demo_data = json.load(f)

    access_token = login(CREDENTIALS)

    # ---- Regions ----
    if "objects" in demo_data:
        post_objects(
            endpoint=REGION_ENDPOINT,
            objects=demo_data["objects"],
            access_token=access_token,
        )

    print("✔ Seeding completed")


if __name__ == "__main__":
    main()
