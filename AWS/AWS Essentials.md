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

        |properties|io2 block express| io2| io1 | gp3| gp2| st1 | sc1|
        |----------|-----------------| ---|-----|----|----|-----|----|
        |Latency|sub milli second | single digit millisecond |single digit milli second  |single digit milli second|single digit milli second  |  |  |
        |Baseline/Burst| |  |  | 3000 IOPS | 3IOPS/GB Burst: 3000 IOPS|40 MB/s per TB Burst 250 MB/s  |12 MB/s per TB Burst 80 MB/s  |
        |Max IOPS |256000 IOPS |64000 IOPS|64000 IOPS |16000 IOPS|16000 IOPS| 500 IOPS| 250 IOPS|  
        |Throughput/Volume |4000 MB/s | 1000 MB/s | 1000 MB/s |1000 MB/s  |250 MB/s  |500 MB/s |250 MB/s |
        |Volume Size|4 GB - 64 TB|4GB - 16 TB|4GB to 16 TB|1 GB to 16 TB|1GB -16 TB |500 GB - 16 TB | 500 GB - 16 TB |
        |Durability|99.999%|99.999% | 99.8% to 99.9%| 99.8% to 99.9% |99.8% to 99.9%  |99.8% to 99.9%  |99.8% to 99.9%  |



    
    
