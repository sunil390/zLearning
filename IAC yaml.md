# Infrastructure as a Code - Design thoughts 

## Using yaml as the Declarive infrastruture Staring point.

1. Review the Ansible's quick yaml guide
<https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html>

2. Review this reference structurte created for DCUF SID

<https://gitlab.com/mainframe-services/zlearning/-/blob/main/Config.yaml>


## Validating the Code

<https://yaml-online-parser.appspot.com/>


### Processing the Code.

<https://www.kite.com/python/answers/how-to-parse-and-extract-data-from-a-yaml-file-in-python>

## Use Cases

### MQ Series RSU

1. Create a yaml file to declare the RSU process....

```yaml

---
# MQ Series RSU

- Sub system :
    Name : MQ
    Version : 9.1
    VUE : yes
    - Previous RSU Libraries :
        Non VSAM : xxxx
        VSAM : xxxx
        HLQ : xxxx
        SMPE : xxxx
    - Next RSU Libraries 
        Non VSAM : xxxx
        VSAM : xxxx
        HLQ : xxxx
        SMPE : xxxx
    - Internet Service Retrieval:
        Certificate : xxx
        Location : xxx
        ID : xxx
        Password : {{ Password_Secret_Repo }}
    - JCL Libraries :
        

       

