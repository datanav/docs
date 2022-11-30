
.. _embedded_source:

Embedded source
---------------

This is a data source that lets you embed the data inside the configuration of the source. This is convenient when you have a small and static dataset. Do not use this source to hold a large number of entities.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 30, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``entities``
     - List<Entity>
     - Contains the list of entities is to be served by the source.
     -
     - Yes

   * - ``if_source_empty``
     - Enum<String>
     - Determines the behaviour of the pipe when the source does not contain any entities. Normally, any previously synced
       entities will be deleted even if the pipe does not receive any entities from its source.
       If set to ``"fail"``, the pipe will automatically fail if the source returns no entities. This means that any
       previous entities in the pipe's dataset are not deleted.
       If set to ``"accept"``, the pipe will *not* fail and any previously synced entities will be deleted.

       The global default ``global_defaults.if_source_empty`` can be set for all pipes in the
       :ref:`service metadata <service_metadata_section>`.
     - ``"accept"``
     -

Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``false`` (Default)

   * - ``is_since_comparable``
     - ``true`` (Default)

   * - ``is_chronological``
     - ``false`` (Default)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

Example:

::

    {
        "source": {
            "type": "embedded",
            "entities": [
                {"_id": "a", "title": "A"},
                {"_id": "b", "title": "B"},
                {"_id": "c", "title": "C"}
            ]
        }
    }


