===========================
HubSpot to HubSpot Dataflow
===========================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Account to HubSpot Account
----------------------------------
Before any synchronization can take place, a link between a HubSpot Account and a HubSpot Account must be established.

A HubSpot Account will merge with a HubSpot Account if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - HubSpot Account Property
   * - portalId
     - portalId

Once a link between a HubSpot Account and a HubSpot Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Account and a HubSpot Account:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - HubSpot Account Property
     - HubSpot Data Type


HubSpot Company to HubSpot Company
----------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a HubSpot Company must be established.

A HubSpot Company will merge with a HubSpot Company if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - HubSpot Company Property
   * - id
     - id

Once a link between a HubSpot Company and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - id
     - id
     - "string"
   * - properties.address
     - properties.address
     - "string"
   * - properties.address2
     - properties.address2
     - "string"
   * - properties.city
     - properties.city
     - "string"
   * - properties.country
     - properties.country
     - "string"
   * - properties.country
     - properties.industry
     - "string"
   * - properties.country
     - properties.state
     - "string"
   * - properties.country
     - properties.type
     - "string"
   * - properties.description
     - properties.description
     - "string"
   * - properties.hs_parent_company_id
     - properties.hs_parent_company_id
     - "string"
   * - properties.industry
     - properties.country
     - "string"
   * - properties.industry
     - properties.industry
     - "string"
   * - properties.industry
     - properties.state
     - "string"
   * - properties.industry
     - properties.type
     - "string"
   * - properties.name
     - properties.name
     - "string"
   * - properties.phone
     - properties.phone
     - "string"
   * - properties.state
     - properties.country
     - "string"
   * - properties.state
     - properties.industry
     - "string"
   * - properties.state
     - properties.type
     - "string"
   * - properties.type
     - properties.country
     - "string"
   * - properties.type
     - properties.industry
     - "string"
   * - properties.type
     - properties.state
     - "string"
   * - properties.type
     - properties.type
     - "string"
   * - properties.website
     - properties.website
     - "string"
   * - properties.zip
     - properties.zip
     - "string"
   * - sesam_org_nr_se
     - sesam_org_number_se
     - "string"
   * - sesam_org_number_se
     - sesam_org_nr_se
     - "string"


HubSpot Contact to HubSpot Contact
----------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a HubSpot Contact must be established.

A HubSpot Contact will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - HubSpot Contact Property
   * - id
     - id
   * - properties.email
     - properties.email

Once a link between a HubSpot Contact and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - id
     - id
     - "string"
   * - properties.address
     - properties.address
     - "string"
   * - properties.city
     - properties.city
     - "string"
   * - properties.country
     - properties.country
     - "string"
   * - properties.country
     - properties.state
     - "string"
   * - properties.date_of_birth
     - properties.date_of_birth
     - "string"
   * - properties.email
     - properties.email
     - "string"
   * - properties.firstname
     - properties.firstname
     - "string"
   * - properties.lastname
     - properties.lastname
     - "string"
   * - properties.mobilephone
     - properties.mobilephone
     - "string"
   * - properties.phone
     - properties.phone
     - "string"
   * - properties.state
     - properties.country
     - "string"
   * - properties.work_email
     - properties.work_email
     - "string"
   * - properties.zip
     - properties.zip
     - "string"


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


HubSpot Contactcompanyassociation to HubSpot Contactcompanyassociation
----------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contactcompanyassociation and a HubSpot Contactcompanyassociation must be established.

A HubSpot Contactcompanyassociation will merge with a HubSpot Contactcompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - HubSpot Contactcompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Contactcompanyassociation and a HubSpot Contactcompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a HubSpot Contactcompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - HubSpot Contactcompanyassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "integer"
   * - sesam_simpleAssociationTypes
     - toObjectId
     - "integer"
   * - toObjectId
     - sesam_simpleAssociationTypes
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "integer"


HubSpot Deal to HubSpot Deal
----------------------------
Before any synchronization can take place, a link between a HubSpot Deal and a HubSpot Deal must be established.

A HubSpot Deal will merge with a HubSpot Deal if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - HubSpot Deal Property
   * - id
     - id

Once a link between a HubSpot Deal and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - HubSpot Deal Property
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
     - toObjectId (Dependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypes)
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
     - toObjectId (Dependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypes)
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
   * - toObjectId (Dependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypes)
     - properties.hubspot_owner_id
     - "string"


