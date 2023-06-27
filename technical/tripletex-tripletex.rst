===============================
Tripletex to Tripletex Dataflow
===============================

Generated: 2023-06-27 11:29:18

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Tripletex Customer
-----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a SuperOffice Contact if it is connected to a SuperOffice Sale, User, Quote, Person, Quoteline, or Quotealternative that is synchronized into Tripletex.

Once a link between a SuperOffice Contact and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Tripletex Customer Property
     - Tripletex Data Type


SuperOffice Person to Tripletex Contact
---------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a SuperOffice Person if it is connected to a SuperOffice Sale, Quote, Project, Quoteline, or Quotealternative that is synchronized into Tripletex.

Once a link between a SuperOffice Person and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Tripletex Contact Property
     - Tripletex Data Type


Tripletex Customer to Tripletex Department
------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Tripletex Department must be established.

A new Tripletex Department will be created from a Tripletex Customer if it is connected to a Tripletex Contact, Employee, or Department that is synchronized into Tripletex.

Once a link between a Tripletex Customer and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - name
     - name
     - "string"


Tripletex Department to Tripletex Customer
------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a Tripletex Department if it is connected to a Tripletex Contact, or Employee that is synchronized into Tripletex.

Once a link between a Tripletex Department and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - name
     - name
     - "string"

