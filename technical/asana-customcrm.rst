============================
Asana to Custom CRM Dataflow
============================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Custom CRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to Custom CRM Customer
----------------------------------
Every Asana Teams will be synchronized with a Custom CRM Customer.

Once a link between a Asana Teams and a Custom CRM Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a Custom CRM Customer:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - Custom CRM Customer Property
     - Custom CRM Data Type
   * - description
     - Description
     - "string"
   * - name
     - Name
     - "string"
   * - permalink_url
     - Website
     - "string"


Asana Workspaces to Custom CRM Customer
---------------------------------------
Every Asana Workspaces will be synchronized with a Custom CRM Customer.

Once a link between a Asana Workspaces and a Custom CRM Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a Custom CRM Customer:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - Custom CRM Customer Property
     - Custom CRM Data Type
   * - email_domains
     - Website
     - "string"
   * - name
     - Name
     - "string"

