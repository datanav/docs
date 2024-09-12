=============================================
Business Central to Business Central Dataflow
=============================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Contacts person to Business Central Contacts person
--------------------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Contacts person and a Business Central Contacts person must be established.

A Business Central Contacts person will merge with a Business Central Contacts person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - Business Central Contacts person Property
   * - id
     - id

Once a link between a Business Central Contacts person and a Business Central Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts person and a Business Central Contacts person:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - Business Central Contacts person Property
     - Business Central Data Type
   * - addressLine1
     - addressLine2
     - "string"
   * - addressLine2
     - addressLine1
     - "string"
   * - mobilePhoneNumber
     - mobilePhoneNumber
     - "string"
   * - mobilePhoneNumber
     - phoneNumber
     - "string"
   * - phoneNumber
     - mobilePhoneNumber
     - "string"


Business Central Contacts person to Business Central Contactsinformation person customer relation
-------------------------------------------------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Contacts person and a Business Central Contactsinformation person customer relation must be established.

A Business Central Contacts person will merge with a Business Central Contactsinformation person customer relation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - Business Central Contactsinformation person customer relation Property
   * - id
     - contactId

Once a link between a Business Central Contacts person and a Business Central Contactsinformation person customer relation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts person and a Business Central Contactsinformation person customer relation:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - Business Central Contactsinformation person customer relation Property
     - Business Central Data Type


Business Central Contactsinformation person customer relation to Business Central Contacts person
-------------------------------------------------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Contactsinformation person customer relation and a Business Central Contacts person must be established.

A Business Central Contactsinformation person customer relation will merge with a Business Central Contacts person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Contactsinformation person customer relation Property
     - Business Central Contacts person Property
   * - contactId
     - id

Once a link between a Business Central Contactsinformation person customer relation and a Business Central Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contactsinformation person customer relation and a Business Central Contacts person:

.. list-table::
   :header-rows: 1

   * - Business Central Contactsinformation person customer relation Property
     - Business Central Contacts person Property
     - Business Central Data Type
   * - contactId
     - id
     - "string"
   * - contactName
     - displayName
     - "string"
   * - contactName.contactName
     - displayName
     - "string"


Business Central Contactsinformation person customer relation to Business Central Contactsinformation person customer relation
------------------------------------------------------------------------------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Contactsinformation person customer relation and a Business Central Contactsinformation person customer relation must be established.

A Business Central Contactsinformation person customer relation will merge with a Business Central Contactsinformation person customer relation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Contactsinformation person customer relation Property
     - Business Central Contactsinformation person customer relation Property
   * - contactId
     - contactId

Once a link between a Business Central Contactsinformation person customer relation and a Business Central Contactsinformation person customer relation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contactsinformation person customer relation and a Business Central Contactsinformation person customer relation:

.. list-table::
   :header-rows: 1

   * - Business Central Contactsinformation person customer relation Property
     - Business Central Contactsinformation person customer relation Property
     - Business Central Data Type


Business Central Currencies to Business Central Currencies
----------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Currencies and a Business Central Currencies must be established.

A Business Central Currencies will merge with a Business Central Currencies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Currencies Property
     - Business Central Currencies Property
   * - code
     - code

Once a link between a Business Central Currencies and a Business Central Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Currencies and a Business Central Currencies:

.. list-table::
   :header-rows: 1

   * - Business Central Currencies Property
     - Business Central Currencies Property
     - Business Central Data Type


Business Central Itemcategories to Business Central Itemcategories
------------------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Itemcategories and a Business Central Itemcategories must be established.

A Business Central Itemcategories will merge with a Business Central Itemcategories if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Itemcategories Property
     - Business Central Itemcategories Property
   * - code
     - code

Once a link between a Business Central Itemcategories and a Business Central Itemcategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Itemcategories and a Business Central Itemcategories:

.. list-table::
   :header-rows: 1

   * - Business Central Itemcategories Property
     - Business Central Itemcategories Property
     - Business Central Data Type


Business Central Items to Business Central Items
------------------------------------------------
Before any synchronization can take place, a link between a Business Central Items and a Business Central Items must be established.

A Business Central Items will merge with a Business Central Items if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Business Central Items Property
   * - gtin
     - gtin

Once a link between a Business Central Items and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Business Central Items Property
     - Business Central Data Type
   * - displayName
     - displayName2
     - "string"
   * - displayName2
     - displayName
     - "string"
   * - itemCategoryId
     - taxGroupId
     - "string"
   * - taxGroupId
     - itemCategoryId
     - "string"


Business Central Customers company to Business Central Companies
----------------------------------------------------------------
Every Business Central Customers company will be synchronized with a Business Central Companies.

Once a link between a Business Central Customers company and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Business Central Companies Property
     - Business Central Data Type


Business Central Contacts person to Business Central Customers person
---------------------------------------------------------------------
Every Business Central Contacts person will be synchronized with a Business Central Customers person.

Once a link between a Business Central Contacts person and a Business Central Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts person and a Business Central Customers person:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - Business Central Customers person Property
     - Business Central Data Type
   * - addressLine1
     - addressLine1
     - "string"
   * - addressLine2
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
   * - country
     - country
     - "string"
   * - displayName
     - displayName
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id (Dependant on having BusinessCentral-contact in type)
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - postalCode
     - address.postalCode
     - "string"
   * - postalCode
     - postalCode
     - "string"
   * - type
     - type
     - "string"


Business Central Customers person to Business Central Contacts person
---------------------------------------------------------------------
Every Business Central Customers person will be synchronized with a Business Central Contacts person.

Once a link between a Business Central Customers person and a Business Central Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a Business Central Contacts person:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - Business Central Contacts person Property
     - Business Central Data Type
   * - address.city
     - city
     - "string"
   * - address.postalCode
     - postalCode
     - "string"
   * - addressLine1
     - addressLine1
     - "string"
   * - addressLine2
     - addressLine2
     - "string"
   * - addressLine2
     - city
     - "string"
   * - city
     - city
     - "string"
   * - country
     - country
     - "string"
   * - displayName
     - displayName
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - postalCode
     - postalCode
     - "string"
   * - type
     - type
     - "string"

