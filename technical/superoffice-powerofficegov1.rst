=======================================
SuperOffice to PowerOfficeGov1 Dataflow
=======================================

Generated: 2023-08-14 08:48:58

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to PowerOfficeGov1. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to PowerOfficeGov1 Contact
----------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a PowerOfficeGov1 Contact must be established.

A SuperOffice Contact will merge with a PowerOfficeGov1 Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOfficeGov1 Contact Property
   * - ContactId
     - ContactId
   * - Emails.Value
     - Emails.Value

Once a link between a SuperOffice Contact and a PowerOfficeGov1 Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a PowerOfficeGov1 Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOfficeGov1 Contact Property
     - PowerOfficeGov1 Data Type


SuperOffice Contact to PowerOfficeGov1 Customer
-----------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a PowerOfficeGov1 Customer must be established.

A SuperOffice Contact will merge with a PowerOfficeGov1 Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOfficeGov1 Customer Property
   * - Emails.Value
     - email
   * - Emails.Value
     - invoiceEmail
   * - Emails.Value
     - overdueNoticeEmail

Once a link between a SuperOffice Contact and a PowerOfficeGov1 Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a PowerOfficeGov1 Customer:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOfficeGov1 Customer Property
     - PowerOfficeGov1 Data Type


SuperOffice Contact to PowerOfficeGov1 Supplier
-----------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a PowerOfficeGov1 Supplier must be established.

A SuperOffice Contact will merge with a PowerOfficeGov1 Supplier if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOfficeGov1 Supplier Property
   * - Emails.Value
     - email
   * - Emails.Value
     - invoiceEmail
   * - Emails.Value
     - overdueNoticeEmail

Once a link between a SuperOffice Contact and a PowerOfficeGov1 Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a PowerOfficeGov1 Supplier:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOfficeGov1 Supplier Property
     - PowerOfficeGov1 Data Type


SuperOffice Ownercontactlink to PowerOfficeGov1 Contact
-------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Ownercontactlink and a PowerOfficeGov1 Contact must be established.

A SuperOffice Ownercontactlink will merge with a PowerOfficeGov1 Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - PowerOfficeGov1 Contact Property
   * - contact_id
     - ContactId

Once a link between a SuperOffice Ownercontactlink and a PowerOfficeGov1 Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ownercontactlink and a PowerOfficeGov1 Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - PowerOfficeGov1 Contact Property
     - PowerOfficeGov1 Data Type


SuperOffice Person to PowerOfficeGov1 Employee
----------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a PowerOfficeGov1 Employee must be established.

A SuperOffice Person will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - PowerOfficeGov1 Employee Property
   * - Emails.Value
     - email

Once a link between a SuperOffice Person and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type


SuperOffice Person to PowerOfficeGov1 Person
--------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a PowerOfficeGov1 Person must be established.

A SuperOffice Person will merge with a PowerOfficeGov1 Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - PowerOfficeGov1 Person Property
   * - Emails.Value
     - Emails.Value

Once a link between a SuperOffice Person and a PowerOfficeGov1 Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a PowerOfficeGov1 Person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - PowerOfficeGov1 Person Property
     - PowerOfficeGov1 Data Type


SuperOffice Product to PowerOfficeGov1 Product
----------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Product and a PowerOfficeGov1 Product must be established.

A SuperOffice Product will merge with a PowerOfficeGov1 Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - PowerOfficeGov1 Product Property
   * - ProductId
     - ProductId
   * - ERPProductKey
     - number
   * - ERPProductKey
     - ERPProductKey

Once a link between a SuperOffice Product and a PowerOfficeGov1 Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a PowerOfficeGov1 Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - PowerOfficeGov1 Product Property
     - PowerOfficeGov1 Data Type


SuperOffice Product to PowerOfficeGov1 Productunit
--------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Product and a PowerOfficeGov1 Productunit must be established.

A SuperOffice Product will merge with a PowerOfficeGov1 Productunit if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - PowerOfficeGov1 Productunit Property
   * - QuantityUnit
     - name

Once a link between a SuperOffice Product and a PowerOfficeGov1 Productunit is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a PowerOfficeGov1 Productunit:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - PowerOfficeGov1 Productunit Property
     - PowerOfficeGov1 Data Type


SuperOffice User to PowerOfficeGov1 Employee
--------------------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a PowerOfficeGov1 Employee must be established.

A SuperOffice User will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - PowerOfficeGov1 Employee Property
   * - personEmail
     - email

Once a link between a SuperOffice User and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type


SuperOffice User to PowerOfficeGov1 Person
------------------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a PowerOfficeGov1 Person must be established.

A SuperOffice User will merge with a PowerOfficeGov1 Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - PowerOfficeGov1 Person Property
   * - personEmail
     - Emails.Value

Once a link between a SuperOffice User and a PowerOfficeGov1 Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a PowerOfficeGov1 Person:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - PowerOfficeGov1 Person Property
     - PowerOfficeGov1 Data Type

