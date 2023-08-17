=======================================
Powerofficego to PowerOfficeGo Dataflow
=======================================

Generated: 2023-08-17 11:02:33

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers to PowerOfficeGo Employees
--------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a PowerOfficeGo Employees must be established.

A Powerofficego Customers will merge with a PowerOfficeGo Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - PowerOfficeGo Employees Property
   * - NationalIdNumber
     - NationalIdNumber

Once a link between a Powerofficego Customers and a PowerOfficeGo Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a PowerOfficeGo Employees:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - PowerOfficeGo Employees Property
     - PowerOfficeGo Data Type
   * - DateOfBirth
     - DateOfBirth
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - Id
     - Id
     - "string"
   * - LastName
     - LastName
     - "string"
   * - MailAddress.addressLine1
     - MailAddress.Address1
     - "string"
   * - MailAddress.addressLine1
     - MailAddress.address1
     - "string"
   * - MailAddress.addressLine2
     - MailAddress.Address2
     - "string"
   * - MailAddress.addressLine2
     - MailAddress.address2
     - "string"
   * - MailAddress.city
     - MailAddress.City
     - "string"
   * - MailAddress.city
     - MailAddress.city
     - "string"
   * - MailAddress.countryCode
     - MailAddress.CountryCode
     - "string"
   * - MailAddress.countryCode
     - MailAddress.countryCode
     - "string"
   * - MailAddress.lastChangedDateTimeOffset
     - MailAddress.LastChanged
     - "string"
   * - MailAddress.lastChangedDateTimeOffset
     - MailAddress.lastChanged
     - "string"
   * - MailAddress.zipCode
     - MailAddress.ZipCode
     - "string"
   * - MailAddress.zipCode
     - MailAddress.zipCode
     - "string"
   * - NationalIdNumber
     - NationalIdNumber
     - "string"
   * - id
     - Id
     - "string"
   * - mailAddress.lastChangedDateTimeOffset
     - MailAddress.LastChanged
     - "string"
   * - mailAddress.zipCode
     - MailAddress.ZipCode
     - "string"
   * - streetAddresses.address1
     - streetAddresses.address1
     - "string"
   * - streetAddresses.address2
     - streetAddresses.address2
     - "string"
   * - streetAddresses.address3
     - streetAddresses.address3
     - "string"
   * - streetAddresses.city
     - streetAddresses.city
     - "string"
   * - streetAddresses.countryCode
     - MailAddress.countryCode
     - "string"
   * - streetAddresses.countryCode
     - streetAddresses.countryCode
     - "string"
   * - streetAddresses.lastChanged
     - streetAddresses.lastChanged
     - "string"
   * - streetAddresses.zipCode
     - streetAddresses.zipCode
     - "string"


Powerofficego Employees to PowerOfficeGo Customers
--------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Employees and a PowerOfficeGo Customers must be established.

A Powerofficego Employees will merge with a PowerOfficeGo Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - PowerOfficeGo Customers Property
   * - NationalIdNumber
     - NationalIdNumber

Once a link between a Powerofficego Employees and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - DateOfBirth
     - DateOfBirth
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - Id
     - Id
     - "string"
   * - Id
     - id
     - "string"
   * - InternationalIdNumber (Dependant on having wd:Q56404156 in InternationalIdType)
     - NationalIdNumber
     - "string"
   * - LastName
     - LastName
     - "string"
   * - MailAddress.Address1
     - MailAddress.addressLine1
     - "string"
   * - MailAddress.Address2
     - MailAddress.addressLine2
     - "string"
   * - MailAddress.City
     - MailAddress.city
     - "string"
   * - MailAddress.CountryCode
     - MailAddress.countryCode
     - "string"
   * - MailAddress.LastChanged
     - MailAddress.lastChangedDateTimeOffset
     - "string"
   * - MailAddress.LastChanged
     - mailAddress.lastChangedDateTimeOffset
     - "string"
   * - MailAddress.ZipCode
     - MailAddress.zipCode
     - "string"
   * - MailAddress.ZipCode
     - mailAddress.zipCode
     - "string"
   * - MailAddress.address1
     - MailAddress.addressLine1
     - "string"
   * - MailAddress.address2
     - MailAddress.addressLine2
     - "string"
   * - MailAddress.city
     - MailAddress.city
     - "string"
   * - MailAddress.countryCode
     - MailAddress.countryCode
     - "string"
   * - MailAddress.countryCode
     - streetAddresses.countryCode
     - "string"
   * - MailAddress.lastChanged
     - MailAddress.lastChangedDateTimeOffset
     - "string"
   * - MailAddress.zipCode
     - MailAddress.zipCode
     - "string"
   * - NationalIdNumber
     - NationalIdNumber
     - "string"
   * - streetAddresses.address1
     - streetAddresses.address1
     - "string"
   * - streetAddresses.address2
     - streetAddresses.address2
     - "string"
   * - streetAddresses.address3
     - streetAddresses.address3
     - "string"
   * - streetAddresses.city
     - streetAddresses.city
     - "string"
   * - streetAddresses.countryCode
     - streetAddresses.countryCode
     - "string"
   * - streetAddresses.lastChanged
     - streetAddresses.lastChanged
     - "string"
   * - streetAddresses.zipCode
     - streetAddresses.zipCode
     - "string"


