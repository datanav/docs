==================================
ZohoCRM to PowerOffice GO Dataflow
==================================

Generated: 2024-09-11 07:53:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Contact to PowerOffice Customers person
-----------------------------------------------
Every ZohoCRM Contact will be synchronized with a PowerOffice Customers person.

Once a link between a ZohoCRM Contact and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type
   * - Email
     - EmailAddress
     - "string"
   * - First_Name
     - FirstName
     - "string"
   * - Last_Name
     - LastName
     - "string"
   * - Mailing_City
     - MailAddress.City
     - "string"
   * - Mailing_Country
     - MailAddress.CountryCode
     - "string"
   * - Mailing_Zip
     - MailAddress.ZipCode
     - "string"
   * - Other_City
     - MailAddress.City
     - "string"
   * - Other_Country
     - MailAddress.CountryCode
     - "string"
   * - Other_Phone
     - PhoneNumber
     - "string"
   * - Other_Zip
     - MailAddress.ZipCode
     - "string"
   * - Phone
     - PhoneNumber
     - "string"
   * - Secondary_Email
     - EmailAddress
     - "string"
   * - id
     - Id
     - "integer"

