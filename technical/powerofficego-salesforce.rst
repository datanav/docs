====================================
Powerofficego to Salesforce Dataflow
====================================

Generated: 2024-08-23 09:01:46

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers to Salesforce Organization
--------------------------------------------------
Every Powerofficego Customers will be synchronized with a Salesforce Organization.

Once a link between a Powerofficego Customers and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Salesforce Organization Property
     - Salesforce Data Type


Powerofficego Departments to Salesforce Organization
----------------------------------------------------
Every Powerofficego Departments will be synchronized with a Salesforce Organization.

Once a link between a Powerofficego Departments and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Salesforce Organization Property
     - Salesforce Data Type


Powerofficego Contactperson to Salesforce Contact
-------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Salesforce Contact.

Once a link between a Powerofficego Contactperson and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - city
     - MailingCity
     - "string"
   * - dateOfBirth
     - Birthdate
     - "string"
   * - emailAddress
     - Email
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - id
     - Id
     - "string"
   * - lastName
     - LastName
     - "string"
   * - phoneNumber
     - HomePhone
     - "string"
   * - phoneNumber
     - Phone
     - "string"
   * - zipCode
     - MailingPostalCode
     - "string"


Powerofficego Product to Salesforce Product2
--------------------------------------------
Every Powerofficego Product will be synchronized with a Salesforce Product2.

Once a link between a Powerofficego Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - description
     - Description	
     - "string"
   * - name
     - Name	
     - "string"


Powerofficego Suppliers person to Salesforce Contact
----------------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a Salesforce Contact.

Once a link between a Powerofficego Suppliers person and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - DateOfBirth
     - Birthdate
     - "string"
   * - EmailAddress
     - Email
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - Id
     - Id
     - "string"
   * - LastName
     - LastName
     - "string"
   * - MailAddress.City
     - MailingCity
     - "string"
   * - MailAddress.CountryCode
     - MailingCountryCode
     - "string"
   * - MailAddress.ZipCode
     - MailingPostalCode
     - "string"
   * - PhoneNumber
     - HomePhone
     - "string"
   * - PhoneNumber
     - Phone
     - "string"

