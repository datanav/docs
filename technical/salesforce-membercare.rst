=======================
Salesforce to  Dataflow
=======================

Generated: 2024-09-02 12:11:09

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

