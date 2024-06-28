===============================
Zendesk to Superoffice Dataflow
===============================

Generated: 2024-06-28 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to Superoffice Person
-----------------------------------
Every Zendesk Users will be synchronized with a Superoffice Person.

If a matching Superoffice Person already exists, the Zendesk Users will be merged with the existing one.
If no matching Superoffice Person is found, a new Superoffice Person will be created.

A Zendesk Users will merge with a Superoffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Superoffice Person Property
   * - email
     - Emails.Value

Once a link between a Zendesk Users and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - email
     - Emails.Value
     - "string"
   * - organization_id
     - Contact.ContactId
     - "integer"
   * - phone
     - PrivatePhones.Value
     - "string"


Zendesk Organizations to Superoffice Contact
--------------------------------------------
Every Zendesk Organizations will be synchronized with a Superoffice Contact.

Once a link between a Zendesk Organizations and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - name
     - Name
     - "string"

