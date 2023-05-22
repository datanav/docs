===================================
SuperOffice to PowerOffice Dataflow
===================================

Generated: 2023-05-22 22:04:18

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to PowerOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Listproductcategoryitems to PowerOffice Productgroup
----------------------------------------------------------------
Every SuperOffice Listproductcategoryitems will be synchronized with a PowerOffice Productgroup.

Once a link between a SuperOffice Listproductcategoryitems and a PowerOffice Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproductcategoryitems and a PowerOffice Productgroup:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproductcategoryitems Property
     - PowerOffice Productgroup Property
     - PowerOffice Data Type
   * - Name
     - Name
     - "string"


SuperOffice Product to PowerOffice Product
------------------------------------------
Every SuperOffice Product will be synchronized with a PowerOffice Product.

Once a link between a SuperOffice Product and a PowerOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a PowerOffice Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - PowerOffice Product Property
     - PowerOffice Data Type
   * - Description
     - Description
     - "string"
   * - Name
     - Name
     - "string"
   * - PriceUnit
     - Unit
     - "string"
   * - ProductCategoryKey
     - ProductGroupId
     - "string"
   * - ProductTypeKey
     - Type
     - "string"
   * - UnitCost
     - CostPrice
     - "string"
   * - UnitListPrice
     - SalesPrice
     - "string"
   * - VAT
     - VatCode
     - "string"


SuperOffice Quoteline to PowerOffice Salesorderline
---------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a PowerOffice Salesorderline.

Once a link between a SuperOffice Quoteline and a PowerOffice Salesorderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a PowerOffice Salesorderline:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - PowerOffice Salesorderline Property
     - PowerOffice Data Type
   * - DiscountPercent
     - Discount
     - "string"
   * - Name
     - Description
     - "string"
   * - Quantity
     - Quantity
     - "string"
   * - TotalPrice
     - SalesOrderLineUnitPrice
     - "string"
   * - UnitListPrice
     - SalesOrderLineUnitPrice
     - "string"
   * - VAT
     - VatReturnSpecification
     - "string"


SuperOffice Sale to PowerOffice Salesorder
------------------------------------------
When a Superoffice Sale gets the status "Sold", it  will be synchronized with a PowerOffice Salesorder.

Once a link between a SuperOffice Sale and a PowerOffice Salesorder is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a PowerOffice Salesorder:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - PowerOffice Salesorder Property
     - PowerOffice Data Type
   * - Contact.ContactId
     - DepartmentCode
     - "string"
   * - Currency.Id
     - Currency
     - "string"
   * - Saledate
     - DeliveryDate
     - "string"
   * - Saledate
     - OrderDate
     - "string"


SuperOffice User to PowerOffice Employee
----------------------------------------
Every SuperOffice User will be synchronized with a PowerOffice Employee.

Once a link between a SuperOffice User and a PowerOffice Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a PowerOffice Employee:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - PowerOffice Employee Property
     - PowerOffice Data Type
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"

