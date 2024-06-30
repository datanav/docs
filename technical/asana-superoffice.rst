=============================
Asana to Superoffice Dataflow
=============================

Generated: 2024-06-30 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to Superoffice Contact
----------------------------------
Every Asana Teams will be synchronized with a Superoffice Contact.

Once a link between a Asana Teams and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - name
     - Name
     - "string"
   * - permalink_url
     - Domains
     - N/A
   * - permalink_url
     - Urls.Value
     - "string"


Asana Workspaces to Superoffice Contact
---------------------------------------
Every Asana Workspaces will be synchronized with a Superoffice Contact.

Once a link between a Asana Workspaces and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - email_domains
     - Domains
     - N/A
   * - email_domains
     - Urls.Value
     - "string"
   * - name
     - Name
     - "string"

