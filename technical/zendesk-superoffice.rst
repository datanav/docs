===============================
Zendesk to SuperOffice Dataflow
===============================

Generated: 2023-06-27 06:28:45

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to SuperOffice Person
-----------------------------------
Every Zendesk Users will be synchronized with a SuperOffice Person.

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


Zendesk Organisations to SuperOffice Contact
--------------------------------------------
Every Zendesk Organisations will be synchronized with a SuperOffice Contact.

Once a link between a Zendesk Organisations and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organisations and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Zendesk Organisations Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - name
     - Name
     - "string"
   * - url
     - Domains
     - "list"

