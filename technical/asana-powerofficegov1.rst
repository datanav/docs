=================================
Asana to PowerOfficeGov1 Dataflow
=================================

Generated: 2023-08-14 09:09:56

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to PowerOfficeGov1. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to PowerOfficeGov1 Contact
--------------------------------------
Every Asana Teams will be synchronized with a PowerOfficeGov1 Contact.

Once a link between a Asana Teams and a PowerOfficeGov1 Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a PowerOfficeGov1 Contact:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - PowerOfficeGov1 Contact Property
     - PowerOfficeGov1 Data Type
   * - name
     - Name
     - "string"
   * - permalink_url
     - Domains
     - "list"
   * - permalink_url
     - Urls.Value
     - "string"


Asana Workspaces to PowerOfficeGov1 Contact
-------------------------------------------
Every Asana Workspaces will be synchronized with a PowerOfficeGov1 Contact.

Once a link between a Asana Workspaces and a PowerOfficeGov1 Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a PowerOfficeGov1 Contact:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - PowerOfficeGov1 Contact Property
     - PowerOfficeGov1 Data Type
   * - email_domains
     - Domains
     - "list"
   * - email_domains
     - Urls.Value
     - "string"
   * - name
     - Name
     - "string"

