=======================
Salesforce to  Dataflow
=======================

Generated: 2024-09-02 13:56:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to  Countries
--------------------------------
Every Salesforce Contact will be synchronized with a  Countries.

Once a link between a Salesforce Contact and a  Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a  Countries:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     -  Countries Property
     -  Data Type
   * - MailingCountry
     - name
     - "string"


Salesforce Organization to  Companies
-------------------------------------
Every Salesforce Organization will be synchronized with a  Companies.

Once a link between a Salesforce Organization and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a  Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     -  Companies Property
     -  Data Type
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

