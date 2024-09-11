==========================================
Business Central to PowerOfficeGO Dataflow
==========================================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to PowerOfficeGO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessCentral Customers to PowerOfficeGO Contactperson
--------------------------------------------------------
Before any synchronization can take place, a link between a BusinessCentral Customers and a PowerOfficeGO Contactperson must be established.

A new PowerOfficeGO Contactperson will be created from a BusinessCentral Customers if it is connected to a BusinessCentral Salesorders that is synchronized into PowerOfficeGO.

Once a link between a BusinessCentral Customers and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type


BusinessCentral Customers to PowerOfficeGO Customers
----------------------------------------------------
Before any synchronization can take place, a link between a BusinessCentral Customers and a PowerOfficeGO Customers must be established.

A new PowerOfficeGO Customers will be created from a BusinessCentral Customers if it is connected to a BusinessCentral Customers, Salesorders, Contact-person, or Contacts-person that is synchronized into PowerOfficeGO.

Once a link between a BusinessCentral Customers and a PowerOfficeGO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers and a PowerOfficeGO Customers:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers Property
     - PowerOfficeGO Customers Property
     - PowerOfficeGO Data Type


BusinessCentral Customers to PowerOfficeGO Customers person
-----------------------------------------------------------
Before any synchronization can take place, a link between a BusinessCentral Customers and a PowerOfficeGO Customers person must be established.

A new PowerOfficeGO Customers person will be created from a BusinessCentral Customers if it is connected to a BusinessCentral Customers, Salesorders, Contact-person, or Contacts-person that is synchronized into PowerOfficeGO.

Once a link between a BusinessCentral Customers and a PowerOfficeGO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers and a PowerOfficeGO Customers person:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers Property
     - PowerOfficeGO Customers person Property
     - PowerOfficeGO Data Type


BusinessCentral Contacts person to PowerOfficeGO Contactperson
--------------------------------------------------------------
Every BusinessCentral Contacts person will be synchronized with a PowerOfficeGO Contactperson.

Once a link between a BusinessCentral Contacts person and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Contacts person and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contacts person Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
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


BusinessCentral Contacts person to PowerOfficeGO Customers
----------------------------------------------------------
Every BusinessCentral Contacts person will be synchronized with a PowerOfficeGO Customers.

Once a link between a BusinessCentral Contacts person and a PowerOfficeGO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Contacts person and a PowerOfficeGO Customers:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contacts person Property
     - PowerOfficeGO Customers Property
     - PowerOfficeGO Data Type


BusinessCentral Contacts person to PowerOfficeGO Customers person
-----------------------------------------------------------------
Every BusinessCentral Contacts person will be synchronized with a PowerOfficeGO Customers person.

Once a link between a BusinessCentral Contacts person and a PowerOfficeGO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Contacts person and a PowerOfficeGO Customers person:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contacts person Property
     - PowerOfficeGO Customers person Property
     - PowerOfficeGO Data Type
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


BusinessCentral Customers company to PowerOfficeGO Customers
------------------------------------------------------------
Every BusinessCentral Customers company will be synchronized with a PowerOfficeGO Customers.

Once a link between a BusinessCentral Customers company and a PowerOfficeGO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers company and a PowerOfficeGO Customers:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers company Property
     - PowerOfficeGO Customers Property
     - PowerOfficeGO Data Type
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


BusinessCentral Customers person to PowerOfficeGO Customers
-----------------------------------------------------------
Every BusinessCentral Customers person will be synchronized with a PowerOfficeGO Customers.

Once a link between a BusinessCentral Customers person and a PowerOfficeGO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers person and a PowerOfficeGO Customers:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers person Property
     - PowerOfficeGO Customers Property
     - PowerOfficeGO Data Type


BusinessCentral Customers person to PowerOfficeGO Customers person
------------------------------------------------------------------
Every BusinessCentral Customers person will be synchronized with a PowerOfficeGO Customers person.

Once a link between a BusinessCentral Customers person and a PowerOfficeGO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers person and a PowerOfficeGO Customers person:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers person Property
     - PowerOfficeGO Customers person Property
     - PowerOfficeGO Data Type
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


BusinessCentral Employees to PowerOfficeGO Employees
----------------------------------------------------
Every BusinessCentral Employees will be synchronized with a PowerOfficeGO Employees.

Once a link between a BusinessCentral Employees and a PowerOfficeGO Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Employees and a PowerOfficeGO Employees:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Employees Property
     - PowerOfficeGO Employees Property
     - PowerOfficeGO Data Type
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


BusinessCentral Items to PowerOfficeGO Product
----------------------------------------------
Every BusinessCentral Items will be synchronized with a PowerOfficeGO Product.

Once a link between a BusinessCentral Items and a PowerOfficeGO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Items and a PowerOfficeGO Product:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Items Property
     - PowerOfficeGO Product Property
     - PowerOfficeGO Data Type
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


BusinessCentral Salesorderlines to PowerOfficeGO Salesorderlines
----------------------------------------------------------------
Every BusinessCentral Salesorderlines will be synchronized with a PowerOfficeGO Salesorderlines.

Once a link between a BusinessCentral Salesorderlines and a PowerOfficeGO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorderlines and a PowerOfficeGO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorderlines Property
     - PowerOfficeGO Salesorderlines Property
     - PowerOfficeGO Data Type
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


BusinessCentral Salesorders to PowerOfficeGO Salesorders
--------------------------------------------------------
Every BusinessCentral Salesorders will be synchronized with a PowerOfficeGO Salesorders.

Once a link between a BusinessCentral Salesorders and a PowerOfficeGO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorders and a PowerOfficeGO Salesorders:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorders Property
     - PowerOfficeGO Salesorders Property
     - PowerOfficeGO Data Type
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

