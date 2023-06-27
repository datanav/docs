=================================
SuperOffice to Tripletex Dataflow
=================================

Generated: 2023-06-27 11:28:38

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Tripletex Customer
-----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a SuperOffice Contact if it is connected to a SuperOffice Sale, User, Quote, Person, Quoteline, or Quotealternative that is synchronized into Tripletex.

Once a link between a SuperOffice Contact and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Tripletex Customer Property
     - Tripletex Data Type


SuperOffice Contact to Tripletex Department
-------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Tripletex Department must be established.

A new Tripletex Department will be created from a SuperOffice Contact if it is connected to a SuperOffice User, or Person that is synchronized into Tripletex.

Once a link between a SuperOffice Contact and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


SuperOffice Person to Tripletex Contact
---------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a SuperOffice Person if it is connected to a SuperOffice Sale, Quote, Project, Quoteline, or Quotealternative that is synchronized into Tripletex.

Once a link between a SuperOffice Person and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Tripletex Contact Property
     - Tripletex Data Type


SuperOffice Quotealternative to Tripletex Order
-----------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a Tripletex Order must be established.

A new Tripletex Order will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Quoteline that is synchronized into Tripletex.

Once a link between a SuperOffice Quotealternative and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - Name
     - invoiceComment
     - "string"


SuperOffice Listproductcategoryitems to Tripletex Productgroup
--------------------------------------------------------------
Every SuperOffice Listproductcategoryitems will be synchronized with a Tripletex Productgroup.

Once a link between a SuperOffice Listproductcategoryitems and a Tripletex Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproductcategoryitems and a Tripletex Productgroup:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproductcategoryitems Property
     - Tripletex Productgroup Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


SuperOffice Ownercontactlink to Tripletex Department
----------------------------------------------------
Every SuperOffice Ownercontactlink will be synchronized with a Tripletex Department.

Once a link between a SuperOffice Ownercontactlink and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ownercontactlink and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - name
     - name
     - "string"


SuperOffice Project to Tripletex Project
----------------------------------------
Every SuperOffice Project will be synchronized with a Tripletex Project.

Once a link between a SuperOffice Project and a Tripletex Project is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Project and a Tripletex Project:

.. list-table::
   :header-rows: 1

   * - SuperOffice Project Property
     - Tripletex Project Property
     - Tripletex Data Type
   * - Associate.AssociateId
     - projectManager.id
     - "integer"
   * - EndDate
     - endDate
     - "datetime-format","%Y-%m-%d","_."]
   * - Name
     - name
     - "string"
   * - NextMilestoneDate
     - startDate
     - "datetime-format","%Y-%m-%d","_."]
   * - ProjectMembers.PersonId
     - contact.id
     - "integer"


SuperOffice Quoteline to Tripletex Orderline
--------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Tripletex Orderline.

Once a link between a SuperOffice Quoteline and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Tripletex Orderline Property
     - Tripletex Data Type
   * - DiscountPercent
     - discount
     - "float"
   * - ERPProductKey
     - product.id
     - "integer"
   * - Name
     - description
     - "string"
   * - Quantity
     - count
     - "float"
   * - QuoteAlternativeId
     - order.id
     - "integer"
   * - UnitListPrice
     - unitPriceExcludingVatCurrency
     - "float"
   * - VAT
     - vatType.id
     - "integer"


SuperOffice User to Tripletex Employee
--------------------------------------
Every SuperOffice User will be synchronized with a Tripletex Employee.

Once a link between a SuperOffice User and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - contactId
     - department.id
     - "if", "neq", "_.", "X"], "integer", "string"]
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - personEmail
     - email
     - "string"

