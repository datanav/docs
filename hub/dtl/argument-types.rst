Argument types
==============

In the function tables below you'll see argument lists like this
``CONDITION(boolean-expression{1}), THEN(transforms{1}), ELSE(transforms{0|1})``.

``CONDITION``, ``THEN`` and ``ELSE`` are logical names that have no
meaning other than so that we can refer to them by name. Inside the
parenthesis is the type of argument, i.e. ``boolean-expression`` and
``transforms``. The numbers inside the curly braces is the cardinality
of the argument. Here are some cardinalites that you'll come across:

#. ``{0|1}``: zero or one, i.e. optional.

#. ``{1}``: exactly one

#. ``{2}``: exactly two

#. ``{>=0}``: zero or more

#. ``{>=1}``: one or more

.. list-table::
   :header-rows: 1
   :widths: 10, 50, 30

   * - Argument type
     - Description
     - Examples

   * - ``boolean-expression``
     - | Refers to an expression that returns a single "boolean" value. Note that
         ``false``, ``null`` and ``[]`` evaluate to false. All other values
         evaluate to true.
     - | ``["eq", "_S.type", "person"]``

   * - ``integer-expression``
     - | Refers to an expression that returns a single "integer" value.
     - | ``["+", 1, 2]``

   * - ``value-expression``
     - | Refers to an expression that returns null, a single value or a
         list of values.
     - | ``["list", 1, 2, 3]``

   * - ``function-expression``
     - | Refers to a value expression argument that operates on a list
         of values, and exposes the ``_`` current value variable for
         each of them.
     - | ``["upper", "_.name"]``

   * - ``string``
     - | Refers to a constant string literal.
     - | ``"Jupiter"``

   * - ``wildcard-string``
     - | Refers to a constant string pattern literal that can include
         the ``*`` and ``?`` wildcard characters.
     - | ``"alpha_*"`` or ``"person"``

   * - ``wildcard-string-list``
     - | Same as ``wildcard-string``, but a list of them.
     - | ``["alpha_*", "beta_*"]``

   * - ``transforms``
     - | A single transform function, or a list of them.
     - | ``["add", "type", "person"]``
       |
       | or
       |
       | ``[["add", "type", "person"],``
       |  ``["copy", ["list", "name", "age"]]]]``
