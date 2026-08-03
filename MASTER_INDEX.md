# PYLIB MASTER INDEX


# ==========================================
# DATA STRUCTURES
# ==========================================


## Singly Linked List

---

## Search Tags

`linked list`  
`singly linked list`  
`node`  
`data structure`  
`linear data structure`  
`pointer structure`  
`list`  


---

# Module

```
pylib.data_structures.singly_linked_list
```


---

# Description

A singly linked list is a linear data structure where each element stores a value and a reference to the next element.

Each element is called a **node**.

Unlike Python's built-in list, linked lists store elements as separate nodes connected through references.

### Features:

- Add elements
- Display elements
- Remove first element
- Remove last element


---

# Import

```python
from pylib.data_structures.singly_linked_list import SLinkedList
```


---

# Basic Usage

```python
from pylib.data_structures.singly_linked_list import SLinkedList


linked = SLinkedList()

linked.add_key(10)
linked.add_key(20)
linked.add_key(30)

linked.display_linkedlist()
```

Output:

```
10 → 20 → 30 → None
```


---


# Class: Node

## Description

Represents a single element inside the linked list.

Each node contains:

- A stored value
- A reference to the next node


## Attributes

### key

Stores the value contained inside the node.

Example:

```python
node = Node(5)

print(node.key)
```

Output:

```
5
```


### next

Stores the reference to the next node.

Default:

```
None
```


---


# Class: SLinkedList

## Description

Creates and manages a singly linked list.

The linked list starts empty and stores the first node using the `head` attribute.


## Attributes


### head

Stores the first node in the linked list.

Default:

```
None
```



---


# Methods


## add_key(key)

### Description

Adds a new node to the end of the linked list.


### Example

```python
linked = SLinkedList()

linked.add_key(5)
linked.add_key(10)
```

Result:

```
5 → 10 → None
```



---


## display_linkedlist()

### Description

Displays all nodes currently stored in the linked list.


### Example

```python
linked.display_linkedlist()
```

Output:

```
5 → 10 → None
```



---


## delete_first()

### Description

Removes the first node from the linked list.

The second node becomes the new head.


### Example

Before:

```
5 → 10 → 15 → None
```

Code:

```python
linked.delete_first()
```

After:

```
10 → 15 → None
```



---


## delete_last()

### Description

Removes the final node from the linked list.


### Example

Before:

```
5 → 10 → 15 → None
```

Code:

```python
linked.delete_last()
```

After:

```
5 → 10 → None
```
