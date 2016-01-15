The task execution dataset
==========================

The task execution dataset is a log (dataset) wich contains entities with information about a particular task's
execution history. The dataset ``id`` is computed from the task's ``_id`` property as "system:task_execution:<task_id>".

It will always contain at least two entities for each time the task runs. The first will have
the ``_id`` "task-started" and the last either "task-ended" *or* "task-completed". In between these entities, there may be
entities recording read- and/or write errors. Depending on the task settings, the write errors can then be retried one or
more times during the next runs.

The task-started entity
-----------------------

The "task-started" is written to the task execution dataset when the task has started, but before any other processing
takes place.

Prototype
^^^^^^^^^

::

    {
        "_id":  "task-started",
        "event_type": "task-started",
        "task_definition": "task-configuration-id",
        "task_instance": "task-instance-id",
        "start_time": "iso-timestamp-in-UTC",
        "source": {
            "the-full": "configuration-entity-of",
            "the-source": "at-the-time-the-task-started"
        },
        "sink": {
            "the-full": "configuration-entity-of",
            "the-sink": "at-the-time-the-task-started"
        },
    }


Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60

   * - Property
     - Type
     - Description

   * - ``_id``
     - String
     - The ``_id`` value for task-started entities is fixed and will always be "task-started"

   * - ``event_type``
     - String
     - The ``event_type`` value for task-started entities is fixed and will always be "task-started"

   * - ``task_definition``
     - String
     - The ``_id`` value of the task configuration used to instantiate the task

   * - ``task_instance``
     - String
     - A GUID value representing the instantiated task instance

   * - ``start_time``
     - String
     - The ISO-formatted timestamp for the timestamp the task started ("YYYY-MM-DDTHH:mm:SS.fZ")

   * - ``source``
     - Object
     - The full configuration for the source of the pipe the task is part of as it was when the task started

   * - ``sink``
     - String
     - The full configuration for the sink of the pipe the task is part of as it was when the task started

The task-completed entity
-------------------------

If the task completes successfully, it will write a "task-completed" entity to the execution log.

