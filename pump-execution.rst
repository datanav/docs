The Pump Execution Dataset
==========================

The pump execution dataset is a log which contains entities with
information about a particular pump's execution history. The dataset
id is computed from the pump's ``_id`` property as
``system:pump_execution:<pump_id>``.

.. WARNING::

   The pump execution entities are subject to change. Their ids and
   structure may be changed in the future. The dataset is not meant
   to be a public API that applications can use.

It will always contain at least two entities for each time the pump
runs. The first will have the id "pump-started" and the last either
"pump-ended" *or* "pump-completed". In between these entities,
there may be entities recording read errors and/or write
errors. Other informational entities such as "pump-enabled"/"pump-disabled" or "pipe-offset-set" may also be present.

Depending on the pump settings, the write errors can then be
retried one or more times during the next runs.

The pump-started entity
-----------------------

The "pump-started" is written to the pump execution dataset when the pump has started, but before any other processing
takes place.

Prototype
^^^^^^^^^

::

    {
        "_id":  "pump-started",
        "event_type": "pump-started",
        "start_time": "iso-timestamp-in-UTC",
        "sync_type": "type-of-sync",
        "pump_definition": "pump-configuration-id",
        "user": {
            "email": "some@user.com",
            "remote_addr": "127.0.0.1",
            "user_id": "some@user.com"
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
     - The ``_id`` value for pump-started entities is fixed and will always be "pump-started"

   * - ``event_type``
     - String
     - The ``event_type`` value for pump-started entities is fixed and will always be "pump-started"

   * - ``sync_type``
     - Enum<String>
     - The ``sync_type`` value denotes the type of pipe run that produced this log entry. It can be one of the followin
       values: ``full``, ``partial`` or ``incremental``.

   * - ``start_time``
     - String
     - The ISO-formatted timestamp for the timestamp the pump started ("YYYY-MM-DDTHH:mm:SS.fZ")

   * - ``pump_definition``
     - String
     - The ``_id`` value of the pump configuration used to instantiate the pump

   * - ``user``
     - Object
     - Information about the user that started the run, if available.

The pump-completed entity
-------------------------

If the pump completes successfully, it will write a "pump-completed" entity to the execution log.

Prototype
^^^^^^^^^
::

    {
        "_id":  "pump-completed",
        "event_type": "pump-completed",
        "pump_definition": "pump-configuration-id",
        "start_time": "pump-started-timestamp-in-UTC",
        "end_time": "pump-ended-iso-timestamp-in-UTC",
        "sync_type": "type-of-sync",
        "pump_started_location": 1234,
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
     - The ``_id`` value for pump-completed entities is fixed and will always be "pump-completed".

   * - ``event_type``
     - String
     - The ``event_type`` value for pump-completed entities is fixed and will always be "pump-completed".

   * - ``pump_definition``
     - String
     - The ``_id`` value of the pump configuration used to instantiate the pump

   * - ``sync_type``
     - Enum<String>
     - The ``sync_type`` value denotes the type of pipe run that produced this log entry. It can be one of the followin
       values: ``full``, ``partial`` or ``incremental``.

   * - ``start_time``
     - String
     - The ISO-formatted timestamp for the timestamp the pump started ("YYYY-MM-DDTHH:mm:SS.fZ").

   * - ``end_time``
     - String
     - The ISO-formatted timestamp for the timestamp the pump ended ("YYYY-MM-DDTHH:mm:SS.fZ").

   * - ``pump_started_location``
     - Integer
     - The absolute index into the log where the corresponding "pump-started" entity is located. It is used by
       the pump's retry mechanism to "rewind" the log to the last successfully completed run.

   * - ``retry_entities_exist``
     - Boolean
     - A flag indicating if there was logged any entities that can be retried during this run.

   * - ``entities_succeeded``
     - Integer
     - A counter with the number of entities that was successfully written to the pipe's sink during this run.

   * - ``entities_failed``
     - Integer
     - A counter with the number of entities that failed to be written to the pipe's sink during this run.

The pump-failed entity
----------------------

If the pump fails for some reason, it will write a "pump-failed" entity when it terminates.

Prototype
^^^^^^^^^

::

    {
        "_id":  "pump-failed",
        "event_type": "pump-failed",
        "pump_definition": "pump-configuration-id",
        "start_time": "pump-started-timestamp-in-UTC",
        "end_time": "pump-ended-iso-timestamp-in-UTC",
        "pump_started_location": 1234,
        "retry_entities_exist": true,
        "entities_succeeded": 123,
        "entities_failed": 10,
        "reason_why_stopped": "traceback-info",
        "sync_type": "type-of-sync",
        "exception_entity": {
          "_id": "id-of-the-entity",
          "entity-property": "entity-value"
        },
        "node_build_info": {
            "build": null,
            "date": "2021-12-29T13:51:21.566325+00:00",
            "dirty": true,
            "git-revision": "6c8eb3c17",
            "hash": "6c8eb3c17",
            "release": "1.0",
            "teamcity-buildnumber": null,
            "version": "1.0.dev"
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
     - The ``_id`` value for pump-failed entities is fixed and will always be "pump-failed".

   * - ``event_type``
     - String
     - The ``event_type`` value for pump-failed entities is fixed and will always be "pump-failed".

   * - ``sync_type``
     - Enum<String>
     - The ``sync_type`` value denotes the type of pipe run that produced this log entry. It can be one of the followin
       values: ``full``, ``partial`` or ``incremental``.

   * - ``pump_definition``
     - String
     - The ``_id`` value of the pump configuration used to instantiate the pump

   * - ``start_time``
     - String
     - The ISO-formatted timestamp for the timestamp the pump started ("YYYY-MM-DDTHH:mm:SS.fZ").

   * - ``end_time``
     - String
     - The ISO-formatted timestamp for the timestamp the pump ended ("YYYY-MM-DDTHH:mm:SS.fZ").

   * - ``pump_started_location``
     - Integer
     - The absolute index into the log where the corresponding "pump-started" entity is located. It is used by
       the pump's retry mechanism to "rewind" the log to the last successfully completed run.

   * - ``retry_entities_exist``
     - Boolean
     - A flag indicating if there was logged any entities that can be retried during this run.

   * - ``exception_entity``
     - Object
     - A complete embedded copy of the entity that caused the failure (if available).

   * - ``entities_succeeded``
     - Integer
     - A counter with the number of entities that was successfully written to the pipe's sink during this run.

   * - ``entities_failed``
     - Integer
     - A counter with the number of entities that failed to be written to the pipe's sink during this run.

   * - ``reason_why_stopped``
     - String
     - Information about why the pump failed. It contains among other things a stack trace of the execution failure.

   * - ``node_build_info``
     - Object
     - Information about the sesam instance the pipe was run on.

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
        "error_code": 0,
        "event_time": "failure-ISO-timestamp-in-UTC",
        "exception": "traceback-info-from-pump",
        "original_exception": "the-exception-cast-by-source"
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
     - Information about from the pump failure. It a stack trace of the execution failure.

   * - ``original_exception``
     - String
     - Information about from the source about the read failure. It contains among other things a stack trace of the
       execution failure in the source.

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
        "error_code": 0,
        "event_time": "failure-ISO-timestamp-in-UTC",
        "retry_attempts": 0,
        "retryable": false,
        "resolved": true,
        "dead": false,
        "entity": {
          "_id": "id-of-the-entity",
          "entity-property": "entity-value"
        },
        "resolved_entity": {
          "_id": "id-of-the-entity-that-resolved-the-error-if-different",
          "entity-property": "entity-value"
        },
        "exception": "traceback-info-from-pump",
        "original_exception": "the-exception-cast-by-sink",
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

       .. _execution_log_resolved_property:
   * - ``resolved``
     - Boolean
     - A flag indicating if the entity was successfully resolved either by a newer version of the entity or because
       a retry succeeded.

   * - ``dead``
     - Boolean
     - A flag indicating if the entity has been given up on, for example having exceeded some number of retries. If a
       dead letter dataset is specified for the pump, the "dead" entity will be written there and a final "write-error"
       entity written to the execution with the ``dead`` flag set to ``true``. This entity will then never be retried
       again (until a new version comes along from the source).

   * - ``entity``
     - Object
     - A complete embedded copy of the failed entity.

       .. _execution_log_resolved_entity:
   * - ``resolved_entity``
     - Object
     - A complete embedded copy of the entity that resolved the write-error if it was retried (and if it differs from
       ``entity``). This property will only be set if ``resolved`` is also ``true``.

   * - ``exception``
     - String
     - Information about from the pump failure. It a stack trace of the execution failure.

   * - ``original_exception``
     - String
     - Information about from the sink about the write failure. It contains among other things a stack trace of the
       execution failure in the sink.

The pump-offset-set entity
--------------------------

The "pump-offset-set" is written to the pump execution dataset when the pump offset has been set or reset explicitly.

Prototype
^^^^^^^^^

::

    {
        "_id":  "pump-offset-set",
        "event_time": "2022-01-04T13:20:28.630647Z",
        "event_type": "pump-offset-set",
        "is_reset": true,
        "original_pipe_offset": "1033311",
        "pipe_offset": "",
        "user": {
            "email": "some@user.com",
            "remote_addr": "127.0.0.1",
            "user_id": "some@user.com"
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
     - The ``_id`` value for pump-offset-set entities is fixed and will always be "pump-offset-set"

   * - ``event_type``
     - String
     - The ``event_type`` value for pump-started entities is fixed and will always be "pump-offset-set"

   * - ``event_time``
     - String
     - The ISO-formatted timestamp for the timestamp the pump offset was set ("YYYY-MM-DDTHH:mm:SS.fZ")

   * - ``pipe_offset``
     - String
     - The pipe offset that was set.

   * - ``original_pipe_offset``
     - String
     - The pipe offset that was set before it was overwritten.

   * - ``is_reset``
     - Boolean
     - A flag indicating if this was caused by someone resetting the pipe.

   * - ``user``
     - Object
     - Information about the user that started the run, if available.
