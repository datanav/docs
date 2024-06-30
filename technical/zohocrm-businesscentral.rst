===================================
ZohoCRM to Businesscentral Dataflow
===================================

Generated: 2024-06-30 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Businesscentral Companies
--------------------------------------------
Every ZohoCRM Account will be synchronized with a Businesscentral Companies.

Once a link between a ZohoCRM Account and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


ZohoCRM Contact to Businesscentral Customers person
---------------------------------------------------
Every ZohoCRM Contact will be synchronized with a Businesscentral Customers person.

Once a link between a ZohoCRM Contact and a Businesscentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Businesscentral Customers person:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Businesscentral Customers person Property
     - Businesscentral Data Type
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

