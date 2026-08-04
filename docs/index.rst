Welcome to PyLib
================

A universal, growing collection of reusable Python utilities that fills gaps in
the standard library without introducing third-party runtime dependencies.

PyLib is organized as a monorepo of independently installable packages. You can
install the domain you need instead of downloading every utility in the project.

.. important::

   PyLib is under active development. APIs may change as the library grows.

Get started
-----------

Install an individual distribution directly from the repository. For example:

.. code-block:: console

   py -m pip install "git+https://github.com/MonoChromatical/Pylib.git#subdirectory=packages/data-structures"

Create a linked list in a few lines:

.. code-block:: python

   from pylib.data_structures.singly_linked_list import SLinkedList

   linked = SLinkedList()
   linked.add_key(10)
   linked.add_key(20)
   linked.display_linkedlist()

.. code-block:: text

   10 → 20 → None

Explore PyLib
-------------

:doc:`getting-started`
   Installation, requirements, and your first example.

:doc:`packages/index`
   Guides for every available package and feature.

:doc:`api/index`
   Exact public classes, methods, and source references.

:doc:`contributing`
   Coding standards and the complete feature contribution workflow.

Why PyLib?
----------

* **Standard-library first:** avoid unnecessary runtime dependencies.
* **Reusable:** share focused utilities across many projects.
* **Lightweight:** keep implementations understandable and efficient.
* **Selective:** install only the broad package domain you need.
* **Expandable:** grow into new domains without turning into one large install.

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Start here

   getting-started
   philosophy

.. toctree::
   :hidden:
   :maxdepth: 3
   :caption: Packages

   packages/index

.. toctree::
   :hidden:
   :maxdepth: 3
   :caption: Reference

   api/index
   contributing
   documenting

Indices
-------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`