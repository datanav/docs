===========================
Asana to Customcrm Dataflow
===========================

Generated: 2024-09-10 15:02:06

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Customcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to Customcrm Customer
---------------------------------
Every Asana Teams will be synchronized with a Customcrm Customer.

Once a link between a Asana Teams and a Customcrm Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a Customcrm Customer:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - Customcrm Customer Property
     - Customcrm Data Type
   * - description
     - Description
     - "string"
   * - name
     - Name
     - "string"
   * - permalink_url
     - Website
     - "string"


Asana Workspaces to Customcrm Customer
--------------------------------------
Every Asana Workspaces will be synchronized with a Customcrm Customer.

Once a link between a Asana Workspaces and a Customcrm Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a Customcrm Customer:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - Customcrm Customer Property
     - Customcrm Data Type
   * - email_domains
     - Website
     - "string"
   * - name
     - Name
     - "string"

