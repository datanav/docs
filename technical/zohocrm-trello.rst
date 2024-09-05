==========================
ZohoCRM to Trello Dataflow
==========================

Generated: 2024-09-05 12:09:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to  Organizations
---------------------------------
Every ZohoCRM Account will be synchronized with a  Organizations.

Once a link between a ZohoCRM Account and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a  Organizations:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     -  Organizations Property
     -  Data Type
   * - Account_Name
     - name
     - "string"
   * - Created_Time
     - desc
     - "string"
   * - Website
     - website
     - "string"


ZohoCRM Contact to  Members
---------------------------
Every ZohoCRM Contact will be synchronized with a  Members.

Once a link between a ZohoCRM Contact and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a  Members:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     -  Members Property
     -  Data Type
   * - Email
     - email
     - "string"
   * - Full_Name
     - fullName
     - "string"
   * - Secondary_Email
     - email
     - "string"

