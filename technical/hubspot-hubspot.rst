===========================
HubSpot to HubSpot Dataflow
===========================

Generated: 2023-05-22 22:07:09

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to HubSpot Contactcompanyassociation
----------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a HubSpot Contactcompanyassociation must be established.

A HubSpot Contact will merge with a HubSpot Contactcompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - HubSpot Contactcompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Contact and a HubSpot Contactcompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a HubSpot Contactcompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - HubSpot Contactcompanyassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "integer"


HubSpot Contactcompanyassociation to HubSpot Contact
----------------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a HubSpot Contact.

If a matching HubSpot Contact already exists, the HubSpot Contactcompanyassociation will be merged with the existing one.
If no matching HubSpot Contact is found, a new HubSpot Contact will be created.

A HubSpot Contactcompanyassociation will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - HubSpot Contact Property
   * - id
     - id

Once a link between a HubSpot Contactcompanyassociation and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - HubSpot Contact Property
     - HubSpot Data Type


HubSpot Deal to HubSpot Dealcompanyassociation
----------------------------------------------
Before any synchronization can take place, a link between a HubSpot Deal and a HubSpot Dealcompanyassociation must be established.

A HubSpot Deal will merge with a HubSpot Dealcompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - HubSpot Dealcompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Deal and a HubSpot Dealcompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a HubSpot Dealcompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - HubSpot Dealcompanyassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"
   * - properties.hubspot_owner_id
     - toObjectId (Dependant on having wd:Q16869121 in sesam_simpleAssociationTypes)
     - "string"


HubSpot Deal to HubSpot Dealcontactassociation
----------------------------------------------
Before any synchronization can take place, a link between a HubSpot Deal and a HubSpot Dealcontactassociation must be established.

A HubSpot Deal will merge with a HubSpot Dealcontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - HubSpot Dealcontactassociation Property
   * - id
     - id

Once a link between a HubSpot Deal and a HubSpot Dealcontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a HubSpot Dealcontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - HubSpot Dealcontactassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"
   * - properties.hubspot_owner_id
     - toObjectId (Dependant on having wd:Q16869121 in sesam_simpleAssociationTypes)
     - "string"


HubSpot Deal to HubSpot Lineitemdealassociation
-----------------------------------------------
Before any synchronization can take place, a link between a HubSpot Deal and a HubSpot Lineitemdealassociation must be established.

A HubSpot Deal will merge with a HubSpot Lineitemdealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - HubSpot Lineitemdealassociation Property
   * - id
     - id

Once a link between a HubSpot Deal and a HubSpot Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a HubSpot Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - HubSpot Lineitemdealassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"
   * - properties.hubspot_owner_id
     - toObjectId (Dependant on having wd:Q16869121 in sesam_simpleAssociationTypes)
     - "string"


HubSpot Dealcompanyassociation to HubSpot Deal
----------------------------------------------
Before any synchronization can take place, a link between a HubSpot Dealcompanyassociation and a HubSpot Deal must be established.

A HubSpot Dealcompanyassociation will merge with a HubSpot Deal if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - HubSpot Deal Property
   * - id
     - id

Once a link between a HubSpot Dealcompanyassociation and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - HubSpot Deal Property
     - HubSpot Data Type
   * - toObjectId (Dependant on having wd:Q16869121 in sesam_simpleAssociationTypes)
     - properties.hubspot_owner_id
     - "string"


HubSpot Dealcompanyassociation to HubSpot Dealcontactassociation
----------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Dealcompanyassociation and a HubSpot Dealcontactassociation must be established.

A HubSpot Dealcompanyassociation will merge with a HubSpot Dealcontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - HubSpot Dealcontactassociation Property
   * - id
     - id

Once a link between a HubSpot Dealcompanyassociation and a HubSpot Dealcontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a HubSpot Dealcontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - HubSpot Dealcontactassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Dealcompanyassociation to HubSpot Lineitemdealassociation
-----------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Dealcompanyassociation and a HubSpot Lineitemdealassociation must be established.

A HubSpot Dealcompanyassociation will merge with a HubSpot Lineitemdealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - HubSpot Lineitemdealassociation Property
   * - id
     - id

Once a link between a HubSpot Dealcompanyassociation and a HubSpot Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a HubSpot Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - HubSpot Lineitemdealassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Dealcontactassociation to HubSpot Deal
----------------------------------------------
Before any synchronization can take place, a link between a HubSpot Dealcontactassociation and a HubSpot Deal must be established.

A HubSpot Dealcontactassociation will merge with a HubSpot Deal if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - HubSpot Deal Property
   * - id
     - id

Once a link between a HubSpot Dealcontactassociation and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - HubSpot Deal Property
     - HubSpot Data Type
   * - toObjectId (Dependant on having wd:Q16869121 in sesam_simpleAssociationTypes)
     - properties.hubspot_owner_id
     - "string"


HubSpot Dealcontactassociation to HubSpot Dealcompanyassociation
----------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Dealcontactassociation and a HubSpot Dealcompanyassociation must be established.

A HubSpot Dealcontactassociation will merge with a HubSpot Dealcompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - HubSpot Dealcompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Dealcontactassociation and a HubSpot Dealcompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a HubSpot Dealcompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - HubSpot Dealcompanyassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Dealcontactassociation to HubSpot Lineitemdealassociation
-----------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Dealcontactassociation and a HubSpot Lineitemdealassociation must be established.

