.. _pump_section:

Pumps
=====

Pumps are responsible for "pumping" data through the :ref:`pipe <pipe_section>` by reading :doc:`entities <entitymodel>`
from a :ref:`source <source_section>` and writing them into a :ref:`sink <sink_section>`. The pump is also responsible
for retrying failed writes of entities and logging its activity. It can also write ultimately failed entities to a "dead letter"
dataset for manual inspection. Pumps log their :doc:`execution history <pump-execution>` in a internal dataset with
the id "system:pump_execution:<pipe_id>". See the chapter on :doc:`the pump execution dataset <pump-execution>` for more
details about the contents of this dataset.

Note that if a pipe is scheduled to run on a cron-defined schedule or on a long scheduled interval (i.e. using an
interval more than an hour long) then the scheduled run start time will be persisted. This means that that if the
service is unable to run the pipe at the pre-scheduled time, it will try to run it as soon as possible when it's able.

Prototype
---------

::

    {
        "comment": "This is a comment",
        "schedule_interval": 30,
        "cron_expression": "* * * * *",
        "rescan_run_count": 10,
        "rescan_cron_expression": "* * * * *",
        "partial_rescan_run_count": 5,
        "partial_rescan_delta": 3600,
        "run_at_startup": false,
        "max_read_retries": 0,
        "read_retry_delay": 0,
        "write_retry_delay": 0,
        "max_retries_per_entity": 5,
        "max_consecutive_write_errors": 1,
        "max_write_errors_in_retry_dataset": 0,
        "fallback_to_single_entities_on_batch_fail": true,
        "dead_letter_dataset": "some-dataset-id",
        "track_dead_letters": false,
        "mode": "scheduled",
        "log_events_noop_runs": false,
        "log_events_noop_runs_changes_only": true,
        "notification_granularity": 99999999999
    }

Properties
----------

Note: A pump configuration needs to have either a ``schedule_interval`` *or* a
``cron_expression`` property to govern when the pump should be run. They are mutually exclusive with the
``cron_expression`` taking precedence if both are present. If neither property is set, the ``schedule_interval``
will be set to a default value. For pipes with a :ref:`dataset sink <dataset_sink>` *and* a
:ref:`dataset source <dataset_source>` the default will be 30 seconds +/- 1.5 seconds. For all other pipes, the default
will be 900 seconds +/- 45 seconds. It is good practice to always set the ``cron_expression`` property
on pipes that reads from or writes to external systems.

If you are unfamiliar with `cron expressions <https://en.wikipedia.org/wiki/Cron>`_, you can read more of how
they are formatted in the :doc:`Cron Expressions <cron-expressions>` document.


