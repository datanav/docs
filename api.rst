===
API
===

Introduction
============

Sesam provides a RESTful API for controlling the service and also working with the data in the datahub.


Services
========

.. contents::
   :local:
   :depth: 1

.. cornice-autodoc::
   :modules: lake.node.webapp.api.pipes,
             lake.node.webapp.api.datasets,
             lake.node.webapp.api.external_systems,
             lake.node.webapp.api.providers,
             lake.node.webapp.api.sinks,
             lake.node.webapp.api.scheduled_tasks,
             lake.node.webapp.api.running_tasks,
             lake.node.webapp.api.status


How do I?
=========

Run a scheduled task now
------------------------

POST /scheduled-tasks/{scheduled-task-id} [empty body]

If the scheduled task is not already running, the request returns a "201 (Created)" response with content-type "application/sesam-task+json". The "Location"-header contains a link to the new running job. The body contains a json-representation of the created task.

If the scheduled task is already running, a "409 (Conflict)"-response will be returned. The content-type is "application/sesam-task+json" and the body contains a json-representation of the existing task.


Disable a scheduled task
------------------------

fetch the representation of the scheduled task resource, set the value of the 'is-disabled' property to "true" and then PUT to that resource.

The response to the PUT-request will be a "200 (Ok)"-response with the content-type "application/sesam-scheduled-task+json" and the body contains a json-representation of the updated scheduled task.


Enable a disabled scheduled task
--------------------------------

fetch the representation of the scheduled task resource, set the value of the 'is-disabled' property to "false" and then PUT to that resource.

The response to the PUT-request will be a "200 (Ok)"-response with the content-type "application/sesam-scheduled-task+json" and the body contains a json-representation of the updated scheduled task.


Stop a running task
-------------------

DELETE /running-tasks/{task-id}

or

DELETE /schedules-tasks/{scheduled-task-id}/instance

These request are equivalent. The "/schedules-tasks/{scheduled-task-id}/instance" url always points to the running instance (if any) of a scheduled task.

The response to the DELETE-request will be a "200 (OK)"-response. If the task was still running, the request will have content-type "application/sesam-task+json" and the body will contain a json-representation of the task that was stopped. If the task was not running (i.e. it had already completed), the body will be empty.


Disable a sync
--------------

fetch the representation of the scheduled-task resource for the SyncTask, set the value of the 'is-disabled' property to 'true' and then PUT to that resource.

The response to the PUT-request will be a "200 (Ok)"-response with the content-type "application/sesam-scheduled-task+json" and the body contains a json-representation of the updated scheduled-task.


Enable a sync
-------------

fetch the representation of the scheduled-task resource for the SyncTask, set the value of the 'is-disabled' property to 'false' and then PUT to that resource.

The response to the PUT-request will be a "200 (Ok)"-response with the content-type "application/sesam-scheduled-task+json" and the body contains a json-representation of the updated scheduled-task.

Start a fragments sync now
--------------------------

POST /scheduled-tasks/{synctask-task-id}

If the sync task is not already running, the request returns a "201 (Created)" response with content-type "application/sesam-task+json". The "Location"-header contains a link to the new running job. The body contains a json-representation of the created task.

If the sync task is already running, a "409 (Conflict)"-response will be returned. The content-type is "application/sesam-task+json" and the body contains a json-representation of the existing task.


Start a snapshot now
---------------------

POST /scheduled-tasks/{snapshot-task-id}

If the snapshot task is not already running, the request returns a "201 (Created)" response with content-type "application/sesam-task+json". The "Location"-header contains a link to the new running job. The body contains a json-representation of the created task.

If the snapshot task is already running, a "409 (Conflict)"-response will be returned. The content-type is "application/sesam-task+json" and the body contains a json-representation of the existing task.



Unset last change date
----------------------

fetch the representation of the synctask resource, update the value of the 'last-change' property and then PUT to that resource.



Set last change date
------------------------

fetch the representation of the synctask resource, update the value of the 'last-change' property and then PUT to that resource.



Stop all sync tasks running on a sdshare client
------------------------

client iterates and stops each one.
