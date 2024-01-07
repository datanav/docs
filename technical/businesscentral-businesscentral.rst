============================
Businesscentral to  Dataflow
============================

Generated: 2024-01-07 00:00:01

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Contacts person to  Contacts person
---------------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Contacts person and a  Contacts person must be established.

A Businesscentral Contacts person will merge with a  Contacts person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     -  Contacts person Property
   * - id
     - id

Once a link between a Businesscentral Contacts person and a  Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a  Contacts person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     -  Contacts person Property
     -  Data Type
   * - addressLine1
     - addressLine2
     - "string"
   * - addressLine2
     - addressLine1
     - "string"
   * - mobilePhoneNumber
     - phoneNumber
     - "string"
   * - phoneNumber
     - mobilePhoneNumber
     - "string"


Businesscentral Contactsinformation person customer relation to  Contacts person
--------------------------------------------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Contactsinformation person customer relation and a  Contacts person must be established.

A Businesscentral Contactsinformation person customer relation will merge with a  Contacts person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contactsinformation person customer relation Property
     -  Contacts person Property
   * - contactId
     - id

Once a link between a Businesscentral Contactsinformation person customer relation and a  Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contactsinformation person customer relation and a  Contacts person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contactsinformation person customer relation Property
     -  Contacts person Property
     -  Data Type
   * - contactId
     - id
     - "string"
   * - contactName
     - displayName
     - "string"
   * - contactName.contactName
     - displayName
     - "string"


Businesscentral Items to  Items
-------------------------------
Before any synchronization can take place, a link between a Businesscentral Items and a  Items must be established.

A Businesscentral Items will merge with a  Items if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Items Property
   * - gtin
     - gtin

Once a link between a Businesscentral Items and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Items:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Items Property
     -  Data Type
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


Businesscentral Customers company to  Companies
-----------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Companies.

Once a link between a Businesscentral Customers company and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Companies:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Companies Property
     -  Data Type


Businesscentral Contacts person to  Customers person
----------------------------------------------------
Every Businesscentral Contacts person will be synchronized with a  Customers person.

Once a link between a Businesscentral Contacts person and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     -  Customers person Property
     -  Data Type
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


Businesscentral Customers person to  Contacts person
----------------------------------------------------
Every Businesscentral Customers person will be synchronized with a  Contacts person.

Once a link between a Businesscentral Customers person and a  Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a  Contacts person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     -  Contacts person Property
     -  Data Type
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
   * - id
     - id
     - "string"
   * - postalCode
     - postalCode
     - "string"
   * - type
     - type
     - "string"