HubSpot Dealcompanyassociation to HubSpot Dealcompanyassociation
----------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Dealcompanyassociation and a HubSpot Dealcompanyassociation must be established.

A HubSpot Dealcompanyassociation will merge with a HubSpot Dealcompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - HubSpot Dealcompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Dealcompanyassociation and a HubSpot Dealcompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a HubSpot Dealcompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - HubSpot Dealcompanyassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
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
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
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
   * - toObjectId (Dependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypes)
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
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Dealcontactassociation to HubSpot Dealcontactassociation
----------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Dealcontactassociation and a HubSpot Dealcontactassociation must be established.

A HubSpot Dealcontactassociation will merge with a HubSpot Dealcontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - HubSpot Dealcontactassociation Property
   * - id
     - id

Once a link between a HubSpot Dealcontactassociation and a HubSpot Dealcontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a HubSpot Dealcontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - HubSpot Dealcontactassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Lineitem to HubSpot Lineitem
------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitem and a HubSpot Lineitem must be established.

A HubSpot Lineitem will merge with a HubSpot Lineitem if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - HubSpot Lineitem Property
   * - id
     - id

Once a link between a HubSpot Lineitem and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - HubSpot Lineitem Property
     - HubSpot Data Type


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


HubSpot Lineitem to HubSpot Lineitemquoteassociation
----------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitem and a HubSpot Lineitemquoteassociation must be established.

A HubSpot Lineitem will merge with a HubSpot Lineitemquoteassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - HubSpot Lineitemquoteassociation Property
   * - id
     - id

Once a link between a HubSpot Lineitem and a HubSpot Lineitemquoteassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a HubSpot Lineitemquoteassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - HubSpot Lineitemquoteassociation Property
     - HubSpot Data Type
   * - id
     - id
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


HubSpot Lineitemdealassociation to HubSpot Lineitemdealassociation
------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitemdealassociation and a HubSpot Lineitemdealassociation must be established.

A HubSpot Lineitemdealassociation will merge with a HubSpot Lineitemdealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - HubSpot Lineitemdealassociation Property
   * - id
     - id

Once a link between a HubSpot Lineitemdealassociation and a HubSpot Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a HubSpot Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - HubSpot Lineitemdealassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Lineitemdealassociation to HubSpot Lineitemquoteassociation
-------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitemdealassociation and a HubSpot Lineitemquoteassociation must be established.

A HubSpot Lineitemdealassociation will merge with a HubSpot Lineitemquoteassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - HubSpot Lineitemquoteassociation Property
   * - id
     - id

Once a link between a HubSpot Lineitemdealassociation and a HubSpot Lineitemquoteassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a HubSpot Lineitemquoteassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - HubSpot Lineitemquoteassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Lineitemquoteassociation to HubSpot Lineitem
----------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitemquoteassociation and a HubSpot Lineitem must be established.

A HubSpot Lineitemquoteassociation will merge with a HubSpot Lineitem if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - HubSpot Lineitem Property
   * - id
     - id

Once a link between a HubSpot Lineitemquoteassociation and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - HubSpot Lineitem Property
     - HubSpot Data Type


HubSpot Lineitemquoteassociation to HubSpot Lineitemdealassociation
-------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitemquoteassociation and a HubSpot Lineitemdealassociation must be established.

A HubSpot Lineitemquoteassociation will merge with a HubSpot Lineitemdealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - HubSpot Lineitemdealassociation Property
   * - id
     - id

Once a link between a HubSpot Lineitemquoteassociation and a HubSpot Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a HubSpot Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - HubSpot Lineitemdealassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q940607 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Lineitemquoteassociation to HubSpot Lineitemquoteassociation
--------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitemquoteassociation and a HubSpot Lineitemquoteassociation must be established.

A HubSpot Lineitemquoteassociation will merge with a HubSpot Lineitemquoteassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - HubSpot Lineitemquoteassociation Property
   * - id
     - id

Once a link between a HubSpot Lineitemquoteassociation and a HubSpot Lineitemquoteassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a HubSpot Lineitemquoteassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - HubSpot Lineitemquoteassociation Property
     - HubSpot Data Type


HubSpot Owner to HubSpot Owner
------------------------------
Before any synchronization can take place, a link between a HubSpot Owner and a HubSpot Owner must be established.

A HubSpot Owner will merge with a HubSpot Owner if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Owner Property
     - HubSpot Owner Property
   * - email
     - email
   * - userId
     - userId

Once a link between a HubSpot Owner and a HubSpot Owner is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Owner and a HubSpot Owner:

