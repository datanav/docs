===========================================
BusinessCentral to BusinessCentral Dataflow
===========================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessCentral to BusinessCentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessCentral Contacts person to BusinessCentral Contacts person
------------------------------------------------------------------
Before any synchronization can take place, a link between a BusinessCentral Contacts person and a BusinessCentral Contacts person must be established.

A BusinessCentral Contacts person will merge with a BusinessCentral Contacts person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contacts person Property
     - BusinessCentral Contacts person Property
   * - id
     - id

Once a link between a BusinessCentral Contacts person and a BusinessCentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Contacts person and a BusinessCentral Contacts person:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contacts person Property
     - BusinessCentral Contacts person Property
     - BusinessCentral Data Type
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


BusinessCentral Contactsinformation person customer relation to BusinessCentral Contacts person
-----------------------------------------------------------------------------------------------
Before any synchronization can take place, a link between a BusinessCentral Contactsinformation person customer relation and a BusinessCentral Contacts person must be established.

A BusinessCentral Contactsinformation person customer relation will merge with a BusinessCentral Contacts person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contactsinformation person customer relation Property
     - BusinessCentral Contacts person Property
   * - contactId
     - id

Once a link between a BusinessCentral Contactsinformation person customer relation and a BusinessCentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Contactsinformation person customer relation and a BusinessCentral Contacts person:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contactsinformation person customer relation Property
     - BusinessCentral Contacts person Property
     - BusinessCentral Data Type
   * - contactId
     - id
     - "string"
   * - contactName
     - displayName
     - "string"
   * - contactName.contactName
     - displayName
     - "string"


BusinessCentral Items to BusinessCentral Items
----------------------------------------------
Before any synchronization can take place, a link between a BusinessCentral Items and a BusinessCentral Items must be established.

A BusinessCentral Items will merge with a BusinessCentral Items if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Items Property
     - BusinessCentral Items Property
   * - gtin
     - gtin

Once a link between a BusinessCentral Items and a BusinessCentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Items and a BusinessCentral Items:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Items Property
     - BusinessCentral Items Property
     - BusinessCentral Data Type
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


BusinessCentral Customers company to BusinessCentral Companies
--------------------------------------------------------------
Every BusinessCentral Customers company will be synchronized with a BusinessCentral Companies.

Once a link between a BusinessCentral Customers company and a BusinessCentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers company and a BusinessCentral Companies:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers company Property
     - BusinessCentral Companies Property
     - BusinessCentral Data Type


BusinessCentral Contacts person to BusinessCentral Customers person
-------------------------------------------------------------------
Every BusinessCentral Contacts person will be synchronized with a BusinessCentral Customers person.

Once a link between a BusinessCentral Contacts person and a BusinessCentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Contacts person and a BusinessCentral Customers person:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contacts person Property
     - BusinessCentral Customers person Property
     - BusinessCentral Data Type
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


BusinessCentral Customers person to BusinessCentral Contacts person
-------------------------------------------------------------------
Every BusinessCentral Customers person will be synchronized with a BusinessCentral Contacts person.

Once a link between a BusinessCentral Customers person and a BusinessCentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers person and a BusinessCentral Contacts person:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers person Property
     - BusinessCentral Contacts person Property
     - BusinessCentral Data Type
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

