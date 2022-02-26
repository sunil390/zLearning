# MS Training on Power BI

## 26th Feb 2022

### Preparing Data

1. Transform -> Fill Down - Alternate of "Ctrl+G -> Blanks  -> Up Arrow -> Control+Enter"
2. Transform -> Split Colum ( by first or last occurance)
3. Add Column -> Column from Exampes -> All Columns 
4. DataType Fixed DecimalNumber for converting from text to Currency with 2 decimals.
5. Home -> Use first Row as header
6. Transform -> Transpose to flip columns to rows
7. Home -> Append Query ( To combine tables)
8. Add Column -> Conditional Column ( to add a new column based on conditions from other columns)
9. Select Subset of Data : Select Column -> Down Arrow -> Date Filter -> In the previous

### Data Modelling and Exploration

1. Use & to Concatenate : ZipCountry = Sales[Zip] & "," & Sales[Country] 
2. Creating Date Table : Date = CALENDAR (DATE(2012,1,1), DATE(2022,12,31))
3. A Calculated column is evaluated row by row. We extend a table by adding calculated columns.
4. A Measure is used when we want to aggregate values from many rows in a table.
5. Previous Year Sales = CALCULATE(SUM(Sales[Revenue]), SAMEPERIODLASTYEAR('Date'[Date]))
6. % Growth = DIVIDE(SUM(Sales[Revenue])-[PY Sales],[PY Sales])
7. Create Relationship

###  18th Nov 2021
1. source as Postgresql
2. Import transform, check all data rows for data types
3. Merge Queries - left outer join is default
4. Transform - use first row as header - done
5. Split column by delimter - done
6. transform ribbon - fill down or up. - done
7. add column - from selection -  
8. add column conditional column
9. disable load - exclude tables
10. OneDrive connector and local connector are different. - ok
11. Change Data source to update b/w onedrive and local folder.
12. Combinevalues
13. Filters on all pages - Drag and drop
14. Top N Filtering
15. New Group - Folter - three dots - 
16. Add Modelling Data table -> link -> Date hierarchy is created.
17. Create heirarchy at column level and add more columns to it
18. New Measure - > Any column from Any Table - Doesn't take any space.
    a. Calculate - expression - filter  ex PY Sales = CALCULATE(SUM(Sales[Revenue]), SAMEPERIODLASTYEAR('DATE'[Date]))  another % Growth = DIVIDE(SUM(Sales[Revenue])-[PY Sales],[PY Sales])
    b. 
19. Format -> Background
    a. change transparency to remove white color in text boxes.
    b. remove background to remove white space around charts

20. Mouse over - Smart narrative
21. Play axis Dynamic Slicer.
22. Bookmark
23. Buttons
24. Button action -> Bookmark
25. Send Alert from Visual....
26. Include in App
