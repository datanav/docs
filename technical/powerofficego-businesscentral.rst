===========================================
PowerOffice GO to Business Central Dataflow
===========================================

Generated: 2024-09-12 13:14:11

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Contactperson to Business Central Customers company
------------------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Contactperson and a Business Central Customers company must be established.

A new Business Central Customers company will be created from a PowerOffice GO Contactperson if it is connected to a PowerOffice GO Powerofficego-salesorders that is synchronized into Business Central.

Once a link between a PowerOffice GO Contactperson and a Business Central Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Business Central Customers company:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Business Central Customers company Property
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
   * - id
     - id
     - "string"
   * - residenceCountryCode
     - country
     - "string"
   * - zipCode
     - postalCode
     - "string"


PowerOffice GO Contactperson to Business Central Customers person
-----------------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Contactperson and a Business Central Customers person must be established.

A new Business Central Customers person will be created from a PowerOffice GO Contactperson if it is connected to a PowerOffice GO Powerofficego-salesorders that is synchronized into Business Central.

Once a link between a PowerOffice GO Contactperson and a Business Central Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Business Central Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Business Central Customers person Property
     - Business Central Data Type
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


PowerOffice GO Contactperson to Business Central Contacts person
----------------------------------------------------------------
Every PowerOffice GO Contactperson will be synchronized with a Business Central Contacts person.

Once a link between a PowerOffice GO Contactperson and a Business Central Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Business Central Contacts person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Business Central Contacts person Property
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


PowerOffice GO Customers to Business Central Contacts person
------------------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Business Central Contacts person.

Once a link between a PowerOffice GO Customers and a Business Central Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Business Central Contacts person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Business Central Contacts person Property
     - Business Central Data Type
   * - IsPerson
     - type
     - "string"


PowerOffice GO Customers to Business Central Customers company
--------------------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Business Central Customers company.

Once a link between a PowerOffice GO Customers and a Business Central Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Business Central Customers company:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Business Central Customers company Property
     - Business Central Data Type
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


PowerOffice GO Customers to Business Central Customers person
-------------------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Business Central Customers person.

Once a link between a PowerOffice GO Customers and a Business Central Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Business Central Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Business Central Customers person Property
     - Business Central Data Type


PowerOffice GO Customers person to Business Central Contacts person
-------------------------------------------------------------------
Every PowerOffice GO Customers person will be synchronized with a Business Central Contacts person.

Once a link between a PowerOffice GO Customers person and a Business Central Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Business Central Contacts person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Business Central Contacts person Property
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


PowerOffice GO Customers person to Business Central Customers person
--------------------------------------------------------------------
Every PowerOffice GO Customers person will be synchronized with a Business Central Customers person.

Once a link between a PowerOffice GO Customers person and a Business Central Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Business Central Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Business Central Customers person Property
     - Business Central Data Type
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
   * - TotalAmount
     - totalAmountExcludingTax
     - "string"


PowerOffice GO Suppliers person to Business Central Contacts person
-------------------------------------------------------------------
Every PowerOffice GO Suppliers person will be synchronized with a Business Central Contacts person.

Once a link between a PowerOffice GO Suppliers person and a Business Central Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Suppliers person and a Business Central Contacts person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Suppliers person Property
     - Business Central Contacts person Property
     - Business Central Data Type
   * - EmailAddress
     - email
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"

