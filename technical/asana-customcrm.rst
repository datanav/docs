============================
Asana to Custom CRM Dataflow
============================

Generated: 2024-09-11 11:39:32

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Custom CRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to CustomCRM Customer
---------------------------------
Every Asana Teams will be synchronized with a CustomCRM Customer.

Once a link between a Asana Teams and a CustomCRM Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a CustomCRM Customer:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - CustomCRM Customer Property
     - CustomCRM Data Type
   * - description
     - Description
     - "string"
   * - name
     - Name
     - "string"
   * - permalink_url
     - Website
     - "string"


Asana Workspaces to CustomCRM Customer
--------------------------------------
Every Asana Workspaces will be synchronized with a CustomCRM Customer.

Once a link between a Asana Workspaces and a CustomCRM Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a CustomCRM Customer:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - CustomCRM Customer Property
     - CustomCRM Data Type
   * - email_domains
     - Website
     - "string"
   * - name
     - Name
     - "string"

