=============================
SuperOffice to Exact Dataflow
=============================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Quotealternative to Exact Salesorders
-------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a Exact Salesorders must be established.

A new Exact Salesorders will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Quoteline that is synchronized into Exact.

Once a link between a SuperOffice Quotealternative and a Exact Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Exact Salesorders:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Exact Salesorders Property
     - Exact Data Type
   * - DiscountPercent
     - Discount
     - "string"
   * - Name
     - Description
     - "string"


SuperOffice Contact to Exact Accounts
-------------------------------------
Every SuperOffice Contact will be synchronized with a Exact Accounts.

Once a link between a SuperOffice Contact and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Exact Accounts Property
     - Exact Data Type
   * - Address.Postal.Address1
     - AddressLine1
     - "string"
   * - Address.Postal.Address2
     - AddressLine2
     - "string"
   * - Address.Postal.Address3
     - AddressLine3
     - "string"
   * - Address.Postal.City
     - City
     - "string"
   * - Address.Postal.Zipcode
     - Postcode
     - "string"
   * - Address.Street.Address1
     - AddressLine1
     - "string"
   * - Address.Street.Address2
     - AddressLine2
     - "string"
   * - Address.Street.Address3
     - AddressLine3
     - "string"
   * - Address.Street.City
     - City
     - "string"
   * - Address.Street.Zipcode
     - Postcode
     - "string"
   * - Country.CountryId
     - Country
     - "string"
   * - Name
     - Name
     - "string"
   * - Phones.Value
     - Phone
     - "string"
   * - Urls.Value
     - Website
     - "string"


SuperOffice Person to Exact Contacts
------------------------------------
Every SuperOffice Person will be synchronized with a Exact Contacts.

Once a link between a SuperOffice Person and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Exact Contacts Property
     - Exact Data Type
   * - Address.Street.City
     - City
     - "string"
   * - BirthDate
     - BirthDate
     - "string"
   * - Country.CountryId
     - Country
     - "string"
   * - Emails.Value
     - Email
     - "string"
   * - Firstname
     - FirstName
     - "string"
   * - Lastname
     - LastName
     - "string"
   * - MobilePhones.Value
     - Mobile
     - "string"
   * - OfficePhones.Value
     - Phone
     - "string"


SuperOffice Quoteline to Exact Quotations
-----------------------------------------
Every SuperOffice Quoteline will be synchronized with a Exact Quotations.

Once a link between a SuperOffice Quoteline and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Exact Quotations Property
     - Exact Data Type


SuperOffice Sale to Exact Quotations
------------------------------------
Every SuperOffice Sale will be synchronized with a Exact Quotations.

Once a link between a SuperOffice Sale and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - Exact Quotations Property
     - Exact Data Type
   * - Currency.Id
     - Currency
     - "string"
   * - Saledate
     - DeliveryDate
     - "string"


SuperOffice Listcurrencyitems to Exact Currencies
-------------------------------------------------
Every SuperOffice Listcurrencyitems will be synchronized with a Exact Currencies.

Once a link between a SuperOffice Listcurrencyitems and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcurrencyitems and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - Exact Currencies Property
     - Exact Data Type
   * - Name
     - Code
     - "string"


SuperOffice Person to Exact Addresses
-------------------------------------
Every SuperOffice Person will be synchronized with a Exact Addresses.

Once a link between a SuperOffice Person and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Exact Addresses Property
     - Exact Data Type
   * - Address.Street.Address1
     - AddressLine1
     - "string"
   * - Address.Street.Address2
     - AddressLine2
     - "string"
   * - Address.Street.Address3
     - AddressLine3
     - "string"
   * - Address.Street.City
     - City
     - "string"
   * - Country.CountryId
     - Country
     - "string"


SuperOffice Product to Exact Items
----------------------------------
Every SuperOffice Product will be synchronized with a Exact Items.

Once a link between a SuperOffice Product and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Exact Items:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Exact Items Property
     - Exact Data Type
   * - Code
     - Code
     - "string"


SuperOffice Product to Exact Vatcodes
-------------------------------------
Every SuperOffice Product will be synchronized with a Exact Vatcodes.

Once a link between a SuperOffice Product and a Exact Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Exact Vatcodes:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Exact Vatcodes Property
     - Exact Data Type
   * - Code
     - Code
     - "string"


SuperOffice Quotealternative to Exact Quotations
------------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a Exact Quotations.

Once a link between a SuperOffice Quotealternative and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Exact Quotations Property
     - Exact Data Type
   * - Name
     - Description
     - "string"


SuperOffice Quotealternative to Exact Vatcodes
----------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a Exact Vatcodes.

Once a link between a SuperOffice Quotealternative and a Exact Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Exact Vatcodes:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Exact Vatcodes Property
     - Exact Data Type
   * - VAT
     - Code
     - "string"


SuperOffice Quoteline to Exact Salesorderlines
----------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Exact Salesorderlines.

Once a link between a SuperOffice Quoteline and a Exact Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Exact Salesorderlines:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Exact Salesorderlines Property
     - Exact Data Type
   * - ERPProductKey
     - Item
     - "string"
   * - QuoteAlternativeId
     - OrderID
     - "string"


SuperOffice Quoteline to Exact Vatcodes
---------------------------------------
Every SuperOffice Quoteline will be synchronized with a Exact Vatcodes.

Once a link between a SuperOffice Quoteline and a Exact Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Exact Vatcodes:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Exact Vatcodes Property
     - Exact Data Type
   * - VAT
     - Code
     - "string"

