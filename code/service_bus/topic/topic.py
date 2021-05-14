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

CONNSTR = ""
TOPIC_NAME = "svcbustopic"
SUBSCRIPTION_1 = "sbcbustopicsub1"
SUBSCRIPTION_2 = "sbcbustopicsub2"

MESSAGE = "Hello azure!"

def send_single_message(servicebus_client):
    sender = servicebus_client.get_topic_sender(TOPIC_NAME)
    message = ServiceBusMessage(MESSAGE)
    with sender:
        sender.send_messages(message)
    print("single message has been sent!")

def receive_messages(servicebus_client):
     receiver = servicebus_client.get_subscription_receiver(TOPIC_NAME, SUBSCRIPTION_1)
     with receiver:
        for msg in receiver.receive_messages(max_message_count=10):
            receiver.complete_message(msg)
            assert str(msg.message) == MESSAGE
            print("received message: {}".format(msg.message))


with ServiceBusClient.from_connection_string(CONNSTR) as client:
    send_single_message(client)
    receive_messages(client)
        
        
