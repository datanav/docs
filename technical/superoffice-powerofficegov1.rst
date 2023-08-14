=======================================
SuperOffice to PowerOfficeGov1 Dataflow
=======================================

Generated: 2023-08-14 08:49:52

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to PowerOfficeGov1. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to PowerOfficeGov1 Contact
----------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a PowerOfficeGov1 Contact must be established.

A new PowerOfficeGov1 Contact will be created from a SuperOffice Contact if it is connected to a SuperOffice User, or Person that is synchronized into PowerOfficeGov1.

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

A new PowerOfficeGov1 Customer will be created from a SuperOffice Contact if it is connected to a SuperOffice Contact, or Ownercontactlink that is synchronized into PowerOfficeGov1.

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


SuperOffice Contact to PowerOfficeGov1 Department
-------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a PowerOfficeGov1 Department must be established.

A new PowerOfficeGov1 Department will be created from a SuperOffice Contact if it is connected to a SuperOffice User, or Person that is synchronized into PowerOfficeGov1.

Once a link between a SuperOffice Contact and a PowerOfficeGov1 Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a PowerOfficeGov1 Department:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOfficeGov1 Department Property
     - PowerOfficeGov1 Data Type


SuperOffice Listbusinessitems to PowerOfficeGov1 Listbusinessitems
------------------------------------------------------------------
Every SuperOffice Listbusinessitems will be synchronized with a PowerOfficeGov1 Listbusinessitems.

Once a link between a SuperOffice Listbusinessitems and a PowerOfficeGov1 Listbusinessitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listbusinessitems and a PowerOfficeGov1 Listbusinessitems:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listbusinessitems Property
     - PowerOfficeGov1 Listbusinessitems Property
     - PowerOfficeGov1 Data Type


SuperOffice Listcategoryitems to PowerOfficeGov1 Listcategoryitems
------------------------------------------------------------------
Every SuperOffice Listcategoryitems will be synchronized with a PowerOfficeGov1 Listcategoryitems.

Once a link between a SuperOffice Listcategoryitems and a PowerOfficeGov1 Listcategoryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcategoryitems and a PowerOfficeGov1 Listcategoryitems:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcategoryitems Property
     - PowerOfficeGov1 Listcategoryitems Property
     - PowerOfficeGov1 Data Type


SuperOffice Listproductcategoryitems to PowerOfficeGov1 Listproductcategoryitems
--------------------------------------------------------------------------------
Every SuperOffice Listproductcategoryitems will be synchronized with a PowerOfficeGov1 Listproductcategoryitems.

Once a link between a SuperOffice Listproductcategoryitems and a PowerOfficeGov1 Listproductcategoryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproductcategoryitems and a PowerOfficeGov1 Listproductcategoryitems:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproductcategoryitems Property
     - PowerOfficeGov1 Listproductcategoryitems Property
     - PowerOfficeGov1 Data Type


SuperOffice Listproductcategoryitems to PowerOfficeGov1 Productgroup
--------------------------------------------------------------------
Every SuperOffice Listproductcategoryitems will be synchronized with a PowerOfficeGov1 Productgroup.

Once a link between a SuperOffice Listproductcategoryitems and a PowerOfficeGov1 Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproductcategoryitems and a PowerOfficeGov1 Productgroup:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproductcategoryitems Property
     - PowerOfficeGov1 Productgroup Property
     - PowerOfficeGov1 Data Type


SuperOffice Listproductfamilyitems to PowerOfficeGov1 Listproductfamilyitems
----------------------------------------------------------------------------
Every SuperOffice Listproductfamilyitems will be synchronized with a PowerOfficeGov1 Listproductfamilyitems.

Once a link between a SuperOffice Listproductfamilyitems and a PowerOfficeGov1 Listproductfamilyitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproductfamilyitems and a PowerOfficeGov1 Listproductfamilyitems:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproductfamilyitems Property
     - PowerOfficeGov1 Listproductfamilyitems Property
     - PowerOfficeGov1 Data Type


SuperOffice Listproducttypeitems to PowerOfficeGov1 Listproducttypeitems
------------------------------------------------------------------------
Every SuperOffice Listproducttypeitems will be synchronized with a PowerOfficeGov1 Listproducttypeitems.

