=============================
ZohoCRM to Chargebee Dataflow
=============================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Chargebee Customer
-------------------------------------
Before any synchronization can take place, a link between a ZohoCRM Account and a Chargebee Customer must be established.

A new Chargebee Customer will be created from a ZohoCRM Account if it is connected to a ZohoCRM Deal that is synchronized into Chargebee.

Once a link between a ZohoCRM Account and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - Billing_Country
     - billing_address.country
     - "string"
   * - Industry
     - billing_address.country
     - "string"
   * - Shipping_Country
     - billing_address.country
     - "string"


ZohoCRM Account to Chargebee Business_entity
--------------------------------------------
Every ZohoCRM Account will be synchronized with a Chargebee Business_entity.

Once a link between a ZohoCRM Account and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - Account_Name
     - name
     - "string"


ZohoCRM Deal to Chargebee Order
-------------------------------
Every ZohoCRM Deal will be synchronized with a Chargebee Order.

Once a link between a ZohoCRM Deal and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - Account_Name.id
     - customer_id
     - "string"
   * - Contact_Name.id
     - customer_id
     - "string"


ZohoCRM Contact to Chargebee Customer
-------------------------------------
Every ZohoCRM Contact will be synchronized with a Chargebee Customer.

Once a link between a ZohoCRM Contact and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Chargebee Customer Property
     - Chargebee Data Type
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

