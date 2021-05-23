# Virtual Machines

## Related resources:

* resource group
* storage account (disk)
* virtual network
* public IP
* network interface
* data disks
* network security groups 

## VM availability 

Availability is the percentage of time a service is available for use.

To ensure your services aren't interrupted and avoid a single point of failure,
it's recommended to deploy at least two instances of each VM. This feature is
called an availability set. Interruption can be due to update on Azure
(hwardware of software of the underlying system), or failures.

#### Availability Set

An availability set is a logical feature used to ensure that a group of related
VMs are deployed so that they aren't all subject to a single point of failure
and not all upgraded at the same time during a host operating system upgrade in
the datacenter. VMs placed in an availability set should perform an identical
set of functionalities and have the same software installed.

When you place VMs into an availability set, Azure guarantees to spread them
across Fault Domains and Update Domains.

Region is multiple buildings. Availability zones guarantees that resources are
in different buildings within a region. Still there can be an outage of the whole region (buildings are geographically close).

Availability levels for a VM:
* VM (95% with HDD, SSD 99.5%, Premium SSD 99.9%) - single rack
* at least 2 VMs in the same availability set (99.95%) - different racks
* at least 2 VMs accross two or more availability zones in the same region
  (99.99%) - different buildings, indepdendent power, cooling and networking
* region replication to a paired region (azure provides storage replication
  between avaialbility zones within a region and to another region). 

#### Fault domains

A fault domain is a logical group of underlying hardware that share a common
power source and network switch, similar to a rack within an on-premises
datacenter. As you create VMs within an availability set, the Azure platform
automatically distributes your VMs across these fault domains. This approach
limits the impact of potential physical hardware failures, network outages, or
power interruptions. You can think of it as a rack within an on-premises
datacenter. 

#### Update domains

An update domain is a logical group of underlying hardware that can undergo
maintenance or be rebooted at the same time. As you create VMs within an
availability set, the Azure platform automatically distributes your VMs across
these update domains. This approach ensures that at least one instance of your
application always remains running as the Azure platform undergoes periodic
maintenance. The order of update domains being rebooted may not proceed
sequentially during planned maintenance, but only one update domain is rebooted
at a time.

#### Failover accross locations 

**Azure Site Recovery** replicates workloads from a primary site to a secondary
location. If an outage happens at your primary site, you can fail over to a
secondary location. This failover enables users to continue to access your
applications without interruption. You can then fail back to the primary
location after it's up and running again. Azure Site Recovery is about
replication of virtual or physical machines; it keeps your workloads available
in an outage.

#### Azure Backup

Backup as a service. wide range of data backup scenarios, such as: 

* Files and folders on Windows OS machines (physical or virtual, local or cloud)
* Application-aware snapshots (Volume Shadow Copy Service) 
* Popular Microsoft server workloads such as Microsoft SQL Server, Microsoft
  SharePoint, and Microsoft Exchange 
* Native support for Azure Virtual Machines, both Windows, and Linux 
* Linux and Windows 10 client machines

offers:

* **Automatic storage management**. Azure Backup automatically allocates and
  manages backup storage and uses a pay-as-you-use model. You only pay for what
  you use. 
* **Unlimited scaling**. Azure Backup uses the power and scalability of Azure to
  deliver high availability. 
* **Multiple storage options**. Azure Backup offers locally redundant storage
  where all copies of the data exist within the same region and geo-redundant
  storage where your data is replicated to a secondary region. 
* **Unlimited data transfer**. Azure Backup does not limit the amount of inbound
  or outbound data you transfer. Azure Backup also does not charge for the data
  that is transferred. 
* **Data encryption**. Data encryption allows for secure transmission and
  storage of your data in Azure.
* **Application-consistent backup**. An application-consistent backup means that
  a recovery point has all required data to restore the backup copy. Azure
  Backup provides application-consistent backups. 
* **Long-term retention**. Azure doesn't limit the length of time you keep the
  backup data.


 # Secure the network

 By default, there is no security boundary between subnets, so services in each
 of these subnets can talk to one another. However, you can set up Network
 Security Groups (NSGs), which allow you to control the traffic flow to and from
 subnets and to and from VMs. NSGs act as software firewalls, applying custom
 rules to each inbound or outbound request at the network interface and subnet
 level. This allows you to fully control every network request coming in or out
 of the VM.

# Storage

* Unmanaged disks - you are responsible for the storage accounts that are used
  to hold the VHDs. Single storage account hsa a fixed-rate limit of 20k IOPS
  (40 standard virtual hard disks at full utilization). If you need more disks, then you need more storage accounts.
* Managed disks - newer and recommended disk storage model. Storage accounts are
  managed by Azure. You specify the size of the disk (up to 4TB) and Azure
  creates and manages both the disk and the storage. Easier to scale out.

# Azure VM Extensions

Azure VM extensions are small applications that enable you to configure and
automate tasks on Azure VMs after initial deployment. Azure VM extensions can be
run with the Azure CLI, PowerShell, Azure Resource Manager templates, and the
Azure portal.

# Create a VM

1. 
```
az group create \
  --name mygroup \
  --location westeurope
```
2. 
```
az vm create \
  --resource-group mygroup \
  --name MeanStack \
  --image Canonical:UbuntuServer:16.04-LTS:latest \
  --admin-username azureuser \
  --generate-ssh-keys
  ```
3. 
```
az vm open-port \
  --port 80 \
  --resource-group mygroup
  --name MeanStack
```