===============================
Tripletex to Crmoffice Dataflow
===============================

Generated: 2024-09-07 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Crmoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer person to Crmoffice Contacts
-----------------------------------------------
Every Tripletex Customer person will be synchronized with a Crmoffice Contacts.

Once a link between a Tripletex Customer person and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
   * - phoneNumber
     - directPhone
     - "string"
   * - phoneNumberMobile
     - mobilePhone
     - "string"


Tripletex Employee to Crmoffice Contacts
----------------------------------------
Every Tripletex Employee will be synchronized with a Crmoffice Contacts.

Once a link between a Tripletex Employee and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
   * - firstName
     - givenName
     - "string"
   * - lastName
     - familyName
     - "string"
   * - phoneNumberMobile
     - mobilePhone
     - "string"
   * - phoneNumberWork
     - directPhone
     - "string"


Tripletex Product to Crmoffice Companies
----------------------------------------
Every Tripletex Product will be synchronized with a Crmoffice Companies.

Once a link between a Tripletex Product and a Crmoffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Crmoffice Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Crmoffice Companies Property
     - Crmoffice Data Type


Tripletex Project to Crmoffice Activities
-----------------------------------------
Every Tripletex Project will be synchronized with a Crmoffice Activities.

Once a link between a Tripletex Project and a Crmoffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a Crmoffice Activities:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     - Crmoffice Activities Property
     - Crmoffice Data Type
   * - name
     - subject
     - "string"
   * - projectManager.id
     - ownerId
     - "string"
   * - startDate
     - startsAt
     - "string"


Tripletex Activity to Crmoffice Activities
------------------------------------------
Every Tripletex Activity will be synchronized with a Crmoffice Activities.

Once a link between a Tripletex Activity and a Crmoffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Activity and a Crmoffice Activities:

.. list-table::
   :header-rows: 1

   * - Tripletex Activity Property
     - Crmoffice Activities Property
     - Crmoffice Data Type
   * - name
     - subject
     - "string"


Tripletex Contact to Crmoffice Contacts
---------------------------------------
Every Tripletex Contact will be synchronized with a Crmoffice Contacts.

Once a link between a Tripletex Contact and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
   * - firstName
     - givenName
     - "string"
   * - lastName
     - familyName
     - "string"
   * - phoneNumberMobile
     - mobilePhone
     - "string"
   * - phoneNumberWork
     - directPhone
     - "string"

