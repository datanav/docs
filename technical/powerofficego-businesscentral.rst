=========================================
PowerOfficeGO to BusinessCentral Dataflow
=========================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOfficeGO to BusinessCentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOfficeGO Contactperson to Business Customers company
---------------------------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGO Contactperson and a Business Customers company must be established.

A new Business Customers company will be created from a PowerOfficeGO Contactperson if it is connected to a PowerOfficeGO Salesorders that is synchronized into Business.

Once a link between a PowerOfficeGO Contactperson and a Business Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Contactperson and a Business Customers company:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Contactperson Property
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


PowerOfficeGO Contactperson to Business Customers person
--------------------------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGO Contactperson and a Business Customers person must be established.

A new Business Customers person will be created from a PowerOfficeGO Contactperson if it is connected to a PowerOfficeGO Salesorders that is synchronized into Business.

Once a link between a PowerOfficeGO Contactperson and a Business Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Contactperson and a Business Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Contactperson Property
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


PowerOfficeGO Contactperson to BusinessCentral Contacts person
--------------------------------------------------------------
Every PowerOfficeGO Contactperson will be synchronized with a BusinessCentral Contacts person.

Once a link between a PowerOfficeGO Contactperson and a BusinessCentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Contactperson and a BusinessCentral Contacts person:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Contactperson Property
     - BusinessCentral Contacts person Property
     - BusinessCentral Data Type
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


PowerOfficeGO Customers to BusinessCentral Contacts person
----------------------------------------------------------
Every PowerOfficeGO Customers will be synchronized with a BusinessCentral Contacts person.

Once a link between a PowerOfficeGO Customers and a BusinessCentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers and a BusinessCentral Contacts person:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers Property
     - BusinessCentral Contacts person Property
     - BusinessCentral Data Type
   * - IsPerson
     - type
     - "string"


PowerOfficeGO Customers to BusinessCentral Customers company
------------------------------------------------------------
Every PowerOfficeGO Customers will be synchronized with a BusinessCentral Customers company.

Once a link between a PowerOfficeGO Customers and a BusinessCentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers and a BusinessCentral Customers company:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers Property
     - BusinessCentral Customers company Property
     - BusinessCentral Data Type
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


PowerOfficeGO Customers to BusinessCentral Customers person
-----------------------------------------------------------
Every PowerOfficeGO Customers will be synchronized with a BusinessCentral Customers person.

Once a link between a PowerOfficeGO Customers and a BusinessCentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers and a BusinessCentral Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers Property
     - BusinessCentral Customers person Property
     - BusinessCentral Data Type


PowerOfficeGO Customers person to BusinessCentral Contacts person
-----------------------------------------------------------------
Every PowerOfficeGO Customers person will be synchronized with a BusinessCentral Contacts person.

Once a link between a PowerOfficeGO Customers person and a BusinessCentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers person and a BusinessCentral Contacts person:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers person Property
     - BusinessCentral Contacts person Property
     - BusinessCentral Data Type
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


PowerOfficeGO Customers person to BusinessCentral Customers person
------------------------------------------------------------------
Every PowerOfficeGO Customers person will be synchronized with a BusinessCentral Customers person.

Once a link between a PowerOfficeGO Customers person and a BusinessCentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers person and a BusinessCentral Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers person Property
     - BusinessCentral Customers person Property
     - BusinessCentral Data Type
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


PowerOfficeGO Employees to BusinessCentral Employees
----------------------------------------------------
Every PowerOfficeGO Employees will be synchronized with a BusinessCentral Employees.

Once a link between a PowerOfficeGO Employees and a BusinessCentral Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Employees and a BusinessCentral Employees:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Employees Property
     - BusinessCentral Employees Property
     - BusinessCentral Data Type
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


PowerOfficeGO Product to BusinessCentral Items
----------------------------------------------
Every PowerOfficeGO Product will be synchronized with a BusinessCentral Items.

Once a link between a PowerOfficeGO Product and a BusinessCentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Product and a BusinessCentral Items:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Product Property
     - BusinessCentral Items Property
     - BusinessCentral Data Type
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


PowerOfficeGO Salesorderlines to BusinessCentral Salesorderlines
----------------------------------------------------------------
Every PowerOfficeGO Salesorderlines will be synchronized with a BusinessCentral Salesorderlines.

Once a link between a PowerOfficeGO Salesorderlines and a BusinessCentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Salesorderlines and a BusinessCentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Salesorderlines Property
     - BusinessCentral Salesorderlines Property
     - BusinessCentral Data Type
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


PowerOfficeGO Salesorders to BusinessCentral Salesorders
--------------------------------------------------------
Every PowerOfficeGO Salesorders will be synchronized with a BusinessCentral Salesorders.

Once a link between a PowerOfficeGO Salesorders and a BusinessCentral Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Salesorders and a BusinessCentral Salesorders:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Salesorders Property
     - BusinessCentral Salesorders Property
     - BusinessCentral Data Type
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


PowerOfficeGO Suppliers person to BusinessCentral Contacts person
-----------------------------------------------------------------
Every PowerOfficeGO Suppliers person will be synchronized with a BusinessCentral Contacts person.

Once a link between a PowerOfficeGO Suppliers person and a BusinessCentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Suppliers person and a BusinessCentral Contacts person:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Suppliers person Property
     - BusinessCentral Contacts person Property
     - BusinessCentral Data Type
   * - EmailAddress
     - email
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"

