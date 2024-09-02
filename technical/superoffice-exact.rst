========================
SuperOffice to  Dataflow
========================

Generated: 2024-09-02 11:04:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Quotealternative to  Salesorders
--------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a  Salesorders must be established.

A new  Salesorders will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Quoteline that is synchronized into .

Once a link between a SuperOffice Quotealternative and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     -  Salesorders Property
     -  Data Type
   * - DiscountPercent
     - Discount
     - "string"
   * - Name
     - Description
     - "string"


SuperOffice Contact to  Accounts
--------------------------------
Every SuperOffice Contact will be synchronized with a  Accounts.

Once a link between a SuperOffice Contact and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Accounts:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Accounts Property
     -  Data Type
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


SuperOffice Person to  Contacts
-------------------------------
Every SuperOffice Person will be synchronized with a  Contacts.

Once a link between a SuperOffice Person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Contacts Property
     -  Data Type
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


SuperOffice Quoteline to  Quotations
------------------------------------
Every SuperOffice Quoteline will be synchronized with a  Quotations.

Once a link between a SuperOffice Quoteline and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a  Quotations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     -  Quotations Property
     -  Data Type


SuperOffice Sale to  Quotations
-------------------------------
Every SuperOffice Sale will be synchronized with a  Quotations.

Once a link between a SuperOffice Sale and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a  Quotations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     -  Quotations Property
     -  Data Type
   * - Currency.Id
     - Currency
     - "string"
   * - Saledate
     - DeliveryDate
     - "string"


SuperOffice Listcurrencyitems to  Currencies
--------------------------------------------
Every SuperOffice Listcurrencyitems will be synchronized with a  Currencies.

Once a link between a SuperOffice Listcurrencyitems and a  Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcurrencyitems and a  Currencies:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     -  Currencies Property
     -  Data Type
   * - Name
     - Code
     - "string"


SuperOffice Person to  Addresses
--------------------------------
Every SuperOffice Person will be synchronized with a  Addresses.

Once a link between a SuperOffice Person and a  Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a  Addresses:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Addresses Property
     -  Data Type
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


SuperOffice Product to  Items
-----------------------------
Every SuperOffice Product will be synchronized with a  Items.

Once a link between a SuperOffice Product and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a  Items:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     -  Items Property
     -  Data Type


SuperOffice Quotealternative to  Quotations
-------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a  Quotations.

Once a link between a SuperOffice Quotealternative and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a  Quotations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     -  Quotations Property
     -  Data Type
   * - Name
     - Description
     - "string"


SuperOffice Quoteline to  Salesorderlines
-----------------------------------------
Every SuperOffice Quoteline will be synchronized with a  Salesorderlines.

Once a link between a SuperOffice Quoteline and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     -  Salesorderlines Property
     -  Data Type
   * - ERPProductKey
     - Item
     - "string"
   * - QuoteAlternativeId
     - OrderID
     - "string"

