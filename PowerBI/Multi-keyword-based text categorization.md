# Reference
<https://community.powerbi.com/t5/Desktop/Text-Categorization-based-on-multiple-Keywords/m-p/1442262>

# Method1

Table - Details
| Column1 | Text | Calculated Column |
| ------ | ------ | ------- |
| cell1 | 111 category | 111 
| cell2 | 222 category | 222

Table - Products
| Products | 
| ------ | 
| 111 | 
| 222 | 


```pbx
Calculated Column =
CONCATENATEX (
    FILTER ( Products, SEARCH ( Products[Products], Details[Text],, 0 ) > 0 ),
    Products[Products],
    ", "
)
```
