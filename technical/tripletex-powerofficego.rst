======================
Tripletex to  Dataflow
======================

Generated: 2023-11-30 00:00:01

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Employee to  Contactperson
------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a  Contactperson must be established.

A Tripletex Employee will merge with a  Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Contactperson Property
   * - email
     - emailAddress
   * - nationalIdentityNumber
     - SocialSecurityNumber

Once a link between a Tripletex Employee and a  Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a  Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Contactperson Property
     -  Data Type
   * - address.addressLine1
     - address1
     - "string"
   * - address.addressLine2
     - address2
     - "string"
   * - address.city
     - city
     - "string"
   * - address.country.id
     - residenceCountryCode
     - "string"
   * - address.postalCode
     - zipCode
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - "datetime-format","%Y-%m-%d","_."]
   * - department.id
     - partyId
     - "integer"
   * - email
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "integer"
   * - lastName
     - lastName
     - "string"
   * - phoneNumberWork
     - phoneNumber
     - "string"


Tripletex Supplier to  Customers
--------------------------------
Before any synchronization can take place, a link between a Tripletex Supplier and a  Customers must be established.

A Tripletex Supplier will merge with a  Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     -  Customers Property
   * - email
     - EmailAddress
   * - email
     - InvoiceEmailAddress
   * - email
     - PaymentReminderEmailAddress

Once a link between a Tripletex Supplier and a  Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a  Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     -  Customers Property
     -  Data Type
   * - deliveryAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - deliveryAddress.city
     - MailAddress.City
     - "string"
   * - deliveryAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - deliveryAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - email
     - EmailAddress
     - "string"
   * - email
     - PaymentReminderEmailAddress
     - "string"
   * - id
     - Id
     - "integer"
   * - invoiceEmail
     - InvoiceEmailAddress
     - "string"
   * - invoiceEmail
     - PaymentReminderEmailAddress
     - "string"
   * - name
     - Name
     - "string"
   * - overdueNoticeEmail
     - PaymentReminderEmailAddress
     - "string"
   * - phoneNumber
     - PhoneNumber
     - "string"
   * - physicalAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - physicalAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - physicalAddress.city
     - MailAddress.City
     - "string"
   * - physicalAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - physicalAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - postalAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - postalAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - postalAddress.city
     - MailAddress.City
     - "string"
   * - postalAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - postalAddress.postalCode
     - MailAddress.ZipCode
     - "string"


Tripletex Contact to PowerOfficeGo Customers person
---------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Tripletex Contact if it is connected to a Tripletex Order, Invoice, or Orderline that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Contact and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type
   * - email
     - EmailAddress
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - phoneNumberWork
     - PhoneNumber
     - "string"


Tripletex Contact to PowerOfficeGo Customers
--------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a PowerOfficeGo Customers must be established.

A new PowerOfficeGo Customers will be created from a Tripletex Contact if it is connected to a Tripletex Order, Invoice, or Orderline that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Contact and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type


Tripletex Customer to PowerOfficeGo Contactperson
-------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOfficeGo Contactperson must be established.

A new PowerOfficeGo Contactperson will be created from a Tripletex Customer if it is connected to a Tripletex Order that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Customer and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type


Tripletex Customer to PowerOfficeGo Customers person
----------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Tripletex Customer if it is connected to a Tripletex Order, Contact, Invoice, Customer, Employee, or Orderline that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Customer and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type
   * - deliveryAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - deliveryAddress.city
     - MailAddress.City
     - "string"
   * - deliveryAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - deliveryAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - id
     - Id
     - "string"
   * - physicalAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - physicalAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - physicalAddress.city
     - MailAddress.City
     - "string"
   * - physicalAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - physicalAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - postalAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - postalAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - postalAddress.city
     - MailAddress.City
     - "string"
   * - postalAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - postalAddress.postalCode
     - MailAddress.ZipCode
     - "string"


Tripletex Department to PowerOfficeGo Customers person
------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Tripletex Department if it is connected to a Tripletex Contact, Customer, or Employee that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Department and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type


Tripletex Department to PowerOfficeGo Customers
-----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a PowerOfficeGo Customers must be established.

A new PowerOfficeGo Customers will be created from a Tripletex Department if it is connected to a Tripletex Contact, Customer, or Employee that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Department and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - name
     - Name
     - "string"


