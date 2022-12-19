.. _merge_source:

Merge source
------------

The merge source is a source that is able to infer the sameness of
entities across multiple datasets. The source uses a set of equality
rules to figure out which entities are the same. Equality is resolved
transitively, so if A is the same as B and B is the same as C then A,
B and C are all considered the same.

Deletes will be output for entity ids that are no longer
applicable. This typically happens when an entity is first merged with
one entity and then later merged with some other entities, and the id
of the resulting entity changes. Those entities will also have the
``$replaced`` property set to ``true``.

If an entity is deleted in its source dataset then the entity will not
be merged, but instead output as a standalone entity with ``_deleted``
set to ``true``.

Merging follows the same :ref:`rules <joins>` as joins in ``hops``.


.. admonition:: Good to know

   Equality expressions that return ``null`` or empty lists will not
   cause merging. This fact can be used to your advantage to prevent
   merging from happening in certain situations. An example is to
   filter out the values that you do not want to be merged on.

.. WARNING::

   The merge source version 2 with ``identity`` set to ``first`` does
   support the same entity id originating from more than one source
   dataset, but *only* iff there is an equality set on the ``_id``
   property or the ``$ids`` property for all the datasets that have
   overlapping entity ids.

.. WARNING::

   If configuration changes are required then be aware of the following:

   - Equality rules added after the merge source has processed
     entities from the involved datasets will not cause merging of
     those entities based on the added equality rules. Only equality
     rules available at the time of processing will take effect. If
     that is not what you want then the pipe must be reset/rescanned
     in order to produce the desired result.

   - Using merge source version ``1`` any reordering will require a
     reset of the pipe and maybe deletion of the downstream dataset.

   - For both merge source version ``1`` and ``2`` any removal of
     datasets will require a full run of the pipe to clear the
     entities from the removed datasets from the merge source. If you
     use rescan in the background, the incremental run will produce
     results based on the current state that includes the datasets
     marked for removal.


Prototype
^^^^^^^^^

Variant 1: Explicit equality-rules with the ``equality`` property
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
::

    {
        "type": "merge",
        "version": 2,
        "datasets": ["A a", "B b", "C c", "D d"],
        "equality": [
            ["eq", "a.x", "b.x"],
            ["eq", "b.x", "c.y"],
            ["eq", "c.z", "d.z"],
        ],
        "supports_signalling": false
    }

