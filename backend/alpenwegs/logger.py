# Python import:
import logging
import uuid

# AlpenWegs application process ID:
process_id = str(uuid.uuid4())

# Initialize AlpenWegs API logger:
api_logger = logger = logging.getLogger('AlpenWeg API')
app_logger = logger = logging.getLogger('AlpenWeg APP')
