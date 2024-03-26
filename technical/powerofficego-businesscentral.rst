=========================================
Powerofficego to Businesscentral Dataflow
=========================================

Generated: 2024-03-26 14:14:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to  Customers company
-------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a  Customers company must be established.

A new  Customers company will be created from a Powerofficego Contactperson if it is connected to a Powerofficego Salesorders that is synchronized into .

Once a link between a Powerofficego Contactperson and a  Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Customers company:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Customers company Property
     -  Data Type
   * - address1
     - addressLine1
     - "string"
   * - address2
     - addressLine2
     - "string"
   * - city
     - city
     - "string"
   * - id
     - id
     - "string"
   * - residenceCountryCode
     - country
     - "string"
   * - zipCode
     - postalCode
     - "string"


Powerofficego Contactperson to  Customers person
------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a  Customers person must be established.

A new  Customers person will be created from a Powerofficego Contactperson if it is connected to a Powerofficego Salesorders that is synchronized into .

Once a link between a Powerofficego Contactperson and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Customers person Property
     -  Data Type
   * - SocialSecurityNumber
     - id (Dependant on having wd:Q1140371 in type)
     - "string"
   * - address1
     - addressLine1
     - "string"
   * - address2
     - addressLine2
     - "string"
   * - city
     - address.city
     - "string"
   * - city
     - addressLine2
     - "string"
   * - city
     - city
     - "string"
   * - emailAddress
     - email
     - "string"
   * - emailAddress
     - id (Dependant on having wd:Q1273217 in type)
     - "string"
   * - id
     - id
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - residenceCountryCode
     - country
     - "string"
   * - zipCode
     - address.postalCode
     - "string"
   * - zipCode
     - postalCode
     - "string"


Powerofficego Customers to  Companies
-------------------------------------
Every Powerofficego Customers will be synchronized with a  Companies.

Once a link between a Powerofficego Customers and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Companies:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Companies Property
     -  Data Type


Powerofficego Departments to  Companies
---------------------------------------
Every Powerofficego Departments will be synchronized with a  Companies.

Once a link between a Powerofficego Departments and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a  Companies:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     -  Companies Property
     -  Data Type


Powerofficego Contactperson to  Contacts person
-----------------------------------------------
Every Powerofficego Contactperson will be synchronized with a  Contacts person.

Once a link between a Powerofficego Contactperson and a  Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Contacts person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Contacts person Property
     -  Data Type
   * - address1
     - addressLine1
     - "string"
   * - address2
     - addressLine2
     - "string"
   * - city
     - city
     - "string"
   * - emailAddress
     - email
     - "string"
   * - id
     - id
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - residenceCountryCode
     - country
     - "string"
   * - zipCode
     - postalCode
     - "string"


Powerofficego Customers to  Contacts person
-------------------------------------------
Every Powerofficego Customers will be synchronized with a  Contacts person.

Once a link between a Powerofficego Customers and a  Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Contacts person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Contacts person Property
     -  Data Type
   * - IsPerson
     - type
     - "string"


Powerofficego Customers to  Customers company
---------------------------------------------
Every Powerofficego Customers will be synchronized with a  Customers company.

Once a link between a Powerofficego Customers and a  Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Customers company:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Customers company Property
     -  Data Type
   * - EmailAddress
     - id (Dependant on having wd:Q1273217 in type)
     - "string"
   * - Id
     - id
     - "string"
   * - InvoiceEmailAddress
     - id (Dependant on having wd:Q1273217 in type)
     - "string"
   * - IsPerson
     - type
     - "string"
   * - MailAddress.AddressLine1
     - addressLine1
     - "string"
   * - MailAddress.AddressLine2
     - addressLine2
     - "string"
   * - MailAddress.City
     - address.city
     - "string"
   * - MailAddress.City
     - city
     - "string"
   * - MailAddress.CountryCode
     - address.countryLetterCode
     - "string"
   * - MailAddress.CountryCode
     - country
     - "string"
   * - MailAddress.ZipCode
     - address.postalCode
     - "string"
   * - MailAddress.ZipCode
     - postalCode
     - "string"
   * - Name
     - displayName
     - "string"
   * - OrganizationNumber
     - id (Dependant on having  in type)
     - "string"
   * - PaymentReminderEmailAddress
     - id (Dependant on having wd:Q1273217 in type)
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"
   * - WebsiteUrl
     - website
     - "string"


Powerofficego Customers to  Customers person
--------------------------------------------
Every Powerofficego Customers will be synchronized with a  Customers person.

Once a link between a Powerofficego Customers and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Customers person Property
     -  Data Type


Powerofficego Customers person to  Contacts person
--------------------------------------------------
Every Powerofficego Customers person will be synchronized with a  Contacts person.

