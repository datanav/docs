===============================
SuperOffice to Zendesk Dataflow
===============================

Generated: 2023-10-10 20:58:59

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to Zendesk Users
-----------------------------------
Every SuperOffice Person will be synchronized with a Zendesk Users.

If a matching Zendesk Users already exists, the SuperOffice Person will be merged with the existing one.
If no matching Zendesk Users is found, a new Zendesk Users will be created.

A SuperOffice Person will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Zendesk Users Property
   * - Emails.Value
     - email

Once a link between a SuperOffice Person and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - Contact.ContactId
     - organization_id
     - "string"
   * - PrivatePhones.Value
     - phone
     - "string"


SuperOffice User to Zendesk Users
---------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a Zendesk Users must be established.

A SuperOffice User will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Zendesk Users Property
   * - personEmail
     - email

Once a link between a SuperOffice User and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - contactId
     - organization_id
     - "string"


SuperOffice Contact to Zendesk Organisations
--------------------------------------------
Every SuperOffice Contact will be synchronized with a Zendesk Organisations.

Once a link between a SuperOffice Contact and a Zendesk Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Zendesk Organisations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Zendesk Organisations Property
     - Zendesk Data Type
   * - Name
     - name
     - "string"
   * - Urls.Value
     - url
     - "string"

