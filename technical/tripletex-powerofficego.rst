===================================
Tripletex to PowerOfficeGo Dataflow
===================================

Generated: 2023-10-17 07:52:39

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to PowerOfficeGo Customers person
---------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Tripletex Contact if it is connected to a Tripletex Order, or Orderline that is synchronized into PowerOfficeGo.

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

A new PowerOfficeGo Customers will be created from a Tripletex Contact if it is connected to a Tripletex Order, or Orderline that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Contact and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type


Tripletex Customer to PowerOfficeGo Customers person
----------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Tripletex Customer if it is connected to a Tripletex Order, Contact, or Orderline that is synchronized into PowerOfficeGo.

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


Tripletex Customer to PowerOfficeGo Departments
-----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOfficeGo Departments must be established.

A new PowerOfficeGo Departments will be created from a Tripletex Customer if it is connected to a Tripletex Employee that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Customer and a PowerOfficeGo Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGo Departments:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGo Departments Property
     - PowerOfficeGo Data Type
   * - changes.timestamp
     - CreatedDateTimeOffset
     - "string"
   * - name
     - Name
     - "string"


Tripletex Department to PowerOfficeGo Customers person
------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Tripletex Department if it is connected to a Tripletex Contact that is synchronized into PowerOfficeGo.

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

A new PowerOfficeGo Customers will be created from a Tripletex Department if it is connected to a Tripletex Contact that is synchronized into PowerOfficeGo.

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


Tripletex Order to PowerOfficeGo Outgoinginvoices
-------------------------------------------------
Every Tripletex Order will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a Tripletex Order and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - changes.timestamp
     - createdDateTimeOffset
     - "string"
   * - contact.id
     - customerId
     - "string"
   * - currency.id
     - CurrencyCode
     - "string"
   * - customer.id
     - customerId
     - "string"
   * - deliveryDate
     - DeliveryDate
     - "string"
   * - deliveryDate
     - sentDateTimeOffset
     - "string"
   * - orderDate
     - OrderDate
     - "string"


Tripletex Orderline to PowerOfficeGo Outgoinginvoices
-----------------------------------------------------
Every Tripletex Orderline will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a Tripletex Orderline and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - changes.timestamp
     - createdDateTimeOffset
     - "string"
   * - currency.id
     - CurrencyCode
     - "string"
   * - order.id
     - OrderNo
     - "string"


Tripletex Contact to PowerOfficeGo Contactperson
------------------------------------------------
Every Tripletex Contact will be synchronized with a PowerOfficeGo Contactperson.

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


Tripletex Currency to PowerOfficeGo Currency
--------------------------------------------
Every Tripletex Currency will be synchronized with a PowerOfficeGo Currency.

If a matching PowerOfficeGo Currency already exists, the Tripletex Currency will be merged with the existing one.
If no matching PowerOfficeGo Currency is found, a new PowerOfficeGo Currency will be created.

A Tripletex Currency will merge with a PowerOfficeGo Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - PowerOfficeGo Currency Property
   * - code
     - Code

Once a link between a Tripletex Currency and a PowerOfficeGo Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Currency and a PowerOfficeGo Currency:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - PowerOfficeGo Currency Property
     - PowerOfficeGo Data Type


Tripletex Customer to PowerOfficeGo Customers
---------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a PowerOfficeGo Customers.

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
   * - id
     - Id
     - "string"
   * - invoiceEmail
     - InvoiceEmailAddress
     - "string"
   * - name
     - Name
     - "string"
   * - organizationNumber
     - OrganizationNumber (Dependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCode)
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


Tripletex Department to PowerOfficeGo Departments
-------------------------------------------------
Every Tripletex Department will be synchronized with a PowerOfficeGo Departments.

Once a link between a Tripletex Department and a PowerOfficeGo Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a PowerOfficeGo Departments:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOfficeGo Departments Property
     - PowerOfficeGo Data Type
   * - changes.timestamp
     - CreatedDateTimeOffset
     - "string"
   * - name
     - Name
     - "string"


Tripletex Employee to PowerOfficeGo Employees
---------------------------------------------
Every Tripletex Employee will be synchronized with a PowerOfficeGo Employees.

If a matching PowerOfficeGo Employees already exists, the Tripletex Employee will be merged with the existing one.
If no matching PowerOfficeGo Employees is found, a new PowerOfficeGo Employees will be created.

A Tripletex Employee will merge with a PowerOfficeGo Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOfficeGo Employees Property
   * - nationalIdentityNumber
     - SocialSecurityNumber

Once a link between a Tripletex Employee and a PowerOfficeGo Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOfficeGo Employees:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOfficeGo Employees Property
     - PowerOfficeGo Data Type
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
   * - phoneNumberMobile
     - PhoneNumber
     - "string"
   * - phoneNumberMobile
     - phoneNumber
     - "string"
   * - userType
     - MailAddress.countryCode
     - "string"


Tripletex Employee to PowerOfficeGo Location
--------------------------------------------
Every Tripletex Employee will be synchronized with a PowerOfficeGo Location.

Once a link between a Tripletex Employee and a PowerOfficeGo Location is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOfficeGo Location:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOfficeGo Location Property
     - PowerOfficeGo Data Type
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
     - countryCode
     - "string"
   * - address.postalCode
     - zipCode
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
   * - currency.id
     - CurrencyCode
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


Tripletex Orderline to PowerOfficeGo Salesorderlines
----------------------------------------------------
Every Tripletex Orderline will be synchronized with a PowerOfficeGo Salesorderlines.

Once a link between a Tripletex Orderline and a PowerOfficeGo Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a PowerOfficeGo Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - PowerOfficeGo Salesorderlines Property
     - PowerOfficeGo Data Type
   * - count
     - Quantity
     - "string"
   * - description
     - Description
     - "string"
   * - discount
     - Discount
     - "string"
   * - order.id
     - sesam_SalesOrdersId
     - "string"
   * - unitCostCurrency
     - ProductUnitCost
     - "string"
   * - unitPriceExcludingVatCurrency
     - ProductUnitPrice
     - "string"
   * - unitPriceExcludingVatCurrency
     - SalesOrderLineUnitPrice
     - "string"
   * - vatType.id
     - VatReturnSpecification
     - "string"


Tripletex Product to PowerOfficeGo Product
------------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a PowerOfficeGo Product.

Once a link between a Tripletex Product and a PowerOfficeGo Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a PowerOfficeGo Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - PowerOfficeGo Product Property
     - PowerOfficeGo Data Type
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


Tripletex Productgroup to PowerOfficeGo Productgroup
----------------------------------------------------
Every Tripletex Productgroup will be synchronized with a PowerOfficeGo Productgroup.

Once a link between a Tripletex Productgroup and a PowerOfficeGo Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgroup and a PowerOfficeGo Productgroup:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgroup Property
     - PowerOfficeGo Productgroup Property
     - PowerOfficeGo Data Type
   * - name
     - Name
     - "string"


Tripletex Vattype to PowerOfficeGo Vatcodes
-------------------------------------------
Every Tripletex Vattype will be synchronized with a PowerOfficeGo Vatcodes.

Once a link between a Tripletex Vattype and a PowerOfficeGo Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Vattype and a PowerOfficeGo Vatcodes:

.. list-table::
   :header-rows: 1

   * - Tripletex Vattype Property
     - PowerOfficeGo Vatcodes Property
     - PowerOfficeGo Data Type
   * - name
     - Name
     - "string"
   * - name
     - name
     - "string"
   * - percentage
     - Rate
     - "string"
   * - percentage
     - rate
     - "string"

