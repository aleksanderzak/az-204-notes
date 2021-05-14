# Virtual Machines

## Related resources:

* resource group
* storage account (disk)
* virtual network
* public IP
* network interface
* data disks

## VM availability 

Region is multiple buildings. Availability zones guarantees that resources are
in different buildings within a region. Still there can be an outage of the whole region (buildings are geographically close).

Availability levels for a VM:
* VM (95% with HDD, SSD 99.5%, Premium SSD 99.9%) - single rack
* at least 2 VMs in the same availability set (99.95%) - different racks
* at least 2 VMs accross two or more availability zones in the same region
  (99.99%) - different buildings
* region replication to a paired region (azure provides storage replication
  between avaialbility zones within a region and to another region). 

### Fault domains

A fault domain is a logical group of underlying hardware that share a common
power source and network switch, similar to a rack within an on-premises
datacenter. As you create VMs within an availability set, the Azure platform
automatically distributes your VMs across these fault domains. This approach
limits the impact of potential physical hardware failures, network outages, or
power interruptions.

### Update domains

An update domain is a logical group of underlying hardware that can undergo
maintenance or be rebooted at the same time. As you create VMs within an
availability set, the Azure platform automatically distributes your VMs across
these update domains. This approach ensures that at least one instance of your
application always remains running as the Azure platform undergoes periodic
maintenance. The order of update domains being rebooted may not proceed
sequentially during planned maintenance, but only one update domain is rebooted
at a time.
