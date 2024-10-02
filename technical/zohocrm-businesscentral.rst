====================================
ZohoCRM to Business Central Dataflow
====================================

Generated: 2024-10-02 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Business Central Companies
---------------------------------------------
Every ZohoCRM Account will be synchronized with a Business Central Companies.

Once a link between a ZohoCRM Account and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Business Central Companies Property
     - Business Central Data Type


ZohoCRM Contact to Business Central Customers (organisation data)
-----------------------------------------------------------------
Every ZohoCRM Contact will be synchronized with a Business Central Customers (organisation data).

Once a link between a ZohoCRM Contact and a Business Central Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Business Central Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Business Central Customers (organisation data) Property
     - Business Central Data Type


ZohoCRM Contact to Business Central Customers (human data)
----------------------------------------------------------
Every ZohoCRM Contact will be synchronized with a Business Central Customers (human data).

Once a link between a ZohoCRM Contact and a Business Central Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Business Central Customers (human data):

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Business Central Customers (human data) Property
     - Business Central Data Type
   * - Email
     - email
     - "string"
   * - Full_Name
     - displayName
     - "string"
   * - Mailing_City
     - city
     - "string"
   * - Mailing_Country
     - country
     - "string"
   * - Mailing_Zip
     - postalCode
     - "string"
   * - Other_City
     - city
     - "string"
   * - Other_Country
     - country
     - "string"
   * - Other_Phone
     - phoneNumber
     - "string"
   * - Other_Zip
     - postalCode
     - "string"
   * - Phone
     - phoneNumber
     - "string"
   * - Secondary_Email
     - email
     - "string"
   * - id
     - id
     - "string"


ZohoCRM Deal to Business Central Salesorders
--------------------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Business Central Salesorders.

Once a link between a ZohoCRM Deal and a Business Central Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a Business Central Salesorders:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - Business Central Salesorders Property
     - Business Central Data Type
   * - Account_Name.id
     - customerId
     - "string"
   * - Closing_Date
     - orderDate
     - N/A
   * - Contact_Name.id
     - customerId
     - "string"

