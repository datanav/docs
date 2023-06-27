=============================
Tripletex to HubSpot Dataflow
=============================

Generated: 2023-06-27 05:11:35

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to HubSpot Contact
------------------------------------
Every Tripletex Contact will be synchronized with a HubSpot Contact.

If a matching HubSpot Contact already exists, the Tripletex Contact will be merged with the existing one.
If no matching HubSpot Contact is found, a new HubSpot Contact will be created.

A Tripletex Contact will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - HubSpot Contact Property
   * - email
     - properties.email

Once a link between a Tripletex Contact and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - HubSpot Contact Property
     - HubSpot Data Type


Tripletex Employee to HubSpot Contact
-------------------------------------
Every Tripletex Employee will be synchronized with a HubSpot Contact.

If a matching HubSpot Contact already exists, the Tripletex Employee will be merged with the existing one.
If no matching HubSpot Contact is found, a new HubSpot Contact will be created.

A Tripletex Employee will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - HubSpot Contact Property
   * - email
     - properties.email

Once a link between a Tripletex Employee and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - HubSpot Contact Property
     - HubSpot Data Type


Tripletex Customer to HubSpot Company
-------------------------------------
Every Tripletex Customer will be synchronized with a HubSpot Company.

Once a link between a Tripletex Customer and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - HubSpot Company Property
     - HubSpot Data Type


Tripletex Customercategory to HubSpot Contactcompanyassociationtype
-------------------------------------------------------------------
Every Tripletex Customercategory will be synchronized with a HubSpot Contactcompanyassociationtype.

Once a link between a Tripletex Customercategory and a HubSpot Contactcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customercategory and a HubSpot Contactcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - Tripletex Customercategory Property
     - HubSpot Contactcompanyassociationtype Property
     - HubSpot Data Type


Tripletex Department to HubSpot Company
---------------------------------------
Every Tripletex Department will be synchronized with a HubSpot Company.

Once a link between a Tripletex Department and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - HubSpot Company Property
     - HubSpot Data Type


Tripletex Order to HubSpot Deal
-------------------------------
Every Tripletex Order will be synchronized with a HubSpot Deal.

Once a link between a Tripletex Order and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - HubSpot Deal Property
     - HubSpot Data Type


Tripletex Orderline to HubSpot Deal
-----------------------------------
Every Tripletex Orderline will be synchronized with a HubSpot Deal.

Once a link between a Tripletex Orderline and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - HubSpot Deal Property
     - HubSpot Data Type


Tripletex Productgroup to HubSpot Contactcompanyassociationtype
---------------------------------------------------------------
Every Tripletex Productgroup will be synchronized with a HubSpot Contactcompanyassociationtype.

Once a link between a Tripletex Productgroup and a HubSpot Contactcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgroup and a HubSpot Contactcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgroup Property
     - HubSpot Contactcompanyassociationtype Property
     - HubSpot Data Type


Tripletex Productgrouprelation to HubSpot Product
-------------------------------------------------
Every Tripletex Productgrouprelation will be synchronized with a HubSpot Product.

Once a link between a Tripletex Productgrouprelation and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgrouprelation and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgrouprelation Property
     - HubSpot Product Property
     - HubSpot Data Type


Tripletex Productunit to HubSpot Contactcompanyassociationtype
--------------------------------------------------------------
Every Tripletex Productunit will be synchronized with a HubSpot Contactcompanyassociationtype.

Once a link between a Tripletex Productunit and a HubSpot Contactcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productunit and a HubSpot Contactcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - Tripletex Productunit Property
     - HubSpot Contactcompanyassociationtype Property
     - HubSpot Data Type


Tripletex Project to HubSpot Ticket
-----------------------------------
Every Tripletex Project will be synchronized with a HubSpot Ticket.

Once a link between a Tripletex Project and a HubSpot Ticket is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a HubSpot Ticket:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     - HubSpot Ticket Property
     - HubSpot Data Type


Tripletex Projectcategory to HubSpot Contactcompanyassociationtype
------------------------------------------------------------------
Every Tripletex Projectcategory will be synchronized with a HubSpot Contactcompanyassociationtype.

Once a link between a Tripletex Projectcategory and a HubSpot Contactcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Projectcategory and a HubSpot Contactcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - Tripletex Projectcategory Property
     - HubSpot Contactcompanyassociationtype Property
     - HubSpot Data Type


Tripletex Supplier to HubSpot Company
-------------------------------------
Every Tripletex Supplier will be synchronized with a HubSpot Company.

Once a link between a Tripletex Supplier and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - HubSpot Company Property
     - HubSpot Data Type


Tripletex Employee to HubSpot User
----------------------------------
Every Tripletex Employee will be synchronized with a HubSpot User.

Once a link between a Tripletex Employee and a HubSpot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a HubSpot User:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - HubSpot User Property
     - HubSpot Data Type


Tripletex Orderline to HubSpot Lineitemdealassociation
------------------------------------------------------
Every Tripletex Orderline will be synchronized with a HubSpot Lineitemdealassociation.

Once a link between a Tripletex Orderline and a HubSpot Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a HubSpot Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - HubSpot Lineitemdealassociation Property
     - HubSpot Data Type


Tripletex Product to HubSpot Product
------------------------------------
Every Tripletex Product will be synchronized with a HubSpot Product.

Once a link between a Tripletex Product and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - HubSpot Product Property
     - HubSpot Data Type

