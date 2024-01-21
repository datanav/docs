============================
Businesscentral to  Dataflow
============================

Generated: 2024-01-21 00:00:01

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Customers to  Contactperson
-------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Customers and a  Contactperson must be established.

A new  Contactperson will be created from a Businesscentral Customers if it is connected to a Businesscentral Salesorders that is synchronized into .

Once a link between a Businesscentral Customers and a  Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a  Contactperson:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     -  Contactperson Property
     -  Data Type


Businesscentral Customers to  Customers
---------------------------------------
Before any synchronization can take place, a link between a Businesscentral Customers and a  Customers must be established.

A new  Customers will be created from a Businesscentral Customers if it is connected to a Businesscentral Customers, Salesorders, Contact-person, or Contacts-person that is synchronized into .

Once a link between a Businesscentral Customers and a  Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a  Customers:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     -  Customers Property
     -  Data Type


Businesscentral Customers to  Customers person
----------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Customers and a  Customers person must be established.

A new  Customers person will be created from a Businesscentral Customers if it is connected to a Businesscentral Customers, Salesorders, Contact-person, or Contacts-person that is synchronized into .

Once a link between a Businesscentral Customers and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     -  Customers person Property
     -  Data Type


Businesscentral Contacts person to  Contactperson
-------------------------------------------------
Every Businesscentral Contacts person will be synchronized with a  Contactperson.

Once a link between a Businesscentral Contacts person and a  Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a  Contactperson:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     -  Contactperson Property
     -  Data Type
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


Businesscentral Contacts person to  Customers person
----------------------------------------------------
Every Businesscentral Contacts person will be synchronized with a  Customers person.

Once a link between a Businesscentral Contacts person and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     -  Customers person Property
     -  Data Type
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
     - "boolean"


Businesscentral Currencies to  Currency
---------------------------------------
Every Businesscentral Currencies will be synchronized with a  Currency.

If a matching  Currency already exists, the Businesscentral Currencies will be merged with the existing one.
If no matching  Currency is found, a new  Currency will be created.

A Businesscentral Currencies will merge with a  Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Businesscentral Currencies Property
     -  Currency Property
   * - code
     - code

Once a link between a Businesscentral Currencies and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Currencies and a  Currency:

.. list-table::
   :header-rows: 1

   * - Businesscentral Currencies Property
     -  Currency Property
     -  Data Type


Businesscentral Customers company to  Customers
-----------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Customers.

Once a link between a Businesscentral Customers company and a  Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Customers:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Customers Property
     -  Data Type
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
     - "boolean"
   * - website
     - WebsiteUrl
     - "string"


Businesscentral Customers person to  Customers person
-----------------------------------------------------
Every Businesscentral Customers person will be synchronized with a  Customers person.

Once a link between a Businesscentral Customers person and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     -  Customers person Property
     -  Data Type
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
     - "boolean"


Businesscentral Employees to  Employees
---------------------------------------
Every Businesscentral Employees will be synchronized with a  Employees.

Once a link between a Businesscentral Employees and a  Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employees and a  Employees:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employees Property
     -  Employees Property
     -  Data Type


Businesscentral Items to  Product
---------------------------------
Every Businesscentral Items will be synchronized with a  Product.

Once a link between a Businesscentral Items and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Product:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Product Property
     -  Data Type
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
     - "if", "is-decimal", "decimal", "integer"]
   * - unitPrice
     - salesPrice
     - "if", "is-decimal", "decimal", "integer"]


Businesscentral Salesorderlines to  Salesorderlines
---------------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a  Salesorderlines.

Once a link between a Businesscentral Salesorderlines and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     -  Salesorderlines Property
     -  Data Type
   * - amountExcludingTax
     - ProductUnitPrice
     - "if", "is-decimal", "decimal", "integer"]
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
     - "integer"
   * - unitPrice
     - ProductUnitPrice
     - "if", "is-decimal", "decimal", "integer"]


Businesscentral Salesorders to  Salesorders
-------------------------------------------
Every Businesscentral Salesorders will be synchronized with a  Salesorders.

Once a link between a Businesscentral Salesorders and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     -  Salesorders Property
     -  Data Type
   * - currencyId
     - CurrencyCode
     - "string"
   * - customerId
     - CustomerReferenceContactPersonId
     - "string"
   * - orderDate
     - SalesOrderDate
     - "string"

