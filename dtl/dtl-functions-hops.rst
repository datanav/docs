.. _hops:
.. _hops_dtl_function:

Hops
----

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   HOPS_SPEC(dict{>1})
       |
       | The HOPS_SPEC is a dictionary that takes the following keys:

       1. ``datasets``: A list of strings with the dataset id
          whitespace separated by the dataset alias. The database
          aliases can be referenced in the ``where`` clause. The list
          must contain at least one element.

       2. ``where``: An expression or a list of expressions. If it is
          a list, then the expressions in the list will be wrapped
          with the ``and`` function. The expressions are then
          evaluated to perform the joins.

       3. ``recurse``: OPTIONAL. A boolean. The default is false. If
          true, then HOPS_SPEC should be traversed recursively. This
          makes it possible for a hops expression to be recursive. The
          output of one evaluation is fed as the input to the next
          evaluation until there are no more output. At that point the
          execution is moved on to the next HOPS_SPEC in the chain.

       4. ``exclude_root``: OPTIONAL. A boolean. The default is
          false. If true, then the original input to the recursion
          will not be included in the final output. This property is
          only meaningful on a HOP_SPEC where ``recurse`` is ``true``.

       5. ``max_depth``: OPTIONAL. An integer. The default is
          ``10``. The recursion will stop after the given number of
          recursion levels. A value of ``2`` means that the recursion will
          happen at most two times. Set it to ``null`` if you want the
          recursion will run until its output is exhausted. This
          property is only meaningful on a HOP_SPEC where ``recurse``
          is ``true``.

       6. ``return``: OPTIONAL. A string, or an expression, or not
          specified. If it is a string, then it should refer to a
          comma separated list of dataset aliases. In that case all
          the values of those aliases will be returned. If it is an
          expression then the expression is used as a template for
          the hops result. In the template you can refer to the
          dataset aliases and the interpolated result is returned. If
          not specified, then it will return the last dataset alias
          in the list. This is the default. It can only be specified
          on the last HOP_SPEC argument. ``return`` cannot be used
          with ``recurse``.

       7. ``track-dependencies``: OPTIONAL. A boolean. The default is
          true. Can be used to disable
          `dependency tracking <concepts.html#dependency-tracking>`_ for this
          particular HOP_SPEC.

       8. ``trace``: OPTIONAL. A string. The default is not set.
          If set, it is used to enable gathering of statistics for the execution of
          the ``hops`` function during runtime. Currently this tracks the maximum
          cardinality of the join statements in the ``hops``. This information
          will be available in the pipe execution log in the ``pump-completed`` and
          ``pump-failed`` entities. The value of the ``trace`` property
          should be unique to the particular ``hops`` function as it
          will be used to key the statistics gathered about its execution.
          The ``trace`` property should only be specified on the last HOP_SPEC argument.

       9. ``subsets``: OPTIONAL. A dict where the keys must be dataset aliases
          specified in the ``datasets`` property. The values must be valid subset
          expressions, i.e. an ``eq`` DTL expression where the left hand side is
          the index expression and the right hand side is the value that represents
          the subset. Example: ``["eq", "_S.category", 72]``

          (``subsets`` replaces the deprecated ``prefilters`` property)

       | If multiple HOP_SPEC arguments are given, then the output of
         a HOP_SPEC is passed on as the input to the next. This is a
         convenient way of chaining hops together. It is mostly useful
         when at least one of the HOP_SPEC arguments use recursion.

       | The join criteria are described by using the
         ``eq`` function. All dataset aliases defined in the
         ``datasets`` key have to be joined and all must by navigable
         from the source entity. If that is not the case, then an error
         will be raised at compile time.

       | The ``hops`` function produces a table inside, one column per
         dataset alias. This table is the projected down into a list
         of values by the ``return`` clause that is then returned by
         the function.

       | Note that the result of the ``hops`` function is deterministic based on the
         ``_id`` property of the entities processed within each dataset. I.e.. re-running a DTL transform with
         a ``hops`` function using the exact same entities in the source and in the datasets in the ``datasets`` property
         will yield the same order of the result. You should apply a ``sorted*`` function to the result to get a
         particular order (for example on a particular property, or if you use the ``return`` keyword).

       .. _hops_function_targeting_sink:

       .. WARNING::

          Hop-ing to the sink dataset is discouraged as there are some gotchas. In practice the pipe's ``batch_size`` must be set to ``1`` in order to guarantee that the hops is able to find the entities being written by the sink. Entities inside the current unflushed batch is not visible to the hops.

     - ::

          ["hops", {
            "datasets": ["Address a", "Country c"],
            "return": "a",
            "where": [
              ["or",
                 ["eq", "a.type", "SHIPPING"],
                 ["eq", "a.type", "BILLING"]],
              ["eq", "_S.address", "a._id"],
              ["eq", "c._id", "a.country"]
            ]}]

       | Join the source entity's ``address`` property with the
         ``Address``'s ``_id`` property, and then the ``Address``'s
         ``country`` property with ``Country``'s ``_id`` property.
         Filter the addresses by type, so that only shipping and
         billing addresses are included in the result. Return the
         addresses found.

       ::

          ["hops", {
            "datasets": ["Person p"],
            "where": [
              ["eq", "_S.children", "p._id"],
              ["eq", "p.gender", "female"]],
            "recurse": true
           },
           {
            "datasets": ["Hobby h"],
            "where": ["eq", "_S.hobbies", "h._id"],
            "return": "h.name"
           }]

       | Recursively retrieve the source entity's daughters (and
         granddaughters and so on) and then return the names of all
         their hobbies. Please note that the result list is not automatically sorted on the ``name`` property - if order
         matters, a ``sorted`` function must be applied before the result is used.
       |

       ::

          ["hops", {
            "datasets": ["orders o", "product p"],
            "where": [
              ["eq", "_S._id", "o.customer_id"]
              ["eq", "o.lines.product_id", "p.product_id"]
            ],
            "subsets": {
              "o": ["eq", "_S.webshop_id", "myshop"]
            }
           }]

       | Find the products that the customer has bought from a specific web shop. This example uses the ``subsets``
         property to reference a subset of the ``orders`` dataset, i.e. the orders placed in the ``myshop`` web shop.

.. _lookup_entity_dtl_function:

lookup-entity
-------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   DATASET_ID(string{1})
       |   ENTITY_ID(string{1})
       |
       | Returns an entity in the given dataset.
     - | ``["lookup-entity", "code-table", "foo"]``
       |
       | Looks up the entity with the ``_id`` property value of ``foo`` in the ``code-table`` dataset.
       | Note that the dataset referenced has to be populated before the DTL transform can run.
       | If the entity doesn't exist in the dataset, ``null`` is returned.

       .. WARNING::

          This function does not support dependency tracking, so if
          the entity that is looked up changes then you may want to
          reset the pipe. This will not happen automatically.
