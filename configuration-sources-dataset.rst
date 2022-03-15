
.. _dataset_source:

Dataset source
--------------

The dataset source is one of the most commonly used sources in a Sesam installation. It simply presents a stream of entities from a
dataset stored in Sesam. Its configuration is very simple and looks like:

Prototype
^^^^^^^^^

::

    {
        "type": "dataset",
        "dataset": "id-of-dataset",
        "include_previous_versions": false,
        "include_replaced": true,
        "supports_signalling": false
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``dataset``
     - String
     - | A dataset id
     -
     - Yes

   * - ``subset``
     - Array
     - | An ``eq`` DTL expression where the left hand side is the index expression and the right hand side is the value that represents the subset. If the subset is specified then only entities that are in that subset will be read from the source.
       |
       | Example: ``["eq", "_S.category", "tank"]``

       .. NOTE:: Make sure that you use indexes version 2 when you use subsets. The reason is that these support deletes. Indexes version 1 does not.
       .. NOTE:: Subsets currently also return non-latest versions of entities within the subset.
       .. NOTE:: `eq` in subsets behaves the way it does in :ref:`joins <joins>`.
     -
     - No

   * - ``completeness``
     - Boolean
     - If set to ``true``, the dataset source completeness filtering feature is enabled. This will instruct the source to only return source entities that have a ``_ts`` value that is older than or equal to the completeness timestamp value of the source dataset.
     - ``false``
     -

   * - ``include_previous_versions``
     - Boolean
     - If set to ``false``, the dataset source will only return the latest
       version of any entity for any unique ``_id`` value in the dataset. This is the default behaviour.
     - ``false``
     -

   * - ``include_replaced``
     - Boolean
     - If set to ``false``, the dataset source will filter out entities where the ``$replaced`` property is ``true``. This typically used when reading from datasets that have been produced by the :ref:`merge <merge_source>` source.
     - ``true``
     -

   * - ``supports_signalling``
     - Boolean
     - Flag used to enable or disable signalling support between internal pipes (dataset to dataset pipes). If enabled, a pipe
       run is scheduled as soon as the input dataset(s) changes. It does not interrupt any already running pipes.

       See ``global_defaults.use_signalling_internally`` in the :ref:`service metadata <service_metadata_section>` section for more details.

       If signalling is turned on globally, you will have to explicitly set ``supports_signalling`` to ``false`` to
       disable it on individual pipes where you don't want to automatically schedule runs on changes. Note that it is
       automatically disabled (if not explicitly enabled on the source) if the schedule interval is less than 2 minutes or a cron
       expression has been used.
     - ``false``
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
     - ``true`` (Fixed)

   * - ``is_since_comparable``
     - ``true`` (Fixed)

   * - ``is_chronological``
     - ``true`` (Fixed)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "dataset",
            "dataset": "northwind:customers",
            "include_previous_versions": true
        }
    }
