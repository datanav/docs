====================================
SuperOffice to Exact Online Dataflow
====================================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Quotealternative to Exact Online Salesorders
--------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a Exact Online Salesorders must be established.

A new Exact Online Salesorders will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Quoteline that is synchronized into Exact Online.

Once a link between a SuperOffice Quotealternative and a Exact Online Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Exact Online Salesorders:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Exact Online Salesorders Property
     - Exact Online Data Type
   * - DiscountPercent
     - Discount
     - "string"
   * - Name
     - Description
     - "string"


SuperOffice Contact to Exact Online Accounts
--------------------------------------------
Every SuperOffice Contact will be synchronized with a Exact Online Accounts.

Once a link between a SuperOffice Contact and a Exact Online Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Exact Online Accounts:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Exact Online Accounts Property
     - Exact Online Data Type
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


SuperOffice Person to Exact Online Contacts
-------------------------------------------
Every SuperOffice Person will be synchronized with a Exact Online Contacts.

Once a link between a SuperOffice Person and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Exact Online Contacts Property
     - Exact Online Data Type
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


SuperOffice Quoteline to Exact Online Quotations
------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Exact Online Quotations.

Once a link between a SuperOffice Quoteline and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Exact Online Quotations Property
     - Exact Online Data Type


SuperOffice Sale to Exact Online Quotations
-------------------------------------------
Every SuperOffice Sale will be synchronized with a Exact Online Quotations.

Once a link between a SuperOffice Sale and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - Exact Online Quotations Property
     - Exact Online Data Type
   * - Currency.Id
     - Currency
     - "string"
   * - Saledate
     - DeliveryDate
     - "string"


SuperOffice Listcurrencyitems to Exact Online Currencies
--------------------------------------------------------
Every SuperOffice Listcurrencyitems will be synchronized with a Exact Online Currencies.

Once a link between a SuperOffice Listcurrencyitems and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcurrencyitems and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - Exact Online Currencies Property
     - Exact Online Data Type
   * - Name
     - Code
     - "string"


SuperOffice Person to Exact Online Addresses
--------------------------------------------
Every SuperOffice Person will be synchronized with a Exact Online Addresses.

Once a link between a SuperOffice Person and a Exact Online Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Exact Online Addresses:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Exact Online Addresses Property
     - Exact Online Data Type
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


SuperOffice Product to Exact Online Items
-----------------------------------------
Every SuperOffice Product will be synchronized with a Exact Online Items.

Once a link between a SuperOffice Product and a Exact Online Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Exact Online Items:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Exact Online Items Property
     - Exact Online Data Type
   * - Code
     - Code
     - "string"


SuperOffice Product to Exact Online Vatcodes
--------------------------------------------
Every SuperOffice Product will be synchronized with a Exact Online Vatcodes.

Once a link between a SuperOffice Product and a Exact Online Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Exact Online Vatcodes:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Exact Online Vatcodes Property
     - Exact Online Data Type
   * - Code
     - Code
     - "string"


SuperOffice Quotealternative to Exact Online Quotations
-------------------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a Exact Online Quotations.

Once a link between a SuperOffice Quotealternative and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Exact Online Quotations Property
     - Exact Online Data Type
   * - Name
     - Description
     - "string"


SuperOffice Quotealternative to Exact Online Vatcodes
-----------------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a Exact Online Vatcodes.

Once a link between a SuperOffice Quotealternative and a Exact Online Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Exact Online Vatcodes:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Exact Online Vatcodes Property
     - Exact Online Data Type
   * - VAT
     - Code
     - "string"


SuperOffice Quoteline to Exact Online Salesorderlines
-----------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Exact Online Salesorderlines.

Once a link between a SuperOffice Quoteline and a Exact Online Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Exact Online Salesorderlines:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Exact Online Salesorderlines Property
     - Exact Online Data Type
   * - ERPProductKey
     - Item
     - "string"
   * - QuoteAlternativeId
     - OrderID
     - "string"


SuperOffice Quoteline to Exact Online Vatcodes
----------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Exact Online Vatcodes.

Once a link between a SuperOffice Quoteline and a Exact Online Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Exact Online Vatcodes:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Exact Online Vatcodes Property
     - Exact Online Data Type
   * - VAT
     - Code
     - "string"