.. list-table::
   :header-rows: 1

   * - HubSpot Owner Property
     - HubSpot Owner Property
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


HubSpot Quote to HubSpot Quote
------------------------------
Before any synchronization can take place, a link between a HubSpot Quote and a HubSpot Quote must be established.

A HubSpot Quote will merge with a HubSpot Quote if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - HubSpot Quote Property
   * - id
     - id

Once a link between a HubSpot Quote and a HubSpot Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a HubSpot Quote:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - HubSpot Quote Property
     - HubSpot Data Type


HubSpot Quote to HubSpot Quotecompanyassociation
------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quote and a HubSpot Quotecompanyassociation must be established.

A HubSpot Quote will merge with a HubSpot Quotecompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - HubSpot Quotecompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Quote and a HubSpot Quotecompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a HubSpot Quotecompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - HubSpot Quotecompanyassociation Property
     - HubSpot Data Type
   * - associations.companies.results.id
     - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - "string"
   * - associations.contacts.results.id
     - toObjectId (Dependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypes)
     - "string"
   * - id
     - id
     - "string"


HubSpot Quote to HubSpot Quotecontactassociation
------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quote and a HubSpot Quotecontactassociation must be established.

A HubSpot Quote will merge with a HubSpot Quotecontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - HubSpot Quotecontactassociation Property
   * - id
     - id

Once a link between a HubSpot Quote and a HubSpot Quotecontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a HubSpot Quotecontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - HubSpot Quotecontactassociation Property
     - HubSpot Data Type
   * - associations.companies.results.id
     - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - "string"
   * - associations.contacts.results.id
     - toObjectId (Dependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypes)
     - "string"
   * - id
     - id
     - "string"


HubSpot Quote to HubSpot Quotedealassociation
---------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quote and a HubSpot Quotedealassociation must be established.

A HubSpot Quote will merge with a HubSpot Quotedealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - HubSpot Quotedealassociation Property
   * - id
     - id

Once a link between a HubSpot Quote and a HubSpot Quotedealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a HubSpot Quotedealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - HubSpot Quotedealassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"


HubSpot Quote to HubSpot Quotequotetemplateassociation
------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quote and a HubSpot Quotequotetemplateassociation must be established.

A HubSpot Quote will merge with a HubSpot Quotequotetemplateassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - HubSpot Quotequotetemplateassociation Property
   * - id
     - id

Once a link between a HubSpot Quote and a HubSpot Quotequotetemplateassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a HubSpot Quotequotetemplateassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - HubSpot Quotequotetemplateassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"


HubSpot Quotecompanyassociation to HubSpot Quote
------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecompanyassociation and a HubSpot Quote must be established.

A HubSpot Quotecompanyassociation will merge with a HubSpot Quote if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - HubSpot Quote Property
   * - id
     - id

Once a link between a HubSpot Quotecompanyassociation and a HubSpot Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a HubSpot Quote:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - HubSpot Quote Property
     - HubSpot Data Type


HubSpot Quotecompanyassociation to HubSpot Quotecompanyassociation
------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecompanyassociation and a HubSpot Quotecompanyassociation must be established.

A HubSpot Quotecompanyassociation will merge with a HubSpot Quotecompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - HubSpot Quotecompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecompanyassociation and a HubSpot Quotecompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a HubSpot Quotecompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - HubSpot Quotecompanyassociation Property
     - HubSpot Data Type


HubSpot Quotecompanyassociation to HubSpot Quotecontactassociation
------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecompanyassociation and a HubSpot Quotecontactassociation must be established.

A HubSpot Quotecompanyassociation will merge with a HubSpot Quotecontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - HubSpot Quotecontactassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecompanyassociation and a HubSpot Quotecontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a HubSpot Quotecontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - HubSpot Quotecontactassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Quotecompanyassociation to HubSpot Quotedealassociation
---------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecompanyassociation and a HubSpot Quotedealassociation must be established.

A HubSpot Quotecompanyassociation will merge with a HubSpot Quotedealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - HubSpot Quotedealassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecompanyassociation and a HubSpot Quotedealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a HubSpot Quotedealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - HubSpot Quotedealassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"


HubSpot Quotecompanyassociation to HubSpot Quotequotetemplateassociation
------------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecompanyassociation and a HubSpot Quotequotetemplateassociation must be established.

