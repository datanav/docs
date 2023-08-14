==========================================
Wave Financial to PowerOfficeGov1 Dataflow
==========================================

Generated: 2023-08-14 12:54:49

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to PowerOfficeGov1. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to PowerOfficeGov1 Employee
-----------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a PowerOfficeGov1 Employee must be established.

A Wave Customer will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGov1 Employee Property
   * - email
     - email

Once a link between a Wave Customer and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - MailAddress.Address1
     - "string"
   * - address.addressLine1
     - address.addressLine1
     - "string"
   * - address.addressLine1
     - streetAddresses.address1
     - "string"
   * - address.addressLine2
     - MailAddress.Address2
     - "string"
   * - address.addressLine2
     - address.addressLine2
     - "string"
   * - address.addressLine2
     - streetAddresses.address2
     - "string"
   * - address.city
     - MailAddress.City
     - "string"
   * - address.city
     - address.city
     - "string"
   * - address.city
     - streetAddresses.city
     - "string"
   * - address.country.code
     - MailAddress.CountryCode
     - "string"
   * - address.country.code
     - address.country.id
     - "integer"
   * - address.country.code
     - streetAddresses.countryCode
     - "string"
   * - address.postalCode
     - MailAddress.ZipCode
     - "string"
   * - address.postalCode
     - address.postalCode
     - "string"
   * - address.postalCode
     - streetAddresses.zipCode
     - "string"
   * - id
     - Id
     - "string"
   * - id
     - id
     - "integer"
   * - mobile
     - phoneNumberMobile
     - "string"


Wave Customer to PowerOfficeGov1 Person
---------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a PowerOfficeGov1 Person must be established.

A Wave Customer will merge with a PowerOfficeGov1 Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGov1 Person Property
   * - email
     - Emails.Value

Once a link between a Wave Customer and a PowerOfficeGov1 Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGov1 Person:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGov1 Person Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - Address.Street.Address1
     - "string"
   * - address.addressLine2
     - Address.Street.Address2
     - "string"
   * - address.city
     - Address.Street.City
     - "string"
   * - address.postalCode
     - Address.Street.Zipcode
     - "string"
   * - email
     - Emails.Value
     - "string"
   * - firstName
     - Firstname
     - "string"
   * - id
     - Contact.ContactId
     - "integer"
   * - id
     - PersonId
     - "integer"
   * - lastName
     - Lastname
     - "string"
   * - mobile
     - MobilePhones.Value
     - "string"


Wave Vendor to PowerOfficeGov1 Employee
---------------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a PowerOfficeGov1 Employee must be established.

A Wave Vendor will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGov1 Employee Property
   * - email
     - email

Once a link between a Wave Vendor and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - MailAddress.Address1
     - "string"
   * - address.addressLine1
     - address.addressLine1
     - "string"
   * - address.addressLine1
     - streetAddresses.address1
     - "string"
   * - address.addressLine2
     - MailAddress.Address2
     - "string"
   * - address.addressLine2
     - address.addressLine2
     - "string"
   * - address.addressLine2
     - streetAddresses.address2
     - "string"
   * - address.city
     - MailAddress.City
     - "string"
   * - address.city
     - address.city
     - "string"
   * - address.city
     - streetAddresses.city
     - "string"
   * - address.country.code
     - MailAddress.CountryCode
     - "string"
   * - address.country.code
     - address.country.id
     - "integer"
   * - address.country.code
     - streetAddresses.countryCode
     - "string"
   * - address.postalCode
     - MailAddress.ZipCode
     - "string"
   * - address.postalCode
     - address.postalCode
     - "string"
   * - address.postalCode
     - streetAddresses.zipCode
     - "string"
   * - id
     - Id
     - "string"
   * - id
     - id
     - "integer"
   * - mobile
     - phoneNumberMobile
     - "string"
   * - phone
     - phoneNumberWork
     - "string"


Wave Vendor to PowerOfficeGov1 Person
-------------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a PowerOfficeGov1 Person must be established.

A Wave Vendor will merge with a PowerOfficeGov1 Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGov1 Person Property
   * - email
     - Emails.Value

Once a link between a Wave Vendor and a PowerOfficeGov1 Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGov1 Person:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGov1 Person Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - Address.Street.Address1
     - "string"
   * - address.addressLine2
     - Address.Street.Address2
     - "string"
   * - address.city
     - Address.Street.City
     - "string"
   * - address.postalCode
     - Address.Street.Zipcode
     - "string"
   * - email
     - Emails.Value
     - "string"
   * - firstName
     - Firstname
     - "string"
   * - id
     - Contact.ContactId
     - "integer"
   * - id
     - PersonId
     - "integer"
   * - lastName
     - Lastname
     - "string"
   * - mobile
     - MobilePhones.Value
     - "string"
   * - phone
     - OfficePhones.Value
     - "string"


Wave Customer to PowerOfficeGov1 Customer
-----------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a PowerOfficeGov1 Customer must be established.

A new PowerOfficeGov1 Customer will be created from a Wave Customer if it is connected to a Wave Invoice that is synchronized into PowerOfficeGov1.

Once a link between a Wave Customer and a PowerOfficeGov1 Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGov1 Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGov1 Customer Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - streetAddresses.address1
     - "string"
   * - address.addressLine2
     - streetAddresses.address2
     - "string"
   * - address.city
     - streetAddresses.city
     - "string"
   * - address.country.code
     - streetAddresses.countryCode
     - "string"
   * - address.postalCode
     - streetAddresses.zipCode
     - "string"
   * - id
     - id
     - "string"
   * - modifiedAt
     - lastChanged
     - "string"
   * - name
     - legalName
     - "string"
   * - phone
     - phoneNumber
     - "string"
   * - shippingDetails.phone
     - phoneNumber
     - "string"
   * - website
     - websiteUrl
     - "string"


