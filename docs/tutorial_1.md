# Tutorial 1 - Getting Started

[View source on GitHub](https://github.com/RomualdRousseau/PyAny2Json).

This short introduction uses [Any2Json](https://github.com/RomualdRousseau/PyAny2Json) to:

1. Load simple tabular documents in CSV and Exce formats.
2. Display the tabular result on the console.

The expected layout of each document is a single header row followed by rows of cells:

![document with simple table](images/tutorial1_data.png)

## Setup PyAny2Json

Before to use the package, you need to download the jars in your project. Run the following command line at the root of
your python project:

```bash
python pyany2json/setup.py
```

### Import the packages and setup the main class:

```python
import pyany2json
```

## Minimal code

The minimal code to load a document is as follow:

```python
with pyany2json.load(file_path, encoding="UTF-8") as doc:
    for sheet in doc.sheets():
        table = sheet.getTable()
        if table.isPresent():
            table = table.get()
            doSomethingWithHeaders(table.headers())
            doSomethingWithRows(table.rows())
```

The encoding ("UTF-8" here) is used if the encoding could not be detected when loading the document.

### Iterate overs the headers:

```python
for header in table.headers():
    # Do something with the header
```

### Iterate over the rows and cells:

```python
for row in table.rows():
    for cell in row.cells():
        # Do something with the cell
```

## Load several file formats

Here is a complete example to load and print the content of different CSV and Excel files:

```python
import pyany2json

FILE_PATHS = [
    "data/document with simple table.csv",
    "data/document with simple table.xls",
    "data/document with simple table.xlsx",
]

for file_path in FILE_PATHS:
    with pyany2json.load(file_path) as doc:
        for sheet in doc.sheets():
            table = sheet.getTable()
            if table.isPresent():
                table = table.get()
                for header in table.headers():
                    print(header.getTag().getValue(), end=" ")
                print()
                for row in table.rows():
                    for cell in row.cells():
                        print(cell.getValue(), end=" ")
                    print()
```

```bash
date client qty amount 
2023/02/01 AAA 1 100 
2023/02/01 BBB 1 100 
2023/02/01 BBB 3 300 
2023/02/01 AAA 1 100 
date client qty amount none 
2023-02-01 AAA 1 100  
2023-02-01 BBB 1 100  
2023-02-01 BBB 3 300  
2023-02-01 AAA 1 100  
date client qty amount 
2023-02-01 AAA 1 100 
2023-02-01 BBB 1 100 
2023-02-01 BBB 3 300 
2023-02-01 AAA 1 100
```

## Conclusion

Congratulations! You have loaded documents using Any2Json.

For more examples of using Any2Json, check out the [tutorials](index.md).