A HubSpot Quotecompanyassociation will merge with a HubSpot Quotequotetemplateassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - HubSpot Quotequotetemplateassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecompanyassociation and a HubSpot Quotequotetemplateassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a HubSpot Quotequotetemplateassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - HubSpot Quotequotetemplateassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"


HubSpot Quotecontactassociation to HubSpot Quote
------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecontactassociation and a HubSpot Quote must be established.

A HubSpot Quotecontactassociation will merge with a HubSpot Quote if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - HubSpot Quote Property
   * - id
     - id

Once a link between a HubSpot Quotecontactassociation and a HubSpot Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a HubSpot Quote:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - HubSpot Quote Property
     - HubSpot Data Type


HubSpot Quotecontactassociation to HubSpot Quotecompanyassociation
------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecontactassociation and a HubSpot Quotecompanyassociation must be established.

A HubSpot Quotecontactassociation will merge with a HubSpot Quotecompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - HubSpot Quotecompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecontactassociation and a HubSpot Quotecompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a HubSpot Quotecompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - HubSpot Quotecompanyassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Quotecontactassociation to HubSpot Quotecontactassociation
------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecontactassociation and a HubSpot Quotecontactassociation must be established.

A HubSpot Quotecontactassociation will merge with a HubSpot Quotecontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - HubSpot Quotecontactassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecontactassociation and a HubSpot Quotecontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a HubSpot Quotecontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - HubSpot Quotecontactassociation Property
     - HubSpot Data Type


HubSpot Quotecontactassociation to HubSpot Quotedealassociation
---------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecontactassociation and a HubSpot Quotedealassociation must be established.

A HubSpot Quotecontactassociation will merge with a HubSpot Quotedealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - HubSpot Quotedealassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecontactassociation and a HubSpot Quotedealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a HubSpot Quotedealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - HubSpot Quotedealassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"


HubSpot Quotecontactassociation to HubSpot Quotequotetemplateassociation
------------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecontactassociation and a HubSpot Quotequotetemplateassociation must be established.

A HubSpot Quotecontactassociation will merge with a HubSpot Quotequotetemplateassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - HubSpot Quotequotetemplateassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecontactassociation and a HubSpot Quotequotetemplateassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a HubSpot Quotequotetemplateassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - HubSpot Quotequotetemplateassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"


HubSpot Quotedealassociation to HubSpot Quote
---------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotedealassociation and a HubSpot Quote must be established.

A HubSpot Quotedealassociation will merge with a HubSpot Quote if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - HubSpot Quote Property
   * - id
     - id

Once a link between a HubSpot Quotedealassociation and a HubSpot Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a HubSpot Quote:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - HubSpot Quote Property
     - HubSpot Data Type


HubSpot Quotedealassociation to HubSpot Quotecompanyassociation
---------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotedealassociation and a HubSpot Quotecompanyassociation must be established.

A HubSpot Quotedealassociation will merge with a HubSpot Quotecompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - HubSpot Quotecompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Quotedealassociation and a HubSpot Quotecompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a HubSpot Quotecompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - HubSpot Quotecompanyassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"


HubSpot Quotedealassociation to HubSpot Quotecontactassociation
---------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotedealassociation and a HubSpot Quotecontactassociation must be established.

A HubSpot Quotedealassociation will merge with a HubSpot Quotecontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - HubSpot Quotecontactassociation Property
   * - id
     - id

Once a link between a HubSpot Quotedealassociation and a HubSpot Quotecontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a HubSpot Quotecontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - HubSpot Quotecontactassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"


HubSpot Quotedealassociation to HubSpot Quotedealassociation
------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotedealassociation and a HubSpot Quotedealassociation must be established.

A HubSpot Quotedealassociation will merge with a HubSpot Quotedealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - HubSpot Quotedealassociation Property
   * - id
     - id

Once a link between a HubSpot Quotedealassociation and a HubSpot Quotedealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a HubSpot Quotedealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - HubSpot Quotedealassociation Property
     - HubSpot Data Type


HubSpot Quotedealassociation to HubSpot Quotequotetemplateassociation
---------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotedealassociation and a HubSpot Quotequotetemplateassociation must be established.

A HubSpot Quotedealassociation will merge with a HubSpot Quotequotetemplateassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - HubSpot Quotequotetemplateassociation Property
   * - id
     - id

Once a link between a HubSpot Quotedealassociation and a HubSpot Quotequotetemplateassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a HubSpot Quotequotetemplateassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - HubSpot Quotequotetemplateassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Quotequotetemplateassociation to HubSpot Quote
------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotequotetemplateassociation and a HubSpot Quote must be established.

