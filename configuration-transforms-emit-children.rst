
.. _emit_children_transform:

Emit children transform
-----------------------

This transform will emit all child entities of its source
entities. All entities in the ``$children`` property that have an
``_id`` property will be emitted. The parent entity will not be
emitted.

This transform should always be used in a separate pipe. If the ``emit_children`` transform is a part of a chained transform, Sesam won't be able to perform deletion tracking on the emitted child entities, as the parent entity will be removed from the sink dataset and not marked as deleted.

Properties
^^^^^^^^^^

There are currently no properties on this transform.

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

  {
      "_id": "children",
      "type": "pipe",
      "source": {
          "type": "dataset",
          "dataset": "parents-with-children"
      },
      "transform": {
          "type": "emit_children"
      }

