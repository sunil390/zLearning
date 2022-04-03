# AWS

## AWS Global Infrastructure Components

1. AWS Regions
    1. Separate geographical area
    2. Min 2 AZ 
    2. Availability Zones
        1. Multiple DC's
        2. Redundant Power
        3. Redundant metro fiber 
    3. 100 GbE metro fiber 
    4. PoP locations
        1. Amazon Cloud Front Global CDN
        2, Edge Cache network
    5. Applications are partitioned across AZ's
        1. Elastic Load Balancer  

2. Custom Hardware
    1. Compute Server
    2. Load Balancer
    3. Router
    4. Silicon

## Amazon Elastic Compute Cloud EC2

1. WebService
2. SLA 99.99% for each EC2 Region
3. EC2 Instance
    1. Virtual Server in Cloud with Instance types and Sizes
    2. Types
        1. General Purpose - Web Servers
        2. Compute Optimized - HPC
        3. Memory Optimized - Big Data Analytics
        4. Storage Optimized - Data Warehousing
        5. Accelerated computing - Machine/Deep Learning
    3. AMI - Amazon Machine Image - Template, Required to Launch an Instance
        1. OS
        2. Applications
        3. Application Server
     
## EC2 Storage and Networking

### EC2 Instance Storage 
1. Instance Store (Temporary Block Level Storage)
    2. AMI stored in S3
    3. Amazon Elastic File System - EFS
2. Elastic Block Storage - Persistent Block Level Storage - Raw unformatted external block device
3. EBS Snapshot of EBS Volume can be Stored on S3

### Networking
1. VPC - Logically isolated area
2. Each AWS Account has Default VPC in a Region where EC2 instances can be launched

### Launching and Instance - Steps
    1. Choose Regions & AZ's
    2. AMI
    3. Instance type and size
    4. Network Access 
        1. VPC's 
        2. AZ's 
        3. Subnets
        4. Firewalls
    5. Storage
        1. Instance Store
        2. EFS
        3. EBS
    6. Tags to Categorize resources
    7. Security Groups
    8. Login Key Pairs
    9. Launch Instance
 
## EBS

1. An EBS volume can be attached to only one EC2 instance
2. Types SSD and HDD
    1. SSD
    2. HDD
3. EBS Features
    1. Dynamically increase capacity
    2. Tune Performance - io1 to io2
    3. No Downtime
    4. Cloud Watch + Lambda -> Automate Volume Changes
    5. EBS Optimized instances
        1. 500 - 19000 Mbps b/w EC2 and EBS
    6. EBS Snapshots
        1. Direct Read Access
        2. Snapshot and Resize EBS Volume
        3. Can be taken from any block storage including on-premise storage
        4. Fast Snapshot Restore
            1. from FSR enabled snapshots
            2. can be shared across accounts
            3. can be copied across Regions
            4. During deletion, data unique to the snapshot only is removed
    7. Data Life Cycle Manager - DLM
        1. tag EBS volumes and create Life cycle policies - for creation and management of backups
        2. Cloud Watch events - For monitoring policies
    8. EBS Multi Attach
        1. zero cost
        2. Attach IOPS SSD to upto 16 Nitro based EC2
        3. Manages strong consistency across multiple writers
    9. SLA - 99.999% Availability
    10. Access controlled by AWS IAM - Identity and Access Manager
    11. Encryption by default - at rest - in transit and backups
    12. Types
        | Provisioned IOPS SSD| General Purpose SSD|Throughput Optimized SSD|
        |----------------------|--------|---------|
        |io2 block express, io2, io1| gp3, gp2 |st1, sc1 |

        |Attributes|io2 block express| io2| io1 | gp3| gp2| st1 | sc1|
        |----------|-----------------| ---|-----|----|----|-----|----|
        |Latency|sub milli second | single digit millisecond |single digit milli second  |single digit milli second|single digit milli second  |  |  |
        |Baseline/Burst| |  |  | 3000 IOPS | 3IOPS/GB Burst: 3000 IOPS|40 MB/s per TB Burst 250 MB/s  |12 MB/s per TB Burst 80 MB/s  |
        |Max IOPS |256000 IOPS |64000 IOPS|64000 IOPS |16000 IOPS|16000 IOPS| 500 IOPS| 250 IOPS|  
        |Throughput/Volume |4000 MB/s | 1000 MB/s | 1000 MB/s |1000 MB/s  |250 MB/s  |500 MB/s |250 MB/s |
        |Volume Size|4 GB - 64 TB|4GB - 16 TB|4GB to 16 TB|1 GB to 16 TB|1GB -16 TB |500 GB - 16 TB | 500 GB - 16 TB |
        |Durability|99.999%|99.999% | 99.8% to 99.9%| 99.8% to 99.9% |99.8% to 99.9%  |99.8% to 99.9%  |99.8% to 99.9%  |


