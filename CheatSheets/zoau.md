
# Bash Shell samples

```bash
1. Dataset Check, non zero return code
dls "IBMUSER.JCLS1" 2>/dev/null >/dev/null

 Test whether a dataset exists
                dls -q ${prefix}.my.jcl
                if [ $? -eq 0 ]; then
                        # dataset match
                fi

2. zfs folder to ds copy
dcp ${cobdir}/*.cobol "${prefix}.PROJ23.COBOL"

3. dataset compare 

ddiff "${prefix}.my.diff(fileone)" "${prefix}.my.diff(filetwo)"

4. writing to dataset

decho "This text will be written to the PDSE member MEMBER#1 as 3 records" "${prefix}.SAMPLE.TEXT(MEMBER#1)"

5. search for text in datasets

dgrep "line" "${prefix}.my.grep"

6. list datasets 

dls -us "${prefix}.*"

7. modify text blocks and surround them with eye-catching markers.

IBMUSER.DATA:
property1=value1
property2=value2

insert a new block of lines between property1 and property2:

dmod -b -m "START\nSTOP\n#{mark} NEW CONTENT" "/property2/i\newproperty1=value\nnewproperty2=value" IBMUSER.DATA


```