Once a link between a SuperOffice Listproducttypeitems and a PowerOfficeGov1 Listproducttypeitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproducttypeitems and a PowerOfficeGov1 Listproducttypeitems:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproducttypeitems Property
     - PowerOfficeGov1 Listproducttypeitems Property
     - PowerOfficeGov1 Data Type


SuperOffice Listprojectstatusitems to PowerOfficeGov1 Listprojectstatusitems
----------------------------------------------------------------------------
Every SuperOffice Listprojectstatusitems will be synchronized with a PowerOfficeGov1 Listprojectstatusitems.

Once a link between a SuperOffice Listprojectstatusitems and a PowerOfficeGov1 Listprojectstatusitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listprojectstatusitems and a PowerOfficeGov1 Listprojectstatusitems:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listprojectstatusitems Property
     - PowerOfficeGov1 Listprojectstatusitems Property
     - PowerOfficeGov1 Data Type


SuperOffice Listprojecttypeitems to PowerOfficeGov1 Listprojecttypeitems
------------------------------------------------------------------------
Every SuperOffice Listprojecttypeitems will be synchronized with a PowerOfficeGov1 Listprojecttypeitems.

Once a link between a SuperOffice Listprojecttypeitems and a PowerOfficeGov1 Listprojecttypeitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listprojecttypeitems and a PowerOfficeGov1 Listprojecttypeitems:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listprojecttypeitems Property
     - PowerOfficeGov1 Listprojecttypeitems Property
     - PowerOfficeGov1 Data Type


SuperOffice Listsaletypeitems to PowerOfficeGov1 Listsaletypeitems
------------------------------------------------------------------
Every SuperOffice Listsaletypeitems will be synchronized with a PowerOfficeGov1 Listsaletypeitems.

Once a link between a SuperOffice Listsaletypeitems and a PowerOfficeGov1 Listsaletypeitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listsaletypeitems and a PowerOfficeGov1 Listsaletypeitems:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listsaletypeitems Property
     - PowerOfficeGov1 Listsaletypeitems Property
     - PowerOfficeGov1 Data Type


SuperOffice Listticketcategoryitems to PowerOfficeGov1 Listticketcategoryitems
------------------------------------------------------------------------------
Every SuperOffice Listticketcategoryitems will be synchronized with a PowerOfficeGov1 Listticketcategoryitems.

Once a link between a SuperOffice Listticketcategoryitems and a PowerOfficeGov1 Listticketcategoryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listticketcategoryitems and a PowerOfficeGov1 Listticketcategoryitems:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listticketcategoryitems Property
     - PowerOfficeGov1 Listticketcategoryitems Property
     - PowerOfficeGov1 Data Type


SuperOffice Ownercontactlink to PowerOfficeGov1 Department
----------------------------------------------------------
Every SuperOffice Ownercontactlink will be synchronized with a PowerOfficeGov1 Department.

Once a link between a SuperOffice Ownercontactlink and a PowerOfficeGov1 Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ownercontactlink and a PowerOfficeGov1 Department:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - PowerOfficeGov1 Department Property
     - PowerOfficeGov1 Data Type


SuperOffice Ownercontactlink to PowerOfficeGov1 Departments
-----------------------------------------------------------
Every SuperOffice Ownercontactlink will be synchronized with a PowerOfficeGov1 Departments.

Once a link between a SuperOffice Ownercontactlink and a PowerOfficeGov1 Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ownercontactlink and a PowerOfficeGov1 Departments:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - PowerOfficeGov1 Departments Property
     - PowerOfficeGov1 Data Type


SuperOffice Product to PowerOfficeGov1 Product
----------------------------------------------
Every SuperOffice Product will be synchronized with a PowerOfficeGov1 Product.

If a matching PowerOfficeGov1 Product already exists, the SuperOffice Product will be merged with the existing one.
If no matching PowerOfficeGov1 Product is found, a new PowerOfficeGov1 Product will be created.

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
Every SuperOffice Product will be synchronized with a PowerOfficeGov1 Productunit.

