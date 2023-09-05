===========================
SuperOffice to Wix Dataflow
===========================

Generated: 2023-09-05 13:57:19

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to Wix Contacts
----------------------------------
Every SuperOffice Person will be synchronized with a Wix Contacts.

If a matching Wix Contacts already exists, the SuperOffice Person will be merged with the existing one.
If no matching Wix Contacts is found, a new Wix Contacts will be created.

A SuperOffice Person will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Wix Contacts Property
   * - Emails.Value
     - info.emails
   * - Emails.Value
     - primaryInfo.email

Once a link between a SuperOffice Person and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Wix Contacts Property
     - Wix Data Type
   * - Emails.Value
     - info.emails
     - "string"
   * - Emails.Value
     - primaryInfo.email
     - "string"
   * - Firstname
     - info.name.first
     - "string"
   * - Lastname
     - info.name.last
     - "string"
   * - MobilePhones.Value
     - info.phones
     - "string"
   * - MobilePhones.Value
     - primaryInfo.phone
     - "string"


SuperOffice Person to Wix Members
---------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Wix Members must be established.

A SuperOffice Person will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Wix Members Property
   * - Emails.Value
     - loginEmail

Once a link between a SuperOffice Person and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Wix Members:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Wix Members Property
     - Wix Data Type
   * - Emails.Value
     - loginEmail
     - "string"


SuperOffice Product to Wix Inventory
------------------------------------
Before any synchronization can take place, a link between a SuperOffice Product and a Wix Inventory must be established.

A SuperOffice Product will merge with a Wix Inventory if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Wix Inventory Property
   * - ERPProductKey
     - id

Once a link between a SuperOffice Product and a Wix Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Wix Inventory:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Wix Inventory Property
     - Wix Data Type


SuperOffice User to Wix Contacts
--------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a Wix Contacts must be established.

A SuperOffice User will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Wix Contacts Property
   * - personEmail
     - info.emails
   * - personEmail
     - primaryInfo.email

Once a link between a SuperOffice User and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Wix Contacts Property
     - Wix Data Type
   * - firstName
     - info.name.first
     - "string"
   * - lastName
     - info.name.last
     - "string"
   * - personEmail
     - info.emails
     - "string"
   * - personEmail
     - primaryInfo.email
     - "string"


SuperOffice User to Wix Members
-------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a Wix Members must be established.

A SuperOffice User will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Wix Members Property
   * - personEmail
     - loginEmail

Once a link between a SuperOffice User and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Wix Members:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Wix Members Property
     - Wix Data Type
   * - personEmail
     - loginEmail
     - "string"

