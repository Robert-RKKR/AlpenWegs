# Python import:
import logging
import uuid

# AlpenWegs application process ID:
process_id = str(uuid.uuid4())

# Initialize AlpenWegs API logger:
test_logger = logger = logging.getLogger('AlpenWeg Test')
api_logger = logger = logging.getLogger('AlpenWeg API')
app_logger = logger = logging.getLogger('AlpenWeg APP')