Wave Customer to PowerOfficeGov1 Contact
----------------------------------------
Every Wave Customer will be synchronized with a PowerOfficeGov1 Contact.

Once a link between a Wave Customer and a PowerOfficeGov1 Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGov1 Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGov1 Contact Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - Address.Street.Address1
     - "string"
   * - address.addressLine2
     - Address.Street.Address2
     - "string"
   * - address.city
     - Address.Street.City
     - "string"
   * - address.postalCode
     - Address.Street.Zipcode
     - "string"
   * - id
     - ContactId
     - "integer"
   * - mobile
     - phoneNumberMobile
     - "if","matches","+*","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
   * - name
     - Name
     - "string"
   * - phone
     - Phones.Value
     - "string"
   * - shippingDetails.phone
     - Phones.Value
     - "string"
   * - website
     - Domains
     - "list"
   * - website
     - Urls.Value
     - "string"


Wave Vendor to PowerOfficeGov1 Contact
--------------------------------------
Every Wave Vendor will be synchronized with a PowerOfficeGov1 Contact.

Once a link between a Wave Vendor and a PowerOfficeGov1 Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGov1 Contact:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGov1 Contact Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - Address.Street.Address1
     - "string"
   * - address.addressLine2
     - Address.Street.Address2
     - "string"
   * - address.city
     - Address.Street.City
     - "string"
   * - address.postalCode
     - Address.Street.Zipcode
     - "string"
   * - id
     - ContactId
     - "integer"
   * - mobile
     - phoneNumberMobile
     - "if","matches","+*","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
   * - name
     - Name
     - "string"
   * - phone
     - phoneNumberWork
     - "string"
   * - website
     - Domains
     - "list"
   * - website
     - Urls.Value
     - "string"


Wave Currency to PowerOfficeGov1 Currency
-----------------------------------------
Every Wave Currency will be synchronized with a PowerOfficeGov1 Currency.

If a matching PowerOfficeGov1 Currency already exists, the Wave Currency will be merged with the existing one.
If no matching PowerOfficeGov1 Currency is found, a new PowerOfficeGov1 Currency will be created.

A Wave Currency will merge with a PowerOfficeGov1 Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - PowerOfficeGov1 Currency Property
   * - code
     - Code
   * - code
     - code

Once a link between a Wave Currency and a PowerOfficeGov1 Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Currency and a PowerOfficeGov1 Currency:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - PowerOfficeGov1 Currency Property
     - PowerOfficeGov1 Data Type


Wave Customer to PowerOfficeGov1 Address
----------------------------------------
Every Wave Customer will be synchronized with a PowerOfficeGov1 Address.

Once a link between a Wave Customer and a PowerOfficeGov1 Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGov1 Address:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGov1 Address Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - address1
     - "string"
   * - address.addressLine2
     - address2
     - "string"
   * - address.city
     - city
     - "string"
   * - address.country.code
     - countryCode
     - "string"
   * - address.postalCode
     - zipCode
     - "string"


Wave Invoice to PowerOfficeGov1 Salesorder
------------------------------------------
Every Wave Invoice will be synchronized with a PowerOfficeGov1 Salesorder.

Once a link between a Wave Invoice and a PowerOfficeGov1 Salesorder is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a PowerOfficeGov1 Salesorder:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - PowerOfficeGov1 Salesorder Property
     - PowerOfficeGov1 Data Type
   * - currency.code
     - Currency
     - "string"
   * - customer.id
     - DepartmentCode
     - "string"


Wave Product to PowerOfficeGov1 Product
---------------------------------------
Every Wave Product will be synchronized with a PowerOfficeGov1 Product.

Once a link between a Wave Product and a PowerOfficeGov1 Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a PowerOfficeGov1 Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - PowerOfficeGov1 Product Property
     - PowerOfficeGov1 Data Type
   * - description
     - Description
     - "string"
   * - description
     - description
     - "string"
   * - expenseAccount.id
     - expenseAccount.id
     - "string"
   * - incomeAccount.id
     - incomeAccount.id
     - "string"
   * - modifiedAt
     - lastChanged
     - "string"
   * - name
     - Name
     - "string"
   * - name
     - name
     - "string"
   * - unitPrice
     - UnitListPrice
     - "decimal"
   * - unitPrice
     - priceExcludingVatCurrency
     - "float"
   * - unitPrice
     - salesPrice
     - "string"
   * - unitPrice
     - unitPrice
     - "string"


Wave Vendor to PowerOfficeGov1 Address
--------------------------------------
Every Wave Vendor will be synchronized with a PowerOfficeGov1 Address.

Once a link between a Wave Vendor and a PowerOfficeGov1 Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGov1 Address:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGov1 Address Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - address1
     - "string"
   * - address.addressLine2
     - address2
     - "string"
   * - address.city
     - city
     - "string"
   * - address.country.code
     - countryCode
     - "string"
   * - address.postalCode
     - zipCode
     - "string"


Wave Vendor to PowerOfficeGov1 Supplier
---------------------------------------
Every Wave Vendor will be synchronized with a PowerOfficeGov1 Supplier.

Once a link between a Wave Vendor and a PowerOfficeGov1 Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGov1 Supplier:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGov1 Supplier Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - address.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - address.city
     - physicalAddress.city
     - "string"
   * - address.country.code
     - physicalAddress.country.id
     - "integer"
   * - address.postalCode
     - physicalAddress.postalCode
     - "string"
   * - id
     - id
     - "integer"
   * - modifiedAt
     - LastChanged
     - "string"
   * - name
     - LegalName
     - "string"
   * - name
     - name
     - "string"
   * - website
     - WebsiteUrl
     - "string"

