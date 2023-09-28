=====================================
SuperOffice to PowerOfficeGo Dataflow
=====================================

Generated: 2023-09-28 09:17:28

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Pricelist to PowerOfficeGo Currency
-----------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Pricelist and a PowerOfficeGo Currency must be established.

A SuperOffice Pricelist will merge with a PowerOfficeGo Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Pricelist Property
     - PowerOfficeGo Currency Property
   * - Currency
     - Code

Once a link between a SuperOffice Pricelist and a PowerOfficeGo Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Pricelist and a PowerOfficeGo Currency:

.. list-table::
   :header-rows: 1

   * - SuperOffice Pricelist Property
     - PowerOfficeGo Currency Property
     - PowerOfficeGo Data Type


SuperOffice Contact to PowerOfficeGo Customers person
-----------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a SuperOffice Contact if it is connected to a SuperOffice Quotealternative that is synchronized into PowerOfficeGo.

Once a link between a SuperOffice Contact and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type


SuperOffice Contact to PowerOfficeGo Customers
----------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a PowerOfficeGo Customers must be established.

A new PowerOfficeGo Customers will be created from a SuperOffice Contact if it is connected to a SuperOffice Quotealternative that is synchronized into PowerOfficeGo.

Once a link between a SuperOffice Contact and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - Address.Postal.Address1
     - MailAddress.AddressLine1
     - "string"
   * - Address.Postal.Address1
     - MailAddress.addressLine1
     - "string"
   * - Address.Postal.Address2
     - MailAddress.AddressLine2
     - "string"
   * - Address.Postal.Address2
     - MailAddress.addressLine2
     - "string"
   * - Address.Postal.City
     - MailAddress.City
     - "string"
   * - Address.Postal.City
     - MailAddress.city
     - "string"
   * - Address.Postal.Zipcode
     - MailAddress.ZipCode
     - "string"
   * - Address.Postal.Zipcode
     - MailAddress.zipCode
     - "string"
   * - Address.Street.Address1
     - MailAddress.AddressLine1
     - "string"
   * - Address.Street.Address2
     - MailAddress.AddressLine2
     - "string"
   * - Address.Street.City
     - MailAddress.City
     - "string"
   * - Address.Street.Zipcode
     - MailAddress.ZipCode
     - "string"
   * - ContactId
     - Id
     - "string"
   * - Country.CountryId
     - MailAddress.CountryCode
     - "string"
   * - Country.CountryId
     - MailAddress.countryCode
     - "string"
   * - Country.ThreeLetterISOCountry
     - OrganizationNumber (Dependant on having wd:Q906278 in MailAddress.countryCodeDependant on having wd:Q906278 in MailAddress.countryCodeDependant on having wd:Q906278 in MailAddress.countryCodeDependant on having wd:Q906278 in MailAddress.countryCodeDependant on having wd:Q906278 in MailAddress.countryCodeDependant on having wd:Q906278 in MailAddress.countryCodeDependant on having wd:Q906278 in MailAddress.countryCode)
     - "string"
   * - Emails.Value
     - EmailAddress
     - "string"
   * - Name
     - Name
     - "string"
   * - OrgNr
     - OrganizationNumber (Dependant on having  in MailAddress.countryCodeDependant on having  in MailAddress.countryCodeDependant on having  in MailAddress.countryCodeDependant on having  in MailAddress.countryCodeDependant on having  in MailAddress.countryCodeDependant on having  in MailAddress.countryCodeDependant on having  in MailAddress.countryCode)
     - "string"
   * - Phones.Value
     - Number
     - "string"
   * - Phones.Value
     - PhoneNumber
     - "string"
   * - Urls.Value
     - WebsiteUrl
     - "string"


SuperOffice Contact to PowerOfficeGo Departments
------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a PowerOfficeGo Departments must be established.

A new PowerOfficeGo Departments will be created from a SuperOffice Contact if it is connected to a SuperOffice User that is synchronized into PowerOfficeGo.

Once a link between a SuperOffice Contact and a PowerOfficeGo Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a PowerOfficeGo Departments:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOfficeGo Departments Property
     - PowerOfficeGo Data Type
   * - CreatedDate
     - CreatedDateTimeOffset
     - "string"
   * - Name
     - Name
     - "string"


SuperOffice Quotealternative to PowerOfficeGo Salesorder
--------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a PowerOfficeGo Salesorder must be established.

A new PowerOfficeGo Salesorder will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Quoteline that is synchronized into PowerOfficeGo.

Once a link between a SuperOffice Quotealternative and a PowerOfficeGo Salesorder is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a PowerOfficeGo Salesorder:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - PowerOfficeGo Salesorder Property
     - PowerOfficeGo Data Type