A HubSpot Quotequotetemplateassociation will merge with a HubSpot Quote if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - HubSpot Quote Property
   * - id
     - id

Once a link between a HubSpot Quotequotetemplateassociation and a HubSpot Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a HubSpot Quote:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - HubSpot Quote Property
     - HubSpot Data Type


HubSpot Quotequotetemplateassociation to HubSpot Quotecompanyassociation
------------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotequotetemplateassociation and a HubSpot Quotecompanyassociation must be established.

A HubSpot Quotequotetemplateassociation will merge with a HubSpot Quotecompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - HubSpot Quotecompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Quotequotetemplateassociation and a HubSpot Quotecompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a HubSpot Quotecompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - HubSpot Quotecompanyassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"


HubSpot Quotequotetemplateassociation to HubSpot Quotecontactassociation
------------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotequotetemplateassociation and a HubSpot Quotecontactassociation must be established.

A HubSpot Quotequotetemplateassociation will merge with a HubSpot Quotecontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - HubSpot Quotecontactassociation Property
   * - id
     - id

Once a link between a HubSpot Quotequotetemplateassociation and a HubSpot Quotecontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a HubSpot Quotecontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - HubSpot Quotecontactassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"


HubSpot Quotequotetemplateassociation to HubSpot Quotedealassociation
---------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotequotetemplateassociation and a HubSpot Quotedealassociation must be established.

A HubSpot Quotequotetemplateassociation will merge with a HubSpot Quotedealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - HubSpot Quotedealassociation Property
   * - id
     - id

Once a link between a HubSpot Quotequotetemplateassociation and a HubSpot Quotedealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a HubSpot Quotedealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - HubSpot Quotedealassociation Property
     - HubSpot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Quotequotetemplateassociation to HubSpot Quotequotetemplateassociation
------------------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotequotetemplateassociation and a HubSpot Quotequotetemplateassociation must be established.

A HubSpot Quotequotetemplateassociation will merge with a HubSpot Quotequotetemplateassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - HubSpot Quotequotetemplateassociation Property
   * - id
     - id

Once a link between a HubSpot Quotequotetemplateassociation and a HubSpot Quotequotetemplateassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a HubSpot Quotequotetemplateassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - HubSpot Quotequotetemplateassociation Property
     - HubSpot Data Type


HubSpot Ticketcompanyassociation to HubSpot Ticketcompanyassociation
--------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Ticketcompanyassociation and a HubSpot Ticketcompanyassociation must be established.

A HubSpot Ticketcompanyassociation will merge with a HubSpot Ticketcompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociation Property
     - HubSpot Ticketcompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Ticketcompanyassociation and a HubSpot Ticketcompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociation and a HubSpot Ticketcompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociation Property
     - HubSpot Ticketcompanyassociation Property
     - HubSpot Data Type


HubSpot User to HubSpot Owner
-----------------------------
Before any synchronization can take place, a link between a HubSpot User and a HubSpot Owner must be established.

A HubSpot User will merge with a HubSpot Owner if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - HubSpot Owner Property
   * - Id
     - userId
   * - email
     - email

Once a link between a HubSpot User and a HubSpot Owner is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a HubSpot Owner:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - HubSpot Owner Property
     - HubSpot Data Type


HubSpot User to HubSpot User
----------------------------
Before any synchronization can take place, a link between a HubSpot User and a HubSpot User must be established.

A HubSpot User will merge with a HubSpot User if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - HubSpot User Property
   * - Id
     - Id
   * - email
     - email

Once a link between a HubSpot User and a HubSpot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a HubSpot User:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - HubSpot User Property
     - HubSpot Data Type
   * - email
     - email
     - "string"


HubSpot Company to HubSpot Contact
----------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a HubSpot Contact must be established.

A new HubSpot Contact will be created from a HubSpot Company if it is connected to a HubSpot Quote, Quotedealassociation, Quotecompanyassociation, Quotecontactassociation, or Quotequotetemplateassociation that is synchronized into HubSpot.

Once a link between a HubSpot Company and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - properties.country
     - properties.country
     - "string"
   * - properties.country
     - properties.state
     - "string"
   * - properties.industry
     - properties.country
     - "string"
   * - properties.industry
     - properties.state
     - "string"
   * - properties.state
     - properties.country
     - "string"
   * - properties.state
     - properties.state
     - "string"
   * - properties.type
     - properties.country
     - "string"
   * - properties.type
     - properties.state
     - "string"


