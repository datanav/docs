===============================
SuperOffice to HubSpot Dataflow
===============================

Generated: 2023-06-27 05:11:35

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to HubSpot Contact
-------------------------------------
Every SuperOffice Person will be synchronized with a HubSpot Contact.

If a matching HubSpot Contact already exists, the SuperOffice Person will be merged with the existing one.
If no matching HubSpot Contact is found, a new HubSpot Contact will be created.

A SuperOffice Person will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - HubSpot Contact Property
   * - Emails.Value
     - properties.email

Once a link between a SuperOffice Person and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - HubSpot Contact Property
     - HubSpot Data Type


SuperOffice Contact to HubSpot Company
--------------------------------------
Every SuperOffice Contact will be synchronized with a HubSpot Company.

Once a link between a SuperOffice Contact and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - HubSpot Company Property
     - HubSpot Data Type


SuperOffice Sale classification status to HubSpot Pipelinedeal
--------------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Sale classification status and a HubSpot Pipelinedeal must be established.

A new HubSpot Pipelinedeal will be created from a SuperOffice Sale classification status if it is connected to a SuperOffice Sale, Quote, Quoteline, or Quotealternative that is synchronized into HubSpot.

Once a link between a SuperOffice Sale classification status and a HubSpot Pipelinedeal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale classification status and a HubSpot Pipelinedeal:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale classification status Property
     - HubSpot Pipelinedeal Property
     - HubSpot Data Type


SuperOffice Listbusinessitems to HubSpot Contactcompanyassociationtype
----------------------------------------------------------------------
Every SuperOffice Listbusinessitems will be synchronized with a HubSpot Contactcompanyassociationtype.

Once a link between a SuperOffice Listbusinessitems and a HubSpot Contactcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listbusinessitems and a HubSpot Contactcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listbusinessitems Property
     - HubSpot Contactcompanyassociationtype Property
     - HubSpot Data Type


SuperOffice Listcategoryitems to HubSpot Contactcompanyassociationtype
----------------------------------------------------------------------
Every SuperOffice Listcategoryitems will be synchronized with a HubSpot Contactcompanyassociationtype.

Once a link between a SuperOffice Listcategoryitems and a HubSpot Contactcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcategoryitems and a HubSpot Contactcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcategoryitems Property
     - HubSpot Contactcompanyassociationtype Property
     - HubSpot Data Type


SuperOffice Listproductcategoryitems to HubSpot Contactcompanyassociationtype
-----------------------------------------------------------------------------
Every SuperOffice Listproductcategoryitems will be synchronized with a HubSpot Contactcompanyassociationtype.

Once a link between a SuperOffice Listproductcategoryitems and a HubSpot Contactcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproductcategoryitems and a HubSpot Contactcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproductcategoryitems Property
     - HubSpot Contactcompanyassociationtype Property
     - HubSpot Data Type


SuperOffice Listproductfamilyitems to HubSpot Contactcompanyassociationtype
---------------------------------------------------------------------------
Every SuperOffice Listproductfamilyitems will be synchronized with a HubSpot Contactcompanyassociationtype.

Once a link between a SuperOffice Listproductfamilyitems and a HubSpot Contactcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproductfamilyitems and a HubSpot Contactcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproductfamilyitems Property
     - HubSpot Contactcompanyassociationtype Property
     - HubSpot Data Type


SuperOffice Listproducttypeitems to HubSpot Contactcompanyassociationtype
-------------------------------------------------------------------------
Every SuperOffice Listproducttypeitems will be synchronized with a HubSpot Contactcompanyassociationtype.

Once a link between a SuperOffice Listproducttypeitems and a HubSpot Contactcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproducttypeitems and a HubSpot Contactcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproducttypeitems Property
     - HubSpot Contactcompanyassociationtype Property
     - HubSpot Data Type


SuperOffice Listprojectstatusitems to HubSpot Contactcompanyassociationtype
---------------------------------------------------------------------------
Every SuperOffice Listprojectstatusitems will be synchronized with a HubSpot Contactcompanyassociationtype.

