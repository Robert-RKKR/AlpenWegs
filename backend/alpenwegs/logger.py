# AlpenWegs application import:
from notification.ashared import Logger

# Python import:
import uuid

# AlpenWegs application process ID:
process_id = str(uuid.uuid4())

# Initialize AlpenWegs API logger:
api_logger = Logger('AlpenWeg API', process_id)