Variant 2: Implicit equality-rules with the ``equality_sets`` property
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
::

    {
        "type": "merge",
        "version": 2,
        "datasets": ["A a", "B b", "C c", "D d"],
        "equality_sets": [
            ["a.x", "b.x", "c.y"],
            ["c.z", "d.z"],
        ],
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

   * - ``version``
     - Number
     - There are two different versions of the merge source. Note that the default value is ``1`` for compatibility reasons. Version ``1`` is deprecated. Use version ``2`` if this is a new pipe.
     - ``1``
     - No

   * - ``datasets``
     - List<String{>=1}>
     - A list of one or more datasets that are to be merged. Each item in this list is a pair of dataset id and dataset alias. A given dataset can only appear once in this list. The syntax is the same as in the ``datasets`` property in :ref:`hops <hops_dtl_function>`.
     -
     - Yes

   * - ``initial_datasets``
     - List<String{>=0}>
     - By default the source will be considered populated if all the datasets in the ``datasets``  property have been populated. If some of these datasets will never be populated then this property can be used to list the datasets that must be populated before the source is considered populated. You should normally not have to use this property.

       See also the :ref:`dataset sink <dataset_sink>` property ``set_initial_offset``.
     -
     -

   * - ``ignore_non_existent_datasets``
     - Boolean
     - If set to ``false``, datasets listed in ``initial_datasets`` that do not exist will prevent the source from
       being populated. With the default value (``true``) the source will be populated even if one or more datasets
       in ``initial_datasets`` do not exist.
     - true
     -

   * - ``equality``
     - List<EqFunctions{>=0}>
     - A list of zero or more ``eq`` functions that are to be used to decide which entities are the same. The functions must follow the rules for :ref:`joins <joins>` in DTL.
       Note: Consider using the newer ``equality_sets`` property instead.
     -
     - No

   * - ``equality_sets``
     - List<List<ValueExpressions>{>0}>
     - A list of lists with one or more value expressions. This is the preferred alternative to using the old
       ``equality`` property to specify the equality-rules. See below for a detailed explanation of the difference between ``equality`` and ``equality_sets``.
     -
     - No

   * - ``identity``
     - String
     - Specifies the strategy for how to create the ``_id`` of the resulting entities.

       * ``"composite"`` - The default, which is to create an id
         composed of all the ids of the entities involved and the
         offset of the dataset from which they originates.

         Example: ``"0|one1|1|two1|1|two2|2|three3"``. This particular
         id consists of four entity ids from three datasets. If it is
         the result of the prototypical merge source shown above, then
         ``one1`` is the id of an entity from the ``d1`` dataset,
         ``two1`` and ``two2`` are ids of entities from the ``d2``
         dataset, and ``three3`` is the id of an entity from the
         ``d3`` dataset.

         The parts of the composite id are first ordered by the offset
         of the dataset in the ``datasets`` property, then by the
         entities' ``_id`` property. This results in a deterministic
         entity id.

       * ``"first"`` - Similar to the ``composite`` strategy, but uses
         the entity id of the first entity given the same ordering
         rules as above.

         Example: ``"one1"``.
     - ``"composite"``
     - No

   * - ``strategy``
     - String
     - The strategy to use to combine the properties of the merged
       entities. This affects how the resulting entities look.

       The examples below illustrate the results of merging the
       following three entities in this particular order (ids omitted for brevity):
       ``{"x":1}``, ``{"y": [2, 1]}``, ``{"y": 2, "z": [3, 3]}``

       * ``"default"`` - The default is to union all the values. This is similar to how the
         :ref:`merge-union <dtl_transform-merge-union>` DTL function
         works. Duplicates are not removed.

         Example: ``{"x": 1, "y": [2, 1, 2], "z": [3, 3]}``

       * ``"compact"`` - Similar to the default strategy, but tries to
         compact the property values; duplicate values are removed,
         properties with empty lists are dropped, and list properties
         with a single value are turned into single valued properties.

         Example: ``{"x": 1, "y": [2, 1], "z": 3}``

       * ``"list"`` - Returns an entity with a ``$merged`` property
         which contains a list of the merged entities. This strategy
         can be used to implement custom strategies.

         | Example:
         | ``{"$merged": [``
         |   ``{"x": 1},``
         |   ``{"y": [2, 1]},``
         |   ``{"y": 2, "z": [3, 3]}]}``

     - ``"default"``
     - No

   * - ``max_merged``
     - Integer
     - Sets the maximum number of entities that can be merged at a time (not supported in version 1).
       The merge pipe will fail if more than ``max_merged`` entities are attempted merged into a single entity.
       Note that the default value for this property is set in the
       :ref:`service metadata <service_metadata_global_defaults_max_merged>`, and it is recommended to reduce
       this value to limit potential memory usage. The merge source will use an excessive amount of RAM if the number of
       merged entities is too high.
     - ``50000``
     -

       .. _merge_source_property_supports_signalling:

   * - ``supports_signalling``
     - Boolean
     - Flag used to enable or disable signalling support between internal pipes (dataset to dataset pipes). If enabled, a pipe
       run is scheduled as soon as the input dataset(s) changes. It does not interrupt any already running pipes.

       See ``global_defaults.use_signalling_internally`` in the :ref:`service metadata <service_metadata_global_defaults_use_signalling_internally>` section for more details.

       If signalling is enabled globally, you will have to explicitly set ``supports_signalling`` to ``false`` to
       disable it on individual pipes where you don't want to automatically schedule runs on changes. Note that it is
       automatically disabled (if not explicitly enabled on the source) if the schedule interval is less than 2 minutes or a cron
       expression has been used.
     - false
     -

   * - ``if_source_empty``
     - Enum<String>
     - Determines the behaviour of the pipe when the merge source does not return any entities. Normally, any previously synced
       entities will be deleted even if the pipe does not receive any entities from its source.
       If set to ``"fail"``, the pipe will automatically fail if the source returns no entities. This means that any
       previous entities in the pipe's dataset are not deleted.
       If set to ``"accept"``, the pipe will *not* fail and any previously synced entities will be deleted.

       The global default ``global_defaults.if_source_empty`` can be set for all pipes in the
       :ref:`service metadata <service_metadata_section>`.
     - ``"accept"``
     -


"equality" vs "equality_sets"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Equality is resolved transitively, so if A is the same as B and B is the same as C then A,
B and C are all considered the same. With the ``equality`` property, these rules must be specified
one at a time, like this::

        "equality": [
            ["eq", "a.x", "b.x"],
            ["eq", "b.x", "c.y"],
            ["eq", "c.z", "d.z"],
        ],

The ``equality_sets`` property was added as a way to makes it clearer which equality-rules belong together.
The equality-rules above could be expressed like this::

        "equality_sets": [
            ["a.x", "b.x", "c.y"],
            ["c.z", "d.z"],
        ],

Note that the ``equality_sets`` property is just a bit of syntactic sugar; behind the scenes the implicit
equality-rules are added to the rules in the ``equality`` property. This means that you can use both the
``equality_sets`` and the ``equality`` property at the same time if you want (although this is not recommended, since
it makes it harder to figure out the equality-rules). It also means that you will not get a configuration warning if
if you accidentally specify two equality-sets that are actually overlapping. If you for example specify this::

        "equality_sets": [
            ["a.x", "b.x", "c.y"],
            ["c.y", "d.y"],
        ],

you won't actually get two equality-sets, since behind the scenes you end up with these equality-rules::

        "equality": [
            ["eq", "a.x", "b.x"],
            ["eq", "b.x", "c.y"],
            ["eq", "c.y", "d.y"]
        ],

, which is equivalent to specifying a single equality-set, like this::

        "equality_sets": [
            ["a.x", "b.x", "c.y", "d.y"],
        ],

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

Below you'll find three datasets ``A``, ``B`` and ``C`` and a pipe configuration
that uses the ``merge`` source.

Dataset ``A``:

::

   [
       {"_id": "a1", "f1": 1},
       {"_id": "a2", "f1": 2}
   ]

Dataset ``B``:

::

   [
       {"_id": "b1", "f1": 1, "f2": "x"},
       {"_id": "b2", "f1": 3}
   ]

Dataset ``C``:

::

   [
       {"_id": "c1", "f3": "X"},
       {"_id": "c2", "_deleted": true, "f3": "Y"},
       {"_id": "c3", "_deleted": true, "f3": "X"},
   ]


Pipe configuration:

::

   {
       "_id": "result",
       "source": {
           "type": "merge",
           "datasets": ["A a", "B b", "C c"],
           "equality": [
               ["eq", "a.f1", "b.f1"],
               ["eq", "b.f2", ["lower", "c.f3"]],
           ]
       }
   }

Given the above we should expect an output that looks like this:

::

   [
       {"$ids": ["a1", "b1", "c1"], "_id": "0|a1|1|b1|2|c1", "_updated": 0,
        "f1": [1, 1], "f2": "x", "f3": "X"},
       {"$ids": ["a2"], "_id": "0|a2", "_updated": 1, "f1": 2},
       {"$ids": ["b2"], "_id": "1|b2", "_updated": 2, "f1": 3},
       {"$ids": ["c2"], "_deleted": true, "_id": "2|c2", "_updated": 3, "f3": "Y"},
       {"$ids": ["c3"], "_deleted": true, "_id": "2|c3", "_updated": 4, "f3": "X"}
   ]

Entities ``a1``, ``b1`` and ``c1`` have been merged. Entities ``a2``
and ``b2`` did not match any other entities. Deleted entities, like
``c2`` and ``c3``, are never merged with any other entities.

The merged entities are combined so that the properties and their
values are merged in the resulting entity. ``null`` values are kept
intact. List values appear in a consistent order and may contain
duplicate values.

The ``_updated`` property is a sequence number that increases every
time a new entity is generated by the source. Entities appear in
chronological order.

The ``_id`` property is a composite id that consists of the dataset
offset and entity id joined by the ``|`` character. The dataset offset
is the index of the dataset in the ``datasets`` property in the pipe
configuration. The composite parts are ordered by dataset offset and
entity in order to get consistent ids.

The ``$ids`` property contains all the original entity ids of the
entities merged into the entity. Note that an entity id will not be
added to this list if the original entity has the ``$ids``
property. Because of how properties are merged the ``$ids`` will end
up being a union of all the orginal entity ids excluding the entity
ids of the merge entities themselves. This is useful when merging
already merged entities downstream.
