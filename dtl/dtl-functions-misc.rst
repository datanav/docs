Misc
====

.. _literal_dtl_function:

``literal``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   MESSAGE(value{1})
       |
       | A function that returns its argument. The argument is not evaluated and is returned as-is. This function is used to avoid side-effects from value expression evaluation.
     - | ``["literal", "_S.foo"]``
       |
       | Returns the string ``_S.foo``, and not the value of the source entity's foo property.

.. _fail_dtl_function:

``fail!``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   MESSAGE(string{1})
       |
       | A function that makes the pump fail. It can be used to conditionally fail the pump. A string error message can be specified in the first argument.
     - | ``["fail!", "Processing stopped because of invalid input. Please review."]``
       |
       | Causes the pump to fail. The error message is reported in the `pump-failed` event in the pump execution dataset.
