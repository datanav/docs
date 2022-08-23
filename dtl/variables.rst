.. _variables:

Built-in Variables
==================

There are six built-in variables in the DTL.
These are ``_S``, ``_T``, ``_P``, ``_R``, ``_B`` and ``_``.

- ``_S`` refers to the source entity
- ``_T`` refers to the target entity
- ``_P`` appears inside the ``apply`` function and refers to the parent context
- ``_R`` is used to refer to the root context containing both ``_S`` and ``_T``
- ``_B`` is used by the :ref:`HTTP endpoint sinks <http_endpoint_sink>` to hold variables defined by URL parameters
- ``_`` refers to the current value in functional expressions

.. note::
  ``_S`` and ``_T`` appear in pairs inside each applied transform

.. list-table::
   :header-rows: 1
   :widths: 10, 50, 30

   * - Variable
     - Description
     - Examples

       .. _s_variable:

   * - ``_S``
     - Refers to the source entity. This is the entity on which the DTL transform operate. Note that with the ``apply`` function you can apply nested transform rules, where each of the values given to ``apply`` is made a source entity for that nested transform.
     - | ``["gt", "_S.age", 42]``
       |
       | The source entity's ``age`` field must have a value greater than 42.

       .. _t_variable:

   * - ``_T``
     - Refers to the target entity. This is the entity that is the
       primary target entity of transforming the source entity. Note
       that the ``create`` transform can be used to emit entities
       in addition to just the target entity.
     - | ``["gt", ["length", "_T.length"], 100]``
       |
       | The target entity's ``description`` field must have a length of
         more than 100 characters.

       .. _p_variable:

   * - ``_P``
     - A dict that contains the source entity and the
       target entity of the parent context. If the parent context also has
       a parent context, then that will also be available. The dict always
       contains the ``_S`` and ``_T`` variables, while the ``_P`` property is
       optional.  ``_P`` does not contain the ``_R`` variable. Note that
       the ``_P`` appears only inside the ``apply`` function.

     - | ``["gt", "_P._S.age", 18]``
       |
       | The parent source entity's ``age`` field must be greater than 18.
       |
       | ``["lt", ["length", "_P._P._T.description"], 100]``
       |
       | The grandparent target entity's ``description`` field must have a
         length of less than 100 characters.

       .. _r_variable:

   * - ``_R``
     - A dict that contains the source entity and the
       target entity of the root context. The root context is the outermost
       context, which in practice is the context of the ``default`` rule. The
       dict contains the ``_S`` and ``_T`` variables.

     - | ``["lt", "_R._S.age", 18]``
       |
       | The root source entity's ``age`` field must be less than 18.
       |
       | ``["lt", ["length", "_R._T.description"], 50]``
       |
       | The root target entity's ``description`` field must have a
         length of less than 50 characters.

       .. _b_variable:

   * - ``_B``
     - A dict that contains properties bound to URL parameters.
       It is useful for parameterizing the transform on an endpoint sink.

     - | A URL parameter ``foo`` given to the endpoint API on the form
       | ``http://my_host:port/api/publishers/my_endpoint?foo=bar``
       | will be reflected in ``_B`` as a key ``foo`` with the value "`bar`".

       .. _underscore_variable:

   * - ``_``
     - Refers to the current entity. This variable is only available
       inside a few functions that take a function expression as an
       argument. Examples of such functions are ``filter``, ``sorted``
       ``min``, ``max``, and ``coalesce``.
     - | ``["filter", ["gt", "_.amount", 100], "_S.orders"]]``
       |
       | Filters out the order entities that have an amount of less than
         100, i.e. the filter function returns only the orders that have
         an amount of greater than 100. As you can see the ``_`` variable
         refers to the individual order entities, one at a time.
