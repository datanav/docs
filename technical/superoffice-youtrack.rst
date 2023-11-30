========================
SuperOffice to  Dataflow
========================

Generated: 2023-11-30 00:00:01

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to  Users
----------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a  Users must be established.

A SuperOffice Person will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Users Property
   * - Emails.Value
     - profile.email.email

Once a link between a SuperOffice Person and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a  Users:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Users Property
     -  Data Type
   * - Emails.Value
     - profile.email
     - "string"
   * - Emails.Value
     - profile.email.email
     - "string"


SuperOffice User to  Users
--------------------------
Before any synchronization can take place, a link between a SuperOffice User and a  Users must be established.

A SuperOffice User will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     -  Users Property
   * - personEmail
     - profile.email.email

Once a link between a SuperOffice User and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a  Users:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     -  Users Property
     -  Data Type


SuperOffice Contact to  Groups
------------------------------
Every SuperOffice Contact will be synchronized with a  Groups.

Once a link between a SuperOffice Contact and a  Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Groups:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Groups Property
     -  Data Type
   * - Name
     - name
     - "string"


SuperOffice Listbusinessitems to  Organizationroles
---------------------------------------------------
Every SuperOffice Listbusinessitems will be synchronized with a  Organizationroles.

Once a link between a SuperOffice Listbusinessitems and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listbusinessitems and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listbusinessitems Property
     -  Organizationroles Property
     -  Data Type


SuperOffice Listcategoryitems to  Organizationroles
---------------------------------------------------
Every SuperOffice Listcategoryitems will be synchronized with a  Organizationroles.

Once a link between a SuperOffice Listcategoryitems and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcategoryitems and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcategoryitems Property
     -  Organizationroles Property
     -  Data Type


SuperOffice Listproductcategoryitems to  Organizationroles
----------------------------------------------------------
Every SuperOffice Listproductcategoryitems will be synchronized with a  Organizationroles.

Once a link between a SuperOffice Listproductcategoryitems and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproductcategoryitems and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproductcategoryitems Property
     -  Organizationroles Property
     -  Data Type


SuperOffice Listproductfamilyitems to  Organizationroles
--------------------------------------------------------
Every SuperOffice Listproductfamilyitems will be synchronized with a  Organizationroles.

Once a link between a SuperOffice Listproductfamilyitems and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproductfamilyitems and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproductfamilyitems Property
     -  Organizationroles Property
     -  Data Type


SuperOffice Listproducttypeitems to  Organizationroles
------------------------------------------------------
Every SuperOffice Listproducttypeitems will be synchronized with a  Organizationroles.

Once a link between a SuperOffice Listproducttypeitems and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproducttypeitems and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproducttypeitems Property
     -  Organizationroles Property
     -  Data Type


SuperOffice Listprojectstatusitems to  Organizationroles
--------------------------------------------------------
Every SuperOffice Listprojectstatusitems will be synchronized with a  Organizationroles.

Once a link between a SuperOffice Listprojectstatusitems and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listprojectstatusitems and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listprojectstatusitems Property
     -  Organizationroles Property
     -  Data Type


SuperOffice Listprojecttypeitems to  Organizationroles
------------------------------------------------------
Every SuperOffice Listprojecttypeitems will be synchronized with a  Organizationroles.

Once a link between a SuperOffice Listprojecttypeitems and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listprojecttypeitems and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listprojecttypeitems Property
     -  Organizationroles Property
     -  Data Type


SuperOffice Listsaletypeitems to  Organizationroles
---------------------------------------------------
Every SuperOffice Listsaletypeitems will be synchronized with a  Organizationroles.

Once a link between a SuperOffice Listsaletypeitems and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listsaletypeitems and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listsaletypeitems Property
     -  Organizationroles Property
     -  Data Type


SuperOffice Listticketcategoryitems to  Organizationroles
---------------------------------------------------------
Every SuperOffice Listticketcategoryitems will be synchronized with a  Organizationroles.

Once a link between a SuperOffice Listticketcategoryitems and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listticketcategoryitems and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listticketcategoryitems Property
     -  Organizationroles Property
     -  Data Type
   * - CategoryMaster
     - organization.id
     - "string"
   * - CategoryMaster
     - owner.id
     - "string"
   * - CategoryMaster
     - role.id
     - "string"


SuperOffice Ticket to  Issues
-----------------------------
Every SuperOffice Ticket will be synchronized with a  Issues.

Once a link between a SuperOffice Ticket and a  Issues is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ticket and a  Issues:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ticket Property
     -  Issues Property
     -  Data Type
   * - OwnedBy.AssociateId
     - reporter.id
     - "string"

