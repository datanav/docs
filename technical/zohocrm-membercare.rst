==============================
ZohoCRM to MemberCare Dataflow
==============================

Generated: 2024-09-23 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to MemberCare Companies
---------------------------------------
Every ZohoCRM Account will be synchronized with a MemberCare Companies.

Once a link between a ZohoCRM Account and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - Account_Name
     - companyName
     - "string"
   * - Website
     - url
     - "string"


ZohoCRM Contact to MemberCare Persons
-------------------------------------
Every ZohoCRM Contact will be synchronized with a MemberCare Persons.

Once a link between a ZohoCRM Contact and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - First_Name
     - firstname
     - "string"
   * - Full_Name
     - name
     - "string"
   * - Last_Name
     - lastname
     - "string"
   * - Mailing_City
     - addresses.postalCode.city
     - "string"
   * - Mailing_Country
     - addresses.country.id
     - "string"
   * - Mailing_Zip
     - addresses.postalCode.zipCode
     - "string"
   * - Other_City
     - addresses.postalCode.city
     - "string"
   * - Other_Country
     - addresses.country.id
     - "string"
   * - Other_Zip
     - addresses.postalCode.zipCode
     - "string"
   * - id
     - addresses.id
     - "string"


ZohoCRM Deal to MemberCare Invoices
-----------------------------------
Every ZohoCRM Deal will be synchronized with a MemberCare Invoices.

Once a link between a ZohoCRM Deal and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - MemberCare Invoices Property
     - MemberCare Data Type


ZohoCRM Account to MemberCare Countries
---------------------------------------
Every ZohoCRM Account will be synchronized with a MemberCare Countries.

Once a link between a ZohoCRM Account and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - MemberCare Countries Property
     - MemberCare Data Type


ZohoCRM Contact to MemberCare Countries
---------------------------------------
Every ZohoCRM Contact will be synchronized with a MemberCare Countries.

Once a link between a ZohoCRM Contact and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - Mailing_Country
     - name
     - "string"
   * - Other_Country
     - name
     - "string"

