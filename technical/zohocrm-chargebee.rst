====================
ZohoCRM to  Dataflow
====================

Generated: 2024-08-28 12:40:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to  Business_entity
-----------------------------------
Every ZohoCRM Account will be synchronized with a  Business_entity.

Once a link between a ZohoCRM Account and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     -  Business_entity Property
     -  Data Type
   * - Account_Name
     - name
     - "string"


ZohoCRM Deal to  Order
----------------------
Every ZohoCRM Deal will be synchronized with a  Order.

Once a link between a ZohoCRM Deal and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a  Order:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     -  Order Property
     -  Data Type
   * - Account_Name.id
     - customer_id
     - "string"
   * - Contact_Name.id
     - customer_id
     - "string"


ZohoCRM Contact to  Customer
----------------------------
Every ZohoCRM Contact will be synchronized with a  Customer.

Once a link between a ZohoCRM Contact and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a  Customer:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     -  Customer Property
     -  Data Type
   * - Email
     - email
     - "string"
   * - First_Name
     - first_name
     - "string"
   * - Last_Name
     - last_name
     - "string"
   * - Mailing_Country
     - billing_address.country
     - "string"
   * - Other_Country
     - billing_address.country
     - "string"
   * - Secondary_Email
     - email
     - "string"