Prototype
^^^^^^^^^
::

    {
        "_id":  "task-completed",
        "event_type": "task-completed",
        "task_definition": "task-configuration-id",
        "task_instance": "task-instance-id",
        "start_time": "task-started-timestamp-in-UTC",
        "end_time": "task-ended-iso-timestamp-in-UTC",
        "task_started_location": 1234,
        "retry_entities_exist": false,
        "entities_succeeded": 123,
        "entities_failed": 0
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60

   * - Property
     - Type
     - Description

   * - ``_id``
     - String
     - The ``_id`` value for task-completed entities is fixed and will always be "task-completed".

   * - ``event_type``
     - String
     - The ``event_type`` value for task-completed entities is fixed and will always be "task-completed".

   * - ``task_definition``
     - String
     - The ``_id`` value of the task configuration used to instantiate the task.

   * - ``task_instance``
     - String
     - A GUID value representing the instantiated task instance.

   * - ``start_time``
     - String
     - The ISO-formatted timestamp for the timestamp the task started ("YYYY-MM-DDTHH:mm:SS.fZ").

   * - ``end_time``
     - String
     - The ISO-formatted timestamp for the timestamp the task ended ("YYYY-MM-DDTHH:mm:SS.fZ").

   * - ``task_started_location``
     - Integer
     - The absolute index into the log where the corresponding "task-started" entity is located. It is used by
       the task's retry mechanism to "rewind" the log to the last successfully completed run.

   * - ``retry_entities_exist``
     - Boolean
     - A flag indicating if there was logged any entities that can be retried during this run.

   * - ``entities_succeeded``
     - Integer
     - A counter with the number of entities that was successfully written to the pipe's sink during this run.

   * - ``entities_failed``
     - Integer
     - A counter with the number of entities that failed to be written to the pipe's sink during this run.


The task-failed entity
----------------------

If the task fails for some reason, it will write a "task-failed" entity when it terminates.

Prototype
^^^^^^^^^

::

    {
        "_id":  "task-failed",
        "event_type": "task-failed",
        "task_definition": "task-configuration-id",
        "task_instance": "task-instance-id",
        "start_time": "task-started-timestamp-in-UTC",
        "end_time": "task-ended-iso-timestamp-in-UTC",
        "task_started_location": 1234,
        "retry_entities_exist": true,
        "entities_succeeded": 123,
        "entities_failed": 10,
        "reason_why_stopped": "traceback-info",
        "source": {
            "the-full": "configuration-entity-of",
            "the-source": "at-the-time-the-task-started"
        },
        "sink": {
            "the-full": "configuration-entity-of",
            "the-sink": "at-the-time-the-task-started"
        }
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60

   * - Property
     - Type
     - Description

   * - ``_id``
     - String
     - The ``_id`` value for task-failed entities is fixed and will always be "task-failed".

   * - ``event_type``
     - String
     - The ``event_type`` value for task-failed entities is fixed and will always be "task-failed".

   * - ``task_definition``
     - String
     - The ``_id`` value of the task configuration used to instantiate the task.

   * - ``task_instance``
     - String
     - A GUID value representing the instantiated task instance.

   * - ``start_time``
     - String
     - The ISO-formatted timestamp for the timestamp the task started ("YYYY-MM-DDTHH:mm:SS.fZ").

   * - ``end_time``
     - String
     - The ISO-formatted timestamp for the timestamp the task ended ("YYYY-MM-DDTHH:mm:SS.fZ").

   * - ``task_started_location``
     - Integer
     - The absolute index into the log where the corresponding "task-started" entity is located. It is used by
       the task's retry mechanism to "rewind" the log to the last successfully completed run.

   * - ``retry_entities_exist``
     - Boolean
     - A flag indicating if there was logged any entities that can be retried during this run.

   * - ``entities_succeeded``
     - Integer
     - A counter with the number of entities that was successfully written to the pipe's sink during this run.

   * - ``entities_failed``
     - Integer
     - A counter with the number of entities that failed to be written to the pipe's sink during this run.

   * - ``reason_why_stopped``
     - String
     - Information about why the task failed. It contains among other things a stack trace of the execution failure.

   * - ``source``
     - Object
     - The full configuration for the source of the pipe the task is part of as it was when the task started

   * - ``sink``
     - String
     - The full configuration for the sink of the pipe the task is part of as it was when the task started

The read-error entity
---------------------

The execution dataset also can contain entities that record failed reads and/or entities wich represents retryable
entities (from write errors).

Prototype
^^^^^^^^^

::

    {
        "_id":  "read-error:<GUID>",
        "event_type": "read-error",
        "task_definition": "task-configuration-id",
        "task_instance": "task-instance-id",
        "error_code": 0,
        "event_time": "failure-ISO-timestamp-in-UTC",
        "exception": "traceback-info-from-task",
        "underlying_exception": "the-exception-cast-by-source",
        "source": {
            "the-full": "configuration-entity-of",
            "the-source": "at-the-time-the-task-started"
        }
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60

   * - Property
     - Type
     - Description

   * - ``_id``
     - String
     - The ``_id`` value for read-error entities is computed from the string prefix "read-error:" concatenated with
       a GUID string.

   * - ``event_type``
     - String
     - The ``event_type`` value for read-error entities is fixed and will always be "read-error".

   * - ``task_definition``
     - String
     - The ``_id`` value of the task configuration used to instantiate the task.

   * - ``task_instance``
     - String
     - A GUID value representing the instantiated task instance.

   * - ``error_code``
     - Integer
     - A integer value that will be either ``0``, meaning that the source was unable to establish communications with
       the source system, or ``1`` - meaning that there was an error while trying to read a particular entity from the
       source.

   * - ``event_time``
     - String
     - The ISO-formatted timestamp for the timestamp when the read error happened ("YYYY-MM-DDTHH:mm:SS.fZ").

   * - ``exception``
     - String
     - Information about from the task failure. It a stack trace of the execution failure.

   * - ``underlying_exception``
     - String
     - Information about from the source about the read failure. It contains among other things a stack trace of the
       execution failure in the source.

   * - ``source``
     - Object
     - The full configuration for the source of the pipe the task is part of as it was when the task started

The write-error entity
----------------------

For retryable (write) errors, the entity has a similar form to the "read-error" entity, except irs ``_id`` property is
computed from the entity that was unsuccessfully written. It also contains the complete entity as an embedded
child entity.

Prototype
^^^^^^^^^

::

    {
        "_id":  "write-error:<entity_id>",
        "event_type": "write-error",
        "task_definition": "task-configuration-id",
        "task_instance": "task-instance-id",
        "error_code": 0,
        "event_time": "failure-ISO-timestamp-in-UTC",
        "retry_attempts": 0,
        "retryable": true,
        "dead": false,
        "entity": {
          "_id": "id-of-the-entity",
          "entity-property": "entity-value"
        },
        "exception": "traceback-info-from-task",
        "underlying_exception": "the-exception-cast-by-sink",
        "sink": {
            "the-full": "configuration-entity-of",
            "the-sink": "at-the-time-the-task-started"
        }
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60

   * - Property
     - Type
     - Description

   * - ``_id``
     - String
     - The ``_id`` value for read-error entities is computed from the string prefix "write-error:" concatenated with
       the failed entity ``_id`` property.

   * - ``event_type``
     - String
     - The ``event_type`` value for write-error entities is fixed and will always be "write-error".

   * - ``task_definition``
     - String
     - The ``_id`` value of the task configuration used to instantiate the task.

   * - ``task_instance``
     - String
     - A GUID value representing the instantiated task instance.

   * - ``error_code``
     - Integer
     - A integer value that will be either ``0``, meaning that the sink was unable to establish communications with
       the target system, or ``1`` - meaning that there was an error while writing the particular entity to the
       target system.

   * - ``event_time``
     - String
     - The ISO-formatted timestamp for the timestamp when the write error happened ("YYYY-MM-DDTHH:mm:SS.fZ").

   * - ``retry_attempts``
     - Integer
     - A counter of how many times the failing entity has been retried. Note that the first time it is written to the
       execution dataset it will be 0.

   * - ``retryable``
     - Boolean
     - A flag indicating if the entity can be retried by the retry mechanism. It is used for the case where a new
       version of a entity comes from the source while there also exist a previously failed version in the
       execution dataset. In this case, if the new version is sucessfully written to the sink a new write-error entity
       is written to the log for this entity, but marked as not retryable (i.e ``false`` value) so it can be skipped
       during retries.

   * - ``dead``
     - Boolean
     - A flag indicating if the entity has been given up on, for example having exceeded some number of retries. If a
       dead letter dataset is specified for the task, the "dead" entity will be written there and a final "write-error"
       entity written to the execution with the ``dead`` flag set to ``true``. This entity will then never be retried
       again (until a new version comes along from the source).

   * - ``entity``
     - Object
     - A complete embedded copy of the failed entity.

   * - ``exception``
     - String
     - Information about from the task failure. It a stack trace of the execution failure.

   * - ``underlying_exception``
     - String
     - Information about from the sink about the write failure. It contains among other things a stack trace of the
       execution failure in the sink.

   * - ``sink``
     - Object
     - The full configuration for the sink of the pipe the task is part of as it was when the task started

The notification entity
-----------------------

Sources can emit special types of entities containing a reserved property ``_notification``. If such an entity is
encountered by the task, a special entity is written to the execution log containing the emiotted entity as a child
entity. Note: *This entity is not written to the sink*.

This type of entity is typically used to signal for example a entity warning or error that is not deemed
serious enough to warrant a task termination (for example a fixable parse error in configuration JSON files on disk).

Prototype
^^^^^^^^^

::

    {
        "_id":  "notification:<entity_id>",
        "event_type": "notification",
        "task_definition": "task-configuration-id",
        "task_instance": "task-instance-id",
        "notification_time": "failure-ISO-timestamp-in-UTC",
        "entity": {
          "_id": "id-of-the-entity",
          "entity-property": "entity-value"
        },
        "source": {
            "the-full": "configuration-entity-of",
            "the-source": "at-the-time-the-task-started"
        },
        "sink": {
            "the-full": "configuration-entity-of",
            "the-sink": "at-the-time-the-task-started"
        }
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60

   * - Property
     - Type
     - Description

   * - ``_id``
     - String
     - The ``_id`` value for notification entities is computed from the string prefix "notification:" concatenated with
       the emitted entity ``_id`` property (usually a GUID).

   * - ``event_type``
     - String
     - The ``event_type`` value for notification entities is fixed and will always be "notification".

   * - ``task_definition``
     - String
     - The ``_id`` value of the task configuration used to instantiate the task.

   * - ``task_instance``
     - String
     - A GUID value representing the instantiated task instance.

   * - ``notification_time``
     - String
     - The ISO-formatted timestamp for the timestamp when the notification happened ("YYYY-MM-DDTHH:mm:SS.fZ").

   * - ``entity``
     - Object
     - A complete embedded copy of the entity emitted.

   * - ``source``
     - Object
     - The full configuration for the source of the pipe the task is part of as it was when the task started

   * - ``sink``
     - Object
     - The full configuration for the sink of the pipe the task is part of as it was when the task started