Powerofficego Outgoinginvoice to PowerOfficeGo Outgoinginvoices
---------------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Outgoinginvoice and a PowerOfficeGo Outgoinginvoices must be established.

A Powerofficego Outgoinginvoice will merge with a PowerOfficeGo Outgoinginvoices if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Outgoinginvoice Property
     - PowerOfficeGo Outgoinginvoices Property
   * - Id
     - Id

Once a link between a Powerofficego Outgoinginvoice and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Outgoinginvoice and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - Powerofficego Outgoinginvoice Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - CreatedDate
     - createdDateTimeOffset
     - "string"
   * - CurrencyCode
     - CurrencyCode
     - "string"
   * - CustomerCode
     - customerId
     - "string"
   * - CustomerEmail
     - customerNo
     - "string"
   * - DeliveryAddress1
     - DeliveryAddress1
     - "string"
   * - DeliveryAddress2
     - DeliveryAddress2
     - "string"
   * - DeliveryAddressCity
     - DeliveryAddressCity
     - "string"
   * - DeliveryAddressCountryCode
     - DeliveryAddressCountryCode
     - "string"
   * - DeliveryAddressZipCode
     - DeliveryAddressZipCode
     - "string"
   * - DeliveryDate
     - DeliveryDate
     - "string"
   * - DeliveryDate
     - sentDateTimeOffset
     - "string"
   * - Id
     - Id
     - "string"
   * - LastChanged
     - lastChangedDateTimeOffset
     - "string"
   * - NetAmount
     - NetAmount
     - "string"
   * - OrderDate
     - OrderDate
     - "string"
   * - OrderNo
     - OrderNo
     - "string"
   * - SentDate
     - DeliveryDate
     - "string"
   * - SentDate
     - sentDateTimeOffset
     - "string"


Powerofficego Supplier to PowerOfficeGo Location
------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Supplier and a PowerOfficeGo Location must be established.

A Powerofficego Supplier will merge with a PowerOfficeGo Location if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGo Location Property
   * - MailAddress.Id
     - id

Once a link between a Powerofficego Supplier and a PowerOfficeGo Location is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Supplier and a PowerOfficeGo Location:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGo Location Property
     - PowerOfficeGo Data Type


Powerofficego Suppliers to PowerOfficeGo Location
-------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Suppliers and a PowerOfficeGo Location must be established.

A Powerofficego Suppliers will merge with a PowerOfficeGo Location if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - PowerOfficeGo Location Property
   * - MailAddress.Id
     - id

Once a link between a Powerofficego Suppliers and a PowerOfficeGo Location is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a PowerOfficeGo Location:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - PowerOfficeGo Location Property
     - PowerOfficeGo Data Type


Powerofficego Customer to PowerOfficeGo Departments
---------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customer and a PowerOfficeGo Departments must be established.

A new PowerOfficeGo Departments will be created from a Powerofficego Customer if it is connected to a Powerofficego Employee, or Customers that is synchronized into PowerOfficeGo.

Once a link between a Powerofficego Customer and a PowerOfficeGo Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a PowerOfficeGo Departments:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGo Departments Property
     - PowerOfficeGo Data Type


Powerofficego Salesorder to PowerOfficeGo Outgoinginvoices
----------------------------------------------------------
Every Powerofficego Salesorder will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a Powerofficego Salesorder and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorder and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorder Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - Currency
     - CurrencyCode
     - "string"
   * - DeliveryDate
     - DeliveryDate
     - "string"
   * - DeliveryDate
     - sentDateTimeOffset
     - "string"
   * - DepartmentCode
     - customerId
     - "string"
   * - OrderDate
     - OrderDate
     - "string"


Powerofficego Salesorderline to PowerOfficeGo Outgoinginvoices
--------------------------------------------------------------
Every Powerofficego Salesorderline will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a Powerofficego Salesorderline and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderline and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderline Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type


