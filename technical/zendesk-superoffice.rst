===============================
Zendesk to SuperOffice Dataflow
===============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to SuperOffice Person
-----------------------------------
Every Zendesk Users will be synchronized with a SuperOffice Person.

If a matching SuperOffice Person already exists, the Zendesk Users will be merged with the existing one.
If no matching SuperOffice Person is found, a new SuperOffice Person will be created.

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
   * - email
     - Emails.Value
     - "string"
   * - organization_id
     - Contact.ContactId
     - "integer"
   * - phone
     - PrivatePhones.Value
     - "string"


Zendesk Organizations to SuperOffice Contact
--------------------------------------------
Every Zendesk Organizations will be synchronized with a SuperOffice Contact.

Once a link between a Zendesk Organizations and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - name
     - Name
     - "string"