HubSpot Contact to HubSpot Company
----------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a HubSpot Company must be established.

A new HubSpot Company will be created from a HubSpot Contact if it is connected to a HubSpot Quote, Quotedealassociation, Quotecompanyassociation, Quotecontactassociation, or Quotequotetemplateassociation that is synchronized into HubSpot.

Once a link between a HubSpot Contact and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - HubSpot Company Property
     - HubSpot Data Type


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
     - properties.email
     - "string"
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


HubSpot Dealcompanyassociationtype to HubSpot Quotecompanyassociationtype
-------------------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a HubSpot Quotecompanyassociationtype.

Once a link between a HubSpot Dealcompanyassociationtype and a HubSpot Quotecompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a HubSpot Quotecompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - HubSpot Quotecompanyassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Dealcompanyassociationtype to HubSpot Quotecontactassociationtype
-------------------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a HubSpot Quotecontactassociationtype.

Once a link between a HubSpot Dealcompanyassociationtype and a HubSpot Quotecontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a HubSpot Quotecontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - HubSpot Quotecontactassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Dealcompanyassociationtype to HubSpot Quotedealassociationtype
----------------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a HubSpot Quotedealassociationtype.

Once a link between a HubSpot Dealcompanyassociationtype and a HubSpot Quotedealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a HubSpot Quotedealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - HubSpot Quotedealassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Dealcompanyassociationtype to HubSpot Quotequotetemplateassociationtype
-------------------------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a HubSpot Quotequotetemplateassociationtype.

Once a link between a HubSpot Dealcompanyassociationtype and a HubSpot Quotequotetemplateassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a HubSpot Quotequotetemplateassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - HubSpot Quotequotetemplateassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Dealcompanyassociationtype to HubSpot Ticketcompanyassociationtype
--------------------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a HubSpot Ticketcompanyassociationtype.

Once a link between a HubSpot Dealcompanyassociationtype and a HubSpot Ticketcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a HubSpot Ticketcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - HubSpot Ticketcompanyassociationtype Property
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


HubSpot Dealcontactassociationtype to HubSpot Quotecompanyassociationtype
-------------------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a HubSpot Quotecompanyassociationtype.

Once a link between a HubSpot Dealcontactassociationtype and a HubSpot Quotecompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a HubSpot Quotecompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - HubSpot Quotecompanyassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Dealcontactassociationtype to HubSpot Quotecontactassociationtype
-------------------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a HubSpot Quotecontactassociationtype.

Once a link between a HubSpot Dealcontactassociationtype and a HubSpot Quotecontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a HubSpot Quotecontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - HubSpot Quotecontactassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Dealcontactassociationtype to HubSpot Quotedealassociationtype
----------------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a HubSpot Quotedealassociationtype.

Once a link between a HubSpot Dealcontactassociationtype and a HubSpot Quotedealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a HubSpot Quotedealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - HubSpot Quotedealassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Dealcontactassociationtype to HubSpot Quotequotetemplateassociationtype
-------------------------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a HubSpot Quotequotetemplateassociationtype.

Once a link between a HubSpot Dealcontactassociationtype and a HubSpot Quotequotetemplateassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a HubSpot Quotequotetemplateassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - HubSpot Quotequotetemplateassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Dealcontactassociationtype to HubSpot Ticketcompanyassociationtype
--------------------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a HubSpot Ticketcompanyassociationtype.

Once a link between a HubSpot Dealcontactassociationtype and a HubSpot Ticketcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a HubSpot Ticketcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - HubSpot Ticketcompanyassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Lineitemdealassociationtype to HubSpot Lineitemquoteassociationtype
---------------------------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a HubSpot Lineitemquoteassociationtype.

Once a link between a HubSpot Lineitemdealassociationtype and a HubSpot Lineitemquoteassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a HubSpot Lineitemquoteassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     - HubSpot Lineitemquoteassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Lineitemquoteassociationtype to HubSpot Lineitemdealassociationtype
---------------------------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a HubSpot Lineitemdealassociationtype.

Once a link between a HubSpot Lineitemquoteassociationtype and a HubSpot Lineitemdealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a HubSpot Lineitemdealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     - HubSpot Lineitemdealassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecompanyassociationtype to HubSpot Dealcompanyassociationtype
-------------------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a HubSpot Dealcompanyassociationtype.

