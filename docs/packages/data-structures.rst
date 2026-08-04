Singly linked list
==================

Module and import
-----------------

Module:

.. code-block:: text

   pylib.data_structures.singly_linked_list

Import the list class:

.. code-block:: python

   from pylib.data_structures.singly_linked_list import SLinkedList

Import both public classes when direct node access is needed:

.. code-block:: python

   from pylib.data_structures.singly_linked_list import Node, SLinkedList

Description
-----------

A singly linked list is a linear data structure where each element stores a
value and a reference to the next element. Each element is called a **node**.

Unlike Python's built-in list, linked-list elements are separate objects
connected through references. This implementation supports:

* adding elements to the end;
* displaying all elements;
* removing the first element; and
* removing the last element.

Basic usage
-----------

.. code-block:: python

   from pylib.data_structures.singly_linked_list import SLinkedList

   linked = SLinkedList()
   linked.add_key(10)
   linked.add_key(20)
   linked.add_key(30)
   linked.display_linkedlist()

Output:

.. code-block:: text

   10 → 20 → 30 → None

`Node`
------

`Node` represents one element in a linked list. It stores a value and a
reference to the next node.

`key` attribute
~~~~~~~~~~~~~~~

The `key` attribute stores the node's value.

.. code-block:: python

   node = Node(5)
   print(node.key)

.. code-block:: text

   5

`next` attribute
~~~~~~~~~~~~~~~~

The `next` attribute references the following node. Its default value is `None`.

.. code-block:: python

   node = Node(5)
   print(node.next)

.. code-block:: text

   None

`SLinkedList`
-------------

`SLinkedList` creates and manages a singly linked list. A new list is empty and
stores its first node in `head`.

`head` attribute
~~~~~~~~~~~~~~~~

`head` references the first node. It defaults to `None` and changes as nodes are
added or removed.

.. code-block:: python

   linked = SLinkedList()
   print(linked.head)

.. code-block:: text

   None

`add_key(key)`
~~~~~~~~~~~~~~

Appends a node containing `key` to the end of the list.

:param key: Value to store in the new node.
:returns: `None`.

.. code-block:: python

   linked = SLinkedList()
   linked.add_key(5)
   linked.add_key(10)
   linked.display_linkedlist()

.. code-block:: text

   5 → 10 → None

`display_linkedlist()`
~~~~~~~~~~~~~~~~~~~~~~

Prints every value from the head to the tail, followed by `None`.

:returns: `None`.

.. code-block:: python

   linked.display_linkedlist()

.. code-block:: text

   5 → 10 → None

An empty list displays:

.. code-block:: text

   None

`delete_first()`
~~~~~~~~~~~~~~~~

Removes the head node. If another node follows, it becomes the new head.

:returns: `None`.

Before:

.. code-block:: text

   5 → 10 → 15 → None

.. code-block:: python

   linked.delete_first()
   linked.display_linkedlist()

After:

.. code-block:: text

   10 → 15 → None

Calling this method on an empty list leaves it unchanged and prints
`List is empty`.

`delete_last()`
~~~~~~~~~~~~~~~

Removes the final node. If the list contains one node, the list becomes empty.

:returns: `None`.

Before:

.. code-block:: text

   5 → 10 → 15 → None

.. code-block:: python

   linked.delete_last()
   linked.display_linkedlist()

After:

.. code-block:: text

   5 → 10 → None

Calling this method on an empty list leaves it unchanged and prints
`List is empty`.

API reference
-------------

See :doc:`../api/data-structures` for generated signatures, docstrings, and
linked source code.