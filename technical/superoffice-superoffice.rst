===================================
SuperOffice to SuperOffice Dataflow
===================================

Generated: 2023-05-22 22:07:22

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Listcurrencyitems to SuperOffice Pricelist
------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Listcurrencyitems and a SuperOffice Pricelist must be established.

A SuperOffice Listcurrencyitems will merge with a SuperOffice Pricelist if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - SuperOffice Pricelist Property
   * - Name
     - Currency

Once a link between a SuperOffice Listcurrencyitems and a SuperOffice Pricelist is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcurrencyitems and a SuperOffice Pricelist:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - SuperOffice Pricelist Property
     - SuperOffice Data Type
   * - Name
     - Currency
     - "string"


SuperOffice Ownercontactlink to SuperOffice Contact
---------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Ownercontactlink and a SuperOffice Contact must be established.

A SuperOffice Ownercontactlink will merge with a SuperOffice Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - SuperOffice Contact Property
   * - contact_id
     - ContactId

Once a link between a SuperOffice Ownercontactlink and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ownercontactlink and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - contact_id
     - ContactId
     - "string"
   * - name
     - Name
     - "string"
   * - ownercontactlink.contact_id
     - ContactId
     - "string"
   * - ownercontactlink.contact_id.name
     - Name
     - "string"


SuperOffice Pricelist to SuperOffice Listcurrencyitems
------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Pricelist and a SuperOffice Listcurrencyitems must be established.

A SuperOffice Pricelist will merge with a SuperOffice Listcurrencyitems if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Pricelist Property
     - SuperOffice Listcurrencyitems Property
   * - Currency
     - Name

Once a link between a SuperOffice Pricelist and a SuperOffice Listcurrencyitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Pricelist and a SuperOffice Listcurrencyitems:

.. list-table::
   :header-rows: 1

   * - SuperOffice Pricelist Property
     - SuperOffice Listcurrencyitems Property
     - SuperOffice Data Type
   * - Description
     - Tooltip
     - "string"
   * - ERPPriceListKey
     - Name
     - "string"


SuperOffice Quote to SuperOffice Sale
-------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quote and a SuperOffice Sale must be established.

A SuperOffice Quote will merge with a SuperOffice Sale if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quote Property
     - SuperOffice Sale Property
   * - SaleId
     - SaleId

Once a link between a SuperOffice Quote and a SuperOffice Sale is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quote and a SuperOffice Sale:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quote Property
     - SuperOffice Sale Property
     - SuperOffice Data Type


SuperOffice User to SuperOffice Person
--------------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a SuperOffice Person must be established.

A SuperOffice User will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - SuperOffice Person Property
   * - personEmail
     - Emails.Value

Once a link between a SuperOffice User and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - contactId
     - Contact.ContactId
     - "integer"
   * - firstName
     - Firstname
     - "string"
   * - lastName
     - Lastname
     - "string"
   * - personEmail
     - Emails.Value
     - "string"


SuperOffice Quoteline to SuperOffice Quotealternative
-----------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a SuperOffice Quotealternative.

Once a link between a SuperOffice Quoteline and a SuperOffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a SuperOffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - SuperOffice Quotealternative Property
     - SuperOffice Data Type
   * - TotalPrice
     - TotalPrice
     - "integer"
   * - VATInfo
     - VATInfo
     - "string"


SuperOffice Sale to SuperOffice Quotealternative
------------------------------------------------
Every SuperOffice Sale will be synchronized with a SuperOffice Quotealternative.

Once a link between a SuperOffice Sale and a SuperOffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a SuperOffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - SuperOffice Quotealternative Property
     - SuperOffice Data Type
   * - Amount
     - TotalPrice
     - "integer"
   * - Heading
     - Name
     - "string"
   * - SaleId
     - sesam_SaleId
     - "integer"
   * - SaleText
     - Description
     - "string"
   * - Status
     - sesam_Accepted
     - "boolean"


SuperOffice User to SuperOffice Listcategoryitems
-------------------------------------------------
Every SuperOffice User will be synchronized with a SuperOffice Listcategoryitems.

Once a link between a SuperOffice User and a SuperOffice Listcategoryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a SuperOffice Listcategoryitems:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - SuperOffice Listcategoryitems Property
     - SuperOffice Data Type
   * - contactCategory
     - Name
     - "string"

