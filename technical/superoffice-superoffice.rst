===================================
SuperOffice to SuperOffice Dataflow
===================================

Generated: 2023-11-29 14:42:03

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Ownercontactlink to SuperOffice Contact
---------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Ownercontactlink and a SuperOffice Contact must be established.

A SuperOffice Ownercontactlink will merge with a SuperOffice Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - SuperOffice Contact Property
   * - contact_id
     - ContactId

Once a link between a SuperOffice Ownercontactlink and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ownercontactlink and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - contact_id
     - ContactId
     - "string"
   * - name
     - Name
     - "string"


SuperOffice User to SuperOffice Person
--------------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a SuperOffice Person must be established.

A SuperOffice User will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - SuperOffice Person Property
   * - personEmail
     - Emails.Value

Once a link between a SuperOffice User and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - contactId
     - Contact.ContactId
     - "integer"
   * - firstName
     - Firstname
     - "string"
   * - lastName
     - Lastname
     - "string"
   * - personEmail
     - Emails.Value
     - "string"


SuperOffice Contact to SuperOffice Person
-----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a SuperOffice Person must be established.

A new SuperOffice Person will be created from a SuperOffice Contact if it is connected to a SuperOffice Sale, or Quote that is synchronized into SuperOffice.

Once a link between a SuperOffice Contact and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - SuperOffice Person Property
     - SuperOffice Data Type


SuperOffice Person to SuperOffice Contact
-----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a SuperOffice Contact must be established.

A new SuperOffice Contact will be created from a SuperOffice Person if it is connected to a SuperOffice Sale, or Quote that is synchronized into SuperOffice.

Once a link between a SuperOffice Person and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - SuperOffice Contact Property
     - SuperOffice Data Type


SuperOffice User to SuperOffice Listcategoryitems
-------------------------------------------------
Every SuperOffice User will be synchronized with a SuperOffice Listcategoryitems.

Once a link between a SuperOffice User and a SuperOffice Listcategoryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a SuperOffice Listcategoryitems:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - SuperOffice Listcategoryitems Property
     - SuperOffice Data Type
   * - contactCategory
     - Name
     - "string"

