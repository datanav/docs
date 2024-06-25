===========================
ZohoCRM to Tilores Dataflow
===========================

Generated: 2024-06-25 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Contact to Tilores Human
--------------------------------
Every ZohoCRM Contact will be synchronized with a Tilores Human.

Once a link between a ZohoCRM Contact and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Tilores Human Property
     - Tilores Data Type
   * - Email
     - email
     - "string"
   * - First_Name
     - firstName
     - "string"
   * - Last_Name
     - lastName
     - "string"
   * - Mailing_City
     - city
     - "string"
   * - Mailing_Street
     - street
     - "string"
   * - Mailing_Zip
     - postalCode
     - "string"
   * - Other_City
     - city
     - "string"
   * - Other_Street
     - street
     - "string"
   * - Other_Zip
     - postalCode
     - "string"
   * - Secondary_Email
     - email
     - "string"
   * - id
     - id
     - "string"

