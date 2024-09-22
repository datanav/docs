===============================
CRMOffice to Tripletex Dataflow
===============================

Generated: 2024-09-22 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CRMOffice to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CRMOffice Activities to Tripletex Activity
------------------------------------------
Every CRMOffice Activities will be synchronized with a Tripletex Activity.

Once a link between a CRMOffice Activities and a Tripletex Activity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Activities and a Tripletex Activity:

.. list-table::
   :header-rows: 1

   * - CRMOffice Activities Property
     - Tripletex Activity Property
     - Tripletex Data Type
   * - subject
     - name
     - "string"


CRMOffice Activities to Tripletex Projectactivity
-------------------------------------------------
Every CRMOffice Activities will be synchronized with a Tripletex Projectactivity.

Once a link between a CRMOffice Activities and a Tripletex Projectactivity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Activities and a Tripletex Projectactivity:

.. list-table::
   :header-rows: 1

   * - CRMOffice Activities Property
     - Tripletex Projectactivity Property
     - Tripletex Data Type
   * - subject
     - activity.name
     - "string"


CRMOffice Contacts to Tripletex Contact
---------------------------------------
Every CRMOffice Contacts will be synchronized with a Tripletex Contact.

Once a link between a CRMOffice Contacts and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Contacts and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - CRMOffice Contacts Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - directPhone
     - phoneNumberWork
     - "string"
   * - familyName
     - lastName
     - "string"
   * - givenName
     - firstName
     - "string"
   * - mobilePhone
     - phoneNumberMobile
     - N/A

