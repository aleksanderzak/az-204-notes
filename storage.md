### Azure storage

* durable - redundancy
* secure - all data is encrypted, fine-grained access control
* scalable - massively scalable
* managed - MS Azure handled maintenance and any critical problems for you

Accessible from anywhere in the world over HTTP or HTTPS.

# Storage classification

* Structured data - relational data, easy to enter qeuery and analyze (azure SQL
  database)
* semi-structured - NoSQL, defined by serialization leanguage: xml, json, yaml
  (cosmos db)
* unstructured - files, photos, videos (azure blob storage)

A **transaction** is a logical group of database operations that execute
together. 

Transactions are often defined by a set of four requirements, referred to as
ACID guarantees. ACID stands for Atomicity, Consistency, Isolation, and
Durability: 
* Atomicity means a transaction must execute exactly once and must be atomic;
  either all of the work is done, or none of it is. Operations within a
  transaction usually share a common intent and are interdependent. 
* Consistency ensures that the data is consistent both before and after the
  transaction. 
* Isolation ensures that one transaction is not impacted by another transaction.
* Durability means that the changes made due to the transaction are permanently
  saved in the system. Committed data is saved by the system so that even in the
  event of a failure and system restart, the data is available in its correct
  state.

### OLTP vs OLAP
Transactional databases are often called OLTP (Online Transaction Processing)
systems. OLTP systems commonly support lots of users, have quick response times,
and handle large volumes of data. They are also highly available (meaning they
have very minimal downtime), and typically handle small or relatively simple
transactions. 

On the contrary, OLAP (Online Analytical Processing) systems
commonly support fewer users, have longer response times, can be less available,
and typically handle large and complex transactions.

## Azure storage 

* blobs - test and binary, can include support for Azure Data Lake Storage
  serving images, documents, full static websites, files for distribured access,
  streaming video and audio, backup and restoration, disaster recover, archiving

  Supports three kinds of blobs:
  * block blobs - text/binary files up to ~5TB in size. Primary use case for
    files that are read from beginning to end. They are named block blobs
    because files larger than 100MB must be uploaded as small blocks. There
    blocks are then consolidated (or committed) into the final blob.
  * page blobs - random access files up to 8TB in size. Used primarly as the
    backing storage for the VHD used to provide durable disks for Azure Virtual
    Machines. They are named page blobs because they provide random read/write
    access to 512-byte pages.
  * Append blobs are specialized block blobs that support only appending new
    data (not updating or deleting existing data), but they're very efficient at
    it. Append blobs are great for scenarios like storing logs or writing
    streamed data.
* files - file shares, SMB protocol. Used for storing shared configuration files
  for VMs, tools, log files, metrics, crash dumps, shared data between
  on-premises applications and Azure VMs to allow migration of apps to the cloud
  over a period of time.
* queues - messages up to 64KB and queue can contain millions of messages.
* tables - NoSQL store for schema-less storage of structured data


## Azure storage account

A storage account is a container that groups a set of Azure Storage services
together. Only data services from Azure Storage can be included in a storage
account (Azure Blobs, Azure Files, Azure Queues, and Azure Tables).

Combining data services into a storage account lets you manage them as a group.
The settings you specify when you create the account, or any that you change
after creation, are applied to everything in the account. Deleting the storage
account deletes all of the data stored inside it.

A storage account defines a policy that applies to all the storage services in the account. For example, you could specify that all the contained services will be stored in the West US datacenter, accessible only over https, and billed to the sales department's subscription.

The settings that are controlled by a storage account are:

* Subscription
* Location: The datacenter that will store the services in the account.
* Performance: Standard allows you to have any data service (Blob, File, Queue, Table) and uses magnetic disk drives. Premium introduces additional services for storing data. For example, storing unstructured object data as block blobs or append blobs, and specialized file storage used to store and create premium file shares. These storage accounts use solid-state drives (SSD) for storage.
* Replication: Determines the strategy used to make copies of your data to protect against hardware failure or natural disaster. At a minimum, Azure will automatically maintain three copies of your data within the data center associated with the storage account. This is called locally-redundant storage (LRS), and guards against hardware failure but does not protect you from an event that incapacitates the entire datacenter. You can upgrade to one of the other options such as geo-redundant storage (GRS) to get replication at different datacenters across the world.
* Access tier: Controls how quickly you will be able to access the blobs in this storage account. Hot gives quicker access than Cool, but at increased cost. This applies only to blobs, and serves as the default value for new blobs.
* Secure transfer required: A security feature that determines the supported protocols for access. Enabled requires HTTPs, while disabled allows HTTP.
* Virtual networks: A security feature that allows inbound access requests only from the virtual network(s) you specify.

#### Accounts types:

* General-purpose v2 (GPv2) - support all of the latest features for blob, files, queues, and tables. Lowest per gigabyte prices.
* General-purpose v1 (GPv1) - may not have the latest features or the lowest per
  gigabyte pricing. For example cool and archive storage are not supported in
  GPv1. Pricing is lower for GPv1 transactions, so workloads with high churn or
  high read rates may benefit from this account type.
* blob storage accounts - legacy account type, support all the same block blob
  features as GPv2, but they are limited to supporting only block and append
  blobs. Pricing is broadly similar to pricing for general-purpose v2 accounts. 

### Deployment model 

