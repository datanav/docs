===========================================
Business Central to PowerOffice GO Dataflow
===========================================

Generated: 2024-09-11 07:55:13

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Customers to PowerOffice Contactperson
-----------------------------------------------
Before any synchronization can take place, a link between a Business Customers and a PowerOffice Contactperson must be established.

A new PowerOffice Contactperson will be created from a Business Customers if it is connected to a Business Businesscentral-salesorders that is synchronized into PowerOffice.

Once a link between a Business Customers and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - Business Customers Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type


Business Customers to PowerOffice Customers
-------------------------------------------
Before any synchronization can take place, a link between a Business Customers and a PowerOffice Customers must be established.

A new PowerOffice Customers will be created from a Business Customers if it is connected to a Business Businesscentral-customers, Businesscentral-salesorders, Businesscentral-contact-person, or Businesscentral-contacts-person that is synchronized into PowerOffice.

Once a link between a Business Customers and a PowerOffice Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers and a PowerOffice Customers:

.. list-table::
   :header-rows: 1

   * - Business Customers Property
     - PowerOffice Customers Property
     - PowerOffice Data Type


Business Customers to PowerOffice Customers person
--------------------------------------------------
Before any synchronization can take place, a link between a Business Customers and a PowerOffice Customers person must be established.

A new PowerOffice Customers person will be created from a Business Customers if it is connected to a Business Businesscentral-customers, Businesscentral-salesorders, Businesscentral-contact-person, or Businesscentral-contacts-person that is synchronized into PowerOffice.

Once a link between a Business Customers and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - Business Customers Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type


Business Contacts person to PowerOffice Contactperson
-----------------------------------------------------
Every Business Contacts person will be synchronized with a PowerOffice Contactperson.

Once a link between a Business Contacts person and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Contacts person and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - Business Contacts person Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
   * - addressLine1
     - address1
     - "string"
   * - addressLine2
     - address2
     - "string"
   * - city
     - city
     - "string"
   * - country
     - residenceCountryCode
     - "string"
   * - email
     - emailAddress
     - "string"
   * - id
     - id
     - "integer"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - postalCode
     - zipCode
     - "string"


Business Contacts person to PowerOffice Customers
-------------------------------------------------
Every Business Contacts person will be synchronized with a PowerOffice Customers.

Once a link between a Business Contacts person and a PowerOffice Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Contacts person and a PowerOffice Customers:

.. list-table::
   :header-rows: 1

   * - Business Contacts person Property
     - PowerOffice Customers Property
     - PowerOffice Data Type


Business Contacts person to PowerOffice Customers person
--------------------------------------------------------
Every Business Contacts person will be synchronized with a PowerOffice Customers person.

Once a link between a Business Contacts person and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Contacts person and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - Business Contacts person Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type
   * - addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - city
     - MailAddress.City
     - "string"
   * - country
     - MailAddress.CountryCode
     - "string"
   * - email
     - EmailAddress
     - "string"
   * - id
     - Id
     - "integer"
   * - phoneNumber
     - PhoneNumber
     - "string"
   * - postalCode
     - MailAddress.ZipCode
     - "string"
   * - type
     - IsPerson
     - N/A


Business Customers company to PowerOffice Customers
---------------------------------------------------
Every Business Customers company will be synchronized with a PowerOffice Customers.

Once a link between a Business Customers company and a PowerOffice Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers company and a PowerOffice Customers:

.. list-table::
   :header-rows: 1

   * - Business Customers company Property
     - PowerOffice Customers Property
     - PowerOffice Data Type
   * - address.city
     - MailAddress.City
     - "string"
   * - address.countryLetterCode
     - MailAddress.CountryCode
     - "string"
   * - address.postalCode
     - MailAddress.ZipCode
     - "string"
   * - addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - city
     - MailAddress.City
     - "string"
   * - country
     - MailAddress.CountryCode
     - "string"
   * - displayName
     - Name
     - "string"
   * - id
     - Id
     - "integer"
   * - phoneNumber
     - PhoneNumber
     - "string"
   * - postalCode
     - MailAddress.ZipCode
     - "string"
   * - type
     - IsPerson
     - N/A
   * - website
     - WebsiteUrl
     - "string"


