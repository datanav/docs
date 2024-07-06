=========================================
Powerofficego to Businesscentral Dataflow
=========================================

Generated: 2024-07-06 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to Businesscentral Customers company
----------------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a Businesscentral Customers company must be established.

A new Businesscentral Customers company will be created from a Powerofficego Contactperson if it is connected to a Powerofficego Salesorders that is synchronized into Businesscentral.

Once a link between a Powerofficego Contactperson and a Businesscentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Businesscentral Customers company:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Businesscentral Customers company Property
     - Businesscentral Data Type
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


Powerofficego Contactperson to Businesscentral Customers person
---------------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a Businesscentral Customers person must be established.

A new Businesscentral Customers person will be created from a Powerofficego Contactperson if it is connected to a Powerofficego Salesorders that is synchronized into Businesscentral.

Once a link between a Powerofficego Contactperson and a Businesscentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Businesscentral Customers person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Businesscentral Customers person Property
     - Businesscentral Data Type
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


Powerofficego Customers to Businesscentral Companies
----------------------------------------------------
Every Powerofficego Customers will be synchronized with a Businesscentral Companies.

Once a link between a Powerofficego Customers and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Powerofficego Departments to Businesscentral Companies
------------------------------------------------------
Every Powerofficego Departments will be synchronized with a Businesscentral Companies.

Once a link between a Powerofficego Departments and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Powerofficego Contactperson to Businesscentral Contacts person
--------------------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Businesscentral Contacts person.

Once a link between a Powerofficego Contactperson and a Businesscentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Businesscentral Contacts person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Businesscentral Contacts person Property
     - Businesscentral Data Type
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


Powerofficego Customers to Businesscentral Contacts person
----------------------------------------------------------
Every Powerofficego Customers will be synchronized with a Businesscentral Contacts person.

Once a link between a Powerofficego Customers and a Businesscentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Businesscentral Contacts person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Businesscentral Contacts person Property
     - Businesscentral Data Type
   * - IsPerson
     - type
     - "string"


Powerofficego Customers to Businesscentral Customers company
------------------------------------------------------------
Every Powerofficego Customers will be synchronized with a Businesscentral Customers company.

Once a link between a Powerofficego Customers and a Businesscentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Businesscentral Customers company:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Businesscentral Customers company Property
     - Businesscentral Data Type
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


Powerofficego Customers to Businesscentral Customers person
-----------------------------------------------------------
Every Powerofficego Customers will be synchronized with a Businesscentral Customers person.

Once a link between a Powerofficego Customers and a Businesscentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Businesscentral Customers person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Businesscentral Customers person Property
     - Businesscentral Data Type


Powerofficego Customers person to Businesscentral Contacts person
-----------------------------------------------------------------
Every Powerofficego Customers person will be synchronized with a Businesscentral Contacts person.

Once a link between a Powerofficego Customers person and a Businesscentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Businesscentral Contacts person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Businesscentral Contacts person Property
     - Businesscentral Data Type
   * - EmailAddress
     - email
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
     - city
     - "string"
   * - MailAddress.CountryCode
     - country
     - "string"
   * - MailAddress.ZipCode
     - postalCode
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"


Powerofficego Customers person to Businesscentral Customers person
------------------------------------------------------------------
Every Powerofficego Customers person will be synchronized with a Businesscentral Customers person.

Once a link between a Powerofficego Customers person and a Businesscentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Businesscentral Customers person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Businesscentral Customers person Property
     - Businesscentral Data Type
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


Powerofficego Employees to Businesscentral Employees
----------------------------------------------------
Every Powerofficego Employees will be synchronized with a Businesscentral Employees.

Once a link between a Powerofficego Employees and a Businesscentral Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a Businesscentral Employees:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Businesscentral Employees Property
     - Businesscentral Data Type
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


Powerofficego Product to Businesscentral Items
----------------------------------------------
Every Powerofficego Product will be synchronized with a Businesscentral Items.

Once a link between a Powerofficego Product and a Businesscentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Businesscentral Items:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Businesscentral Items Property
     - Businesscentral Data Type
   * - costPrice
     - unitCost
     - N/A
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
     - N/A
   * - vatCode
     - taxGroupCode
     - "string"


Powerofficego Salesorderlines to Businesscentral Salesorderlines
----------------------------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a Businesscentral Salesorderlines.

Once a link between a Powerofficego Salesorderlines and a Businesscentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a Businesscentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     - Businesscentral Salesorderlines Property
     - Businesscentral Data Type
   * - Allowance
     - discountPercent
     - N/A
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
     - N/A
   * - VatId
     - taxPercent
     - N/A
   * - VatRate
     - taxPercent
     - N/A
   * - sesam_SalesOrderId
     - documentId
     - "string"


Powerofficego Salesorders to Businesscentral Salesorders
--------------------------------------------------------
Every Powerofficego Salesorders will be synchronized with a Businesscentral Salesorders.

Once a link between a Powerofficego Salesorders and a Businesscentral Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a Businesscentral Salesorders:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - Businesscentral Salesorders Property
     - Businesscentral Data Type
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
     - N/A
   * - TotalAmount
     - totalAmountExcludingTax
     - "string"


Powerofficego Suppliers person to Businesscentral Contacts person
-----------------------------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a Businesscentral Contacts person.

Once a link between a Powerofficego Suppliers person and a Businesscentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a Businesscentral Contacts person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     - Businesscentral Contacts person Property
     - Businesscentral Data Type
   * - EmailAddress
     - email
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"

