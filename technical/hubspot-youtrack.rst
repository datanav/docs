============================
HubSpot to YouTrack Dataflow
============================

Generated: 2023-11-27 14:21:22

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to YouTrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to YouTrack Users
---------------------------------
Every HubSpot Contact will be synchronized with a YouTrack Users.

If a matching YouTrack Users already exists, the HubSpot Contact will be merged with the existing one.
If no matching YouTrack Users is found, a new YouTrack Users will be created.

A HubSpot Contact will merge with a YouTrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - YouTrack Users Property
   * - properties.email
     - 
   * - properties.email
     - profile.email
   * - properties.email
     - profile.email.email

Once a link between a HubSpot Contact and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - YouTrack Users Property
     - YouTrack Data Type
   * - properties.email
     - profile.email
     - "string"
   * - properties.email
     - profile.email.email
     - "string"
   * - properties.work_email
     - profile.email.email
     - "string"


HubSpot Company to YouTrack Groups
----------------------------------
Every HubSpot Company will be synchronized with a YouTrack Groups.

Once a link between a HubSpot Company and a YouTrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a YouTrack Groups:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - YouTrack Groups Property
     - YouTrack Data Type
   * - properties.name
     - name
     - "string"


HubSpot Company to YouTrack Usergroups
--------------------------------------
Every HubSpot Company will be synchronized with a YouTrack Usergroups.

Once a link between a HubSpot Company and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - YouTrack Usergroups Property
     - YouTrack Data Type
   * - properties.name
     - name
     - "string"


HubSpot Company to YouTrack Workitems
-------------------------------------
Every HubSpot Company will be synchronized with a YouTrack Workitems.

Once a link between a HubSpot Company and a YouTrack Workitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a YouTrack Workitems:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - YouTrack Workitems Property
     - YouTrack Data Type
   * - properties.description
     - date
     - "string"
   * - properties.name
     - updated
     - "string"


HubSpot Contact to YouTrack Usersyoutrack
-----------------------------------------
Every HubSpot Contact will be synchronized with a YouTrack Usersyoutrack.

Once a link between a HubSpot Contact and a YouTrack Usersyoutrack is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a YouTrack Usersyoutrack:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - YouTrack Usersyoutrack Property
     - YouTrack Data Type


HubSpot Contactcompanyassociation to YouTrack Users
---------------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a YouTrack Users.

Once a link between a HubSpot Contactcompanyassociation and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - YouTrack Users Property
     - YouTrack Data Type


HubSpot Contactcompanyassociation to YouTrack Usersyoutrack
-----------------------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a YouTrack Usersyoutrack.

Once a link between a HubSpot Contactcompanyassociation and a YouTrack Usersyoutrack is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a YouTrack Usersyoutrack:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - YouTrack Usersyoutrack Property
     - YouTrack Data Type


HubSpot Contactcompanyassociationtype to YouTrack Organizationroles
-------------------------------------------------------------------
Every HubSpot Contactcompanyassociationtype will be synchronized with a YouTrack Organizationroles.

Once a link between a HubSpot Contactcompanyassociationtype and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociationtype and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociationtype Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


HubSpot Dealcompanyassociationtype to YouTrack Organizationroles
----------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a YouTrack Organizationroles.

Once a link between a HubSpot Dealcompanyassociationtype and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


HubSpot Dealcontactassociationtype to YouTrack Organizationroles
----------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a YouTrack Organizationroles.

Once a link between a HubSpot Dealcontactassociationtype and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


HubSpot Lineitemdealassociationtype to YouTrack Organizationroles
-----------------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a YouTrack Organizationroles.

Once a link between a HubSpot Lineitemdealassociationtype and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


HubSpot Lineitemquoteassociationtype to YouTrack Organizationroles
------------------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a YouTrack Organizationroles.

Once a link between a HubSpot Lineitemquoteassociationtype and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


HubSpot Quotecompanyassociationtype to YouTrack Organizationroles
-----------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a YouTrack Organizationroles.

Once a link between a HubSpot Quotecompanyassociationtype and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


HubSpot Quotecontactassociationtype to YouTrack Organizationroles
-----------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a YouTrack Organizationroles.

Once a link between a HubSpot Quotecontactassociationtype and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


HubSpot Quotedealassociationtype to YouTrack Organizationroles
--------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a YouTrack Organizationroles.

Once a link between a HubSpot Quotedealassociationtype and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


HubSpot Quotequotetemplateassociationtype to YouTrack Organizationroles
-----------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a YouTrack Organizationroles.

Once a link between a HubSpot Quotequotetemplateassociationtype and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


HubSpot Ticket to YouTrack Hubprojects
--------------------------------------
Every HubSpot Ticket will be synchronized with a YouTrack Hubprojects.

Once a link between a HubSpot Ticket and a YouTrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticket and a YouTrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticket Property
     - YouTrack Hubprojects Property
     - YouTrack Data Type


HubSpot Ticket to YouTrack Organizationroles
--------------------------------------------
Every HubSpot Ticket will be synchronized with a YouTrack Organizationroles.

Once a link between a HubSpot Ticket and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticket and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticket Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


HubSpot Ticket to YouTrack Usergroups
-------------------------------------
Every HubSpot Ticket will be synchronized with a YouTrack Usergroups.

Once a link between a HubSpot Ticket and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticket and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticket Property
     - YouTrack Usergroups Property
     - YouTrack Data Type
   * - properties.subject
     - users.id
     - "string"


HubSpot Ticketcompanyassociationtype to YouTrack Organizationroles
------------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a YouTrack Organizationroles.

Once a link between a HubSpot Ticketcompanyassociationtype and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


HubSpot User to YouTrack Usersyoutrack
--------------------------------------
Every HubSpot User will be synchronized with a YouTrack Usersyoutrack.

Once a link between a HubSpot User and a YouTrack Usersyoutrack is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a YouTrack Usersyoutrack:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - YouTrack Usersyoutrack Property
     - YouTrack Data Type


HubSpot Ticket to YouTrack Issues
---------------------------------
Every HubSpot Ticket will be synchronized with a YouTrack Issues.

Once a link between a HubSpot Ticket and a YouTrack Issues is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticket and a YouTrack Issues:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticket Property
     - YouTrack Issues Property
     - YouTrack Data Type


HubSpot User to YouTrack Users
------------------------------
Every HubSpot User will be synchronized with a YouTrack Users.

Once a link between a HubSpot User and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - YouTrack Users Property
     - YouTrack Data Type
   * - email
     - profile.email.email
     - "string"

