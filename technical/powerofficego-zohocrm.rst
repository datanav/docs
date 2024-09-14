==================================
PowerOffice GO to ZohoCRM Dataflow
==================================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Customers to ZohoCRM Account
-------------------------------------------
Every PowerOffice GO Customers will be synchronized with a ZohoCRM Account.

Once a link between a PowerOffice GO Customers and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - MailAddress.City
     - Billing_City
     - "string"
   * - MailAddress.City
     - Shipping_City
     - "string"
   * - MailAddress.CountryCode
     - Billing_Country
     - "string"
   * - MailAddress.CountryCode
     - Shipping_Country
     - "string"
   * - MailAddress.ZipCode
     - Billing_Code
     - "string"
   * - MailAddress.ZipCode
     - Shipping_Code
     - "string"
   * - Name
     - Account_Name
     - "string"
   * - PhoneNumber
     - Phone
     - "string"
   * - WebsiteUrl
     - Website
     - "string"


PowerOffice GO Departments to ZohoCRM Account
---------------------------------------------
Every PowerOffice GO Departments will be synchronized with a ZohoCRM Account.

Once a link between a PowerOffice GO Departments and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Departments and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - Name
     - Account_Name
     - "string"


PowerOffice GO Customers person to ZohoCRM Contact
--------------------------------------------------
Every PowerOffice GO Customers person will be synchronized with a ZohoCRM Contact.

Once a link between a PowerOffice GO Customers person and a ZohoCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a ZohoCRM Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - ZohoCRM Contact Property
     - ZohoCRM Data Type
   * - EmailAddress
     - Email
     - "string"
   * - EmailAddress
     - Secondary_Email
     - "string"
   * - FirstName
     - First_Name
     - "string"
   * - LastName
     - Last_Name
     - "string"
   * - MailAddress.City
     - Mailing_City
     - "string"
   * - MailAddress.City
     - Other_City
     - "string"
   * - MailAddress.CountryCode
     - Mailing_Country
     - "string"
   * - MailAddress.CountryCode
     - Other_Country
     - "string"
   * - MailAddress.ZipCode
     - Mailing_Zip
     - "string"
   * - MailAddress.ZipCode
     - Other_Zip
     - "string"
   * - PhoneNumber
     - Other_Phone
     - "string"
   * - PhoneNumber
     - Phone
     - "string"

