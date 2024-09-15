============================
ZohoCRM to Invoiced Dataflow
============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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

