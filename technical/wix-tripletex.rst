=============================
Wix.com to Tripletex Dataflow
=============================

Generated: 2023-09-05 09:11:34

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Tripletex Contact
-------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a Tripletex Contact must be established.

A Wix.com Contacts will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Tripletex Contact Property
   * - info.emails
     - email

Once a link between a Wix.com Contacts and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - info.emails
     - email
     - "string"
   * - info.name.first
     - firstName
     - "string"
   * - info.phones
     - phoneNumberMobile
     - "if","matches","+*","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]


Wix.com Contacts to Tripletex Employee
--------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a Tripletex Employee must be established.

A Wix.com Contacts will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Tripletex Employee Property
   * - info.emails
     - email

Once a link between a Wix.com Contacts and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - info.emails
     - email
     - "string"
   * - info.name.first
     - firstName
     - "string"
   * - info.phones
     - phoneNumberMobile
     - "string"


Wix.com Members to Tripletex Contact
------------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a Tripletex Contact must be established.

A Wix.com Members will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Tripletex Contact Property
   * - loginEmail
     - email

Once a link between a Wix.com Members and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - loginEmail
     - email
     - "string"


Wix.com Members to Tripletex Employee
-------------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a Tripletex Employee must be established.

A Wix.com Members will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Tripletex Employee Property
   * - loginEmail
     - email

Once a link between a Wix.com Members and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - loginEmail
     - email
     - "string"

