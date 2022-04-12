.. _tutorial_microservices_continuation_support:

Microservices - Continuation support
====================================

In this lesson we will look closer into :ref:`continuation support <continuation_support_microservices>` and change tracking for data imported from a microservice.

.. admonition::  Objectives:
   
    After you complete these tutorials you would have learned the following:

    #. How to implement continuation support in a Microservice
    #. How to implement continuation support in an input pipe

.. admonition:: Pre-requisits

  **Prerequisites**

  This lesson covers how to implement change tracking through continuation support in microservices. Before starting on this lesson we expect a general understanding on input pipes in Sesam and we recommend that you do the tutorial :ref:`Custom Data Source - The Microservice System <tutorial_custom_data_source_microservice>`. 

Disclaimer
----------
Continuation support refers to the functionality which helps the pipe remember what it did last time in order to continue from that spot while change tracking refers to the whole action of importing changes and processing them as a stream of changes in Sesam.

Use-case
--------
In addition to importing contacts (see the tutorial :ref:`Custom Data Source - The Microservice System <tutorial_custom_data_source_microservice>`) the company realizes that importing every contacts every time seems redundant. They would like you to add logic to make sure that only contacts that has been updated since the last time Sesam imported data is included in the new batch. This will save both time and money for the company in the long run.  

Remember
--------
Each API has different functionalities, and not every API supports query parameters to access only updated data. It's important to throuroughly read the API's documentation in order to set the correct query parameter as you since parameter.

Assignment
----------
Write a microservice with :ref:`continuation support <continuation_support_microservices>` that connects to your developer HubSpot account and imports only updated contacts to your Sesam node. You can make sure that only updates are collected by making a minor change to one of your contacts in HubSpot and see if the pipe registers the change.

Use the same microservice template (or the whole microservice if you finished the assignment) as given in :ref:`Custom Data Source - The Microservice System <tutorial_custom_data_source_microservice>` if possible.

.. tip::
    For this assignment it might be beneficial to look into HubSpot's `search <https://developers.hubspot.com/docs/api/crm/search>`_ API.         

Result
------

When finished with this assignment you should still have the same number of contacts inside your Sesam node as you do inside your HubSpot account, only now if you update one of your HubSpot contacts only that contact will be imported to your Sesam node the next time the pipe runs. To make sure everything works the way it should you can look at the pipe's Execution Log. The ``pipe_offset`` in the Execution Log should now reflect your chosen since value, and ``processed_last_run`` should only reflect the number of contacts that has been changed.