A HubSpot Dealcontactassociation will merge with a HubSpot Lineitemdealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - HubSpot Lineitemdealassociation Property
   * - id
     - id

Once a link between a HubSpot Dealcontactassociation and a HubSpot Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a HubSpot Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - HubSpot Lineitemdealassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Lineitem to HubSpot Lineitemdealassociation
---------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitem and a HubSpot Lineitemdealassociation must be established.

A HubSpot Lineitem will merge with a HubSpot Lineitemdealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - HubSpot Lineitemdealassociation Property
   * - id
     - id

Once a link between a HubSpot Lineitem and a HubSpot Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a HubSpot Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - HubSpot Lineitemdealassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"


HubSpot Lineitemdealassociation to HubSpot Deal
-----------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitemdealassociation and a HubSpot Deal must be established.

A HubSpot Lineitemdealassociation will merge with a HubSpot Deal if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - HubSpot Deal Property
   * - id
     - id

Once a link between a HubSpot Lineitemdealassociation and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - HubSpot Deal Property
     - HubSpot Data Type
   * - toObjectId (Dependant on having wd:Q16869121 in sesam_simpleAssociationTypes)
     - properties.hubspot_owner_id
     - "string"


HubSpot Lineitemdealassociation to HubSpot Dealcompanyassociation
-----------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitemdealassociation and a HubSpot Dealcompanyassociation must be established.

A HubSpot Lineitemdealassociation will merge with a HubSpot Dealcompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - HubSpot Dealcompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Lineitemdealassociation and a HubSpot Dealcompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a HubSpot Dealcompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - HubSpot Dealcompanyassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Lineitemdealassociation to HubSpot Dealcontactassociation
-----------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitemdealassociation and a HubSpot Dealcontactassociation must be established.

A HubSpot Lineitemdealassociation will merge with a HubSpot Dealcontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - HubSpot Dealcontactassociation Property
   * - id
     - id

Once a link between a HubSpot Lineitemdealassociation and a HubSpot Dealcontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a HubSpot Dealcontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - HubSpot Dealcontactassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Lineitemdealassociation to HubSpot Lineitem
---------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitemdealassociation and a HubSpot Lineitem must be established.

A HubSpot Lineitemdealassociation will merge with a HubSpot Lineitem if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - HubSpot Lineitem Property
   * - id
     - id

Once a link between a HubSpot Lineitemdealassociation and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - HubSpot Lineitem Property
     - HubSpot Data Type


HubSpot Owner to HubSpot User
-----------------------------
Before any synchronization can take place, a link between a HubSpot Owner and a HubSpot User must be established.

A HubSpot Owner will merge with a HubSpot User if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Owner Property
     - HubSpot User Property
   * - userId
     - Id
   * - email
     - email

Once a link between a HubSpot Owner and a HubSpot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Owner and a HubSpot User:

.. list-table::
   :header-rows: 1

   * - HubSpot Owner Property
     - HubSpot User Property
     - HubSpot Data Type
   * - email
     - email
     - "string"


HubSpot Quote to HubSpot Company
--------------------------------
Before any synchronization can take place, a link between a HubSpot Quote and a HubSpot Company must be established.

A HubSpot Quote will merge with a HubSpot Company if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - HubSpot Company Property
   * - associations.companies.results.id
     - id

Once a link between a HubSpot Quote and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - HubSpot Company Property
     - HubSpot Data Type


HubSpot Quote to HubSpot Contact
--------------------------------
Before any synchronization can take place, a link between a HubSpot Quote and a HubSpot Contact must be established.

A HubSpot Quote will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - HubSpot Contact Property
   * - associations.contacts.results.id
     - id

Once a link between a HubSpot Quote and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - HubSpot Contact Property
     - HubSpot Data Type


HubSpot Quote to HubSpot Contactcompanyassociation
--------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quote and a HubSpot Contactcompanyassociation must be established.

A HubSpot Quote will merge with a HubSpot Contactcompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - HubSpot Contactcompanyassociation Property
   * - associations.contacts.results.id
     - id

Once a link between a HubSpot Quote and a HubSpot Contactcompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a HubSpot Contactcompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - HubSpot Contactcompanyassociation Property
     - HubSpot Data Type
   * - associations.contacts.results.id
     - id
     - "integer"


HubSpot User to HubSpot Contact
-------------------------------
Every HubSpot User will be synchronized with a HubSpot Contact.

Once a link between a HubSpot User and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - email
     - properties.work_email
     - "string"


HubSpot Dealcompanyassociationtype to HubSpot Dealcontactassociationtype
------------------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a HubSpot Dealcontactassociationtype.

Once a link between a HubSpot Dealcompanyassociationtype and a HubSpot Dealcontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a HubSpot Dealcontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - HubSpot Dealcontactassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Dealcontactassociationtype to HubSpot Dealcompanyassociationtype
------------------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a HubSpot Dealcompanyassociationtype.

Once a link between a HubSpot Dealcontactassociationtype and a HubSpot Dealcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a HubSpot Dealcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - HubSpot Dealcompanyassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"