## VPC

### Overview

1. Logically isolated section of AWS cloud
2. Virtual Network Environment
    1. IP Address Range
    2. Subnets
    3. Route Tables
    4. Network Gateways
3. Default ipv4 private ip addresses
4. VPC Spans all the available AZ's in the region
5. One or more subnets in each AZ
6. Each Subnet must remain within one AZ
7. By Default 5 VPC's can be created per AWS Account per region. Call AWS Support to increase this.


### Concepts

1. Private IP address range - Classless Inter-Domain Routing Block (CIDR)
2. Allowed CIDR Block size : /16 and /28 
    1. eg:- 10.0.0.0/16 
        1. first 16 are fixed
        2. 2^16 = 65536 ip addresses ( 5 are reserved by AWS)
    2. CIDR Block 0.0.0.0/0 access to any ip address
    3. Secondary CIDR block can be assigned to Primary CIDR Block to expand VPC
3. Globally unique IPv4 address to be assigned to instance for access from Internet.
4. IPv6 addresses are public and accessible over Internet.
5. VPC with 10.0.0.0/16 -> Subnet1 and Subnet2 CIDR Blocks should not overlap
    1. 10.0.10.0/24 and 10.0.20.0/24 
    2. first 24 are fixed , 2^8 = 256 -5 = 251
6. Route Table
    1. Main Route Table by default
        1. 10.0.0.0/16 (Dest) Target(local)
    2. Custom Route Table
    3. Subnet Route Table
        1. Public Subnet 10.0.10.0/24
            1. 0.0.0.0/0(dest) target(igw-id)
        2. Private Subnet 10.0.20.0/24
            1. no route to internet gateway

### VPC Peering Connections

1. nw connection b/w twoi VPC
2. Private v4 or v6 addresses
3. across different aws accounts
4. different regions - Inter region
5. Uses existing infrastructure of VPC
6. do not use gateway or vpn connection
7. no SPOC and bandwidth bottlenecks
8. stays on AWS backbone
9. Establishing VPC Peering Connection
    1. VPC 10.0.0.0/16 - Private Subnet 10.0.10.0/24 (Requestor)  <---->  VPC 172.31.0.0/16 - Private Subnet 172.31.10.0/24(Accepter)
    2. UnSupported
        1. Overlapping CIDR Blocks
        2. no transitive properties
        3. no edge to edge routing
    3. Owner of Requester VPC sends a peering request to Owner of Accepter VPC
    4. Owner of the Accepter accepts the peering request.
    5. Manually add routes in each VPC
        1. Requestor 
            1. Destination(10.0.0.0/16) Target (local)
            2. Destination(172.31.0.0/16) Target(peering id)
        2. Accepter
            1. Destination(172.31.0.0/16) Target (local)
            2. Destination(10.0.0.0/16) Target(peering id)
    6. Update Securrity Groups to ensure traffic is not restricted
 
    
### VPC Internet Gateway

1. Horizontally scaled
2. Redundant and highly available
3. Steps
    1. Attach Internet Gateway igw-id
    2. Add Route in Subnet Routing Table
    3. Instance should have Public v4 ip, v6 ip or elastic ip
        1. elastic ip addresses are static and can be rapidly moved from one instance or Network Interface 
    4. Network Access Control List
    5. Security Groups
4. NAT Gateway
    1. nat-gwy-id in Public Subnet.
    2. Should associate with Public Subnet
    3. elastic ip address in Public Subnet for nat-gway-id
    4. Private Subnet 
        1. Destination(10.0.0.0/16) Target (local)
        2. Destination(0.0.0.0/0) Target(nat-gwy-id)
    5. NAT Gateway are not supported in ipv6 traffic
5. Egress-Only Internet Gateway
    1. Stateful (remembers)
    2. Private Subnet 2001:db8:1234:1a00::/56 
        1. Destination(10.0.0.0/16) Target (local)
        2. Destination(2001:db8:1234:1a00::/56) Target (local)
        3. Destination(::/0) Target(eigw-id)
    