Business Customers person to PowerOffice Customers
--------------------------------------------------
Every Business Customers person will be synchronized with a PowerOffice Customers.

Once a link between a Business Customers person and a PowerOffice Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers person and a PowerOffice Customers:

.. list-table::
   :header-rows: 1

   * - Business Customers person Property
     - PowerOffice Customers Property
     - PowerOffice Data Type


Business Customers person to PowerOffice Customers person
---------------------------------------------------------
Every Business Customers person will be synchronized with a PowerOffice Customers person.

Once a link between a Business Customers person and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers person and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - Business Customers person Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type
   * - address.city
     - MailAddress.City
     - "string"
   * - address.postalCode
     - MailAddress.ZipCode
     - "string"
   * - addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - addressLine2
     - MailAddress.City
     - "string"
   * - city
     - MailAddress.City
     - "string"
   * - country
     - MailAddress.CountryCode
     - "string"
   * - email
     - EmailAddress
     - "string"
   * - id
     - Id
     - "integer"
   * - phoneNumber
     - PhoneNumber
     - "string"
   * - postalCode
     - MailAddress.ZipCode
     - "string"
   * - type
     - IsPerson
     - N/A


Business Employees to PowerOffice Employees
-------------------------------------------
Every Business Employees will be synchronized with a PowerOffice Employees.

Once a link between a Business Employees and a PowerOffice Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Employees and a PowerOffice Employees:

.. list-table::
   :header-rows: 1

   * - Business Employees Property
     - PowerOffice Employees Property
     - PowerOffice Data Type
   * - birthDate
     - DateOfBirth
     - N/A
   * - email
     - EmailAddress
     - "string"
   * - givenName
     - FirstName
     - "string"
   * - jobTitle
     - DepartmentId (Dependant on having  in JobTitle)
     - "string"
   * - jobTitle
     - JobTitle
     - "string"
   * - mobilePhone
     - PhoneNumber
     - "string"
   * - surname
     - LastName
     - "string"


Business Items to PowerOffice Product
-------------------------------------
Every Business Items will be synchronized with a PowerOffice Product.

Once a link between a Business Items and a PowerOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Items and a PowerOffice Product:

.. list-table::
   :header-rows: 1

   * - Business Items Property
     - PowerOffice Product Property
     - PowerOffice Data Type
   * - displayName
     - name
     - "string"
   * - displayName.string
     - name
     - "string"
   * - displayName2
     - name
     - "string"
   * - gtin
     - gtin
     - "string"
   * - inventory
     - availableStock
     - "integer"
   * - taxGroupCode
     - vatCode
     - "string"
   * - unitCost
     - costPrice
     - N/A
   * - unitPrice
     - salesPrice
     - N/A


Business Salesorderlines to PowerOffice Salesorderlines
-------------------------------------------------------
Every Business Salesorderlines will be synchronized with a PowerOffice Salesorderlines.

Once a link between a Business Salesorderlines and a PowerOffice Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Salesorderlines and a PowerOffice Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Business Salesorderlines Property
     - PowerOffice Salesorderlines Property
     - PowerOffice Data Type
   * - amountExcludingTax
     - ProductUnitPrice
     - N/A
   * - description
     - Description
     - "string"
   * - discountPercent
     - Allowance
     - "float"
   * - documentId
     - sesam_SalesOrderId
     - "string"
   * - invoiceQuantity
     - Quantity
     - "integer"
   * - itemId
     - ProductId
     - "integer"
   * - quantity
     - Quantity
     - N/A
   * - taxPercent
     - VatId
     - "string"
   * - unitPrice
     - ProductUnitPrice
     - N/A


Business Salesorders to PowerOffice Salesorders
-----------------------------------------------
Every Business Salesorders will be synchronized with a PowerOffice Salesorders.

Once a link between a Business Salesorders and a PowerOffice Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Salesorders and a PowerOffice Salesorders:

.. list-table::
   :header-rows: 1

   * - Business Salesorders Property
     - PowerOffice Salesorders Property
     - PowerOffice Data Type
   * - currencyId
     - CurrencyCode
     - "string"
   * - customerId
     - CustomerId
     - "integer"
   * - customerId
     - CustomerReferenceContactPersonId
     - "integer"
   * - orderDate
     - SalesOrderDate
     - "string"