Tripletex Contact to PowerOfficeGo Contactperson
------------------------------------------------
Every Tripletex Contact will be synchronized with a PowerOfficeGo Contactperson.

If a matching PowerOfficeGo Contactperson already exists, the Tripletex Contact will be merged with the existing one.
If no matching PowerOfficeGo Contactperson is found, a new PowerOfficeGo Contactperson will be created.

A Tripletex Contact will merge with a PowerOfficeGo Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGo Contactperson Property
   * - email
     - emailAddress

Once a link between a Tripletex Contact and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type
   * - customer.id
     - partyCustomerCode
     - "string"
   * - customer.id
     - partyId
     - "string"
   * - customer.id
     - partySupplierCode
     - "string"
   * - email
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - phoneNumberWork
     - phoneNumber
     - "string"


Tripletex Currency to  Currency
-------------------------------
Every Tripletex Currency will be synchronized with a  Currency.

If a matching  Currency already exists, the Tripletex Currency will be merged with the existing one.
If no matching  Currency is found, a new  Currency will be created.

A Tripletex Currency will merge with a  Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     -  Currency Property
   * - code
     - code

Once a link between a Tripletex Currency and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Currency and a  Currency:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     -  Currency Property
     -  Data Type


Tripletex Customer to PowerOfficeGo Customers
---------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a PowerOfficeGo Customers.

If a matching PowerOfficeGo Customers already exists, the Tripletex Customer will be merged with the existing one.
If no matching PowerOfficeGo Customers is found, a new PowerOfficeGo Customers will be created.

A Tripletex Customer will merge with a PowerOfficeGo Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGo Customers Property
   * - email
     - EmailAddress
   * - email
     - InvoiceEmailAddress
   * - email
     - PaymentReminderEmailAddress

Once a link between a Tripletex Customer and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - deliveryAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - deliveryAddress.city
     - MailAddress.City
     - "string"
   * - deliveryAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - deliveryAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - email
     - EmailAddress
     - "string"
   * - email
     - PaymentReminderEmailAddress
     - "string"
   * - id
     - Id
     - "string"
   * - invoiceEmail
     - InvoiceEmailAddress
     - "string"
   * - invoiceEmail
     - PaymentReminderEmailAddress
     - "string"
   * - name
     - Name
     - "string"
   * - organizationNumber
     - OrganizationNumber (Dependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.CountryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCode)
     - "string"
   * - overdueNoticeEmail
     - PaymentReminderEmailAddress
     - "string"
   * - phoneNumber
     - Number
     - "string"
   * - phoneNumber
     - PhoneNumber
     - "string"
   * - physicalAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - physicalAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - physicalAddress.city
     - MailAddress.City
     - "string"
   * - physicalAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - physicalAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - postalAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - postalAddress.addressLine1
     - MailAddress.addressLine1
     - "string"
   * - postalAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - postalAddress.addressLine2
     - MailAddress.addressLine2
     - "string"
   * - postalAddress.city
     - MailAddress.City
     - "string"
   * - postalAddress.city
     - MailAddress.city
     - "string"
   * - postalAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - postalAddress.country.id
     - MailAddress.countryCode
     - "string"
   * - postalAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - postalAddress.postalCode
     - MailAddress.zipCode
     - "string"
   * - url
     - WebsiteUrl
     - "string"
   * - website
     - WebsiteUrl
     - "string"


Tripletex Department to  Departments
------------------------------------
Every Tripletex Department will be synchronized with a  Departments.

Once a link between a Tripletex Department and a  Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a  Departments:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     -  Departments Property
     -  Data Type
   * - changes.timestamp
     - CreatedDateTimeOffset
     - "string"
   * - name
     - Name
     - "string"


Tripletex Employee to  Employees
--------------------------------
Every Tripletex Employee will be synchronized with a  Employees.

If a matching  Employees already exists, the Tripletex Employee will be merged with the existing one.
If no matching  Employees is found, a new  Employees will be created.

A Tripletex Employee will merge with a  Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Employees Property
   * - employeeNumber
     - Number

