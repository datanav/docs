====================
ZohoCRM to  Dataflow
====================

Generated: 2024-05-11 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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
   * - Mailing_City
     - addresses.city
     - "string"
   * - Mailing_Country
     - addresses.country
     - "string"
   * - Mailing_State
     - addresses.province_code
     - "string"
   * - Mailing_Zip
     - addresses.zip
     - "string"
   * - Other_City
     - addresses.city
     - "string"
   * - Other_Country
     - addresses.country
     - "string"
   * - Other_Phone
     - phone
     - "string"
   * - Other_State
     - addresses.province_code
     - "string"
   * - Other_Zip
     - addresses.zip
     - "string"
   * - Phone
     - phone
     - "string"
   * - Secondary_Email
     - email
     - "string"