.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 1

   * - Property
     - Type
     - Description
     - Default
     -
      .. _pump_param_schedule_interval:

   * - ``comment``
     - String or list of strings
     - A human readable comment on the pump (optional).
     -
     -

   * - ``schedule_interval``
     - Number
     - The number of seconds between runs. It is mutually exclusive with the ``cron_expression`` property.
     - (see the note above)
     -
      .. _pump_param_cron_expression:

   * - ``cron_expression``
     - String
     - A cron expression that indicates when the pump should run.
       It is mutually exclusive with the ``schedule_interval`` property.
     -
     -

       .. _pump_rescan_run_count:
   * - ``rescan_run_count``
     - Integer(>=1)
     - How many times the pump should run before scheduling a complete rescan of the source of the pipe that the pump
       is part of. It is mutually exclusive with the ``rescan_cron_expression`` property.
     -
     -

       .. _pump_rescan_cron_expression:
   * - ``rescan_cron_expression``
     - String
     - A cron expression that indicates when the pump should schedule a full rescan of the source of the pipe the pump
       is part of. It is mutually exclusive with the ``rescan_run_count`` property.
     -
     -

   * - ``partial_rescan_run_count``
     - Integer(>=1)
     - How many times the pump should run before scheduling a partial rescan of the
       source of the pipe that the pump is part of. Any complete rescans will take
       precedence if they both apply. If this property is specified then the
       ``partial_rescan_delta`` must also be specified.
     -
     -

   * - ``partial_rescan_delta``
     - Integer(>=1)
     - This specifies the delta to perform a partial rescan of.

       If the since value is an integer the value is substracted.

       Example: If the since value is ``12637`` and the delta value is ``100``, then
       the since value will be shifted to ``12537``.

       If the since value is a timestamp then the value in seconds is substracted.

       Example: If the since value is
       ``"~t2018-04-27T15:46:40Z"`` and the delta value is 3600, then the
       since value will be shifted one hour back to ``"~t2018-04-27T14:46:40Z"``.
     -
     -

   * - ``run_at_startup``
     - Boolean
     - A flag that indicates if the pump should run when Sesam starts up, in addition to the normal schedule
       specified by the ``schedule_interval`` or ``cron_expression`` properties.
     - false
     -


   * - ``use_dead_letter_dataset``
     - Boolean
     - Deprecated. Use the ``dead_letter_dataset`` property instead. This is a flag used to indicate whether to write
       any entities that fail retries to a special "dead letter" dataset. This can only happen if
       ``max_write_errors_in_retry_dataset`` is non-zero and ``max_retries_per_entity`` for
       the particular entity has been exceeded. Note that unspecified dead letter datasets for a pipe has the special
       id pattern ``system:dead-letter:pipe-id``. Only users with the authorization to see the pipe configuration can
       access this dataset.
     -
     -

   * - ``dead_letter_dataset``
     - String
     - This is string that indicates which dataset to write any entities that fail retries if
       ``max_write_errors_in_retry_dataset`` is non-zero and ``max_retries_per_entity`` for the particular entity has
       been exceeded. Only users with the authorization to see the pipe configuration will have access to this dataset.
       The dataset indicated must be unique per pipe.
     -
     -

   * - ``track_dead_letters``
     - Boolean
     - A flag that indicates if the pump should delete any previously "dead letter" entities if a later version of it
       is successfully written to the sink. It is only active if the ``use_dead_letter_dataset`` property is set and
       retries are active. Note that enabling this option wil incur a performance cost because all successfully
       written entities must be looked up in the execution log to determine if it has been previously marked as "dead".
     - false
     -

   * - ``max_read_retries``
     - Integer
     - A counter that indicates to the pump how many times it should retry when failing to read a entity from a source.
       The default (0) means that it should not retry but log an error immediately when encountering read errors.
       See also the ``read_retry_delay`` property.
     - 0
     -

   * - ``read_retry_delay``
     - Number
     - How many seconds to wait before retrying after a read error (i.e. only if ``max_read_retries`` is non-zero).
       The default value is 0 which will retry immediately. If the reason for the read error is non-transient,
       the number of retries set by ``max_read_retries`` will be exhausted quickly - in this case, set this property to
       match the expected interval.
     - 0
     -

   * - ``write_retry_delay``
     - Number
     - How many seconds to wait before retrying after a write error (i.e. only if ``max_consecutive_write_errors`` is
       larger than 1).
       The default value is 0 which will retry immediately. If the reason for the write error is non-transient,
       the number of retries set by ``max_consecutive_write_errors`` will be exhausted quickly - in this case, set this
       property to match the expected interval.
     - 0
     -

   * - ``max_retries_per_entity``
     - Integer
     - A counter that indicates to the pump how many times it should retry a failing entity when writing to a sink before
       giving up on it, which in case it can optionally write it to the dataset referenced in ``dead_letter_dataset``
       (if specified).
     - 5
     -

   * - ``max_consecutive_write_errors``
     - Integer
     - A counter that indicates to the pump how many consecutive write errors it tolerates before terminating the
       current run. The default (1) means it will terminate after the first write error it encounters.
       See also the ``write_retry_delay`` property.
     - 1
     -

   * - ``max_write_errors_in_retry_dataset``
     - Integer
     - A counter that indicates to the pump how many write errors it accepts in its execution history dataset. If the number of
       retryable and not "dead" failed entities in the dataset exceeds this number, the pump will refuse to
       write any more failed entities to the execution dataset and terminate, even if the ``max_retries_per_entity`` or
       ``max_consecutive_write_errors`` is not reached at that point. This purpose of this property is to limit the size of the
       pump execution dataset in the case where a target system is unreachable (or misconfigured). The default value (0) effectively
       disables retries for write errors.
     - 0
     -

   * - ``fallback_to_single_entities_on_batch_fail``
     - Boolean
     - A flag that controls if the pipes should attempt to process a single entity at a time if a batch
       write operation fails. This can be useful to turn off if the cost of processing a single entity at a time
       is prohibitively high. This single-entity-at-a-time fallback is on by default (``true``).
     - true
     -

   * - ``mode``
     - String
     - The mode of operation. Valid options are "``scheduled``" (the default), "``manual``" and
       "``off``".

       Pumps in ``scheduled`` mode will follow the configured schedule and the scheduler can be
       enabled and disabled at runtime.

       Pumps in ``manual`` mode will not be scheduled and can only be operated manually through
       the Service API.

       Pumps in ``off`` mode cannot be started at all.
     - "scheduled"
     -

   * - ``log_events_noop_runs``
     - Boolean
     - A flag that controls if a "noop" ("no-operation") pipe run should be logged in the pipe execution log or not. The default
       value ``false`` means that runs that results in no processed or changed entities (the semantic depends on the type of sink)
       will never be logged. See also the ``log_events_noop_runs_changes_only`` property which controls if the source or
       the sink decides if a run is considered a "noop" or not. Note that any errors or retries will always imply logging
       to the execution dataset.
     - false
     -

   * - ``log_events_noop_runs_changes_only``
     - Boolean
     - A flag that controls what kind of metric is used to determine if a pipe run was a "noop" ("no-operation") run or not.
       The default setting ``true`` means that a run is considered a "noop" run if the sink reported that no entities
       was changed, even if the source produced entities. If it is set to ``false`` then all runs which yielded no
       new entities from the source is considered a "noop" run. Note that any errors or retries will always imply logging
       to the execution dataset.
     - true
     -

   * - ``notification_granularity``
     - int
     - This property lets the pipe "override" the ``log_events_noop_runs`` property and force the pipe to log a run
       at regular intervals, even if it was a "noop" run. The value is in seconds. The default value
       is ``999999999999999`` and means "never". A value of 900 means always log a pipe run if the last logged
       "completed" event is older than 15 minutes). Note that any errors or retries will always imply logging to the
       execution dataset.
     - true
     -


