===========================================
Businesscentral to Businesscentral Dataflow
===========================================

Generated: 2024-06-27 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Contacts person to Businesscentral Contacts person
------------------------------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Contacts person and a Businesscentral Contacts person must be established.

A Businesscentral Contacts person will merge with a Businesscentral Contacts person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     - Businesscentral Contacts person Property
   * - id
     - id

Once a link between a Businesscentral Contacts person and a Businesscentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a Businesscentral Contacts person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     - Businesscentral Contacts person Property
     - Businesscentral Data Type
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


Businesscentral Contactsinformation person customer relation to Businesscentral Contacts person
-----------------------------------------------------------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Contactsinformation person customer relation and a Businesscentral Contacts person must be established.

A Businesscentral Contactsinformation person customer relation will merge with a Businesscentral Contacts person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contactsinformation person customer relation Property
     - Businesscentral Contacts person Property
   * - contactId
     - id

Once a link between a Businesscentral Contactsinformation person customer relation and a Businesscentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contactsinformation person customer relation and a Businesscentral Contacts person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contactsinformation person customer relation Property
     - Businesscentral Contacts person Property
     - Businesscentral Data Type
   * - contactId
     - id
     - "string"
   * - contactName
     - displayName
     - "string"
   * - contactName.contactName
     - displayName
     - "string"


Businesscentral Items to Businesscentral Items
----------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Items and a Businesscentral Items must be established.

A Businesscentral Items will merge with a Businesscentral Items if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     - Businesscentral Items Property
   * - gtin
     - gtin

Once a link between a Businesscentral Items and a Businesscentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a Businesscentral Items:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     - Businesscentral Items Property
     - Businesscentral Data Type
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


Businesscentral Customers company to Businesscentral Companies
--------------------------------------------------------------
Every Businesscentral Customers company will be synchronized with a Businesscentral Companies.

Once a link between a Businesscentral Customers company and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Businesscentral Contacts person to Businesscentral Customers person
-------------------------------------------------------------------
Every Businesscentral Contacts person will be synchronized with a Businesscentral Customers person.

Once a link between a Businesscentral Contacts person and a Businesscentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a Businesscentral Customers person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     - Businesscentral Customers person Property
     - Businesscentral Data Type
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


Businesscentral Customers person to Businesscentral Contacts person
-------------------------------------------------------------------
Every Businesscentral Customers person will be synchronized with a Businesscentral Contacts person.

Once a link between a Businesscentral Customers person and a Businesscentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a Businesscentral Contacts person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     - Businesscentral Contacts person Property
     - Businesscentral Data Type
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

