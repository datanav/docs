.. _automatic_reprocessing:

:badge:`Free feature,badge-success badge-pill`

Automatic Reprocessing
======================

When enabled, Automatic Reprocessing will detect when a pipe has fallen out of sync and needs to be reset. When enabled in a pipe, or in service metadata, the pipe will automatically reset itself and perform a full rescan – making sure that it is no longer out of sync. In some situations it may rewind a bit instead of doing a full rescan. Both actions will put the pipe back in sync.

Use case
--------

Automatic Reprocessing is useful when pipes fall out of sync. There are many reasons why a pipe may fall out of sync, including:

- The configuration may change
- Datasets may be deleted and then recreated
- Sources may be truncated
- Data may be restored from a backup
- Joins to new datasets can be introduced or datasets that are input to a pipe
- Datasets that are hop-ed to by a pipe may be deleted.

When a pipe falls out of sync the pipe should be reset, and it should perform a full rescan to get a new view of the data.

When enabled, Automatic Reprocessing will automatically detect that the pipe is out of sync and reset it.

How to enable
-------------

By default, a pipe will not reset automatically if it goes out of sync, but it will maintain a list of effected datasets. You can set the property ``reprocessing_policy`` so that resets happen automatically.

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
     - Specifies the policy that the pipe uses to decide if a pipe needs to be reset or not. The default policy for all pipes can be set in :ref:`service metadata <service_metadata_global_defaults_reprocessing_policy>`.

       - ``continue`` (default) - the pipe will continue processing input entities and not reset the pipe. even though there might be factors indicating the the pipe should be reset.

       - ``automatic`` - the pipe will automatically reset itself when it finds that there are factors indicating that it is out of sync. Resetting the pipe reprocesses the input entities so that the output is correct.
     - ``continue``
     - No
