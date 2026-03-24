.. _retract_feature:

:badge:`Free feature,badge-success badge-pill`

Retract
=======

The retract feature is designed for situations where GDPR or other data-protection requirements
demand that historical versions of an entity — which may contain PII such as social security
numbers or contact details — are permanently erased from storage.

A standard soft-delete (``_deleted: true``) removes an entity logically but leaves all prior
versions on disk. Retract addresses that gap: when an output entity carries ``$retract: true``
and the pipe has ``compaction.retract`` enabled, all earlier versions of that entity are
permanently removed from the sink dataset while the current version is retained. Deletion state
is unaffected. The operation is idempotent.

Enabling retract
----------------

Retract must be explicitly opted into. It can be enabled per pipe via the ``compaction.retract``
property, or globally for all pipes via the :ref:`node metadata <service_metadata_section>`
property ``global_defaults.compaction_retract``.

See :ref:`compaction.retract <compaction_feature>` for the pipe-level property and
:ref:`global_defaults.compaction_retract <service_metadata_global_defaults_compaction_retract>`
for the global default.

Limitations and caveats
------------------------

.. WARNING::

   Retract is irreversible. Once earlier versions of an entity have been pruned they cannot
   be recovered. Ensure the current version of the entity contains all data that must be
   preserved before triggering a retract.

**Only the sink dataset is affected.** Retract prunes versions in the pipe's sink dataset only.
Upstream datasets, audit logs, backups, and any external systems that have already received the
data are not affected. A full data-erasure strategy must account for all downstream consumers.

**Downstream propagation is your responsibility.** ``$retract`` propagates like any other field,
but patterns such as :ref:`merge sources <merge_source>` or
:ref:`emit_children <emit_children_transform>` may not carry it through to the output entity.
Any pipe further downstream that needs to honour the retract must explicitly include
``$retract`` in its output and have ``compaction.retract`` enabled. Without this, those
downstream datasets will retain their full version history.

Example: removing PII on offboarding
--------------------------------------

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
