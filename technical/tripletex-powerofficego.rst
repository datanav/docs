===================================
Tripletex to PowerOfficeGo Dataflow
===================================

Generated: 2023-08-17 08:30:31

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to PowerOfficeGo Customer
--------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOfficeGo Customer must be established.

A new PowerOfficeGo Customer will be created from a Tripletex Customer if it is connected to a Tripletex Contact that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Customer and a PowerOfficeGo Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGo Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGo Customer Property
     - PowerOfficeGo Data Type
   * - accountManager.id
     - ourReferenceEmployeeCode
     - "string"
   * - email
     - emailAddress
     - "string"
   * - email
     - vatNumber (Dependant on having wd:Q1273217 in mailAddress.countryCodeDependant on having wd:Q1273217 in streetAddresses.countryCode)
     - "string"
   * - id
     - id
     - "string"
   * - invoiceEmail
     - InvoiceEmailAddressCC
     - "string"
   * - invoiceEmail
     - vatNumber (Dependant on having wd:Q1273217 in mailAddress.countryCodeDependant on having wd:Q1273217 in streetAddresses.countryCode)
     - "string"
   * - name
     - legalName
     - "string"
   * - organizationNumber
     - vatNumber (Dependant on having NO in mailAddress.countryCodeDependant on having NOR in mailAddress.countryCodeDependant on having NOR in streetAddresses.countryCodeDependant on having wd:Q11994066 in mailAddress.countryCodeDependant on having wd:Q11994066 in streetAddresses.countryCode)
     - "string"
   * - overdueNoticeEmail
     - vatNumber (Dependant on having wd:Q1273217 in mailAddress.countryCodeDependant on having wd:Q1273217 in streetAddresses.countryCode)
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - phoneNumber
     - phoneNumberMobile
     - "string"
   * - physicalAddress.addressLine1
     - streetAddresses.address1
     - "string"
   * - physicalAddress.addressLine2
     - streetAddresses.address2
     - "string"
   * - physicalAddress.city
     - streetAddresses.city
     - "string"
   * - physicalAddress.country.id
     - streetAddresses.countryCode
     - "string"
   * - physicalAddress.postalCode
     - streetAddresses.zipCode
     - "string"
   * - postalAddress.addressLine1
     - mailAddress.address1
     - "string"
   * - postalAddress.addressLine2
     - mailAddress.address2
     - "string"
   * - postalAddress.city
     - mailAddress.city
     - "string"
   * - postalAddress.country.id
     - mailAddress.countryCode
     - "string"
   * - postalAddress.postalCode
     - mailAddress.zipCode
     - "string"


Tripletex Department to PowerOfficeGo Customer
----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a PowerOfficeGo Customer must be established.

A new PowerOfficeGo Customer will be created from a Tripletex Department if it is connected to a Tripletex Contact that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Department and a PowerOfficeGo Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a PowerOfficeGo Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOfficeGo Customer Property
     - PowerOfficeGo Data Type
   * - name
     - legalName
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


Tripletex Contact to PowerOfficeGo Customers
--------------------------------------------
Every Tripletex Contact will be synchronized with a PowerOfficeGo Customers.

Once a link between a Tripletex Contact and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - email
     - EmailAddress
     - "string"
   * - email
     - emailAddress
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


Tripletex Currency to PowerOfficeGo Currency
--------------------------------------------
Every Tripletex Currency will be synchronized with a PowerOfficeGo Currency.

Once a link between a Tripletex Currency and a PowerOfficeGo Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Currency and a PowerOfficeGo Currency:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - PowerOfficeGo Currency Property
     - PowerOfficeGo Data Type


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
     - "string"
   * - dateOfBirth
     - dateOfBirth
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


Tripletex Order to PowerOfficeGo Salesorder
-------------------------------------------
Every Tripletex Order will be synchronized with a PowerOfficeGo Salesorder.

Once a link between a Tripletex Order and a PowerOfficeGo Salesorder is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a PowerOfficeGo Salesorder:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - PowerOfficeGo Salesorder Property
     - PowerOfficeGo Data Type
   * - currency.id
     - Currency
     - "string"
   * - customer.id
     - DepartmentCode
     - "string"
   * - deliveryDate
     - DeliveryDate
     - "string"
   * - orderDate
     - OrderDate
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
   * - reference
     - PurchaseOrderReference
     - "string"


Tripletex Orderline to PowerOfficeGo Salesorderline
---------------------------------------------------
Every Tripletex Orderline will be synchronized with a PowerOfficeGo Salesorderline.

Once a link between a Tripletex Orderline and a PowerOfficeGo Salesorderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a PowerOfficeGo Salesorderline:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - PowerOfficeGo Salesorderline Property
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
   * - unitPriceExcludingVatCurrency
     - SalesOrderLineUnitPrice
     - "string"
   * - vatType.id
     - VatReturnSpecification
     - "string"


Tripletex Product to PowerOfficeGo Product
------------------------------------------
Every Tripletex Product will be synchronized with a PowerOfficeGo Product.

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
     - "string"
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


Tripletex Supplier to PowerOfficeGo Suppliers
---------------------------------------------
Every Tripletex Supplier will be synchronized with a PowerOfficeGo Suppliers.

Once a link between a Tripletex Supplier and a PowerOfficeGo Suppliers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a PowerOfficeGo Suppliers:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOfficeGo Suppliers Property
     - PowerOfficeGo Data Type
   * - email
     - EmailAddress
     - "string"
   * - id
     - Id
     - "string"
   * - name
     - LegalName
     - "string"
   * - phoneNumber
     - PhoneNumber
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