SuperOffice Quotealternative to PowerOfficeGo Salesorders
---------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a PowerOfficeGo Salesorders must be established.

A new PowerOfficeGo Salesorders will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Quoteline that is synchronized into PowerOfficeGo.

Once a link between a SuperOffice Quotealternative and a PowerOfficeGo Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a PowerOfficeGo Salesorders:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - PowerOfficeGo Salesorders Property
     - PowerOfficeGo Data Type
   * - TotalPrice
     - TotalAmount
     - "string"
   * - sesam_SaleId (Dependant on having poweroffice-salesorder in sesam_AcceptedDependant on having poweroffice-salesorder in sesam_AcceptedDependant on having poweroffice-salesorder in sesam_AcceptedDependant on having poweroffice-salesorder in sesam_AcceptedDependant on having poweroffice-salesorder in sesam_Accepted)
     - Id
     - "string"


SuperOffice Quoteline to PowerOfficeGo Outgoinginvoices
-------------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a SuperOffice Quoteline and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - QuoteAlternativeId
     - OrderNo
     - "string"
   * - TotalPrice
     - NetAmount
     - "string"


SuperOffice Listcurrencyitems to PowerOfficeGo Currency
-------------------------------------------------------
Every SuperOffice Listcurrencyitems will be synchronized with a PowerOfficeGo Currency.

If a matching PowerOfficeGo Currency already exists, the SuperOffice Listcurrencyitems will be merged with the existing one.
If no matching PowerOfficeGo Currency is found, a new PowerOfficeGo Currency will be created.

A SuperOffice Listcurrencyitems will merge with a PowerOfficeGo Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - PowerOfficeGo Currency Property
   * - Name
     - Code

Once a link between a SuperOffice Listcurrencyitems and a PowerOfficeGo Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcurrencyitems and a PowerOfficeGo Currency:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - PowerOfficeGo Currency Property
     - PowerOfficeGo Data Type


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


SuperOffice Ownercontactlink to PowerOfficeGo Departments
---------------------------------------------------------
Every SuperOffice Ownercontactlink will be synchronized with a PowerOfficeGo Departments.

Once a link between a SuperOffice Ownercontactlink and a PowerOfficeGo Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ownercontactlink and a PowerOfficeGo Departments:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - PowerOfficeGo Departments Property
     - PowerOfficeGo Data Type
   * - name
     - Name
     - "string"


SuperOffice Person to PowerOfficeGo Location
--------------------------------------------
Every SuperOffice Person will be synchronized with a PowerOfficeGo Location.

Once a link between a SuperOffice Person and a PowerOfficeGo Location is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a PowerOfficeGo Location:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - PowerOfficeGo Location Property
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
   * - VATInfo
     - unitOfMeasureCode
     - "string"


SuperOffice Product to PowerOfficeGo Vatcodes
---------------------------------------------
Every SuperOffice Product will be synchronized with a PowerOfficeGo Vatcodes.

Once a link between a SuperOffice Product and a PowerOfficeGo Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a PowerOfficeGo Vatcodes:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - PowerOfficeGo Vatcodes Property
     - PowerOfficeGo Data Type
   * - QuantityUnit
     - Name
     - "string"
   * - VAT
     - Rate
     - "string"
   * - VAT
     - rate
     - "string"
   * - VATInfo
     - Name
     - "string"
   * - VATInfo
     - name
     - "string"


SuperOffice Quotealternative to PowerOfficeGo Vatcodes
------------------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a PowerOfficeGo Vatcodes.

Once a link between a SuperOffice Quotealternative and a PowerOfficeGo Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a PowerOfficeGo Vatcodes:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - PowerOfficeGo Vatcodes Property
     - PowerOfficeGo Data Type
   * - VAT
     - Rate
     - "string"
   * - VAT
     - rate
     - "string"
   * - VATInfo
     - Name
     - "string"
   * - VATInfo
     - name
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


SuperOffice Quoteline to PowerOfficeGo Vatcodes
-----------------------------------------------
Every SuperOffice Quoteline will be synchronized with a PowerOfficeGo Vatcodes.

Once a link between a SuperOffice Quoteline and a PowerOfficeGo Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a PowerOfficeGo Vatcodes:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - PowerOfficeGo Vatcodes Property
     - PowerOfficeGo Data Type
   * - VAT
     - Rate
     - "string"
   * - VAT
     - rate
     - "string"
   * - VATInfo
     - Name
     - "string"
   * - VATInfo
     - name
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
   * - contactCategory
     - MailAddress.countryCode
     - "string"
   * - contactId
     - DepartmendId
     - "string"
   * - contactId
     - DepartmentId
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - lastName
     - lastName
     - "string"

