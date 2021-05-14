# Why use queues?

A queue increases resiliency by temporarily storing waiting messages. At times
of low or normal demand, the size of the queue remains small because the
destination component removes messages from the queue faster than they are
added. At times of high demand, the queue may increase in size, but messages are
not lost. The destination component can catch up and empty the queue as demand
returns to normal.

# Events vs messages


**Message** 

* raw data, produced by one component and conusmed by another component
* contains data, not reference
* sending component expects data to be processed in a certain way
* likely to be used when distributed app requires a guarantee that the
  communication will be processed
* the sender and receiver of a message are often coupled by a strict data
  contract

**Events**

* most often broadcast communications, may be sent to multiple receivers, or
  none at all
* publishers and subscribers
* lightweight notification
* often ephemeral, might not be handled


# **Azure Queue Storage**

Queue storage is a service that uses Azure Storage to store large numbers of
messages that can be securely accessed from anywhere in the world using a simple
REST-based interface. Queues can contain millions of messages, limited only by
the capacity of the storage account that owns it. Simpler than Azure Service
bus, supports queues bigger than 80GB (unlimited queue size). Maintains a log of
all messages.Use when you need an audit trail of all messages that pass through
the queue. If your requiremenrs are simple and you want to wrtie code as quickly
as possible, a storage queue may the best option. Otherwise, Service Bus queues
provide many more options and flexibility. 

- A single queue can be up to 500 TB in size, so it can potentially store
  millions of messages. 
- The target throughput for a single queue is 2000 messages per second
- message must be smaller than 64KB

Use Azure Queue Storage:
1. Create a storage account - contains all of your Azure Storage data objects: blobs, files, queues, tables and disks. It provides a unique namespace for your Azure Storage data accessible from anywhere in the world over HTTP. For queues it must be Azure general-purpose storage account, can't be blob storage acc.
2. Create a storage queue.
3. 

Access authorization:
- azure active directory
- shared key == account key, Every storage account has two of these keys that
  can be passed with each request to authenticate access. Using this approach is
  like using a root password - it provides full access to the storage account
- shared access signature - A shared access signature (SAS) is a generated URI
  that grants limited access to objects in your storage account to clients. You
  can restrict access to specific resources, permissions, and scope to a data
  range to automatically turn off access after a period of time.

Accessing queues:
- REST API: http://<storage account>.queue.core.windows.net/<queue name>. An
  Authorization header must be included with every request. The value can be any
  of the three authorization styles.

After the receiver gets a message, that message remains in the queue but is
invisible for 30 seconds. If the receiver crashes or experiences a power failure
during processing, then it will never delete the message from the queue. After
30 seconds, the message will reappear in the queue and another instance of the
receiver can process it to completion (receiver must call DELETE).

a common pattern for queue creation: the sender application should always be
responsible for creating the queue. This keeps your application more
self-contained and less dependent on administrative set-up.

# **Azure Service Bus**

Service Bus is a message broker system intended for enterprise applications.
These apps often utilize multiple communication protocols, have different data
contracts, higher security requirements, and can include both cloud and
on-premises services. Service Bus is built on top of a dedicated messaging
infrastructure designed for exactly these scenarios. Supports RBAC,
transactions, but queues can be no bigger than 80GB.

- supports larger message sizes sizes of 256KB (standard tier) or 1MB (premium
  tier)
- supports at-most-once and at-least-once delivery
- FIFO guarantees
- can group multiple messages into a transaction
- RBAC
- does not require destionation components to continously poll the queue

Service bus queues and topics are excellent tools that you can use to increase
the resilience of communications within a distributed application.

*topic* - like queue, but can have multiple subscribers. Internally, topics use
queues. When you post to a topic, the message is copied and dropped into the
queue for each subscription. 

*increased reliability* - Queues increase the reliability of the message
exchange because, at times of high demand, messages can simply wait until a
destination component is ready to process them.

*relay* - an object that performs synchronous, two-way communication between
applications. Unlike queues and topics, it is not a temporary storage location
for messages. Instead, it provides bidirectional, unbuffered connections across
network boundaries such as firewalls. Use a relay when you want direct
communications between components as if they were located on the same network
segment but separated by network security devices.

* At-Least-Once Delivery
* At-Most-Once Delivery 
* First-In-First-Out (FIFO) 

Use Azure Service Bus:
1. Create a Service Bus namespace - container with a unique fully qualified domain name, for queues, topics, and relays.
2. Create a queue
3. Create a topic and a subscription
4. Use sdk for coding

# **Azure Event Grid**

Azure Event Grid is a fully-managed event routing service running on top of
Azure Service Fabric. Event Grid distributes events from different sources, such
as Azure Blob storage accounts or Azure Media Services, to different handlers,
such as Azure Functions or Webhooks. Event Grid was created to make it easier to
build event-based and serverless applications on Azure. Knative Eventing, Argo
Events equivalent.

Use Event Grid when you need these features:

* Simplicity: It is straightforward to connect sources to subscribers in Event
  Grid.
* Advanced filtering: Subscriptions have close control over the events they
  receive from a topic.
* Fan-out: You can subscribe to an unlimited number of endpoints to the same
  events and topics.
* Reliability: Event Grid retries event delivery for up to 24 hours for each
  subscription.
* Pay-per-event: Pay only for the number of events that you transmit.


# **Azure Event Hub**

Event Hubs is an intermediary for the publish-subscribe communication pattern.
Unlike Event Grid, however, it is optimized for extremely high throughput, a
large number of publishers, security, and resiliency. Kafka equivalent. Similar
to kafka concept of partitions. Most often used for a specific type of high-flow
steram of communications used for analytics. 

Choose Event Hubs if:
* You need to support authenticating a large number of publishers.
* You need to save a stream of events to Data Lake or Blob storage.
* You need aggregation or analytics on your event stream.
* You need reliable messaging or resiliency.
