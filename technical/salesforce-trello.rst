=============================
Salesforce to Trello Dataflow
=============================

Generated: 2024-09-14 00:00:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to Trello Members
------------------------------------
Every Salesforce Contact will be synchronized with a Trello Members.

Once a link between a Salesforce Contact and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Trello Members:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Trello Members Property
     - Trello Data Type
   * - Email
     - email
     - "string"


Salesforce Customer to Trello Members
-------------------------------------
Every Salesforce Customer will be synchronized with a Trello Members.

Once a link between a Salesforce Customer and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Trello Members:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Trello Members Property
     - Trello Data Type
   * - Name
     - fullName
     - "string"


Salesforce Division to Trello Organizations
-------------------------------------------
Every Salesforce Division will be synchronized with a Trello Organizations.

Once a link between a Salesforce Division and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - Trello Organizations Property
     - Trello Data Type
   * - Name
     - name
     - "string"


Salesforce Seller to Trello Members
-----------------------------------
Every Salesforce Seller will be synchronized with a Trello Members.

Once a link between a Salesforce Seller and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Seller and a Trello Members:

.. list-table::
   :header-rows: 1

   * - Salesforce Seller Property
     - Trello Members Property
     - Trello Data Type
   * - Name
     - fullName
     - "string"


Salesforce Task to Trello Actions
---------------------------------
Every Salesforce Task will be synchronized with a Trello Actions.

Once a link between a Salesforce Task and a Trello Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Task and a Trello Actions:

.. list-table::
   :header-rows: 1

   * - Salesforce Task Property
     - Trello Actions Property
     - Trello Data Type
   * - OwnerId
     - memberCreator.id
     - "string"


Salesforce Organization to Trello Organizations
-----------------------------------------------
Every Salesforce Organization will be synchronized with a Trello Organizations.

Once a link between a Salesforce Organization and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Trello Organizations Property
     - Trello Data Type
   * - Name
     - name
     - "string"
   * - Name	
     - name
     - "string"


Salesforce Task to Trello Cards
-------------------------------
Every Salesforce Task will be synchronized with a Trello Cards.

Once a link between a Salesforce Task and a Trello Cards is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Task and a Trello Cards:

.. list-table::
   :header-rows: 1

   * - Salesforce Task Property
     - Trello Cards Property
     - Trello Data Type
   * - ActivityDate
     - due
     - "string"
   * - CompletedDateTime
     - dueComplete
     - "string"
   * - Subject
     - name
     - "string"


Salesforce User to Trello Members
---------------------------------
Every Salesforce User will be synchronized with a Trello Members.

Once a link between a Salesforce User and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Trello Members:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Trello Members Property
     - Trello Data Type
   * - Email
     - email
     - "string"
   * - Name
     - fullName
     - "string"