Once a link between a Powerofficego Customers person and a  Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Contacts person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Contacts person Property
     -  Data Type
   * - Id
     - id
     - "string"
   * - IsPerson
     - type
     - "string"
   * - MailAddress.AddressLine1
     - addressLine1
     - "string"
   * - MailAddress.AddressLine2
     - addressLine2
     - "string"
   * - MailAddress.City
     - city
     - "string"
   * - MailAddress.CountryCode
     - country
     - "string"
   * - MailAddress.ZipCode
     - postalCode
     - "string"


Powerofficego Customers person to  Customers person
---------------------------------------------------
Every Powerofficego Customers person will be synchronized with a  Customers person.

Once a link between a Powerofficego Customers person and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Customers person Property
     -  Data Type
   * - EmailAddress
     - email
     - "string"
   * - EmailAddress
     - id (Dependant on having wd:Q1273217 in type)
     - "string"
   * - Id
     - id
     - "string"
   * - IsPerson
     - type
     - "string"
   * - MailAddress.AddressLine1
     - addressLine1
     - "string"
   * - MailAddress.AddressLine2
     - addressLine2
     - "string"
   * - MailAddress.City
     - address.city
     - "string"
   * - MailAddress.City
     - addressLine2
     - "string"
   * - MailAddress.City
     - city
     - "string"
   * - MailAddress.CountryCode
     - country
     - "string"
   * - MailAddress.ZipCode
     - address.postalCode
     - "string"
   * - MailAddress.ZipCode
     - postalCode
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"


Powerofficego Employees to  Employees
-------------------------------------
Every Powerofficego Employees will be synchronized with a  Employees.

Once a link between a Powerofficego Employees and a  Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a  Employees:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     -  Employees Property
     -  Data Type
   * - DateOfBirth
     - birthDate
     - "string"
   * - DepartmentId (Dependant on having  in JobTitle)
     - jobTitle
     - "string"
   * - EmailAddress
     - email
     - "string"
   * - EmailAddress
     - personalEmail
     - "string"
   * - FirstName
     - givenName
     - "string"
   * - Id
     - id
     - "string"
   * - JobTitle
     - jobTitle
     - "string"
   * - LastName
     - surname
     - "string"
   * - MailAddress.Address1
     - addressLine1
     - "string"
   * - MailAddress.Address2
     - addressLine2
     - "string"
   * - MailAddress.City
     - city
     - "string"
   * - MailAddress.CountryCode
     - country
     - "string"
   * - MailAddress.ZipCode
     - postalCode
     - "string"
   * - PhoneNumber
     - mobilePhone
     - "string"


Powerofficego Product to  Items
-------------------------------
Every Powerofficego Product will be synchronized with a  Items.

Once a link between a Powerofficego Product and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a  Items:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     -  Items Property
     -  Data Type
   * - costPrice
     - unitCost
     - "decimal"
   * - gtin
     - gtin
     - "string"
   * - name
     - displayName
     - "string"
   * - name
     - displayName.string
     - "string"
   * - name
     - displayName2
     - "string"
   * - salesPrice
     - unitPrice
     - "decimal"
   * - vatCode
     - taxGroupCode
     - "string"


Powerofficego Salesorderlines to  Salesorderlines
-------------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a  Salesorderlines.

Once a link between a Powerofficego Salesorderlines and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     -  Salesorderlines Property
     -  Data Type
   * - Allowance
     - discountPercent
     - "decimal"
   * - Description
     - description
     - "string"
   * - ProductId
     - itemId
     - "string"
   * - ProductUnitPrice
     - amountExcludingTax
     - "string"
   * - ProductUnitPrice
     - unitPrice
     - "float"
   * - Quantity
     - invoiceQuantity
     - "string"
   * - Quantity
     - quantity
     - "integer", "decimal"]
   * - VatId
     - taxPercent
     - "decimal"
   * - VatRate
     - taxPercent
     - "decimal"
   * - sesam_SalesOrderId
     - documentId
     - "string"


Powerofficego Salesorders to  Salesorders
-----------------------------------------
Every Powerofficego Salesorders will be synchronized with a  Salesorders.

Once a link between a Powerofficego Salesorders and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     -  Salesorders Property
     -  Data Type
   * - CurrencyCode
     - currencyId
     - "string"
   * - CustomerId
     - customerId
     - "string"
   * - CustomerReferenceContactPersonId
     - customerId
     - "string"
   * - SalesOrderDate
     - orderDate
     - "datetime-parse", "%Y-%m-%dT%H:%M:%S.%fZ"
   * - TotalAmount
     - totalAmountExcludingTax
     - "string"


Powerofficego Suppliers person to  Contacts person
--------------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a  Contacts person.

Once a link between a Powerofficego Suppliers person and a  Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a  Contacts person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     -  Contacts person Property
     -  Data Type
   * - EmailAddress
     - email
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"

