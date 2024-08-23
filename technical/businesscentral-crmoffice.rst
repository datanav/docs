============================
Businesscentral to  Dataflow
============================

Generated: 2024-08-23 12:33:25

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Customers person to  Contacts
---------------------------------------------
Every Businesscentral Customers person will be synchronized with a  Contacts.

Once a link between a Businesscentral Customers person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     -  Contacts Property
     -  Data Type


Businesscentral Employees to  Contacts
--------------------------------------
Every Businesscentral Employees will be synchronized with a  Contacts.

Once a link between a Businesscentral Employees and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employees and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employees Property
     -  Contacts Property
     -  Data Type
   * - givenName
     - givenName
     - "string"
   * - surname
     - familyName
     - "string"


Businesscentral Items to  Companies
-----------------------------------
Every Businesscentral Items will be synchronized with a  Companies.

Once a link between a Businesscentral Items and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Companies:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Companies Property
     -  Data Type


Businesscentral Contacts person to  Contacts
--------------------------------------------
Every Businesscentral Contacts person will be synchronized with a  Contacts.

Once a link between a Businesscentral Contacts person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     -  Contacts Property
     -  Data Type


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
   * - city
     - postAddress.postalArea
     - "string"
   * - country
     - postAddress.country
     - "string"
   * - country
     - visitAddress.country
     - "string"
   * - postalCode
     - postAddress.postCode
     - "string"

