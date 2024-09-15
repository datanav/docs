===============================
Tripletex to CRMOffice Dataflow
===============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer person to CRMOffice Contacts
-----------------------------------------------
Every Tripletex Customer person will be synchronized with a CRMOffice Contacts.

Once a link between a Tripletex Customer person and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - phoneNumber
     - directPhone
     - "string"
   * - phoneNumberMobile
     - mobilePhone
     - "string"


Tripletex Employee to CRMOffice Contacts
----------------------------------------
Every Tripletex Employee will be synchronized with a CRMOffice Contacts.

Once a link between a Tripletex Employee and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
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


Tripletex Product to CRMOffice Companies
----------------------------------------
Every Tripletex Product will be synchronized with a CRMOffice Companies.

Once a link between a Tripletex Product and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - CRMOffice Companies Property
     - CRMOffice Data Type


Tripletex Project to CRMOffice Activities
-----------------------------------------
Every Tripletex Project will be synchronized with a CRMOffice Activities.

Once a link between a Tripletex Project and a CRMOffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a CRMOffice Activities:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     - CRMOffice Activities Property
     - CRMOffice Data Type
   * - name
     - subject
     - "string"
   * - projectManager.id
     - ownerId
     - "string"
   * - startDate
     - startsAt
     - "string"


Tripletex Projectactivity to CRMOffice Activities
-------------------------------------------------
Every Tripletex Projectactivity will be synchronized with a CRMOffice Activities.

Once a link between a Tripletex Projectactivity and a CRMOffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Projectactivity and a CRMOffice Activities:

.. list-table::
   :header-rows: 1

   * - Tripletex Projectactivity Property
     - CRMOffice Activities Property
     - CRMOffice Data Type


Tripletex Activity to CRMOffice Activities
------------------------------------------
Every Tripletex Activity will be synchronized with a CRMOffice Activities.

Once a link between a Tripletex Activity and a CRMOffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Activity and a CRMOffice Activities:

.. list-table::
   :header-rows: 1

   * - Tripletex Activity Property
     - CRMOffice Activities Property
     - CRMOffice Data Type
   * - name
     - subject
     - "string"


Tripletex Contact to CRMOffice Contacts
---------------------------------------
Every Tripletex Contact will be synchronized with a CRMOffice Contacts.

Once a link between a Tripletex Contact and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
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

