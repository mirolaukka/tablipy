# Tablipy Python Package Documentation

**Table of Contents**

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
    - [Initializing a Tablipy Instance](#initializing-a-tablipy-instance)
    - [Retrieving Data](#retrieving-data)
    - [Setting Data](#setting-data)
    - [Printing the Table](#printing-the-table)
    - [Adding Columns and Rows](#adding-columns-and-rows)

## Introduction

The `Tablipy` package is a Python utility that allows you to work with tabular data in a flexible and user-friendly manner. It provides a convenient interface for creating, manipulating, and printing tables. The package includes methods to retrieve specific columns, rows, and cells, set data, print tables in a formatted manner, and more.

## Installation

You can install the `Tablipy` package using `pip`:

```bash
pip install tablipy
```

## Usage

### Initializing a Tablipy Instance

To begin using `Tablipy`, import the class and create an instance with optional column headers and pre-existing data. The `Tablipy` class automatically handles the initialization of data during the instance creation, so you don't need to use the `build_from_data` method explicitly.

```python
from tablipy import Tablipy

# Automatically initializes data during instance creation
table = Tablipy(col_headers=['Name', 'Age', 'Location'], data=[
    ['John', '30', 'New York'],
    ['Jane', '25', 'Los Angeles']
])
```

### Retrieving Data

You can retrieve data from the table using methods like `get_column`, `get_row`, and `get_cell`.

```python
# Retrieve a specific column
column_data = table.get_column('Name')  # or table.get_column(0)

# Retrieve a specific row
row_data = table.get_row(1)

# Retrieve a specific cell
cell_value = table.get_cell('Age', 0)  # or table.get_cell(1, 0)
```

### Setting Data

You can set data in the table using methods like `set_column`, `set_row`, and `set_cell`.

```python
# Set values in a column
table.set_column(2, ['Chicago', 'San Francisco'])

# Set values in a row
table.set_row(0, ['Sam', '28', 'Miami'])

# Set a specific cell's value
table.set_cell(1, 1, '31')
```

### Printing the Table

You can print the table in a formatted tabular format using the `print` method.

```python
table.print()
```

### Adding Columns and Rows

You can add new columns and rows to the table using the `add_column` and `add_row` methods.

```python
# Add a new column
table.add_column('Gender', ['Male', 'Female'])

# Add a new row
table.add_row(['Chris', '24', 'Denver', 'Male'])
```

## Conclusion

The `Tablipy` package provides a convenient way to work with tabular data in Python. It allows you to initialize tables, retrieve and set data, print tables in a formatted manner, and add columns and rows. This documentation should serve as a comprehensive guide to using the `Tablipy` package effectively in your projects. For more detailed information, refer to the class and method docstrings in the source code.