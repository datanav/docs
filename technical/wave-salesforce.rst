=====================================
Wave Financial to Salesforce Dataflow
=====================================

Generated: 2024-08-23 08:51:10

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Salesforce Contact
-----------------------------------
Every Wave Customer will be synchronized with a Salesforce Contact.

Once a link between a Wave Customer and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - address.city
     - MailingCity
     - "string"
   * - address.country.code
     - MailingCountry
     - "string"
   * - address.postalCode
     - MailingPostalCode
     - "string"
   * - address.province.code
     - MailingState
     - "string"
   * - email
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
   * - mobile
     - MobilePhone
     - "string"
   * - shippingDetails.address.city
     - MailingCity
     - "string"
   * - shippingDetails.address.country.code
     - MailingCountry
     - "string"
   * - shippingDetails.address.postalCode
     - MailingPostalCode
     - "string"
   * - shippingDetails.address.province.code
     - MailingState
     - "string"


Wave Product to Salesforce Product2
-----------------------------------
Every Wave Product will be synchronized with a Salesforce Product2.

Once a link between a Wave Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Salesforce Product2 Property
     - Salesforce Data Type


Wave Vendor to Salesforce Contact
---------------------------------
Every Wave Vendor will be synchronized with a Salesforce Contact.

Once a link between a Wave Vendor and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - address.city
     - MailingCity
     - "string"
   * - address.postalCode
     - MailingPostalCode
     - "string"
   * - address.province.code
     - MailingState
     - "string"
   * - email
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
   * - mobile
     - MobilePhone
     - "string"
   * - phone
     - HomePhone
     - "string"
   * - phone
     - Phone
     - "string"

