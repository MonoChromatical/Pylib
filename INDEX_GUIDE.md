# PYLIB MASTER INDEX CONTRIBUTION TEMPLATE

This document defines the required format for adding new modules,
classes, functions, and utilities to the Pylib master index.

Every new addition MUST follow this structure.

---

# CATEGORY NAME

IF IT DOESNT EXIST

Examples:

- DATA STRUCTURES
- ALGORITHMS
- UTILITIES
- MATHEMATICS


---

# MODULE NAME

Example:

Singly Linked List


---

## Search Tags

Add keywords users may search for.

Include:
- Common names
- Alternative names
- Related concepts
- Use cases


Example:

```
linked list
singly linked list
node
data structure
linear structure
```


---

## Module

The import location of the module.

Format:

```
pylib.category.module_name
```


Example:

```
pylib.data_structures.singly_linked_list
```


---

## Import

Show the exact import required to use the feature.

Example:

```python
from pylib.data_structures.singly_linked_list import SLinkedList
```


---

## Description

Explain:

- What it does
- Why it exists
- When someone would use it
- Important details


Example:

```
A singly linked list implementation that stores
elements as nodes connected through references.
```


---

## Features

List the main capabilities.

Example:

- Add elements
- Remove elements
- Search elements
- Display contents


---

# Usage Example

Provide a complete working example.

Requirements:

- Must include imports
- Must show creation/initialization
- Must show common usage
- Must include output when applicable


Example:

```python
from pylib.example import Example


item = Example()

item.run()
```


Output:

```
Example output
```


---

# Classes

Document every class included in the module.


Format:


# Class: ClassName


## Description

Explain what the class represents.


---

## Attributes

Document important attributes.


Format:


### attribute_name

Description:

What the attribute stores.


Default:

```
default value
```


---

## Methods

Document every public method.


Format:


## method_name(parameter)


### Description

Explain what the method does.


### Parameters


| Parameter | Description |
|-|-|
| parameter | purpose |


### Example


```python
object.method_name(value)
```


Output:

```
result
```



---

# Functions

For standalone functions.


Format:


# function_name(parameters)


## Description

Explain what the function does.


## Parameters


| Parameter | Description |
|-|-|
| parameter | purpose |


## Returns

Describe returned value.


## Example


```python
function_name(value)
```


Output:

```
result
```


---

# Rules

## Required

Every entry must include:

✅ Name  
✅ Search tags  
✅ Module path  
✅ Import example  
✅ Description  
✅ Usage example  


For classes:

✅ Class description  
✅ Attributes  
✅ Methods  


For functions:

✅ Parameters  
✅ Return information  
✅ Example  


---

## Naming Rules

Use:

```
Category
    Module
        Class
            Method
```

Example:

```
DATA STRUCTURES

    Singly Linked List

        SLinkedList

            add_key()
```


---

## Do Not

Do not add:

❌ undocumented functions  
❌ empty descriptions  
❌ missing examples  
❌ internal/private methods (`_function`) unless necessary  


---

## Final Checklist Before Adding

[ ] Added correct category  
[ ] Added search tags  
[ ] Added import path  
[ ] Added description  
[ ] Added example usage  
[ ] Documented classes  
[ ] Documented methods/functions  
[ ] Tested example code works