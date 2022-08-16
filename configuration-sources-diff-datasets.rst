
.. _diff_datasets_source:

Diff datasets source (Experimental)
-----------------------------------

The diff datasets source is similar to the ``merge dataset source``, except that
it also compares the entities from the datasets. The comparison produces a diff and filters out
entities that are equal.

For each merged entity (same as the ``all`` strategy in ``merge dataset source``)
an additional ``$diff`` property is also generated. The diff contains the datasets and values for
the properties that are not equal across all the datasets.

Entity ids are not modified in any way.

Prototype
^^^^^^^^^

::

   {
       "type": "diff_datasets",
       "datasets": ["id-of-dataset1", "id-of-dataset2"]
    }

Properties
^^^^^^^^^^

The configuration only requires the property ``datasets`` which must
be a list of datasets ids.

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``datasets``
     - List<String>
     - A list of datasets ids.
     -
     - Yes

   * - ``initial_datasets``
     - List<String{>=0}>
     - By default the source will be considered populated if all the datasets in the ``datasets``  property have been populated. If some of these datasets will never be populated then this property can be used to list the datasets that must be populated before the source is considered populated. You should normally not have to use this property.

       See also the :ref:`dataset sink <dataset_sink>` property ``set_initial_offset``.
     -
     -

   * - ``whitelist``
     - List<String>
     - The names of the properties to include in the comparison. If there is a
       ``blacklist`` also specified, the whitelist will be filtered against the contents of the
       blacklist.
     -
     -

   * - ``blacklist``
     - List<String>
     - The names of the properties to exclude from the comparison. If there is a
       ``whitelist`` also specified, the blacklist operates on the values of the whitelist (and not
       the properties present in the entities).
     -
     -


   * - ``treat_lists_as_sets``
     - Boolean
     - Flag to indicate if you want to ignore duplicates and ordering of lists in the entities
       you are comparing. This option also affects lists nested deeper inside the entity.
     - false
     -


   * - ``ignore_deletes``
     - Boolean
     - Flag to indicate if you want to ignore deleted entities during the comparison. By default
       there will be produced a difference if one of the datasets contains a deleted entity while
       the other datasets does not contain the deleted entity.

       If ``true`` the deleted entities are treated as if they don't exist.
     - false
     -

   * - ``if_source_empty``
     - Enum<String>
     - Determines the behaviour of the pipe when the datasets do not return any entities. Normally, any previously synced
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
     - ``true`` (Fixed)

   * - ``is_since_comparable``
     - ``true`` (Fixed)

   * - ``is_chronological``
     - ``true`` (Fixed)


Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>`
configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "diff_datasets",
            "datasets": ["product", "other-products"]
        }
    }

Example result
^^^^^^^^^^^^^^

::

   {
       "_id": "some-product",
       "$diff": {
           "price": {
               "products": "price-from-products",
               "other-products": "price-from-other-products",
           }
       }
    }