Once a link between a SuperOffice Listprojectstatusitems and a HubSpot Contactcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listprojectstatusitems and a HubSpot Contactcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listprojectstatusitems Property
     - HubSpot Contactcompanyassociationtype Property
     - HubSpot Data Type


SuperOffice Listprojecttypeitems to HubSpot Contactcompanyassociationtype
-------------------------------------------------------------------------
Every SuperOffice Listprojecttypeitems will be synchronized with a HubSpot Contactcompanyassociationtype.

Once a link between a SuperOffice Listprojecttypeitems and a HubSpot Contactcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listprojecttypeitems and a HubSpot Contactcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listprojecttypeitems Property
     - HubSpot Contactcompanyassociationtype Property
     - HubSpot Data Type


SuperOffice Listsaletypeitems to HubSpot Contactcompanyassociationtype
----------------------------------------------------------------------
Every SuperOffice Listsaletypeitems will be synchronized with a HubSpot Contactcompanyassociationtype.

Once a link between a SuperOffice Listsaletypeitems and a HubSpot Contactcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listsaletypeitems and a HubSpot Contactcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listsaletypeitems Property
     - HubSpot Contactcompanyassociationtype Property
     - HubSpot Data Type


SuperOffice Listticketcategoryitems to HubSpot Contactcompanyassociationtype
----------------------------------------------------------------------------
Every SuperOffice Listticketcategoryitems will be synchronized with a HubSpot Contactcompanyassociationtype.

Once a link between a SuperOffice Listticketcategoryitems and a HubSpot Contactcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listticketcategoryitems and a HubSpot Contactcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listticketcategoryitems Property
     - HubSpot Contactcompanyassociationtype Property
     - HubSpot Data Type


SuperOffice Quote to HubSpot Deal
---------------------------------
Every SuperOffice Quote will be synchronized with a HubSpot Deal.

Once a link between a SuperOffice Quote and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quote and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quote Property
     - HubSpot Deal Property
     - HubSpot Data Type


SuperOffice Quotealternative to HubSpot Deal
--------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a HubSpot Deal.

Once a link between a SuperOffice Quotealternative and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - HubSpot Deal Property
     - HubSpot Data Type


SuperOffice Quoteline to HubSpot Deal
-------------------------------------
Every SuperOffice Quoteline will be synchronized with a HubSpot Deal.

Once a link between a SuperOffice Quoteline and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - HubSpot Deal Property
     - HubSpot Data Type


SuperOffice Product to HubSpot Product
--------------------------------------
Every SuperOffice Product will be synchronized with a HubSpot Product.

Once a link between a SuperOffice Product and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - HubSpot Product Property
     - HubSpot Data Type


SuperOffice Quotealternative to HubSpot Quote
---------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a HubSpot Quote.

Once a link between a SuperOffice Quotealternative and a HubSpot Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a HubSpot Quote:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - HubSpot Quote Property
     - HubSpot Data Type


SuperOffice Quoteline to HubSpot Lineitemdealassociation
--------------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a HubSpot Lineitemdealassociation.

Once a link between a SuperOffice Quoteline and a HubSpot Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a HubSpot Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - HubSpot Lineitemdealassociation Property
     - HubSpot Data Type


SuperOffice Sale to HubSpot Deal
--------------------------------
Every SuperOffice Sale will be synchronized with a HubSpot Deal.

Once a link between a SuperOffice Sale and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - HubSpot Deal Property
     - HubSpot Data Type


SuperOffice Ticket to HubSpot Ticket
------------------------------------
Every SuperOffice Ticket will be synchronized with a HubSpot Ticket.

Once a link between a SuperOffice Ticket and a HubSpot Ticket is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ticket and a HubSpot Ticket:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ticket Property
     - HubSpot Ticket Property
     - HubSpot Data Type


SuperOffice User to HubSpot User
--------------------------------
Every SuperOffice User will be synchronized with a HubSpot User.

Once a link between a SuperOffice User and a HubSpot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a HubSpot User:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - HubSpot User Property
     - HubSpot Data Type

