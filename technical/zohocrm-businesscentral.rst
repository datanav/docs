===================================
ZohoCRM to BusinessCentral Dataflow
===================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to BusinessCentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to BusinessCentral Companies
--------------------------------------------
Every ZohoCRM Account will be synchronized with a BusinessCentral Companies.

Once a link between a ZohoCRM Account and a BusinessCentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a BusinessCentral Companies:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - BusinessCentral Companies Property
     - BusinessCentral Data Type


ZohoCRM Contact to BusinessCentral Customers person
---------------------------------------------------
Every ZohoCRM Contact will be synchronized with a BusinessCentral Customers person.

Once a link between a ZohoCRM Contact and a BusinessCentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a BusinessCentral Customers person:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - BusinessCentral Customers person Property
     - BusinessCentral Data Type
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