Example configuration
---------------------

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

A scheduled pump running every 30 seconds, no retries or dead letter dataset:

::

    {
        "pump": {
           "schedule_interval": 30
       }
    }

A cron pump running every day at midnight with max 5 retries, maximum 100 retries in the execution log and a dead letter
dataset. Also max ten consecutive write failures allowed:

::

    {
        "pump": {
           "cron_expression": "0 0 * * *",
           "max_retries_per_entity": 5,
           "max_consecutive_write_errors": 10,
           "max_write_errors_in_retry_dataset": 100,
           "dead_letter_dataset": "mypipe-dead-letters"
       }
    }

A scheduled pump running every 30 seconds but do a full rescan of the source every full hour. No retries or dead letter
datasets:

::

    {
        "pump": {
           "schedule_interval": 30,
           "rescan_cron_expression": "0 * * * *"
       }
    }

A scheduled pump running every 5 minutes from 14:00 and ending at 14:55, AND fire every 5 minutes starting at
18:00 and ending at 18:55, every day. No retries or dead letter datasets:

::

    {
        "pump": {
           "cron_expression": "0/5 14,18 * * ?"
       }
    }


.. _pipe_rescans:

Rescans
-------

Definition of terms:

Incremental run:
  This is what a pump does when it is started when the stored "last_seen" value is set to a non-empty value,
  i.e. the pipe will only process source-entities that has appeared after the previous run of the pipe. This is
  the most common way to run a pipe.

