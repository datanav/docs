============================
ZohoCRM to Invoiced Dataflow
============================

Generated: 2024-09-17 07:28:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Contact to Invoiced Customers company
---------------------------------------------
Every ZohoCRM Contact will be synchronized with a Invoiced Customers company.

Once a link between a ZohoCRM Contact and a Invoiced Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Invoiced Customers company:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Invoiced Customers company Property
     - Invoiced Data Type


ZohoCRM Contact to Invoiced Customers person
--------------------------------------------
Every ZohoCRM Contact will be synchronized with a Invoiced Customers person.

Once a link between a ZohoCRM Contact and a Invoiced Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Invoiced Customers person:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Invoiced Customers person Property
     - Invoiced Data Type


ZohoCRM Deal to Invoiced Invoices
---------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Invoiced Invoices.

Once a link between a ZohoCRM Deal and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - Invoiced Invoices Property
     - Invoiced Data Type
   * - Account_Name.id
     - customer
     - "string"
   * - Contact_Name.id
     - customer
     - "string"

