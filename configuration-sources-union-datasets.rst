
.. _union_datasets_source:

Union datasets source
---------------------

The union datasets source is similar to the ``dataset source``, except
it can process several datasets at once and keep track of each one in
its ``since`` marker handler. The union datasets source reads its
datasets in order, exhausting each one before moving to the next.

The entity ``_id`` property in entities is prefixed by the dataset
id separated by the ``:`` character. This is done to prevent unwanted
identity collisions. The entity id ``dave`` from the ``men`` dataset
will end up with the id ``men:dave``, and the entity id ``claire``
from the ``women`` dataset will end up with the id ``women:claire``.

Prototype
^^^^^^^^^

::

    {
        "type": "union_datasets",
        "datasets": ["id-of-dataset1", "id-of-dataset2"],
        "include_previous_versions": false,
        "supports_signalling": false
    }

Properties
^^^^^^^^^^

The configuration of this source is identical to the ``dataset``
source, except ``datasets`` can be a list of datasets ids.

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

   * - ``ignore_non_existent_datasets``
     - Boolean
     - If set to ``false``, datasets listed in ``initial_datasets`` that do not exist will prevent the source from
       being populated. With the default value (``true``) the source will be populated even if one or more datasets
       in ``initial_datasets`` do not exist.
     - true
     -

   * - ``include_previous_versions``
     - Boolean
     - If set to ``false``, the
       data source will only return the latest version of any entity for
       any unique ``_id`` value in the dataset. This is the default behaviour.
     - false
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
     - false
     -

   * - ``prefix_ids``
     - Boolean
     - If set to ``false``, then the entity ids will not be prefixed with the dataset id.
     - true
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
            "type": "union_datasets",
            "datasets": ["northwind:customers", "northwind:orders"],
            "include_previous_versions": true
        }
    }
