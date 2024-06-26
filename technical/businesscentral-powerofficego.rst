=========================================
Businesscentral to Powerofficego Dataflow
=========================================

Generated: 2024-06-26 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Customers to Powerofficego Contactperson
--------------------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Customers and a Powerofficego Contactperson must be established.

A new Powerofficego Contactperson will be created from a Businesscentral Customers if it is connected to a Businesscentral Salesorders that is synchronized into Powerofficego.

Once a link between a Businesscentral Customers and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type


Businesscentral Customers to Powerofficego Customers
----------------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Customers and a Powerofficego Customers must be established.

A new Powerofficego Customers will be created from a Businesscentral Customers if it is connected to a Businesscentral Customers, Salesorders, Contact-person, or Contacts-person that is synchronized into Powerofficego.

Once a link between a Businesscentral Customers and a Powerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a Powerofficego Customers:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     - Powerofficego Customers Property
     - Powerofficego Data Type


Businesscentral Customers to Powerofficego Customers person
-----------------------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Customers and a Powerofficego Customers person must be established.

A new Powerofficego Customers person will be created from a Businesscentral Customers if it is connected to a Businesscentral Customers, Salesorders, Contact-person, or Contacts-person that is synchronized into Powerofficego.

Once a link between a Businesscentral Customers and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     - Powerofficego Customers person Property
     - Powerofficego Data Type


Businesscentral Contacts person to Powerofficego Contactperson
--------------------------------------------------------------
Every Businesscentral Contacts person will be synchronized with a Powerofficego Contactperson.

Once a link between a Businesscentral Contacts person and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type
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


Businesscentral Contacts person to Powerofficego Customers
----------------------------------------------------------
Every Businesscentral Contacts person will be synchronized with a Powerofficego Customers.

Once a link between a Businesscentral Contacts person and a Powerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a Powerofficego Customers:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     - Powerofficego Customers Property
     - Powerofficego Data Type


Businesscentral Contacts person to Powerofficego Customers person
-----------------------------------------------------------------
Every Businesscentral Contacts person will be synchronized with a Powerofficego Customers person.

Once a link between a Businesscentral Contacts person and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     - Powerofficego Customers person Property
     - Powerofficego Data Type
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


Businesscentral Customers company to Powerofficego Customers
------------------------------------------------------------
Every Businesscentral Customers company will be synchronized with a Powerofficego Customers.

Once a link between a Businesscentral Customers company and a Powerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a Powerofficego Customers:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     - Powerofficego Customers Property
     - Powerofficego Data Type
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


Businesscentral Customers person to Powerofficego Customers
-----------------------------------------------------------
Every Businesscentral Customers person will be synchronized with a Powerofficego Customers.

Once a link between a Businesscentral Customers person and a Powerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a Powerofficego Customers:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     - Powerofficego Customers Property
     - Powerofficego Data Type


Businesscentral Customers person to Powerofficego Customers person
------------------------------------------------------------------
Every Businesscentral Customers person will be synchronized with a Powerofficego Customers person.

Once a link between a Businesscentral Customers person and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     - Powerofficego Customers person Property
     - Powerofficego Data Type
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


Businesscentral Employees to Powerofficego Employees
----------------------------------------------------
Every Businesscentral Employees will be synchronized with a Powerofficego Employees.

Once a link between a Businesscentral Employees and a Powerofficego Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employees and a Powerofficego Employees:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employees Property
     - Powerofficego Employees Property
     - Powerofficego Data Type
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


Businesscentral Items to Powerofficego Product
----------------------------------------------
Every Businesscentral Items will be synchronized with a Powerofficego Product.

Once a link between a Businesscentral Items and a Powerofficego Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a Powerofficego Product:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     - Powerofficego Product Property
     - Powerofficego Data Type
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


Businesscentral Salesorderlines to Powerofficego Salesorderlines
----------------------------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a Powerofficego Salesorderlines.

Once a link between a Businesscentral Salesorderlines and a Powerofficego Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a Powerofficego Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     - Powerofficego Salesorderlines Property
     - Powerofficego Data Type
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


Businesscentral Salesorders to Powerofficego Salesorders
--------------------------------------------------------
Every Businesscentral Salesorders will be synchronized with a Powerofficego Salesorders.

Once a link between a Businesscentral Salesorders and a Powerofficego Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a Powerofficego Salesorders:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     - Powerofficego Salesorders Property
     - Powerofficego Data Type
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

