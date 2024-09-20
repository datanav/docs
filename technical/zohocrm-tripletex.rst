=============================
ZohoCRM to Tripletex Dataflow
=============================

Generated: 2024-09-20 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Contact to Tripletex Customer
-------------------------------------
Every ZohoCRM Contact will be synchronized with a Tripletex Customer.

Once a link between a ZohoCRM Contact and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Tripletex Customer Property
     - Tripletex Data Type


ZohoCRM Contact to Tripletex Customer (human data)
--------------------------------------------------
Every ZohoCRM Contact will be synchronized with a Tripletex Customer (human data).

Once a link between a ZohoCRM Contact and a Tripletex Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Tripletex Customer (human data):

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Tripletex Customer (human data) Property
     - Tripletex Data Type


ZohoCRM Deal to Tripletex Order
-------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Tripletex Order.

Once a link between a ZohoCRM Deal and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - Account_Name.id
     - contact.id
     - "integer"
   * - Account_Name.id
     - customer.id
     - "integer"
   * - Closing_Date
     - orderDate
     - N/A
   * - Contact_Name.id
     - contact.id
     - "integer"
   * - Contact_Name.id
     - customer.id
     - "integer"