6. NACL
    1. Firewall at the Subnet Boundary
    2. default NACL allows all inbound and outboud
    3. Custom NACL denies all inbound and outbound traffic
    4. Multiple subnets can be associated with a NACL, Only One NACL per Subnet.
    5. NACL's are stateless
    6. Requires Explicit rules for inbound and outboud tracffic
    7. Numbered list of rules , Lowest having highest priority, match means evaluation stops , Allow/Deny
        1. Type 
        2. Protocol
        3. Port range
        4. Source
7. Security Group
    1. Virtual Firewall at instance level.
    2. By default denies all inbound traffic and allows all outbound traffic
    3. No deny rules as by default deny all for inbound
    4. Stateful - Responces to inbound traffic automatically allowed.
    5. All rules are evaluated
        1. Type 
        2. Protocol
        3. Port range
        4. Source

### Marketing and Finance

1. Marketing
    1. CIDR 10.10.0.0/16
        1. dest 10.10.0.0/16  target local
        2. dest 172.31.0.0/16 target pcx
2. Finance
    1. CIDR 172.31.0.0/16 
        1. dest 172.31.0.0/16 target local
        2. dest 10.10.0.0/16  target pcx 

### Lab
    1. Create Peering Group
    2. Add Routing Rules in both subnets
    3. Update Security Groups to allow ICMP inbound from other subnet.

## RDS

1. Resizable capacity
2. provisioning , setup, patching , backups 
3. Aurora, PGsql, MySQL, MariaDB, Oracle, SQLServer
4. IPSec VPN Connection to Existing IT Infra

### Availability and Durability

1. Automated Backups
2. Stored in S3
3. upto last 5 min - snapshot
4. Automatic Host replacement
5. Multi AZ DB Instance
6. Across Region Failover

### Lower Admin Burden 

1. DB Instance Class
    1. Standard
    2. Memory Optimized
    3. Burstable performance
2. Automatic Software Patches
    1. Best Practice suggestions
3. Performance
    1. General Purpose SSD Storage
        1. 3 IOPS/GB to 3000 IOPS
        2. gp2
    2. Provisioned IOPS SSD Storage
        1. Upto 40000 IOPS per DB
    3. Magnetic Storage
        1. backward compatibility
4. Managebeability and Cost Metrics
    1. Cloud watch
    2. Mgmt Console
    3. 50 Metrics covering   cpu, memory, i/o, file system and performance insights
    4. Event Notifications SNS
    5. Amazon Config
    6. Pay only for use, Reserved instances, Stop and Start
5. Scalability
    1. upto 32 vcpu and 244 GiB 64 TB , SQL Server only upto 16 TB
    2. Aurora Multi Master Cluster
        1. Master in Multiple AZ
        2. Shared Storage Volumes across AZ's
6. Security
    1. Network Isolation - VPC
    2. Security Groups at Instance level , NACL's at Subnet level
    3. IPSec VPN to on prem, Network firewalls and IDS
    4. IAM controls snapshots, parameter groups, option groups , control actions, tags
    5. AWS Key Management Service - Encryption at rest and transit
    6. Transparen Data Encryption
    7. AWs Cloud HSM - Hardware Security Module
    8. SSL or TLS

## AWS IAM

### Shared Responsibility Model

1. Customer - Responsible for "Security IN the cloud. /Data Security/OS/Applications
2. AWS - - Responsible for "Security OF the cloud. /Virtualization/Facilities/Hardware

### IAM
1. IAM User, IAM Group
2. IAM Policy
3. IAM Roles to delegate access
4. TOD conditions, IP Address , MFA, SSL, 
5. Analyze Access.
6. Identity Federation SAML 2.0

### IAM Permissions

1. IAM Policy
    1. Version Statements
    2. SID - Statement ID
    3. Effect - Allow/Deny
    4. Principal - IAM Entities - USer, Federated User, Group, Roles 
    5. Action - actions to allow/deny - Access Levels below
        1. List
        2. Read
        3. Tagging
        4. Write
        5. Permisions Management
    6. Resources - 
    7. Conditions - 

    8. Management Console - Policy Summaries
2. IAM Roles
    1. AWS Identity with permission policies
        1. No Long term Credential such as password and access keys
        2. Temporary security credential
        3. Delegate Access using Roles
3. Access Analyzer
    1. Comprehencive findings
    2. Monitors and helps to refine permissions
    3. service last accessed - remove obsolete
    4. Automated reasoning
    