Powerofficego Salesorders to PowerOfficeGo Outgoinginvoices
-----------------------------------------------------------
Every Powerofficego Salesorders will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a Powerofficego Salesorders and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - CreatedDateTimeOffset
     - createdDateTimeOffset
     - "string"
   * - CurrencyCode
     - CurrencyCode
     - "string"
   * - NetAmount
     - NetAmount
     - "string"
   * - OrderDate
     - OrderDate
     - "string"
   * - TotalAmount
     - NetAmount
     - "string"


Powerofficego Contactperson to PowerOfficeGo Customers
------------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a PowerOfficeGo Customers.

Once a link between a Powerofficego Contactperson and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - dateOfBirth
     - DateOfBirth
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - "string"
   * - emailAddress
     - EmailAddress
     - "string"
   * - emailAddress
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


Powerofficego Contactperson to PowerOfficeGo Location
-----------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a PowerOfficeGo Location.

Once a link between a Powerofficego Contactperson and a PowerOfficeGo Location is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a PowerOfficeGo Location:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - PowerOfficeGo Location Property
     - PowerOfficeGo Data Type
   * - address1
     - address1
     - "string"
   * - address2
     - address2
     - "string"
   * - city
     - city
     - "string"
   * - residenceCountryCode
     - countryCode
     - "string"
   * - zipCode
     - zipCode
     - "string"


Powerofficego Customer to PowerOfficeGo Contactperson
-----------------------------------------------------
Every Powerofficego Customer will be synchronized with a PowerOfficeGo Contactperson.

Once a link between a Powerofficego Customer and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type
   * - LastName
     - lastName
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - "string"
   * - emailAddress
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "integer"
   * - lastChanged
     - lastChanged
     - "string"
   * - mailAddress.address1
     - address1
     - "string"
   * - mailAddress.address2
     - address2
     - "string"
   * - mailAddress.city
     - city
     - "string"
   * - mailAddress.countryCode
     - residenceCountryCode
     - "string"
   * - mailAddress.zipCode
     - zipCode
     - "string"


Powerofficego Customer to PowerOfficeGo Customers
-------------------------------------------------
Every Powerofficego Customer will be synchronized with a PowerOfficeGo Customers.

If a matching PowerOfficeGo Customers already exists, the Powerofficego Customer will be merged with the existing one.
If no matching PowerOfficeGo Customers is found, a new PowerOfficeGo Customers will be created.

A Powerofficego Customer will merge with a PowerOfficeGo Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGo Customers Property
   * - id
     - Id

Once a link between a Powerofficego Customer and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - InvoiceEmailAddressCC
     - InvoiceEmailAddress
     - "string"
   * - LastName
     - LastName
     - "string"
   * - dateOfBirth
     - DateOfBirth
     - "string"
   * - emailAddress
     - EmailAddress
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - id
     - Id
     - "string"
   * - invoiceEmailAddress
     - InvoiceEmailAddress
     - "string"
   * - invoiceEmailAddressCC
     - InvoiceEmailAddressCC
     - "string"
   * - legalName
     - Name
     - "string"
   * - mailAddress.address1
     - MailAddress.addressLine1
     - "string"
   * - mailAddress.address2
     - MailAddress.addressLine2
     - "string"
   * - mailAddress.city
     - MailAddress.city
     - "string"
   * - mailAddress.countryCode
     - MailAddress.countryCode
     - "string"
   * - mailAddress.lastChanged
     - MailAddress.lastChangedDateTimeOffset
     - "string"
   * - mailAddress.zipCode
     - MailAddress.zipCode
     - "string"
   * - phoneNumber
     - Number
     - "string"
   * - phoneNumber
     - PhoneNumber
     - "string"
   * - streetAddresses.countryCode
     - MailAddress.countryCode
     - "string"
   * - vatNumber
     - OrganizationNumber (Dependant on having  in MailAddress.countryCode)
     - "string"
   * - websiteUrl
     - WebsiteUrl
     - "string"


Powerofficego Customers to PowerOfficeGo Contactperson
------------------------------------------------------
Every Powerofficego Customers will be synchronized with a PowerOfficeGo Contactperson.

Once a link between a Powerofficego Customers and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type
   * - DateOfBirth
     - dateOfBirth
     - "string"
   * - EmailAddress
     - emailAddress
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - "string"
   * - emailAddress
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"


Powerofficego Employee to PowerOfficeGo Employees
-------------------------------------------------
Every Powerofficego Employee will be synchronized with a PowerOfficeGo Employees.

If a matching PowerOfficeGo Employees already exists, the Powerofficego Employee will be merged with the existing one.
If no matching PowerOfficeGo Employees is found, a new PowerOfficeGo Employees will be created.

