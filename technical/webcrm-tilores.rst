==========================
WebCRM to Tilores Dataflow
==========================

Generated: 2024-11-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Persons to Tilores Human
-------------------------------
Every WebCRM Persons will be synchronized with a Tilores Human.

Once a link between a WebCRM Persons and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Persons and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - WebCRM Persons Property
     - Tilores Human Property
     - Tilores Data Type
   * - PersonEmail
     - email
     - "string"
   * - PersonFirstName
     - firstName
     - "string"
   * - PersonLastName
     - lastName
     - "string"
   * - document_number
     - dateOfBirth
     - "string"


WebCRM Users to Tilores Human
-----------------------------
Every WebCRM Users will be synchronized with a Tilores Human.

Once a link between a WebCRM Users and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Users and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - WebCRM Users Property
     - Tilores Human Property
     - Tilores Data Type

