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
 
