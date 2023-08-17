=========================
HubSpot to Asana Dataflow
=========================

Generated: 2023-08-17 08:57:39

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to Asana Teams
------------------------------
Every HubSpot Company will be synchronized with a Asana Teams.

Once a link between a HubSpot Company and a Asana Teams is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Asana Teams:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Asana Teams Property
     - Asana Data Type
   * - properties.description
     - description
     - "string"
   * - properties.description
     - html_description
     - "string"
   * - properties.name
     - member_invite_management_access_level
     - "string"
   * - properties.name
     - name
     - "string"
   * - properties.website
     - permalink_url
     - "string"


HubSpot Ticket to Asana Projects
--------------------------------
Every HubSpot Ticket will be synchronized with a Asana Projects.

Once a link between a HubSpot Ticket and a Asana Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticket and a Asana Projects:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticket Property
     - Asana Projects Property
     - Asana Data Type
   * - properties.createdate
     - created_at
     - "string"
   * - properties.hubspot_owner_id
     - owner.gid
     - "string"
   * - properties.subject
     - name
     - "string"


HubSpot Account to Asana Teams
------------------------------
Every HubSpot Account will be synchronized with a Asana Teams.

Once a link between a HubSpot Account and a Asana Teams is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Account and a Asana Teams:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - Asana Teams Property
     - Asana Data Type

