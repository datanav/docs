===========================================
PowerOffice GO to Business Central Dataflow
===========================================

Generated: 2024-09-24 13:32:19

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Customers to Business Central Companies
------------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Business Central Companies.

Once a link between a PowerOffice GO Customers and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Business Central Companies Property
     - Business Central Data Type


PowerOffice GO Departments to Business Central Companies
--------------------------------------------------------
Every PowerOffice GO Departments will be synchronized with a Business Central Companies.

Once a link between a PowerOffice GO Departments and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Departments and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - Business Central Companies Property
     - Business Central Data Type


PowerOffice GO Contactperson to Business Central Contacts (human data)
----------------------------------------------------------------------
Every PowerOffice GO Contactperson will be synchronized with a Business Central Contacts (human data).

Once a link between a PowerOffice GO Contactperson and a Business Central Contacts (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Business Central Contacts (human data):

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Business Central Contacts (human data) Property
     - Business Central Data Type
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


PowerOffice GO Customers to Business Central Contacts (classification data)
---------------------------------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Business Central Contacts (classification data).

Once a link between a PowerOffice GO Customers and a Business Central Contacts (classification data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Business Central Contacts (classification data):

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Business Central Contacts (classification data) Property
     - Business Central Data Type
   * - IsPerson
     - type
     - "string"


PowerOffice GO Customers to Business Central Customers (organisation data)
--------------------------------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Business Central Customers (organisation data).

Once a link between a PowerOffice GO Customers and a Business Central Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Business Central Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Business Central Customers (organisation data) Property
     - Business Central Data Type
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
   * - Name
     - displayName
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"
   * - WebsiteUrl
     - website
     - "string"


PowerOffice GO Customers to Business Central Customers (classification data)
----------------------------------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Business Central Customers (classification data).

Once a link between a PowerOffice GO Customers and a Business Central Customers (classification data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Business Central Customers (classification data):

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Business Central Customers (classification data) Property
     - Business Central Data Type


PowerOffice GO Customers to Business Central Customers (human data)
-------------------------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Business Central Customers (human data).

Once a link between a PowerOffice GO Customers and a Business Central Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Business Central Customers (human data):

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Business Central Customers (human data) Property
     - Business Central Data Type


PowerOffice GO Customers (classification data) to Business Central Contacts (classification data)
-------------------------------------------------------------------------------------------------
Every PowerOffice GO Customers (classification data) will be synchronized with a Business Central Contacts (classification data).

Once a link between a PowerOffice GO Customers (classification data) and a Business Central Contacts (classification data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers (classification data) and a Business Central Contacts (classification data):

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers (classification data) Property
     - Business Central Contacts (classification data) Property
     - Business Central Data Type
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


PowerOffice GO Customers (organisation data) to Business Central Customers (organisation data)
----------------------------------------------------------------------------------------------
Every PowerOffice GO Customers (organisation data) will be synchronized with a Business Central Customers (organisation data).

Once a link between a PowerOffice GO Customers (organisation data) and a Business Central Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers (organisation data) and a Business Central Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers (organisation data) Property
     - Business Central Customers (organisation data) Property
     - Business Central Data Type


PowerOffice GO Customers (classification data) to Business Central Customers (classification data)
--------------------------------------------------------------------------------------------------
Every PowerOffice GO Customers (classification data) will be synchronized with a Business Central Customers (classification data).

Once a link between a PowerOffice GO Customers (classification data) and a Business Central Customers (classification data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers (classification data) and a Business Central Customers (classification data):

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers (classification data) Property
     - Business Central Customers (classification data) Property
     - Business Central Data Type


PowerOffice GO Customers (human data) to Business Central Customers (human data)
--------------------------------------------------------------------------------
Every PowerOffice GO Customers (human data) will be synchronized with a Business Central Customers (human data).

Once a link between a PowerOffice GO Customers (human data) and a Business Central Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers (human data) and a Business Central Customers (human data):

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers (human data) Property
     - Business Central Customers (human data) Property
     - Business Central Data Type
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


PowerOffice GO Employees to Business Central Employees
------------------------------------------------------
Every PowerOffice GO Employees will be synchronized with a Business Central Employees.

Once a link between a PowerOffice GO Employees and a Business Central Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Employees and a Business Central Employees:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - Business Central Employees Property
     - Business Central Data Type
   * - DateOfBirth
     - birthDate
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


PowerOffice GO Product to Business Central Items
------------------------------------------------
Every PowerOffice GO Product will be synchronized with a Business Central Items.

Once a link between a PowerOffice GO Product and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
     - Business Central Items Property
     - Business Central Data Type
   * - costPrice
     - unitCost
     - N/A
   * - gtin
     - gtin
     - "string"
   * - name
     - displayName
     - "string"
   * - salesPrice
     - unitPrice
     - N/A


PowerOffice GO Salesorderlines to Business Central Salesorderlines
------------------------------------------------------------------
Every PowerOffice GO Salesorderlines will be synchronized with a Business Central Salesorderlines.

Once a link between a PowerOffice GO Salesorderlines and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorderlines and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorderlines Property
     - Business Central Salesorderlines Property
     - Business Central Data Type
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
     - unitPrice
     - "float"
   * - Quantity
     - quantity
     - N/A
   * - VatRate
     - taxPercent
     - N/A
   * - sesam_SalesOrderId
     - documentId
     - "string"


PowerOffice GO Salesorders to Business Central Salesorders
----------------------------------------------------------
Every PowerOffice GO Salesorders will be synchronized with a Business Central Salesorders.

Once a link between a PowerOffice GO Salesorders and a Business Central Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorders and a Business Central Salesorders:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorders Property
     - Business Central Salesorders Property
     - Business Central Data Type
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


PowerOffice GO Suppliers (human data) to Business Central Contacts (human data)
-------------------------------------------------------------------------------
Every PowerOffice GO Suppliers (human data) will be synchronized with a Business Central Contacts (human data).

Once a link between a PowerOffice GO Suppliers (human data) and a Business Central Contacts (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Suppliers (human data) and a Business Central Contacts (human data):

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Suppliers (human data) Property
     - Business Central Contacts (human data) Property
     - Business Central Data Type
   * - EmailAddress
     - email
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"

