===============================
Zendesk to SuperOffice Dataflow
===============================

Generated: 2023-06-27 11:30:12

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to SuperOffice Person
-----------------------------------
Before any synchronization can take place, a link between a Zendesk Users and a SuperOffice Person must be established.

A new SuperOffice Person will be created from a Zendesk Users if it is connected to a Zendesk Tickets that is synchronized into SuperOffice.

A Zendesk Users will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - SuperOffice Person Property
   * - email
     - Emails.Value

Once a link between a Zendesk Users and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - phone
     - PrivatePhones.Value
     - "string"