A Powerofficego Employee will merge with a PowerOfficeGo Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employee Property
     - PowerOfficeGo Employees Property
   * - Id
     - Id
   * - id
     - Id

Once a link between a Powerofficego Employee and a PowerOfficeGo Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employee and a PowerOfficeGo Employees:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employee Property
     - PowerOfficeGo Employees Property
     - PowerOfficeGo Data Type
   * - DateOfBirth
     - DateOfBirth
     - "string"
   * - EmailAddress
     - EmailAddress
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - Id
     - Id
     - "string"
   * - InternationalIdNumber (Dependant on having wd:Q56404156 in InternationalIdType)
     - NationalIdNumber
     - "string"
   * - JobTitle
     - JobTitle
     - "string"
   * - LastName
     - LastName
     - "string"
   * - MailAddress.Address1
     - MailAddress.address1
     - "string"
   * - MailAddress.Address2
     - MailAddress.address2
     - "string"
   * - MailAddress.Address3
     - MailAddress.address3
     - "string"
   * - MailAddress.City
     - MailAddress.city
     - "string"
   * - MailAddress.CountryCode
     - MailAddress.countryCode
     - "string"
   * - MailAddress.LastChanged
     - MailAddress.lastChanged
     - "string"
   * - MailAddress.ZipCode
     - MailAddress.zipCode
     - "string"
   * - createdDate
     - EmployeeCreatedDateTimeOffset
     - "string"


Powerofficego Salesorder to PowerOfficeGo Salesorders
-----------------------------------------------------
Every Powerofficego Salesorder will be synchronized with a PowerOfficeGo Salesorders.

Once a link between a Powerofficego Salesorder and a PowerOfficeGo Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorder and a PowerOfficeGo Salesorders:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorder Property
     - PowerOfficeGo Salesorders Property
     - PowerOfficeGo Data Type
   * - Currency
     - CurrencyCode
     - "string"
   * - OrderDate
     - OrderDate
     - "string"


Powerofficego Salesorders to PowerOfficeGo Salesorder
-----------------------------------------------------
Every Powerofficego Salesorders will be synchronized with a PowerOfficeGo Salesorder.

Once a link between a Powerofficego Salesorders and a PowerOfficeGo Salesorder is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a PowerOfficeGo Salesorder:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - PowerOfficeGo Salesorder Property
     - PowerOfficeGo Data Type
   * - CurrencyCode
     - Currency
     - "string"
   * - OrderDate
     - OrderDate
     - "string"


Powerofficego Supplier to PowerOfficeGo Suppliers
-------------------------------------------------
Every Powerofficego Supplier will be synchronized with a PowerOfficeGo Suppliers.

If a matching PowerOfficeGo Suppliers already exists, the Powerofficego Supplier will be merged with the existing one.
If no matching PowerOfficeGo Suppliers is found, a new PowerOfficeGo Suppliers will be created.

A Powerofficego Supplier will merge with a PowerOfficeGo Suppliers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGo Suppliers Property
   * - Id
     - Id

Once a link between a Powerofficego Supplier and a PowerOfficeGo Suppliers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Supplier and a PowerOfficeGo Suppliers:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGo Suppliers Property
     - PowerOfficeGo Data Type
   * - EmailAddress
     - EmailAddress
     - "string"
   * - Id
     - Id
     - "string"
   * - InternationalIdCountryCode
     - InternationalIdCountryCode
     - "string"
   * - LastChanged
     - LastChanged
     - "string"
   * - LegalName
     - LegalName
     - "string"
   * - PhoneNumber
     - PhoneNumber
     - "string"
   * - WebsiteUrl
     - WebsiteUrl
     - "string"


Powerofficego Vatcode to PowerOfficeGo Vatcodes
-----------------------------------------------
Every Powerofficego Vatcode will be synchronized with a PowerOfficeGo Vatcodes.

If a matching PowerOfficeGo Vatcodes already exists, the Powerofficego Vatcode will be merged with the existing one.
If no matching PowerOfficeGo Vatcodes is found, a new PowerOfficeGo Vatcodes will be created.

A Powerofficego Vatcode will merge with a PowerOfficeGo Vatcodes if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Vatcode Property
     - PowerOfficeGo Vatcodes Property
   * - id
     - Id

Once a link between a Powerofficego Vatcode and a PowerOfficeGo Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Vatcode and a PowerOfficeGo Vatcodes:

.. list-table::
   :header-rows: 1

   * - Powerofficego Vatcode Property
     - PowerOfficeGo Vatcodes Property
     - PowerOfficeGo Data Type
   * - description
     - Description
     - "string"
   * - name
     - Name
     - "string"
   * - rate
     - Rate
     - "string"

