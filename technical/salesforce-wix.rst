==========================
Salesforce to Wix Dataflow
==========================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to Wix Contacts
----------------------------------
Every Salesforce Contact will be synchronized with a Wix Contacts.

Once a link between a Salesforce Contact and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Wix Contacts Property
     - Wix Data Type
   * - Email
     - primaryInfo.email
     - "string"
   * - FirstName
     - info.name.first
     - "string"
   * - HomePhone
     - primaryInfo.phone
     - "string"
   * - LastName
     - info.name.last
     - "string"
   * - Phone
     - primaryInfo.phone
     - "string"


Salesforce Product2 to Wix Products
-----------------------------------
Every Salesforce Product2 will be synchronized with a Wix Products.

Once a link between a Salesforce Product2 and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Wix Products:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Wix Products Property
     - Wix Data Type
   * - Name
     - name
     - "string"
   * - Name	
     - name
     - "string"