Resource Manager: the current model that uses the Azure Resource Manager API
Classic: a legacy offering that uses the Azure Service Management API

The key feature difference between the two models is their support for grouping.
The Resource Manager model adds the concept of a resource group, which is not
available in the classic model. A resource group lets you deploy and manage a
collection of resources as a single unit.

### Account kind

Storage account kind is a set of policies that determine which data services you
can include in the account and the pricing of those services. There are three
kinds of storage accounts: 

* StorageV2 (general purpose v2): the current offering
that supports all storage types and all of the latest features 
* Storage (general purpose v1): a legacy kind that supports all storage types
  but may not support all features 
* Blob storage: a legacy kind that allows only block blobs and append blobs

### Security Access Keys

Each storage account has two unique access keys that are used to secure the
storage account. If your app needs to connect to multiple storage accounts, your
app will require an access key for each storage account.

Each storage account has two access keys. The reason for this is to allow keys
to be rotated (regenerated) periodically as part of security best practice in
keeping your storage account secure. 

Access keys are the easiest approach to authenticating access to a storage
account. However they provide full access to anything in the storage account,
similar to a root password on a computer. 

Storage accounts offer a separate authentication mechanism called shared access
signatures that support expiration and limited permissions for scenarios where
you need to grant limited access. You should use this approach when you are
allowing other users to read and write data to your storage account.


### REST API endpoint

The REST endpoint is a combination of your storage account name, the data type, and a known domain. For example:
* Blobs	https://[name].blob.core.windows.net/
* Queues	https://[name].queue.core.windows.net/
* Table	https://[name].table.core.windows.net/
* Files	https://[name].file.core.windows.net/

### Connection strings

The simplest way to handle access keys and endpoint URLs within applications is
to use storage account connection strings. A connection string provides all
needed connectivity information in a single text string.

example:

```
DefaultEndpointsProtocol=https;AccountName={your-storage};
   AccountKey={your-access-key};
   EndpointSuffix=core.windows.net
```

## Security

* Encryption at rest - incurs no additional charges and doesn't degrade
  performance. It can't be disabled. For virtual machines (VMs), Azure lets you
  encrypt virtual hard disks (VHDs) by using Azure Disk Encryption. This
  encryption uses BitLocker for Windows images, and it uses dm-crypt for
  Linux.Azure Key Vault stores the keys automatically to help you control and
  manage the disk-encryption keys and secrets. So even if someone gets access to
  the VHD image and downloads it, they can't access the data on the VHD.
* Encryption in transit -  Always use HTTPS to secure communication over the
  public internet. When you call the REST APIs to access objects in storage
  accounts, you can enforce the use of HTTPS by requiring secure transfer for
  the storage account.
* Role-based access control - Every request to a secure resource must be
  authorized. The service ensures that the client has the permissions required
  to access the data. You can choose from several access options. Arguably, the
  most flexible option is role-based access. Azure Storage supports Azure Active
  Directory and role-based access control (RBAC) for both resource management
  and data operations.
* auditing - Storage Analytics logs every operation in real time, and you can
  search the Storage Analytics logs for specific requests. Filter based on the
  authentication mechanism, the success of the operation, or the resource that
  was accessed.

## Storage Account Keys

In Azure Storage accounts, shared keys are called storage account keys. Azure
creates two of these keys (primary and secondary) for each storage account you
create. The keys give access to everything in the account.

## shared access signatures

For untrusted clients, use a shared access signature (SAS). A SAS is a string
that contains a security token that can be attached to a URI. Use a SAS to
delegate access to storage objects and specify constraints, such as the
permissions and the time range of access.

You can use a service-level SAS to allow access to specific resources in a
storage account. You'd use this type of SAS, for example, to allow an app to
retrieve a list of files in a file system, or to download a file. 

Use an account-level SAS to allow access to anything that a service-level SAS
can allow, plus additional resources and abilities. For example, you can use an
account-level SAS to allow the ability to create file systems.

## network access

By default, storage accounts accept connections from clients on any network. To
limit access to selected networks, you must first change the default action. You
can restrict access to specific IP addresses, ranges, or virtual networks.

## advanced threat protection for Azure Storage

Azure Defender for Storage provides an extra layer of security intelligence that
detects unusual and potentially harmful attempts to access or exploit storage
accounts. This layer of protection allows you to address threats without being a
security expert or managing security monitoring systems.

# Blob Storage

Blobs are files for the cloud. Apps work with blobs in much the same way as they
would work with files on a disk, like reading and writing data. However, unlike
a local file, blobs can be reached from anywhere with an internet connection.

In Blob storage, every blob lives inside a blob container. You can store an
unlimited number of blobs in a container and an unlimited number of containers
in a storage account. Containers are "flat" — they can only store blobs, not
other containers.

A single storage account is flexible enough to organize your blobs however you
like, but you should use additional storage accounts as necessary to logically
separate costs and control access to data.

Technically, containers are "flat" and do not support any kind of nesting or
hierarchy. But if you give your blobs hierarchical names that look like file
paths (such as finance/budgets/2017/q1.xls), the API's listing operation can
filter results to specific prefixes. This enables you to navigate the list as if
it was a hierarchical system of files and folders. This feature is often called
virtual directories because some tools and client libraries use it to visualize
and navigate Blob storage as if it was a file system. Each folder navigation
triggers a separate call to list the blobs in that folder.
