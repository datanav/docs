=============================
Chargebee to ZohoCRM Dataflow
=============================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Business_entity to ZohoCRM Account
--------------------------------------------
Every Chargebee Business_entity will be synchronized with a ZohoCRM Account.

Once a link between a Chargebee Business_entity and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - name
     - Account_Name
     - "string"


Chargebee Customer to ZohoCRM Contact
-------------------------------------
Every Chargebee Customer will be synchronized with a ZohoCRM Contact.

Once a link between a Chargebee Customer and a ZohoCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a ZohoCRM Contact:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - ZohoCRM Contact Property
     - ZohoCRM Data Type
   * - email
     - Email
     - "string"
   * - email
     - Secondary_Email
     - "string"
   * - first_name
     - First_Name
     - "string"
   * - last_name
     - Last_Name
     - "string"

