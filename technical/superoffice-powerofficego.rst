=====================================
SuperOffice to PowerOfficeGo Dataflow
=====================================

Generated: 2023-08-14 10:12:52

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Listproductcategoryitems to PowerOfficeGo Productgroup
------------------------------------------------------------------
Every SuperOffice Listproductcategoryitems will be synchronized with a PowerOfficeGo Productgroup.

Once a link between a SuperOffice Listproductcategoryitems and a PowerOfficeGo Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproductcategoryitems and a PowerOfficeGo Productgroup:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproductcategoryitems Property
     - PowerOfficeGo Productgroup Property
     - PowerOfficeGo Data Type
   * - Name
     - Name
     - "string"


SuperOffice Person to PowerOfficeGo Address
-------------------------------------------
Every SuperOffice Person will be synchronized with a PowerOfficeGo Address.

Once a link between a SuperOffice Person and a PowerOfficeGo Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a PowerOfficeGo Address:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - PowerOfficeGo Address Property
     - PowerOfficeGo Data Type
   * - Address.Street.Address1
     - address1
     - "string"
   * - Address.Street.Address2
     - address2
     - "string"
   * - Address.Street.Address3
     - address3
     - "string"
   * - Address.Street.City
     - city
     - "string"
   * - Address.Street.Zipcode
     - zipCode
     - "string"
   * - Country.CountryId
     - countryCode
     - "string"


SuperOffice Product to PowerOfficeGo Product
--------------------------------------------
Every SuperOffice Product will be synchronized with a PowerOfficeGo Product.

Once a link between a SuperOffice Product and a PowerOfficeGo Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a PowerOfficeGo Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - PowerOfficeGo Product Property
     - PowerOfficeGo Data Type
   * - Description
     - Description
     - "string"
   * - Description
     - description
     - "string"
   * - Name
     - Name
     - "string"
   * - Name
     - name
     - "string"
   * - ProductCategoryKey
     - ProductGroupId
     - "string"
   * - ProductCategoryKey
     - productGroupId
     - "string"
   * - ProductTypeKey
     - Type
     - "string"
   * - ProductTypeKey
     - type
     - "string"
   * - QuantityUnit
     - Unit
     - "string"
   * - QuantityUnit
     - unit
     - "string"
   * - QuantityUnit
     - unitOfMeasureCode
     - "string"
   * - UnitCost
     - CostPrice
     - "string"
   * - UnitCost
     - costPrice
     - "string"
   * - UnitListPrice
     - SalesPrice
     - "string"
   * - UnitListPrice
     - salesPrice
     - "string"
   * - VAT
     - VatCode
     - "string"
   * - VAT
     - vatCode
     - "string"


SuperOffice Quoteline to PowerOfficeGo Salesorderline
-----------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a PowerOfficeGo Salesorderline.

Once a link between a SuperOffice Quoteline and a PowerOfficeGo Salesorderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a PowerOfficeGo Salesorderline:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - PowerOfficeGo Salesorderline Property
     - PowerOfficeGo Data Type
   * - DiscountPercent
     - Discount
     - "string"
   * - Name
     - Description
     - "string"
   * - Quantity
     - Quantity
     - "string"
   * - UnitListPrice
     - SalesOrderLineUnitPrice
     - "string"
   * - VAT
     - VatReturnSpecification
     - "string"


SuperOffice User to PowerOfficeGo Employee
------------------------------------------
Every SuperOffice User will be synchronized with a PowerOfficeGo Employee.

Once a link between a SuperOffice User and a PowerOfficeGo Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a PowerOfficeGo Employee:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - PowerOfficeGo Employee Property
     - PowerOfficeGo Data Type
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"


SuperOffice User to PowerOfficeGo Employees
-------------------------------------------
Every SuperOffice User will be synchronized with a PowerOfficeGo Employees.

Once a link between a SuperOffice User and a PowerOfficeGo Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a PowerOfficeGo Employees:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - PowerOfficeGo Employees Property
     - PowerOfficeGo Data Type

