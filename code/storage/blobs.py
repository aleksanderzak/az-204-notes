#!/usr/bin/env python
"""
Example to demonstrate how to upload blob.

You need to set connection string in AZURE_STORAGE_CONNECTION string 
environment variable. You can do so by exectuing below command:

```
AZURE_STORAGE_CONNECTION_STRING=$(az storage account show-connection-string \
    --name namesa \
    --resource-group rgsa \
)
```

"""


import os
from azure.core.exceptions import ResourceExistsError
from azure.storage.blob import BlobServiceClient

CONTAINER_NAME = "photos"

def create_blob_service_client():
    conn_str = os.getenv("AZURE_CLIENT_CONNECTION_STRING")
    return BlobServiceClient.from_connection_string(conn_str)

blob_service_client = create_blob_service_client()
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

try:
    container_client.create_container()
except ResourceExistsError:
    pass

with open("provision.sh", "rb") as data:
    container_client.upload_blob(name="image", data=data, overwrite=True)

for b in container_client.walk_blobs():
    print(b.name + ", last modified: " + str(b.last_modified))

