# Events vs messages

**Message** 

* raw data, produced by one component and conusmed by another component
* contains data, not reference
* sending component expects data to be processed in a certain way
* likely to be used when distributed app requires a guarantee that the communication will be processed

**Events**

* most often broadcast communications
* publishers and subscribers
* lightweight notification
* often ephemeral, might not be handled

**Azure Queue Storage**

Queue storage is a service that uses Azure Storage to store large numbers of messages that can be securely accessed from anywhere in the world using a simple REST-based interface. Queues can contain millions of messages, limited only by the capacity of the storage account that owns it.

**Azure Service Bus**

Service Bus is a message broker system intended for enterprise applications. These apps often utilize multiple communication protocols, have different data contracts, higher security requirements, and can include both cloud and on-premises services. Service Bus is built on top of a dedicated messaging infrastructure designed for exactly these scenarios.

*topic* - like queue, but can have multiple subscribers. Internally, topics use queues. When you post to a topic, the message is copied and dropped into the queue for each subscription. 

*increased reliability* - Queues increase the reliability of the message exchange because, at times of high demand, messages can simply wait until a destination component is ready to process them.

*message deliveryy guarantees*

* At-Least-Once Delivery
* At-Most-Once Delivery :white_check_mark:
* First-In-First-Out (FIFO) :white_check_mark:

*transactional support*

*RBAC*

*queue no bigger than 80GB*

**Queue Storage**

*simpler*

*supports queues bigger than 80GB*

**Azure Event Grid**

Azure Event Grid is a fully-managed event routing service running on top of Azure Service Fabric. Event Grid distributes events from different sources, such as Azure Blob storage accounts or Azure Media Services, to different handlers, such as Azure Functions or Webhooks. Event Grid was created to make it easier to build event-based and serverless applications on Azure.

Use Event Grid when you need these features:

* Simplicity: It is straightforward to connect sources to subscribers in Event Grid.
* Advanced filtering: Subscriptions have close control over the events they receive from a topic.
* Fan-out: You can subscribe to an unlimited number of endpoints to the same events and topics.
* Reliability: Event Grid retries event delivery for up to 24 hours for each subscription.
* Pay-per-event: Pay only for the number of events that you transmit.

t's designed for one-event-at-a-time delivery

**Azure Event Hub**

Event Hubs is an intermediary for the publish-subscribe communication pattern. Unlike Event Grid, however, it is optimized for extremely high throughput, a large number of publishers, security, and resiliency.

*partitions*

Choose Event Hubs if:
* You need to support authenticating a large number of publishers.
* You need to save a stream of events to Data Lake or Blob storage.
* You need aggregation or analytics on your event stream.
* You need reliable messaging or resiliency.