Once a link between a HubSpot Quotecompanyassociationtype and a HubSpot Dealcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a HubSpot Dealcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - HubSpot Dealcompanyassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecompanyassociationtype to HubSpot Dealcontactassociationtype
-------------------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a HubSpot Dealcontactassociationtype.

Once a link between a HubSpot Quotecompanyassociationtype and a HubSpot Dealcontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a HubSpot Dealcontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - HubSpot Dealcontactassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecompanyassociationtype to HubSpot Quotecontactassociationtype
--------------------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a HubSpot Quotecontactassociationtype.

Once a link between a HubSpot Quotecompanyassociationtype and a HubSpot Quotecontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a HubSpot Quotecontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - HubSpot Quotecontactassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecompanyassociationtype to HubSpot Quotedealassociationtype
-----------------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a HubSpot Quotedealassociationtype.

Once a link between a HubSpot Quotecompanyassociationtype and a HubSpot Quotedealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a HubSpot Quotedealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - HubSpot Quotedealassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecompanyassociationtype to HubSpot Quotequotetemplateassociationtype
--------------------------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a HubSpot Quotequotetemplateassociationtype.

Once a link between a HubSpot Quotecompanyassociationtype and a HubSpot Quotequotetemplateassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a HubSpot Quotequotetemplateassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - HubSpot Quotequotetemplateassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecompanyassociationtype to HubSpot Ticketcompanyassociationtype
---------------------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a HubSpot Ticketcompanyassociationtype.

Once a link between a HubSpot Quotecompanyassociationtype and a HubSpot Ticketcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a HubSpot Ticketcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - HubSpot Ticketcompanyassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecontactassociationtype to HubSpot Dealcompanyassociationtype
-------------------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a HubSpot Dealcompanyassociationtype.

Once a link between a HubSpot Quotecontactassociationtype and a HubSpot Dealcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a HubSpot Dealcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - HubSpot Dealcompanyassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecontactassociationtype to HubSpot Dealcontactassociationtype
-------------------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a HubSpot Dealcontactassociationtype.

Once a link between a HubSpot Quotecontactassociationtype and a HubSpot Dealcontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a HubSpot Dealcontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - HubSpot Dealcontactassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecontactassociationtype to HubSpot Quotecompanyassociationtype
--------------------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a HubSpot Quotecompanyassociationtype.

Once a link between a HubSpot Quotecontactassociationtype and a HubSpot Quotecompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a HubSpot Quotecompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - HubSpot Quotecompanyassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecontactassociationtype to HubSpot Quotedealassociationtype
-----------------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a HubSpot Quotedealassociationtype.

Once a link between a HubSpot Quotecontactassociationtype and a HubSpot Quotedealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a HubSpot Quotedealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - HubSpot Quotedealassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecontactassociationtype to HubSpot Quotequotetemplateassociationtype
--------------------------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a HubSpot Quotequotetemplateassociationtype.

Once a link between a HubSpot Quotecontactassociationtype and a HubSpot Quotequotetemplateassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a HubSpot Quotequotetemplateassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - HubSpot Quotequotetemplateassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecontactassociationtype to HubSpot Ticketcompanyassociationtype
---------------------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a HubSpot Ticketcompanyassociationtype.

Once a link between a HubSpot Quotecontactassociationtype and a HubSpot Ticketcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a HubSpot Ticketcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - HubSpot Ticketcompanyassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotedealassociationtype to HubSpot Dealcompanyassociationtype
----------------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a HubSpot Dealcompanyassociationtype.

Once a link between a HubSpot Quotedealassociationtype and a HubSpot Dealcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a HubSpot Dealcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - HubSpot Dealcompanyassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotedealassociationtype to HubSpot Dealcontactassociationtype
----------------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a HubSpot Dealcontactassociationtype.

Once a link between a HubSpot Quotedealassociationtype and a HubSpot Dealcontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a HubSpot Dealcontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - HubSpot Dealcontactassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotedealassociationtype to HubSpot Quotecompanyassociationtype
-----------------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a HubSpot Quotecompanyassociationtype.

Once a link between a HubSpot Quotedealassociationtype and a HubSpot Quotecompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a HubSpot Quotecompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - HubSpot Quotecompanyassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotedealassociationtype to HubSpot Quotecontactassociationtype
-----------------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a HubSpot Quotecontactassociationtype.

