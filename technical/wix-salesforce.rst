==============================
Wix.com to Salesforce Dataflow
==============================

Generated: 2024-08-25 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Salesforce Contact
--------------------------------------
Every Wix.com Contacts will be synchronized with a Salesforce Contact.

Once a link between a Wix.com Contacts and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - info.name.first
     - FirstName
     - "string"
   * - info.name.last
     - LastName
     - "string"
   * - primaryInfo.email
     - Email
     - "string"
   * - primaryInfo.phone
     - HomePhone
     - "string"
   * - primaryInfo.phone
     - Phone
     - "string"


Wix.com Products to Salesforce Product2
---------------------------------------
Every Wix.com Products will be synchronized with a Salesforce Product2.

Once a link between a Wix.com Products and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - name
     - Name	
     - "string"