Background rescan:
  This is what a pump does when it is started by the :ref:`rescan_cron_expression <pump_rescan_cron_expression>` or
  :ref:`rescan_run_count <pump_rescan_run_count>` config-properties (or if it is manually started by the
  "start-rescan" pump-operation) and :ref:`enable_background_rescan <pipe_settings_enable_background_rescan>` is set
  to ``true``. It will process all the source-entities, and do deletion tracking when finished.

  Only pipes with a :ref:`dataset sink <dataset_sink>` support background rescans. This is because a rescan run
  needs a way to check that it isn't overwriting newer entities from an incremental run, and only the dataset sink
  has the required functionality.

  The rescan functionality is not enabled by default. To enable it, either set the pipe's
  :ref:`enable_background_rescan <pipe_settings_enable_background_rescan>` setting to ``true``
  to enable rescans on that specific pipe, or set the service metadata property
  :ref:`global_defaults.enable_background_rescan <service_metadata_global_defaults_enable_background_rescan>`
  to ``true`` to enable rescans on all pipes.


Reset/Full run:
  This is what a pump does when the user has explicitly reset the pipe. It will process all the source-entities,
  and do deletion tracking when finished.

The use-case for rescans is that the user wants new entities to flow through the pipe as quickly as possible,
but the user also wants to reprocess *all* the source entities. The latter can be very time-consuming, and sometimes
it is not an option to simply reset the pipe to reprocess everything, since that would prevent any new entities from
flowing through the pipe until all the old entities have been processed.

Example: The pipe reads from a sql database-table that has an "last_modified_time"-column, but no "deleted" column;
new and modified rows can be selected with a an appropriate sql-statement, but there is no way to query the sql
database for deleted rows. In this case a rescan can be used to detect deleted rows, while incremental runs can
be used to process new rows at the same time.

There are two different "flavors" of rescans:

1. The entities produced by the incremental runs are known to be correct. This is the case if the user has just
   changed the DTL of a pipe.

   If one or more incremental run has been started while a rescan was in progress, the rescan will stop processing
   entities when it reaches the "last_seen" offset used by the first incremental run.

   If no incremental run has been started, the rescan will proceed past the "last_seen" offset and start to update
   the stored "last_seen" value.  It is not possible to start an incremental run if a rescan is running and it has
   already passed the "last_seen" offset.

   The rescan will not overwrite any entities that have been written by an incremental run.
   At the end of the rescan, the recan will do deletion-tracking, but will not delete any entities that were output
   by the incremental run(s).

   Caveats of doing rescan+incremental runs:

   * The order of the resulting entities can be different that it would be in a normal "reset"-run.
   * Since the rescan can't overwrite entities that has been output by the incremental run, the pipe may not output
     all the versions of an entity that it would in a normal run. This can happen for instance if the pipe has a
     :ref:`dataset source <dataset_source>` with the ``include_previous_versions`` property set to true; once the
     incremental run has output entity "A", any older versions of "A" that is produces by the rescan will be ignored.

2. The entities produced by the incremental run may not be correct in all cases. This is the case if the pipe has
   a "merge"-source, and the user has changed the configuration of the merge-source.

   In this case the incremental run will use the old version of the merge-source, which may produce erronous results.
   The entities from the incremental run will not be put into the sink's seen-tracker. The incremental run will not
   overwrite any entities that have been produced by the rescan run.

   Once the rescan finishes, any incremental run in progress will be stopped. The rescan will then process any entities
   that have appeared since the start of the rescan. Once that is done, the rescan will do deletion-tracking. This will
   delete any erronous entities that was emitted by the incremental run.

   Caveats of doing rescan+incremental runs:

   * The order of the resulting entities can be different that it would be in a normal "reset"-run.
   * The output can temporarily contain erronous entities (produced by the incremental runs).
     Such entities will deleted once the rescan has finished.

Only one incremental run can be active at once, but once an incremental run has finished a new incremental run can be
started. A rescan run can also be started while an incremental run is in progress.

The incremental runs will not do retries, since the rescan will reprocess any previously failed entities.
The incremental runs will do dependency tracking.
