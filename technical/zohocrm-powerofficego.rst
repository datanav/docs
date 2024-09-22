==================================
ZohoCRM to PowerOffice GO Dataflow
==================================

Generated: 2024-09-22 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Contact to PowerOffice GO Customers
-------------------------------------------
Every ZohoCRM Contact will be synchronized with a PowerOffice GO Customers.

Once a link between a ZohoCRM Contact and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type


ZohoCRM Contact to PowerOffice GO Customers (human data)
--------------------------------------------------------
Every ZohoCRM Contact will be synchronized with a PowerOffice GO Customers (human data).

Once a link between a ZohoCRM Contact and a PowerOffice GO Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a PowerOffice GO Customers (human data):

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - PowerOffice GO Customers (human data) Property
     - PowerOffice GO Data Type
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


ZohoCRM Deal to PowerOffice GO Salesorders
------------------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a PowerOffice GO Salesorders.

Once a link between a ZohoCRM Deal and a PowerOffice GO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a PowerOffice GO Salesorders:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - PowerOffice GO Salesorders Property
     - PowerOffice GO Data Type
   * - Account_Name.id
     - CustomerId
     - "integer"
   * - Account_Name.id
     - CustomerReferenceContactPersonId
     - "integer"
   * - Closing_Date
     - SalesOrderDate
     - "string"
   * - Contact_Name.id
     - CustomerId
     - "integer"
   * - Contact_Name.id
     - CustomerReferenceContactPersonId
     - "integer"

