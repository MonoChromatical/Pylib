Contributing
============

Contributions should preserve PyLib's standard-library-first philosophy, remain
easy to discover, and include complete user-facing documentation.

Before you begin
----------------

* Confirm the feature does not add an unnecessary third-party runtime dependency.
* Choose the existing package domain that best owns the feature.
* Create a new distribution only when real code exists for a genuinely separate
  domain.
* Keep imports beneath the shared `pylib` namespace.
* Discuss breaking public API changes before implementation.

Feature implementation workflow
-------------------------------

1. Choose the package and module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Place the implementation beneath the matching distribution:

.. code-block:: text

   packages/<distribution>/src/pylib/<package>/<module>.py

Use lowercase `snake_case` module names and descriptive public class, function,
method, and variable names.

2. Implement the feature
~~~~~~~~~~~~~~~~~~~~~~~~

* Prefer Python's standard library.
* Keep behaviour focused and predictable.
* Handle important empty, invalid, and boundary cases.
* Add docstrings to every public class, method, and function.
* Avoid undocumented public objects.

3. Add tests
~~~~~~~~~~~~

Tests should cover normal use, edge cases, and expected failure behaviour. A new
feature is not complete until its examples and public behaviour have been tested.

4. Document the package guide
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Update the appropriate page under `docs/packages`. Every feature guide must
include:

* its full module path and exact import statement;
* what it does, why it exists, and when to use it;
* a list of supported capabilities;
* a complete basic usage example and expected output;
* every public class and its important attributes;
* every public method or function;
* parameters and return behaviour;
* method-level examples and important edge cases.

5. Update the API reference
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add the module to the corresponding page under `docs/api` so Sphinx can generate
a reference from its docstrings. Do not use the generated API page as a
replacement for the user-focused package guide.

For detailed Sphinx syntax, navigation, API generation, and preview instructions,
follow :doc:`documenting`.

6. Run project checks
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

   ruff check .
   pytest
   py -m pip install ./packages/<distribution>
   py -m sphinx -W --keep-going -b html docs docs/_build/html

7. Review the finished change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Confirm imports and examples work exactly as documented, generated files are not
included, and the change does not create placeholder package directories.

Documentation checklist
-----------------------

Before submitting a feature, confirm:

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Requirement
     - Complete
   * - Correct package and module location
     - ☐
   * - Exact import path
     - ☐
   * - Description and intended use
     - ☐
   * - Complete usage example and output
     - ☐
   * - Public classes and attributes documented
     - ☐
   * - Public methods and functions documented
     - ☐
   * - Parameters and return behaviour documented
     - ☐
   * - Edge cases documented and tested
     - ☐
   * - Sphinx build passes without warnings
     - ☐

Building these docs
-------------------

.. code-block:: console

   py -m pip install -r requirements-docs.txt
   py -m sphinx -W --keep-going -b html docs docs/_build/html

Serve `docs/_build/html` locally to check navigation, search, examples, and API
output before submitting the change.