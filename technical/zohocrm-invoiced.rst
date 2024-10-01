============================
ZohoCRM to Invoiced Dataflow
============================

Generated: 2024-10-01 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Contact to Invoiced Customers (organisation data)
---------------------------------------------------------
Every ZohoCRM Contact will be synchronized with a Invoiced Customers (organisation data).

Once a link between a ZohoCRM Contact and a Invoiced Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Invoiced Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Invoiced Customers (organisation data) Property
     - Invoiced Data Type


ZohoCRM Contact to Invoiced Customers (human data)
--------------------------------------------------
Every ZohoCRM Contact will be synchronized with a Invoiced Customers (human data).

Once a link between a ZohoCRM Contact and a Invoiced Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Invoiced Customers (human data):

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Invoiced Customers (human data) Property
     - Invoiced Data Type
   * - Full_Name
     - name
     - "string"
   * - Mailing_City
     - city
     - "string"
   * - Mailing_Country
     - country
     - "string"
   * - Mailing_Zip
     - postal_code
     - "string"
   * - Other_City
     - city
     - "string"
   * - Other_Country
     - country
     - "string"
   * - Other_Zip
     - postal_code
     - "string"
   * - id
     - id
     - "string"


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

