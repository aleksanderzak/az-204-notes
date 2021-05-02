#!/usr/bin/env python

"""
Example to show sending and receiving a message from Azure Service Bus Queue.

You can get connection string using az cli:
```
az servicebus namespace authorization-rule keys list \
    --resource-group servicebusrg \
    --name RootManageSharedAccessKey \
    --query primaryConnectionString \
    --output tsv \
    --namespace-name svcbusns
```

"""

from azure.servicebus import ServiceBusClient, ServiceBusMessage

CONNSTR = "Endpoint=sb://svcbusns.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=LOj0a+3oQvCbZPX+twC69qMQ9YlAKLcrERapzgsf36c="
QUEUE_NAME = "svcbusq"
MESSAGE = "Hello azure!"

def send_single_message(client):
    sender = client.get_queue_sender(QUEUE_NAME)
    message = ServiceBusMessage(MESSAGE)
    with sender:
        sender.send_messages(message)
    print("single message has been sent!")

def receive_messages(client):
    receiver = client.get_queue_receiver(QUEUE_NAME)
    with receiver:
        for msg in receiver.receive_messages(max_message_count=10):
            receiver.complete_message(msg)
            assert str(msg.message) == MESSAGE
            print("received message: {}".format(msg.message))


with ServiceBusClient.from_connection_string(CONNSTR) as client:
    send_single_message(client)
    receive_messages(client)
        
        