If a matching PowerOfficeGov1 Productunit already exists, the SuperOffice Product will be merged with the existing one.
If no matching PowerOfficeGov1 Productunit is found, a new PowerOfficeGov1 Productunit will be created.

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


SuperOffice Product to PowerOfficeGov1 Vatcode
----------------------------------------------
Every SuperOffice Product will be synchronized with a PowerOfficeGov1 Vatcode.

Once a link between a SuperOffice Product and a PowerOfficeGov1 Vatcode is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a PowerOfficeGov1 Vatcode:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - PowerOfficeGov1 Vatcode Property
     - PowerOfficeGov1 Data Type


SuperOffice Project to PowerOfficeGov1 Projects
-----------------------------------------------
Every SuperOffice Project will be synchronized with a PowerOfficeGov1 Projects.

Once a link between a SuperOffice Project and a PowerOfficeGov1 Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Project and a PowerOfficeGov1 Projects:

.. list-table::
   :header-rows: 1

   * - SuperOffice Project Property
     - PowerOfficeGov1 Projects Property
     - PowerOfficeGov1 Data Type


SuperOffice Quotealternative to PowerOfficeGov1 Vatcode
-------------------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a PowerOfficeGov1 Vatcode.

Once a link between a SuperOffice Quotealternative and a PowerOfficeGov1 Vatcode is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a PowerOfficeGov1 Vatcode:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - PowerOfficeGov1 Vatcode Property
     - PowerOfficeGov1 Data Type


SuperOffice Quoteline to PowerOfficeGov1 Orderline
--------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a PowerOfficeGov1 Orderline.

Once a link between a SuperOffice Quoteline and a PowerOfficeGov1 Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a PowerOfficeGov1 Orderline:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - PowerOfficeGov1 Orderline Property
     - PowerOfficeGov1 Data Type


SuperOffice Quoteline to PowerOfficeGov1 Quoteline
--------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a PowerOfficeGov1 Quoteline.

Once a link between a SuperOffice Quoteline and a PowerOfficeGov1 Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a PowerOfficeGov1 Quoteline:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - PowerOfficeGov1 Quoteline Property
     - PowerOfficeGov1 Data Type


SuperOffice Quoteline to PowerOfficeGov1 Salesorderline
-------------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a PowerOfficeGov1 Salesorderline.

Once a link between a SuperOffice Quoteline and a PowerOfficeGov1 Salesorderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a PowerOfficeGov1 Salesorderline:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - PowerOfficeGov1 Salesorderline Property
     - PowerOfficeGov1 Data Type


SuperOffice Quoteline to PowerOfficeGov1 Vatcode
------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a PowerOfficeGov1 Vatcode.

Once a link between a SuperOffice Quoteline and a PowerOfficeGov1 Vatcode is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a PowerOfficeGov1 Vatcode:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - PowerOfficeGov1 Vatcode Property
     - PowerOfficeGov1 Data Type


SuperOffice Ticket to PowerOfficeGov1 Tickets
---------------------------------------------
Every SuperOffice Ticket will be synchronized with a PowerOfficeGov1 Tickets.

Once a link between a SuperOffice Ticket and a PowerOfficeGov1 Tickets is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ticket and a PowerOfficeGov1 Tickets:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ticket Property
     - PowerOfficeGov1 Tickets Property
     - PowerOfficeGov1 Data Type


SuperOffice User to PowerOfficeGov1 Employee
--------------------------------------------
Every SuperOffice User will be synchronized with a PowerOfficeGov1 Employee.

If a matching PowerOfficeGov1 Employee already exists, the SuperOffice User will be merged with the existing one.
If no matching PowerOfficeGov1 Employee is found, a new PowerOfficeGov1 Employee will be created.

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


SuperOffice User to PowerOfficeGov1 Listcategoryitems
-----------------------------------------------------
Every SuperOffice User will be synchronized with a PowerOfficeGov1 Listcategoryitems.

Once a link between a SuperOffice User and a PowerOfficeGov1 Listcategoryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a PowerOfficeGov1 Listcategoryitems:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - PowerOfficeGov1 Listcategoryitems Property
     - PowerOfficeGov1 Data Type

