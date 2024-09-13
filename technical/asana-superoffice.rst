=============================
Asana to SuperOffice Dataflow
=============================

Generated: 2024-09-13 00:00:27

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to SuperOffice Contact
----------------------------------
Every Asana Teams will be synchronized with a SuperOffice Contact.

Once a link between a Asana Teams and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - name
     - Name
     - "string"
   * - permalink_url
     - Domains
     - N/A
   * - permalink_url
     - Urls.Value
     - "string"


Asana Workspaces to SuperOffice Contact
---------------------------------------
Every Asana Workspaces will be synchronized with a SuperOffice Contact.

Once a link between a Asana Workspaces and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - email_domains
     - Domains
     - N/A
   * - email_domains
     - Urls.Value
     - "string"
   * - name
     - Name
     - "string"

