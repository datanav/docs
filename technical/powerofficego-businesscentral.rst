===========================================
PowerOffice GO to Business Central Dataflow
===========================================

Generated: 2024-09-11 07:54:14

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice Contactperson to Business Customers company
-------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice Contactperson and a Business Customers company must be established.

A new Business Customers company will be created from a PowerOffice Contactperson if it is connected to a PowerOffice Powerofficego-salesorders that is synchronized into Business.

Once a link between a PowerOffice Contactperson and a Business Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Contactperson and a Business Customers company:

.. list-table::
   :header-rows: 1

   * - PowerOffice Contactperson Property
     - Business Customers company Property
     - Business Data Type
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


PowerOffice Contactperson to Business Customers person
------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice Contactperson and a Business Customers person must be established.

A new Business Customers person will be created from a PowerOffice Contactperson if it is connected to a PowerOffice Powerofficego-salesorders that is synchronized into Business.

Once a link between a PowerOffice Contactperson and a Business Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Contactperson and a Business Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOffice Contactperson Property
     - Business Customers person Property
     - Business Data Type
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


PowerOffice Contactperson to Business Contacts person
-----------------------------------------------------
Every PowerOffice Contactperson will be synchronized with a Business Contacts person.

Once a link between a PowerOffice Contactperson and a Business Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Contactperson and a Business Contacts person:

.. list-table::
   :header-rows: 1

   * - PowerOffice Contactperson Property
     - Business Contacts person Property
     - Business Data Type
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


PowerOffice Customers to Business Contacts person
-------------------------------------------------
Every PowerOffice Customers will be synchronized with a Business Contacts person.

Once a link between a PowerOffice Customers and a Business Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers and a Business Contacts person:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers Property
     - Business Contacts person Property
     - Business Data Type
   * - IsPerson
     - type
     - "string"


PowerOffice Customers to Business Customers company
---------------------------------------------------
Every PowerOffice Customers will be synchronized with a Business Customers company.

Once a link between a PowerOffice Customers and a Business Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers and a Business Customers company:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers Property
     - Business Customers company Property
     - Business Data Type
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


PowerOffice Customers to Business Customers person
--------------------------------------------------
Every PowerOffice Customers will be synchronized with a Business Customers person.

Once a link between a PowerOffice Customers and a Business Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers and a Business Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers Property
     - Business Customers person Property
     - Business Data Type


PowerOffice Customers person to Business Contacts person
--------------------------------------------------------
Every PowerOffice Customers person will be synchronized with a Business Contacts person.

Once a link between a PowerOffice Customers person and a Business Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers person and a Business Contacts person:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers person Property
     - Business Contacts person Property
     - Business Data Type
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


PowerOffice Customers person to Business Customers person
---------------------------------------------------------
Every PowerOffice Customers person will be synchronized with a Business Customers person.

Once a link between a PowerOffice Customers person and a Business Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers person and a Business Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers person Property
     - Business Customers person Property
     - Business Data Type
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


PowerOffice Employees to Business Employees
-------------------------------------------
Every PowerOffice Employees will be synchronized with a Business Employees.

Once a link between a PowerOffice Employees and a Business Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Employees and a Business Employees:

.. list-table::
   :header-rows: 1

   * - PowerOffice Employees Property
     - Business Employees Property
     - Business Data Type
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


PowerOffice Product to Business Items
-------------------------------------
Every PowerOffice Product will be synchronized with a Business Items.

Once a link between a PowerOffice Product and a Business Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Product and a Business Items:

.. list-table::
   :header-rows: 1

   * - PowerOffice Product Property
     - Business Items Property
     - Business Data Type
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


PowerOffice Salesorderlines to Business Salesorderlines
-------------------------------------------------------
Every PowerOffice Salesorderlines will be synchronized with a Business Salesorderlines.

Once a link between a PowerOffice Salesorderlines and a Business Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Salesorderlines and a Business Salesorderlines:

.. list-table::
   :header-rows: 1

   * - PowerOffice Salesorderlines Property
     - Business Salesorderlines Property
     - Business Data Type
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


PowerOffice Salesorders to Business Salesorders
-----------------------------------------------
Every PowerOffice Salesorders will be synchronized with a Business Salesorders.

Once a link between a PowerOffice Salesorders and a Business Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Salesorders and a Business Salesorders:

.. list-table::
   :header-rows: 1

   * - PowerOffice Salesorders Property
     - Business Salesorders Property
     - Business Data Type
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


PowerOffice Suppliers person to Business Contacts person
--------------------------------------------------------
Every PowerOffice Suppliers person will be synchronized with a Business Contacts person.

Once a link between a PowerOffice Suppliers person and a Business Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Suppliers person and a Business Contacts person:

.. list-table::
   :header-rows: 1

   * - PowerOffice Suppliers person Property
     - Business Contacts person Property
     - Business Data Type
   * - EmailAddress
     - email
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"

