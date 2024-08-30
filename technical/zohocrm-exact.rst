====================
ZohoCRM to  Dataflow
====================

Generated: 2024-08-30 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to  Accounts
----------------------------
Every ZohoCRM Account will be synchronized with a  Accounts.

Once a link between a ZohoCRM Account and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a  Accounts:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     -  Accounts Property
     -  Data Type
   * - Account_Name
     - Name
     - "string"
   * - Billing_City
     - City
     - "string"
   * - Billing_Code
     - Postcode
     - "string"
   * - Billing_Country
     - Country
     - "string"
   * - Phone
     - Phone
     - "string"
   * - Shipping_City
     - City
     - "string"
   * - Shipping_Code
     - Postcode
     - "string"
   * - Shipping_Country
     - Country
     - "string"
   * - Website
     - Website
     - "string"


ZohoCRM Contact to  Contacts
----------------------------
Every ZohoCRM Contact will be synchronized with a  Contacts.

Once a link between a ZohoCRM Contact and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a  Contacts:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     -  Contacts Property
     -  Data Type
   * - Email
     - Email
     - "string"
   * - First_Name
     - FirstName
     - "string"
   * - Full_Name
     - FullName
     - "string"
   * - Last_Name
     - LastName
     - "string"
   * - Mailing_City
     - City
     - "string"
   * - Mailing_Country
     - Country
     - "string"
   * - Mobile
     - Mobile
     - "string"
   * - Other_City
     - City
     - "string"
   * - Other_Country
     - Country
     - "string"
   * - Other_Phone
     - Phone
     - "string"
   * - Phone
     - Phone
     - "string"
   * - Secondary_Email
     - Email
     - "string"


ZohoCRM Deal to  Quotations
---------------------------
Every ZohoCRM Deal will be synchronized with a  Quotations.

Once a link between a ZohoCRM Deal and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a  Quotations:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     -  Quotations Property
     -  Data Type


ZohoCRM Contact to  Addresses
-----------------------------
Every ZohoCRM Contact will be synchronized with a  Addresses.

Once a link between a ZohoCRM Contact and a  Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a  Addresses:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     -  Addresses Property
     -  Data Type
   * - Mailing_City
     - City
     - "string"
   * - Mailing_Country
     - Country
     - "string"
   * - Mailing_Country
     - CountryName
     - "string"
   * - Other_City
     - City
     - "string"
   * - Other_Country
     - Country
     - "string"
   * - Other_Country
     - CountryName
     - "string"

