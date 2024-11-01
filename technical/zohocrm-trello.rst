==========================
ZohoCRM to Trello Dataflow
==========================

Generated: 2024-11-01 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Trello Organizations
---------------------------------------
Every ZohoCRM Account will be synchronized with a Trello Organizations.

Once a link between a ZohoCRM Account and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Trello Organizations Property
     - Trello Data Type
   * - Account_Name
     - name
     - "string"
   * - Created_Time
     - desc
     - "string"
   * - Website
     - website
     - "string"


ZohoCRM Contact to Trello Members
---------------------------------
Every ZohoCRM Contact will be synchronized with a Trello Members.

Once a link between a ZohoCRM Contact and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Trello Members:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Trello Members Property
     - Trello Data Type
   * - Email
     - email
     - "string"
   * - Full_Name
     - fullName
     - "string"
   * - Secondary_Email
     - email
     - "string"

