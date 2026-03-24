.. _retract_feature:

:badge:`Free feature,badge-success badge-pill`

Retract
=======

The retract feature allows a pipe to permanently prune the version history of individual entities in its sink dataset. When an output entity carries the ``$retract: true`` field and the pipe has ``compaction.retract`` enabled, all earlier versions of that entity are removed while the current version is retained. Deletion state is unaffected. The operation is idempotent.

This is useful in situations where sensitive data (e.g. personal identifiers) was present in earlier versions of an entity and must be removed from storage without deleting the entity itself.

.. note::
   ``$retract`` propagates downstream like any other field. However, patterns such as
   :ref:`merge sources <merge_source>` or :ref:`emit_children <emit_children_transform>`
   may not carry it through to the output entity and require explicit handling.

Enabling retract
----------------

Retract must be explicitly opted into. It can be enabled per pipe via the ``compaction.retract``
property, or globally for all pipes via the :ref:`node metadata <service_metadata_section>`
property ``global_defaults.compaction_retract``.

See :ref:`compaction.retract <compaction_feature>` for the pipe-level property and
:ref:`global_defaults.compaction_retract <service_metadata_global_defaults_compaction_retract>`
for the global default.

Configuration example
---------------------

When a customer is offboarded, their SSN is no longer needed. The pipe emits a sanitised entity
(omitting ``ssn``) and sets ``$retract: true`` to prune the version history that contained it.
``compaction.retract`` is set to ``true`` on the pipe to opt into this behaviour:

.. code-block:: json

   {
       "_id": "customer-status-retract-history",
       "type": "pipe",
       "compaction": {
           "retract": true
       },
       "source": {
           "type": "dataset",
           "dataset": "customer_status"
       },
       "transform": {
           "type": "dtl",
           "rules": {
               "default": [
                   ["if", ["eq", "_S.status", "offboarded"],
                       [
                           ["copy", "_id"],
                           ["copy", "status"],
                           ["add", "$retract", true]
                       ],
                       ["copy", "*"]
                   ]
               ]
           }
       }
   }

Source entity while the customer is active:

.. code-block:: json

   {
       "_id": "customer_123",
       "status": "paid",
       "ssn": "123456789"
   }

After offboarding, the pipe outputs:

.. code-block:: json

   {
       "_id": "customer_123",
       "status": "offboarded",
       "$retract": true
   }

The sink writes this as the latest version and permanently removes all earlier versions,
including those that contained ``ssn``.
