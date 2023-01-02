
.. _dtl_transform:

DTL transform
-------------

This is a transform that lets you apply :doc:`Data Transformation Language <../../../data-transformation-language>`
transformations on the entities stream produced by the data source.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 3, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``rules``
     - Object
     - The named rules of the DTL transform. The ``default`` named rule is required and is the rule that will be applied on the source entity. The other rules can be applied via the :ref:`apply <apply_dtl_function>` and :ref:`apply-hops <apply_hops_dtl_function>` DTL functions.
     -
     - Yes

   * - ``id_required``
     - Boolean
     - If ``true`` then the DTL transform will fail if the target entity's ``_id`` property is either missing or is not a string. It will also do so if the arguments to :ref:`"create" <dtl_transform-create>` and  :ref:`"create-child" <dtl_transform-create-child>` is not a dict or is missing the ``_id`` property or the ``_id`` property is of a non-string type. If the value is ``false`` then it will not fail in these situation. Instead the values will be ignored.
     - ``true``
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

Pipe configuration that reads entities from the
``Northwind:Customers`` dataset and transforms them using the Data
Transformation Language before writing them to the
``customer-with-orders`` dataset.

::

   {
       "_id": "customer-with-orders",
       "name": "Customers with orders",
       "type": "pipe",
       "source": {
          "type": "dataset",
          "dataset": "Northwind:Customers"
       },
       "transform": {
           "type": "dtl",
           "rules": {
               "default": [
                   ["copy", "_id"],
                   ["add", "name", "_S.ContactName"],
                   ["add", "orders", ["apply", "order", ["hops", {
                       "datasets": ["Northwind:Orders o"],
                       "where": [
                           ["eq", "_S._id", "o.CustomerID"]
                       ]
                   }]]]
               ],
               "order": [
                   ["add", "order_id", "_S.OrderID"],
                   ["add", "order_date", "_S.OrderDate"]
               ]
           }
       }
   }
