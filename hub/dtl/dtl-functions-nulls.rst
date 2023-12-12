.. _nulls:

Nulls
=====

.. _coalesce_dtl_function:

``coalesce``
------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   FUNCTION(function-expression{0|1}),
       |   VALUES(value-expression{1})
       |
       | Returns the first value in VALUES that is not ``null``. If the
         FUNCTION argument is specified then the first value that returns a
         true value for the expression is returned.
     - | ``["coalesce", "_S.tags"]``
       |
       | Returns the first value in the source entity's ``tags``
         field that is not null.
       |
       | ``["coalesce",``
       |     ``["gt", "_.expenses", 1000], "_S.hobbies"]``
       |
       | Returns the first hobby that has expenses greater than 1000.

.. _coalesce_args_dtl_function:

``coalesce-args``
-----------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{>=1})
       |
       | Returns the first argument in VALUES that is not ``null``. The function is 
         evaluating the arguments in order and will short-circuit once there is a 
         non-null value. If all arguments evaluate to ``null`` then the function 
         will return ``null``.

         This function is different from ``coalesce`` in that it evaluates its 
         arguments in order and stops when it finds an argument that is not null. 
         This can in many situations be a lot more efficient.
     - | ``["coalesce-args", "_S.one", "_S.two", "_S.three"]``
       |
       | Returns the the value of ``_S.two`` if that evaluates to non-null and 
         ``_S.one`` evaluates to null.
       |
       | ``["coalesce-args",``
       |     ``null, null, 123, 236]``
       |
       | Returns ``123`` as that is the first non-null argument.
       |
       | ``["coalesce-args",``
       |     ``null, ["list"], 123, 236]``
       |
       | Returns ``[]`` as that is the first non-null argument.

.. _if_null_dtl_function:

``if-null``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUE(value-expression{1})
       |   FALLBACK-VALUE(value-expression{1})
       |
       | If ``is-null`` is false for VALUE then VALUE is returned, otherwise
         FALLBACK-VALUE is returned.
       |
     - | ``["if-null", null, 2]``
       |
       | Returns ``2``.
       |
       | ``["if-null", 1, 2]``
       |
       | Returns ``1``.
       |
       | ``["if-null", ["list", null], 2]``
       |
       | Returns ``2``.
       |
       | ``["if-null", ["list", null, 123], 2]``
       |
       | Returns ``2``.
       |
       | ``["if-null", ["list", 1, "12345"], 2]``
       |
       | Returns ``[1, "12345"]``.

.. _is_not_null_dtl_function:

``is-not-null``
---------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns ``false`` if value is either ``null``, an
         empty list, or a list where the first element in the list is ``null``.
       |
     - | ``["is-not-null", null]``
       |
       | Returns ``false``.
       |
       | ``["is-not-null", 1]``
       |
       | Returns ``true``.
       |
       | ``["is-not-null", ["list"]]``
       |
       | Returns ``false``.
       |
       | ``["is-not-null", ["list", null]]``
       |
       | Returns ``false``.
       |
       | ``["is-not-null", ["list", null, 123]]``
       |
       | Returns ``false``. Note that the function only looks at the first value
         in the list.
       |
       | ``["is-not-null", ["list", 1, "12345"]]``
       |
       | Returns ``true``.

.. _is_null_dtl_function:

``is-null``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns ``true`` if value is either ``null``, an
         empty list, or a list where the first element in the list is ``null``.
       |
     - | ``["is-null", null]``
       |
       | Returns ``true``.
       |
       | ``["is-null", 1]``
       |
       | Returns ``false``.
       |
       | ``["is-null", ["list"]]``
       |
       | Returns ``true``.
       |
       | ``["is-null", ["list", null]]``
       |
       | Returns ``true``.
       |
       | ``["is-null", ["list", null, 123]]``
       |
       | Returns ``true``. Note that the function only looks at the first value
         in the list.
       |
       | ``["is-null", ["list", 1, "12345"]]``
       |
       | Returns ``false``.
