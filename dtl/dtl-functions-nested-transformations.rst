Nested transformations
======================

.. _apply_dtl_function:

``apply``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   RULE_ID(string{1}),
       |   VALUES(value-expression{1})
       |
       | Applies the RULE_ID transform rule on the values in VALUES.
         RULE_ID must be the id of a transform rule in the current DTL
         specification.
     - | ``["apply", "order", "_S.orders"]``
       |
       | This will transform the order values in the source entity's
         ``orders`` field using the ``order`` transform rules. The output is
         the transformed order values.

.. _apply_hops_dtl_function:

``apply-hops``
--------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   RULE_ID(string{1}),
       |   HOPS_SPEC(dict{>1})
       |
       | This function is a combined ``hops`` and ``apply`` function. It
         evaluates the hops, and then passes the result through
         the RULE_ID transform rule.

       | See the :ref:`apply <apply_dtl_function>`
         and the :ref:`hops <hops_dtl_function>` functions for more information
         about the parts.

       .. NOTE::

          Use this function instead of ``apply`` if you use ``hops`` inside
          the transformation rule. This is required so that
          `dependency tracking <concepts.html#dependency-tracking>`_
          can work. Calling ``apply`` on a rule that contains ``hops`` or
          ``apply-hops`` is not allowed.

     - | ``["apply-hops", "order", {``
       |   ``"datasets": ["orders o"],``
       |   ``"where": ["eq", "_S._id", "o.cust_id"]``
       |  ``}]``
       |
       | This will retrieve orders from the hops expression and then
         transform them using the ``order`` transformation rule. The output
         is the transformed order values.