Once a link between a Tripletex Employee and a  Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a  Employees:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Employees Property
     -  Data Type
   * - changes.timestamp
     - EmployeeCreatedDateTimeOffset
     - "string"
   * - changes.timestamp
     - employeeCreatedDateTimeOffset
     - "string"
   * - dateOfBirth
     - DateOfBirth
     - "datetime-format","%Y-%m-%d","_."]
   * - dateOfBirth
     - dateOfBirth
     - "string"
   * - department.id
     - DepartmendId
     - "string"
   * - department.id
     - DepartmentId (Dependant on having wd:Q703534 in JobTitle)
     - "string"
   * - email
     - EmailAddress
     - "string"
   * - employeeNumber
     - Number
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
   * - phoneNumberMobile
     - PhoneNumber
     - "string"
   * - phoneNumberMobile
     - phoneNumber
     - "string"
   * - userType
     - MailAddress.CountryCode
     - "string"
   * - userType
     - MailAddress.countryCode
     - "string"


Tripletex Order to PowerOfficeGo Salesorders
--------------------------------------------
Every Tripletex Order will be synchronized with a PowerOfficeGo Salesorders.

Once a link between a Tripletex Order and a PowerOfficeGo Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a PowerOfficeGo Salesorders:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - PowerOfficeGo Salesorders Property
     - PowerOfficeGo Data Type
   * - changes.timestamp
     - CreatedDateTimeOffset
     - "string"
   * - contact.id
     - CustomerReferenceContactPersonId
     - "string"
   * - currency.id
     - CurrencyCode
     - "string"
   * - customer.id
     - CustomerReferenceContactPersonId
     - "string"
   * - orderDate
     - OrderDate
     - "string"
   * - orderDate
     - SalesOrderDate
     - "string"
   * - reference
     - PurchaseOrderReference
     - "string"


Tripletex Orderline to  Salesorderlines
---------------------------------------
Every Tripletex Orderline will be synchronized with a  Salesorderlines.

Once a link between a Tripletex Orderline and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     -  Salesorderlines Property
     -  Data Type
   * - count
     - Quantity
     - "integer"
   * - description
     - Description
     - "string"
   * - discount
     - Allowance
     - "float"
   * - discount
     - Discount
     - "string"
   * - order.id
     - sesam_SalesOrderId
     - "string"
   * - order.id
     - sesam_SalesOrdersId
     - "string"
   * - product.id
     - ProductCode
     - "string"
   * - product.id
     - ProductId
     - "integer"
   * - unitCostCurrency
     - ProductUnitCost
     - "if", "is-decimal", "decimal", "integer"]
   * - unitPriceExcludingVatCurrency
     - ProductUnitPrice
     - "if", "is-decimal", "decimal", "integer"]
   * - unitPriceExcludingVatCurrency
     - SalesOrderLineUnitPrice
     - "string"
   * - vatType.id
     - VatReturnSpecification
     - "string"


Tripletex Product to  Product
-----------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a  Product.

Once a link between a Tripletex Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Product Property
     -  Data Type
   * - costExcludingVatCurrency
     - CostPrice
     - "string"
   * - costExcludingVatCurrency
     - costPrice
     - "string"
   * - description
     - Description
     - "string"
   * - description
     - description
     - "string"
   * - ean
     - Gtin
     - "string"
   * - ean
     - gtin
     - "string"
   * - name
     - Name
     - "string"
   * - name
     - name
     - "string"
   * - priceExcludingVatCurrency
     - SalesPrice
     - "string"
   * - priceExcludingVatCurrency
     - salesPrice
     - "string"
   * - productUnit.id
     - Unit
     - "string"
   * - productUnit.id
     - unit
     - "string"
   * - productUnit.id
     - unitOfMeasureCode
     - "string"
   * - stockOfGoods
     - AvailableStock
     - "string"
   * - stockOfGoods
     - availableStock
     - "integer"
   * - vatType.id
     - VatCode
     - "string"
   * - vatType.id
     - vatCode
     - "string"


Tripletex Productgroup to  Productgroup
---------------------------------------
Every Tripletex Productgroup will be synchronized with a  Productgroup.

Once a link between a Tripletex Productgroup and a  Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgroup and a  Productgroup:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgroup Property
     -  Productgroup Property
     -  Data Type
   * - name
     - Name
     - "string"

