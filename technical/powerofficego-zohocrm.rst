==========================
Powerofficego to  Dataflow
==========================

Generated: 2024-03-26 13:42:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers to  Account
-----------------------------------
Every Powerofficego Customers will be synchronized with a  Account.

Once a link between a Powerofficego Customers and a  Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Account:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Account Property
     -  Data Type
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


Powerofficego Departments to  Account
-------------------------------------
Every Powerofficego Departments will be synchronized with a  Account.

Once a link between a Powerofficego Departments and a  Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a  Account:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     -  Account Property
     -  Data Type
   * - Name
     - Account_Name
     - "string"


Powerofficego Customers person to  Contact
------------------------------------------
Every Powerofficego Customers person will be synchronized with a  Contact.

Once a link between a Powerofficego Customers person and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Contact Property
     -  Data Type
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

