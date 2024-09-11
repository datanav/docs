============================================
BusinessCentral to Business Central Dataflow
============================================

Generated: 2024-09-11 08:36:19

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessCentral to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessCentral Contacts person to Business Contacts person
-----------------------------------------------------------
Before any synchronization can take place, a link between a BusinessCentral Contacts person and a Business Contacts person must be established.

A BusinessCentral Contacts person will merge with a Business Contacts person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contacts person Property
     - Business Contacts person Property
   * - id
     - id

Once a link between a BusinessCentral Contacts person and a Business Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Contacts person and a Business Contacts person:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contacts person Property
     - Business Contacts person Property
     - Business Data Type
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


BusinessCentral Contactsinformation person customer relation to Business Contacts person
----------------------------------------------------------------------------------------
Before any synchronization can take place, a link between a BusinessCentral Contactsinformation person customer relation and a Business Contacts person must be established.

A BusinessCentral Contactsinformation person customer relation will merge with a Business Contacts person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contactsinformation person customer relation Property
     - Business Contacts person Property
   * - contactId
     - id

Once a link between a BusinessCentral Contactsinformation person customer relation and a Business Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Contactsinformation person customer relation and a Business Contacts person:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contactsinformation person customer relation Property
     - Business Contacts person Property
     - Business Data Type
   * - contactId
     - id
     - "string"
   * - contactName
     - displayName
     - "string"
   * - contactName.contactName
     - displayName
     - "string"


BusinessCentral Items to Business Items
---------------------------------------
Before any synchronization can take place, a link between a BusinessCentral Items and a Business Items must be established.

A BusinessCentral Items will merge with a Business Items if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Items Property
     - Business Items Property
   * - gtin
     - gtin

Once a link between a BusinessCentral Items and a Business Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Items and a Business Items:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Items Property
     - Business Items Property
     - Business Data Type
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


Business Contacts person to Business Customers person
-----------------------------------------------------
Every Business Contacts person will be synchronized with a Business Customers person.

Once a link between a Business Contacts person and a Business Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Contacts person and a Business Customers person:

.. list-table::
   :header-rows: 1

   * - Business Contacts person Property
     - Business Customers person Property
     - Business Data Type
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


Business Customers person to Business Contacts person
-----------------------------------------------------
Every Business Customers person will be synchronized with a Business Contacts person.

Once a link between a Business Customers person and a Business Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers person and a Business Contacts person:

.. list-table::
   :header-rows: 1

   * - Business Customers person Property
     - Business Contacts person Property
     - Business Data Type
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

