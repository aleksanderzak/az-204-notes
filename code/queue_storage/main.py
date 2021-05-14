#!/usr/bin/env python
"""
Example to show sending and receiving a message from Azure Queue storage.

You need to set connection string in AZURE_STORAGE_CONNECTION string 
environment variable. You can do so by exectuing below command:

```
AZURE_STORAGE_CONNECTION_STRING=$(az storage account show-connection-string \
    --name queuestoragesa \
    --resource-group queuestoragerg \
)
```

"""

from azure.storage.queue import QueueClient
from azure.core.exceptions import ResourceExistsError

import os, uuid

def create_client_with_connection_string_from_env(qname):
    connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    return QueueClient.from_connection_string(connect_str, qname)

def send_message(client, msg):
    create_queue_if_not_exists(client)
    

def create_queue_if_not_exists(client):
    try:
        client.create_queue()
        print("Create a new queue: " + client.queue_name)
    except ResourceExistsError:
        pass


qname = "myqueue"
msg = "Hi there!"
client = create_client_with_connection_string_from_env(qname)
send_message(client, msg)