Once a link between a HubSpot Quotedealassociationtype and a HubSpot Quotecontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a HubSpot Quotecontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - HubSpot Quotecontactassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotedealassociationtype to HubSpot Quotequotetemplateassociationtype
-----------------------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a HubSpot Quotequotetemplateassociationtype.

Once a link between a HubSpot Quotedealassociationtype and a HubSpot Quotequotetemplateassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a HubSpot Quotequotetemplateassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - HubSpot Quotequotetemplateassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotedealassociationtype to HubSpot Ticketcompanyassociationtype
------------------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a HubSpot Ticketcompanyassociationtype.

Once a link between a HubSpot Quotedealassociationtype and a HubSpot Ticketcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a HubSpot Ticketcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - HubSpot Ticketcompanyassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotequotetemplateassociationtype to HubSpot Dealcompanyassociationtype
-------------------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a HubSpot Dealcompanyassociationtype.

Once a link between a HubSpot Quotequotetemplateassociationtype and a HubSpot Dealcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a HubSpot Dealcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - HubSpot Dealcompanyassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotequotetemplateassociationtype to HubSpot Dealcontactassociationtype
-------------------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a HubSpot Dealcontactassociationtype.

Once a link between a HubSpot Quotequotetemplateassociationtype and a HubSpot Dealcontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a HubSpot Dealcontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - HubSpot Dealcontactassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotequotetemplateassociationtype to HubSpot Quotecompanyassociationtype
--------------------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a HubSpot Quotecompanyassociationtype.

Once a link between a HubSpot Quotequotetemplateassociationtype and a HubSpot Quotecompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a HubSpot Quotecompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - HubSpot Quotecompanyassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotequotetemplateassociationtype to HubSpot Quotecontactassociationtype
--------------------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a HubSpot Quotecontactassociationtype.

Once a link between a HubSpot Quotequotetemplateassociationtype and a HubSpot Quotecontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a HubSpot Quotecontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - HubSpot Quotecontactassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotequotetemplateassociationtype to HubSpot Quotedealassociationtype
-----------------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a HubSpot Quotedealassociationtype.

Once a link between a HubSpot Quotequotetemplateassociationtype and a HubSpot Quotedealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a HubSpot Quotedealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - HubSpot Quotedealassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Quotequotetemplateassociationtype to HubSpot Ticketcompanyassociationtype
---------------------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a HubSpot Ticketcompanyassociationtype.

Once a link between a HubSpot Quotequotetemplateassociationtype and a HubSpot Ticketcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a HubSpot Ticketcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - HubSpot Ticketcompanyassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Ticketcompanyassociationtype to HubSpot Dealcompanyassociationtype
--------------------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a HubSpot Dealcompanyassociationtype.

Once a link between a HubSpot Ticketcompanyassociationtype and a HubSpot Dealcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a HubSpot Dealcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     - HubSpot Dealcompanyassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Ticketcompanyassociationtype to HubSpot Dealcontactassociationtype
--------------------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a HubSpot Dealcontactassociationtype.

Once a link between a HubSpot Ticketcompanyassociationtype and a HubSpot Dealcontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a HubSpot Dealcontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     - HubSpot Dealcontactassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Ticketcompanyassociationtype to HubSpot Quotecompanyassociationtype
---------------------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a HubSpot Quotecompanyassociationtype.

Once a link between a HubSpot Ticketcompanyassociationtype and a HubSpot Quotecompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a HubSpot Quotecompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     - HubSpot Quotecompanyassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Ticketcompanyassociationtype to HubSpot Quotecontactassociationtype
---------------------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a HubSpot Quotecontactassociationtype.

Once a link between a HubSpot Ticketcompanyassociationtype and a HubSpot Quotecontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a HubSpot Quotecontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     - HubSpot Quotecontactassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Ticketcompanyassociationtype to HubSpot Quotedealassociationtype
------------------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a HubSpot Quotedealassociationtype.

Once a link between a HubSpot Ticketcompanyassociationtype and a HubSpot Quotedealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a HubSpot Quotedealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     - HubSpot Quotedealassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"


HubSpot Ticketcompanyassociationtype to HubSpot Quotequotetemplateassociationtype
---------------------------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a HubSpot Quotequotetemplateassociationtype.

Once a link between a HubSpot Ticketcompanyassociationtype and a HubSpot Quotequotetemplateassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a HubSpot Quotequotetemplateassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     - HubSpot Quotequotetemplateassociationtype Property
     - HubSpot Data Type
   * - label
     - label
     - "string"

