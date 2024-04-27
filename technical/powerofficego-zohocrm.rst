=================================
Powerofficego to ZohoCRM Dataflow
=================================

Generated: 2024-04-27 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers to ZohoCRM Account
------------------------------------------
Every Powerofficego Customers will be synchronized with a ZohoCRM Account.

Once a link between a Powerofficego Customers and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
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


Powerofficego Departments to ZohoCRM Account
--------------------------------------------
Every Powerofficego Departments will be synchronized with a ZohoCRM Account.

Once a link between a Powerofficego Departments and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - Name
     - Account_Name
     - "string"


Powerofficego Customers person to ZohoCRM Contact
-------------------------------------------------
Every Powerofficego Customers person will be synchronized with a ZohoCRM Contact.

Once a link between a Powerofficego Customers person and a ZohoCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a ZohoCRM Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
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

