.. _automatic-reprocessing:

:badge:`Free feature,badge-success badge-pill`

Automatic Reprocessing
======================

When enabled, Automatic Reprocessing will detect when the pipe has fallen out of sync and needs to be reset. When enabled in the pipe, or in service metadata, the pipe will automatically reset itself and perform a full rescan – making sure that it is no longer out of sync. In some situations it may need to rewind a bit, instead of doing a full rescan - in any case you can then be sure that the pipe is no longer out of sync.

Usecase
--------

Automatic Reprocessing is useful when pipes fall out of sync. There are many possible reasons why a pipe may fall out of sync:

- Configuration may change
- Datasets may be deleted and then recreated
- Sources may be truncated
- Data may be restored from backup
- Joins to new datasets can be introduced or datasets that are input to a pipe
- Datasets that are hop-ed to by a pipe may be deleted.

In the cases sabove the pipe should be reset and it should perform a full rescan to get a new view of the data.

When enabled Automatic Reprocessing will automatically detect that the pipe is out of sync and reset it.

How to enable
-------------

When this happens the data output by a pipe is no longer in sync with the input data. By default a pipe will not reset automatically if this happens, but it will maintain a list of datasets that are out of sync. Alternatively one can set the reprocessing policy to automatic so that such resets happen automatically.

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

   * - ``reprocessing_policy``
     - Enum<String>
     - Specifies the policy that the pipe uses to decide if a pipe needs to be reset or not. The default policy for pipes can be set in :ref:`service metadata <service_metadata_global_defaults_reprocessing_policy>`.

       - ``continue`` (the default) means that the pipe will continue processing input entities, and not reset the pipe, even though there might be factors indicating the the pipe should be reset.

       - ``automatic`` means that the pipe will automatically reset the pipe when it finds that there are factors that indicate that the pipe should be reset. The rationale for resetting the pipe is so that input entities can the reprocessed so that the output is correct.
     - ``continue``
     - No
