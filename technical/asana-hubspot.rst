=========================
Asana to Hubspot Dataflow
=========================

Generated: 2024-06-26 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to Hubspot Company
------------------------------
Every Asana Teams will be synchronized with a Hubspot Company.

Once a link between a Asana Teams and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - description
     - properties.description
     - "string"
   * - html_description
     - properties.description
     - "string"
   * - name
     - properties.name
     - "string"
   * - permalink_url
     - properties.website
     - "string"


Asana Workspaces to Hubspot Company
-----------------------------------
Every Asana Workspaces will be synchronized with a Hubspot Company.

Once a link between a Asana Workspaces and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - email_domains
     - properties.website
     - "string"
   * - name
     - properties.name
     - "string"

