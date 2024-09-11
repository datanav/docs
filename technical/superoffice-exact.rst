===================================
SuperOffice to ExactOnline Dataflow
===================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to ExactOnline. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Quotealternative to ExactOnline Salesorders
-------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a ExactOnline Salesorders must be established.

A new ExactOnline Salesorders will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Quoteline that is synchronized into ExactOnline.

Once a link between a SuperOffice Quotealternative and a ExactOnline Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a ExactOnline Salesorders:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - ExactOnline Salesorders Property
     - ExactOnline Data Type
   * - DiscountPercent
     - Discount
     - "string"
   * - Name
     - Description
     - "string"


SuperOffice Contact to ExactOnline Accounts
-------------------------------------------
Every SuperOffice Contact will be synchronized with a ExactOnline Accounts.

Once a link between a SuperOffice Contact and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type
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


SuperOffice Person to ExactOnline Contacts
------------------------------------------
Every SuperOffice Person will be synchronized with a ExactOnline Contacts.

Once a link between a SuperOffice Person and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type
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


SuperOffice Quoteline to ExactOnline Quotations
-----------------------------------------------
Every SuperOffice Quoteline will be synchronized with a ExactOnline Quotations.

Once a link between a SuperOffice Quoteline and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type


SuperOffice Sale to ExactOnline Quotations
------------------------------------------
Every SuperOffice Sale will be synchronized with a ExactOnline Quotations.

Once a link between a SuperOffice Sale and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type
   * - Currency.Id
     - Currency
     - "string"
   * - Saledate
     - DeliveryDate
     - "string"


SuperOffice Listcurrencyitems to ExactOnline Currencies
-------------------------------------------------------
Every SuperOffice Listcurrencyitems will be synchronized with a ExactOnline Currencies.

Once a link between a SuperOffice Listcurrencyitems and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcurrencyitems and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - Name
     - Code
     - "string"


SuperOffice Person to ExactOnline Addresses
-------------------------------------------
Every SuperOffice Person will be synchronized with a ExactOnline Addresses.

Once a link between a SuperOffice Person and a ExactOnline Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a ExactOnline Addresses:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - ExactOnline Addresses Property
     - ExactOnline Data Type
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


SuperOffice Product to ExactOnline Items
----------------------------------------
Every SuperOffice Product will be synchronized with a ExactOnline Items.

Once a link between a SuperOffice Product and a ExactOnline Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a ExactOnline Items:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - ExactOnline Items Property
     - ExactOnline Data Type
   * - Code
     - Code
     - "string"


SuperOffice Product to ExactOnline Vatcodes
-------------------------------------------
Every SuperOffice Product will be synchronized with a ExactOnline Vatcodes.

Once a link between a SuperOffice Product and a ExactOnline Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a ExactOnline Vatcodes:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - ExactOnline Vatcodes Property
     - ExactOnline Data Type
   * - Code
     - Code
     - "string"


SuperOffice Quotealternative to ExactOnline Quotations
------------------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a ExactOnline Quotations.

Once a link between a SuperOffice Quotealternative and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type
   * - Name
     - Description
     - "string"


SuperOffice Quotealternative to ExactOnline Vatcodes
----------------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a ExactOnline Vatcodes.

Once a link between a SuperOffice Quotealternative and a ExactOnline Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a ExactOnline Vatcodes:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - ExactOnline Vatcodes Property
     - ExactOnline Data Type
   * - VAT
     - Code
     - "string"


SuperOffice Quoteline to ExactOnline Salesorderlines
----------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a ExactOnline Salesorderlines.

Once a link between a SuperOffice Quoteline and a ExactOnline Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a ExactOnline Salesorderlines:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - ExactOnline Salesorderlines Property
     - ExactOnline Data Type
   * - ERPProductKey
     - Item
     - "string"
   * - QuoteAlternativeId
     - OrderID
     - "string"


SuperOffice Quoteline to ExactOnline Vatcodes
---------------------------------------------
Every SuperOffice Quoteline will be synchronized with a ExactOnline Vatcodes.

Once a link between a SuperOffice Quoteline and a ExactOnline Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a ExactOnline Vatcodes:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - ExactOnline Vatcodes Property
     - ExactOnline Data Type
   * - VAT
     - Code
     - "string"

