=================================
Salesforce to Membercare Dataflow
=================================

Generated: 2024-09-03 14:17:35

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to Membercare Countries
------------------------------------------
Every Salesforce Contact will be synchronized with a Membercare Countries.

Once a link between a Salesforce Contact and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Membercare Countries Property
     - Membercare Data Type
   * - MailingCountry
     - name
     - "string"


Salesforce Organization to Membercare Companies
-----------------------------------------------
Every Salesforce Organization will be synchronized with a Membercare Companies.

Once a link between a Salesforce Organization and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Membercare Companies Property
     - Membercare Data Type
   * - City
     - addresses.postalCode.city
     - "string"
   * - Country
     - addresses.country.id
     - "string"
   * - Name	
     - companyName
     - "string"
   * - Name	
     - name
     - "string"
   * - PostalCode	
     - addresses.postalCode.zipCode
     - "string"
   * - Street	
     - addresses.street
     - "string"


Salesforce Organization to Membercare Organizations
---------------------------------------------------
Every Salesforce Organization will be synchronized with a Membercare Organizations.

Once a link between a Salesforce Organization and a Membercare Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Membercare Organizations:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Membercare Organizations Property
     - Membercare Data Type

