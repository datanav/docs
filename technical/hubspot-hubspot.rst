===========================
HubSpot to Hubspot Dataflow
===========================

Generated: 2024-07-05 00:00:33

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to Hubspot Company
----------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Hubspot Company must be established.

A HubSpot Company will merge with a Hubspot Company if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Hubspot Company Property
   * - id
     - id

Once a link between a HubSpot Company and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Hubspot Company Property
     - Hubspot Data Type
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


HubSpot Contact to Hubspot Contact
----------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Hubspot Contact must be established.

A HubSpot Contact will merge with a Hubspot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Hubspot Contact Property
   * - id
     - id
   * - properties.email
     - properties.email

Once a link between a HubSpot Contact and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Hubspot Contact Property
     - Hubspot Data Type
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


HubSpot Contact to Hubspot Contactcompanyassociation
----------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Hubspot Contactcompanyassociation must be established.

A HubSpot Contact will merge with a Hubspot Contactcompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Hubspot Contactcompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Contact and a Hubspot Contactcompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Hubspot Contactcompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Hubspot Contactcompanyassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "integer"


HubSpot Contactcompanyassociation to Hubspot Contact
----------------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a Hubspot Contact.

If a matching Hubspot Contact already exists, the HubSpot Contactcompanyassociation will be merged with the existing one.
If no matching Hubspot Contact is found, a new Hubspot Contact will be created.

A HubSpot Contactcompanyassociation will merge with a Hubspot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - Hubspot Contact Property
   * - id
     - id

Once a link between a HubSpot Contactcompanyassociation and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - Hubspot Contact Property
     - Hubspot Data Type


HubSpot Contactcompanyassociation to Hubspot Contactcompanyassociation
----------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contactcompanyassociation and a Hubspot Contactcompanyassociation must be established.

A HubSpot Contactcompanyassociation will merge with a Hubspot Contactcompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - Hubspot Contactcompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Contactcompanyassociation and a Hubspot Contactcompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a Hubspot Contactcompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - Hubspot Contactcompanyassociation Property
     - Hubspot Data Type
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


HubSpot Deal to Hubspot Deal
----------------------------
Before any synchronization can take place, a link between a HubSpot Deal and a Hubspot Deal must be established.

A HubSpot Deal will merge with a Hubspot Deal if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Hubspot Deal Property
   * - id
     - id

Once a link between a HubSpot Deal and a Hubspot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Hubspot Deal:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Hubspot Deal Property
     - Hubspot Data Type


HubSpot Deal to Hubspot Dealcompanyassociation
----------------------------------------------
Before any synchronization can take place, a link between a HubSpot Deal and a Hubspot Dealcompanyassociation must be established.

A HubSpot Deal will merge with a Hubspot Dealcompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Hubspot Dealcompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Deal and a Hubspot Dealcompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Hubspot Dealcompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Hubspot Dealcompanyassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"
   * - properties.hubspot_owner_id
     - toObjectId (Dependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypes)
     - "string"


HubSpot Deal to Hubspot Dealcontactassociation
----------------------------------------------
Before any synchronization can take place, a link between a HubSpot Deal and a Hubspot Dealcontactassociation must be established.

A HubSpot Deal will merge with a Hubspot Dealcontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Hubspot Dealcontactassociation Property
   * - id
     - id

Once a link between a HubSpot Deal and a Hubspot Dealcontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Hubspot Dealcontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Hubspot Dealcontactassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"
   * - properties.hubspot_owner_id
     - toObjectId (Dependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypes)
     - "string"


HubSpot Dealcompanyassociation to Hubspot Deal
----------------------------------------------
Before any synchronization can take place, a link between a HubSpot Dealcompanyassociation and a Hubspot Deal must be established.

A HubSpot Dealcompanyassociation will merge with a Hubspot Deal if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - Hubspot Deal Property
   * - id
     - id

Once a link between a HubSpot Dealcompanyassociation and a Hubspot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a Hubspot Deal:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - Hubspot Deal Property
     - Hubspot Data Type
   * - toObjectId (Dependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypes)
     - properties.hubspot_owner_id
     - "string"


HubSpot Dealcompanyassociation to Hubspot Dealcompanyassociation
----------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Dealcompanyassociation and a Hubspot Dealcompanyassociation must be established.

A HubSpot Dealcompanyassociation will merge with a Hubspot Dealcompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - Hubspot Dealcompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Dealcompanyassociation and a Hubspot Dealcompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a Hubspot Dealcompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - Hubspot Dealcompanyassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Dealcompanyassociation to Hubspot Dealcontactassociation
----------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Dealcompanyassociation and a Hubspot Dealcontactassociation must be established.

A HubSpot Dealcompanyassociation will merge with a Hubspot Dealcontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - Hubspot Dealcontactassociation Property
   * - id
     - id

Once a link between a HubSpot Dealcompanyassociation and a Hubspot Dealcontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a Hubspot Dealcontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - Hubspot Dealcontactassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Dealcontactassociation to Hubspot Deal
----------------------------------------------
Before any synchronization can take place, a link between a HubSpot Dealcontactassociation and a Hubspot Deal must be established.

A HubSpot Dealcontactassociation will merge with a Hubspot Deal if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - Hubspot Deal Property
   * - id
     - id

Once a link between a HubSpot Dealcontactassociation and a Hubspot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a Hubspot Deal:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - Hubspot Deal Property
     - Hubspot Data Type
   * - toObjectId (Dependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypes)
     - properties.hubspot_owner_id
     - "string"


HubSpot Dealcontactassociation to Hubspot Dealcompanyassociation
----------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Dealcontactassociation and a Hubspot Dealcompanyassociation must be established.

A HubSpot Dealcontactassociation will merge with a Hubspot Dealcompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - Hubspot Dealcompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Dealcontactassociation and a Hubspot Dealcompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a Hubspot Dealcompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - Hubspot Dealcompanyassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Dealcontactassociation to Hubspot Dealcontactassociation
----------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Dealcontactassociation and a Hubspot Dealcontactassociation must be established.

A HubSpot Dealcontactassociation will merge with a Hubspot Dealcontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - Hubspot Dealcontactassociation Property
   * - id
     - id

Once a link between a HubSpot Dealcontactassociation and a Hubspot Dealcontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a Hubspot Dealcontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - Hubspot Dealcontactassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Lineitem to Hubspot Lineitem
------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitem and a Hubspot Lineitem must be established.

A HubSpot Lineitem will merge with a Hubspot Lineitem if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Hubspot Lineitem Property
   * - id
     - id

Once a link between a HubSpot Lineitem and a Hubspot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Hubspot Lineitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Hubspot Lineitem Property
     - Hubspot Data Type


HubSpot Lineitem to Hubspot Lineitemdealassociation
---------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitem and a Hubspot Lineitemdealassociation must be established.

A HubSpot Lineitem will merge with a Hubspot Lineitemdealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Hubspot Lineitemdealassociation Property
   * - id
     - id

Once a link between a HubSpot Lineitem and a Hubspot Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Hubspot Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Hubspot Lineitemdealassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"


HubSpot Lineitem to Hubspot Lineitemquoteassociation
----------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitem and a Hubspot Lineitemquoteassociation must be established.

A HubSpot Lineitem will merge with a Hubspot Lineitemquoteassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Hubspot Lineitemquoteassociation Property
   * - id
     - id

Once a link between a HubSpot Lineitem and a Hubspot Lineitemquoteassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Hubspot Lineitemquoteassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Hubspot Lineitemquoteassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"


HubSpot Lineitemdealassociation to Hubspot Lineitem
---------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitemdealassociation and a Hubspot Lineitem must be established.

A HubSpot Lineitemdealassociation will merge with a Hubspot Lineitem if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - Hubspot Lineitem Property
   * - id
     - id

Once a link between a HubSpot Lineitemdealassociation and a Hubspot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a Hubspot Lineitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - Hubspot Lineitem Property
     - Hubspot Data Type


HubSpot Lineitemdealassociation to Hubspot Lineitemdealassociation
------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitemdealassociation and a Hubspot Lineitemdealassociation must be established.

A HubSpot Lineitemdealassociation will merge with a Hubspot Lineitemdealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - Hubspot Lineitemdealassociation Property
   * - id
     - id

Once a link between a HubSpot Lineitemdealassociation and a Hubspot Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a Hubspot Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - Hubspot Lineitemdealassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Lineitemdealassociation to Hubspot Lineitemquoteassociation
-------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitemdealassociation and a Hubspot Lineitemquoteassociation must be established.

A HubSpot Lineitemdealassociation will merge with a Hubspot Lineitemquoteassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - Hubspot Lineitemquoteassociation Property
   * - id
     - id

Once a link between a HubSpot Lineitemdealassociation and a Hubspot Lineitemquoteassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a Hubspot Lineitemquoteassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - Hubspot Lineitemquoteassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Lineitemquoteassociation to Hubspot Lineitem
----------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitemquoteassociation and a Hubspot Lineitem must be established.

A HubSpot Lineitemquoteassociation will merge with a Hubspot Lineitem if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - Hubspot Lineitem Property
   * - id
     - id

Once a link between a HubSpot Lineitemquoteassociation and a Hubspot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a Hubspot Lineitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - Hubspot Lineitem Property
     - Hubspot Data Type


HubSpot Lineitemquoteassociation to Hubspot Lineitemdealassociation
-------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitemquoteassociation and a Hubspot Lineitemdealassociation must be established.

A HubSpot Lineitemquoteassociation will merge with a Hubspot Lineitemdealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - Hubspot Lineitemdealassociation Property
   * - id
     - id

Once a link between a HubSpot Lineitemquoteassociation and a Hubspot Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a Hubspot Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - Hubspot Lineitemdealassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q940607 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Lineitemquoteassociation to Hubspot Lineitemquoteassociation
--------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitemquoteassociation and a Hubspot Lineitemquoteassociation must be established.

A HubSpot Lineitemquoteassociation will merge with a Hubspot Lineitemquoteassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - Hubspot Lineitemquoteassociation Property
   * - id
     - id

Once a link between a HubSpot Lineitemquoteassociation and a Hubspot Lineitemquoteassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a Hubspot Lineitemquoteassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - Hubspot Lineitemquoteassociation Property
     - Hubspot Data Type


HubSpot Owner to Hubspot User
-----------------------------
Before any synchronization can take place, a link between a HubSpot Owner and a Hubspot User must be established.

A HubSpot Owner will merge with a Hubspot User if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Owner Property
     - Hubspot User Property
   * - userId
     - Id
   * - email
     - email

Once a link between a HubSpot Owner and a Hubspot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Owner and a Hubspot User:

.. list-table::
   :header-rows: 1

   * - HubSpot Owner Property
     - Hubspot User Property
     - Hubspot Data Type
   * - email
     - email
     - "string"


HubSpot Quote to Hubspot Quote
------------------------------
Before any synchronization can take place, a link between a HubSpot Quote and a Hubspot Quote must be established.

A HubSpot Quote will merge with a Hubspot Quote if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Hubspot Quote Property
   * - id
     - id

Once a link between a HubSpot Quote and a Hubspot Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a Hubspot Quote:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Hubspot Quote Property
     - Hubspot Data Type


HubSpot Quote to Hubspot Quotecompanyassociation
------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quote and a Hubspot Quotecompanyassociation must be established.

A HubSpot Quote will merge with a Hubspot Quotecompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Hubspot Quotecompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Quote and a Hubspot Quotecompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a Hubspot Quotecompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Hubspot Quotecompanyassociation Property
     - Hubspot Data Type
   * - associations.companies.results.id
     - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - "string"
   * - associations.contacts.results.id
     - toObjectId (Dependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypes)
     - "string"
   * - id
     - id
     - "string"


HubSpot Quote to Hubspot Quotecontactassociation
------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quote and a Hubspot Quotecontactassociation must be established.

A HubSpot Quote will merge with a Hubspot Quotecontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Hubspot Quotecontactassociation Property
   * - id
     - id

Once a link between a HubSpot Quote and a Hubspot Quotecontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a Hubspot Quotecontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Hubspot Quotecontactassociation Property
     - Hubspot Data Type
   * - associations.companies.results.id
     - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - "string"
   * - associations.contacts.results.id
     - toObjectId (Dependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypes)
     - "string"
   * - id
     - id
     - "string"


HubSpot Quote to Hubspot Quotedealassociation
---------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quote and a Hubspot Quotedealassociation must be established.

A HubSpot Quote will merge with a Hubspot Quotedealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Hubspot Quotedealassociation Property
   * - id
     - id

Once a link between a HubSpot Quote and a Hubspot Quotedealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a Hubspot Quotedealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Hubspot Quotedealassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"


HubSpot Quote to Hubspot Quotequotetemplateassociation
------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quote and a Hubspot Quotequotetemplateassociation must be established.

A HubSpot Quote will merge with a Hubspot Quotequotetemplateassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Hubspot Quotequotetemplateassociation Property
   * - id
     - id

Once a link between a HubSpot Quote and a Hubspot Quotequotetemplateassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a Hubspot Quotequotetemplateassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Hubspot Quotequotetemplateassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"


HubSpot Quotecompanyassociation to Hubspot Quote
------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecompanyassociation and a Hubspot Quote must be established.

A HubSpot Quotecompanyassociation will merge with a Hubspot Quote if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - Hubspot Quote Property
   * - id
     - id

Once a link between a HubSpot Quotecompanyassociation and a Hubspot Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a Hubspot Quote:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - Hubspot Quote Property
     - Hubspot Data Type


HubSpot Quotecompanyassociation to Hubspot Quotecompanyassociation
------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecompanyassociation and a Hubspot Quotecompanyassociation must be established.

A HubSpot Quotecompanyassociation will merge with a Hubspot Quotecompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - Hubspot Quotecompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecompanyassociation and a Hubspot Quotecompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a Hubspot Quotecompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - Hubspot Quotecompanyassociation Property
     - Hubspot Data Type


HubSpot Quotecompanyassociation to Hubspot Quotecontactassociation
------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecompanyassociation and a Hubspot Quotecontactassociation must be established.

A HubSpot Quotecompanyassociation will merge with a Hubspot Quotecontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - Hubspot Quotecontactassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecompanyassociation and a Hubspot Quotecontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a Hubspot Quotecontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - Hubspot Quotecontactassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Quotecompanyassociation to Hubspot Quotedealassociation
---------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecompanyassociation and a Hubspot Quotedealassociation must be established.

A HubSpot Quotecompanyassociation will merge with a Hubspot Quotedealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - Hubspot Quotedealassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecompanyassociation and a Hubspot Quotedealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a Hubspot Quotedealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - Hubspot Quotedealassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"


HubSpot Quotecompanyassociation to Hubspot Quotequotetemplateassociation
------------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecompanyassociation and a Hubspot Quotequotetemplateassociation must be established.

A HubSpot Quotecompanyassociation will merge with a Hubspot Quotequotetemplateassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - Hubspot Quotequotetemplateassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecompanyassociation and a Hubspot Quotequotetemplateassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a Hubspot Quotequotetemplateassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - Hubspot Quotequotetemplateassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"


HubSpot Quotecontactassociation to Hubspot Quote
------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecontactassociation and a Hubspot Quote must be established.

A HubSpot Quotecontactassociation will merge with a Hubspot Quote if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - Hubspot Quote Property
   * - id
     - id

Once a link between a HubSpot Quotecontactassociation and a Hubspot Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a Hubspot Quote:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - Hubspot Quote Property
     - Hubspot Data Type


HubSpot Quotecontactassociation to Hubspot Quotecompanyassociation
------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecontactassociation and a Hubspot Quotecompanyassociation must be established.

A HubSpot Quotecontactassociation will merge with a Hubspot Quotecompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - Hubspot Quotecompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecontactassociation and a Hubspot Quotecompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a Hubspot Quotecompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - Hubspot Quotecompanyassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Quotecontactassociation to Hubspot Quotecontactassociation
------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecontactassociation and a Hubspot Quotecontactassociation must be established.

A HubSpot Quotecontactassociation will merge with a Hubspot Quotecontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - Hubspot Quotecontactassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecontactassociation and a Hubspot Quotecontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a Hubspot Quotecontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - Hubspot Quotecontactassociation Property
     - Hubspot Data Type


HubSpot Quotecontactassociation to Hubspot Quotedealassociation
---------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecontactassociation and a Hubspot Quotedealassociation must be established.

A HubSpot Quotecontactassociation will merge with a Hubspot Quotedealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - Hubspot Quotedealassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecontactassociation and a Hubspot Quotedealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a Hubspot Quotedealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - Hubspot Quotedealassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"


HubSpot Quotecontactassociation to Hubspot Quotequotetemplateassociation
------------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecontactassociation and a Hubspot Quotequotetemplateassociation must be established.

A HubSpot Quotecontactassociation will merge with a Hubspot Quotequotetemplateassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - Hubspot Quotequotetemplateassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecontactassociation and a Hubspot Quotequotetemplateassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a Hubspot Quotequotetemplateassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - Hubspot Quotequotetemplateassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"


HubSpot Quotedealassociation to Hubspot Quote
---------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotedealassociation and a Hubspot Quote must be established.

A HubSpot Quotedealassociation will merge with a Hubspot Quote if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - Hubspot Quote Property
   * - id
     - id

Once a link between a HubSpot Quotedealassociation and a Hubspot Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a Hubspot Quote:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - Hubspot Quote Property
     - Hubspot Data Type


HubSpot Quotedealassociation to Hubspot Quotecompanyassociation
---------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotedealassociation and a Hubspot Quotecompanyassociation must be established.

A HubSpot Quotedealassociation will merge with a Hubspot Quotecompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - Hubspot Quotecompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Quotedealassociation and a Hubspot Quotecompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a Hubspot Quotecompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - Hubspot Quotecompanyassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"


HubSpot Quotedealassociation to Hubspot Quotecontactassociation
---------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotedealassociation and a Hubspot Quotecontactassociation must be established.

A HubSpot Quotedealassociation will merge with a Hubspot Quotecontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - Hubspot Quotecontactassociation Property
   * - id
     - id

Once a link between a HubSpot Quotedealassociation and a Hubspot Quotecontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a Hubspot Quotecontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - Hubspot Quotecontactassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"


HubSpot Quotedealassociation to Hubspot Quotedealassociation
------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotedealassociation and a Hubspot Quotedealassociation must be established.

A HubSpot Quotedealassociation will merge with a Hubspot Quotedealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - Hubspot Quotedealassociation Property
   * - id
     - id

Once a link between a HubSpot Quotedealassociation and a Hubspot Quotedealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a Hubspot Quotedealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - Hubspot Quotedealassociation Property
     - Hubspot Data Type


HubSpot Quotedealassociation to Hubspot Quotequotetemplateassociation
---------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotedealassociation and a Hubspot Quotequotetemplateassociation must be established.

A HubSpot Quotedealassociation will merge with a Hubspot Quotequotetemplateassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - Hubspot Quotequotetemplateassociation Property
   * - id
     - id

Once a link between a HubSpot Quotedealassociation and a Hubspot Quotequotetemplateassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a Hubspot Quotequotetemplateassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - Hubspot Quotequotetemplateassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Quotequotetemplateassociation to Hubspot Quote
------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotequotetemplateassociation and a Hubspot Quote must be established.

A HubSpot Quotequotetemplateassociation will merge with a Hubspot Quote if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - Hubspot Quote Property
   * - id
     - id

Once a link between a HubSpot Quotequotetemplateassociation and a Hubspot Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a Hubspot Quote:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - Hubspot Quote Property
     - Hubspot Data Type


HubSpot Quotequotetemplateassociation to Hubspot Quotecompanyassociation
------------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotequotetemplateassociation and a Hubspot Quotecompanyassociation must be established.

A HubSpot Quotequotetemplateassociation will merge with a Hubspot Quotecompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - Hubspot Quotecompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Quotequotetemplateassociation and a Hubspot Quotecompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a Hubspot Quotecompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - Hubspot Quotecompanyassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"


HubSpot Quotequotetemplateassociation to Hubspot Quotecontactassociation
------------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotequotetemplateassociation and a Hubspot Quotecontactassociation must be established.

A HubSpot Quotequotetemplateassociation will merge with a Hubspot Quotecontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - Hubspot Quotecontactassociation Property
   * - id
     - id

Once a link between a HubSpot Quotequotetemplateassociation and a Hubspot Quotecontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a Hubspot Quotecontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - Hubspot Quotecontactassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"


HubSpot Quotequotetemplateassociation to Hubspot Quotedealassociation
---------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotequotetemplateassociation and a Hubspot Quotedealassociation must be established.

A HubSpot Quotequotetemplateassociation will merge with a Hubspot Quotedealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - Hubspot Quotedealassociation Property
   * - id
     - id

Once a link between a HubSpot Quotequotetemplateassociation and a Hubspot Quotedealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a Hubspot Quotedealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - Hubspot Quotedealassociation Property
     - Hubspot Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Quotequotetemplateassociation to Hubspot Quotequotetemplateassociation
------------------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotequotetemplateassociation and a Hubspot Quotequotetemplateassociation must be established.

A HubSpot Quotequotetemplateassociation will merge with a Hubspot Quotequotetemplateassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - Hubspot Quotequotetemplateassociation Property
   * - id
     - id

Once a link between a HubSpot Quotequotetemplateassociation and a Hubspot Quotequotetemplateassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a Hubspot Quotequotetemplateassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - Hubspot Quotequotetemplateassociation Property
     - Hubspot Data Type


HubSpot User to Hubspot User
----------------------------
Before any synchronization can take place, a link between a HubSpot User and a Hubspot User must be established.

A HubSpot User will merge with a Hubspot User if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Hubspot User Property
   * - Id
     - Id
   * - email
     - email

Once a link between a HubSpot User and a Hubspot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Hubspot User:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Hubspot User Property
     - Hubspot Data Type
   * - email
     - email
     - "string"


HubSpot Company to Hubspot Contact
----------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Hubspot Contact must be established.

A new Hubspot Contact will be created from a HubSpot Company if it is connected to a HubSpot Quote, Quotedealassociation, Quotecompanyassociation, Quotecontactassociation, or Quotequotetemplateassociation that is synchronized into Hubspot.

Once a link between a HubSpot Company and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Hubspot Contact Property
     - Hubspot Data Type
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


HubSpot Contact to Hubspot Company
----------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Hubspot Company must be established.

A new Hubspot Company will be created from a HubSpot Contact if it is connected to a HubSpot Quote, Quotedealassociation, Quotecompanyassociation, Quotecontactassociation, or Quotequotetemplateassociation that is synchronized into Hubspot.

Once a link between a HubSpot Contact and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Hubspot Company Property
     - Hubspot Data Type


HubSpot User to Hubspot Contact
-------------------------------
Every HubSpot User will be synchronized with a Hubspot Contact.

Once a link between a HubSpot User and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Hubspot Contact Property
     - Hubspot Data Type
   * - email
     - properties.email
     - "string"
   * - email
     - properties.work_email
     - "string"


HubSpot Dealcompanyassociationtype to Hubspot Dealcontactassociationtype
------------------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a Hubspot Dealcontactassociationtype.

Once a link between a HubSpot Dealcompanyassociationtype and a Hubspot Dealcontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a Hubspot Dealcontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - Hubspot Dealcontactassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Dealcompanyassociationtype to Hubspot Quotecompanyassociationtype
-------------------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a Hubspot Quotecompanyassociationtype.

Once a link between a HubSpot Dealcompanyassociationtype and a Hubspot Quotecompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a Hubspot Quotecompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - Hubspot Quotecompanyassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Dealcompanyassociationtype to Hubspot Quotecontactassociationtype
-------------------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a Hubspot Quotecontactassociationtype.

Once a link between a HubSpot Dealcompanyassociationtype and a Hubspot Quotecontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a Hubspot Quotecontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - Hubspot Quotecontactassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Dealcompanyassociationtype to Hubspot Quotedealassociationtype
----------------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a Hubspot Quotedealassociationtype.

Once a link between a HubSpot Dealcompanyassociationtype and a Hubspot Quotedealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a Hubspot Quotedealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - Hubspot Quotedealassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Dealcompanyassociationtype to Hubspot Quotequotetemplateassociationtype
-------------------------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a Hubspot Quotequotetemplateassociationtype.

Once a link between a HubSpot Dealcompanyassociationtype and a Hubspot Quotequotetemplateassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a Hubspot Quotequotetemplateassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - Hubspot Quotequotetemplateassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Dealcontactassociationtype to Hubspot Dealcompanyassociationtype
------------------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a Hubspot Dealcompanyassociationtype.

Once a link between a HubSpot Dealcontactassociationtype and a Hubspot Dealcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a Hubspot Dealcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - Hubspot Dealcompanyassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Dealcontactassociationtype to Hubspot Quotecompanyassociationtype
-------------------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a Hubspot Quotecompanyassociationtype.

Once a link between a HubSpot Dealcontactassociationtype and a Hubspot Quotecompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a Hubspot Quotecompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - Hubspot Quotecompanyassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Dealcontactassociationtype to Hubspot Quotecontactassociationtype
-------------------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a Hubspot Quotecontactassociationtype.

Once a link between a HubSpot Dealcontactassociationtype and a Hubspot Quotecontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a Hubspot Quotecontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - Hubspot Quotecontactassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Dealcontactassociationtype to Hubspot Quotedealassociationtype
----------------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a Hubspot Quotedealassociationtype.

Once a link between a HubSpot Dealcontactassociationtype and a Hubspot Quotedealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a Hubspot Quotedealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - Hubspot Quotedealassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Dealcontactassociationtype to Hubspot Quotequotetemplateassociationtype
-------------------------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a Hubspot Quotequotetemplateassociationtype.

Once a link between a HubSpot Dealcontactassociationtype and a Hubspot Quotequotetemplateassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a Hubspot Quotequotetemplateassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - Hubspot Quotequotetemplateassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Lineitemdealassociationtype to Hubspot Lineitemquoteassociationtype
---------------------------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a Hubspot Lineitemquoteassociationtype.

Once a link between a HubSpot Lineitemdealassociationtype and a Hubspot Lineitemquoteassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a Hubspot Lineitemquoteassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     - Hubspot Lineitemquoteassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Lineitemquoteassociationtype to Hubspot Lineitemdealassociationtype
---------------------------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a Hubspot Lineitemdealassociationtype.

Once a link between a HubSpot Lineitemquoteassociationtype and a Hubspot Lineitemdealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a Hubspot Lineitemdealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     - Hubspot Lineitemdealassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecompanyassociationtype to Hubspot Dealcompanyassociationtype
-------------------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a Hubspot Dealcompanyassociationtype.

Once a link between a HubSpot Quotecompanyassociationtype and a Hubspot Dealcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a Hubspot Dealcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - Hubspot Dealcompanyassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecompanyassociationtype to Hubspot Dealcontactassociationtype
-------------------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a Hubspot Dealcontactassociationtype.

Once a link between a HubSpot Quotecompanyassociationtype and a Hubspot Dealcontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a Hubspot Dealcontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - Hubspot Dealcontactassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecompanyassociationtype to Hubspot Quotecontactassociationtype
--------------------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a Hubspot Quotecontactassociationtype.

Once a link between a HubSpot Quotecompanyassociationtype and a Hubspot Quotecontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a Hubspot Quotecontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - Hubspot Quotecontactassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecompanyassociationtype to Hubspot Quotedealassociationtype
-----------------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a Hubspot Quotedealassociationtype.

Once a link between a HubSpot Quotecompanyassociationtype and a Hubspot Quotedealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a Hubspot Quotedealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - Hubspot Quotedealassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecompanyassociationtype to Hubspot Quotequotetemplateassociationtype
--------------------------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a Hubspot Quotequotetemplateassociationtype.

Once a link between a HubSpot Quotecompanyassociationtype and a Hubspot Quotequotetemplateassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a Hubspot Quotequotetemplateassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - Hubspot Quotequotetemplateassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecontactassociationtype to Hubspot Dealcompanyassociationtype
-------------------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a Hubspot Dealcompanyassociationtype.

Once a link between a HubSpot Quotecontactassociationtype and a Hubspot Dealcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a Hubspot Dealcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - Hubspot Dealcompanyassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecontactassociationtype to Hubspot Dealcontactassociationtype
-------------------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a Hubspot Dealcontactassociationtype.

Once a link between a HubSpot Quotecontactassociationtype and a Hubspot Dealcontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a Hubspot Dealcontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - Hubspot Dealcontactassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecontactassociationtype to Hubspot Quotecompanyassociationtype
--------------------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a Hubspot Quotecompanyassociationtype.

Once a link between a HubSpot Quotecontactassociationtype and a Hubspot Quotecompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a Hubspot Quotecompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - Hubspot Quotecompanyassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecontactassociationtype to Hubspot Quotedealassociationtype
-----------------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a Hubspot Quotedealassociationtype.

Once a link between a HubSpot Quotecontactassociationtype and a Hubspot Quotedealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a Hubspot Quotedealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - Hubspot Quotedealassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Quotecontactassociationtype to Hubspot Quotequotetemplateassociationtype
--------------------------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a Hubspot Quotequotetemplateassociationtype.

Once a link between a HubSpot Quotecontactassociationtype and a Hubspot Quotequotetemplateassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a Hubspot Quotequotetemplateassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - Hubspot Quotequotetemplateassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Quotedealassociationtype to Hubspot Dealcompanyassociationtype
----------------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a Hubspot Dealcompanyassociationtype.

Once a link between a HubSpot Quotedealassociationtype and a Hubspot Dealcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a Hubspot Dealcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - Hubspot Dealcompanyassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Quotedealassociationtype to Hubspot Dealcontactassociationtype
----------------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a Hubspot Dealcontactassociationtype.

Once a link between a HubSpot Quotedealassociationtype and a Hubspot Dealcontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a Hubspot Dealcontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - Hubspot Dealcontactassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Quotedealassociationtype to Hubspot Quotecompanyassociationtype
-----------------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a Hubspot Quotecompanyassociationtype.

Once a link between a HubSpot Quotedealassociationtype and a Hubspot Quotecompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a Hubspot Quotecompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - Hubspot Quotecompanyassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Quotedealassociationtype to Hubspot Quotecontactassociationtype
-----------------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a Hubspot Quotecontactassociationtype.

Once a link between a HubSpot Quotedealassociationtype and a Hubspot Quotecontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a Hubspot Quotecontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - Hubspot Quotecontactassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Quotedealassociationtype to Hubspot Quotequotetemplateassociationtype
-----------------------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a Hubspot Quotequotetemplateassociationtype.

Once a link between a HubSpot Quotedealassociationtype and a Hubspot Quotequotetemplateassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a Hubspot Quotequotetemplateassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - Hubspot Quotequotetemplateassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Quotequotetemplateassociationtype to Hubspot Dealcompanyassociationtype
-------------------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a Hubspot Dealcompanyassociationtype.

Once a link between a HubSpot Quotequotetemplateassociationtype and a Hubspot Dealcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a Hubspot Dealcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - Hubspot Dealcompanyassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Quotequotetemplateassociationtype to Hubspot Dealcontactassociationtype
-------------------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a Hubspot Dealcontactassociationtype.

Once a link between a HubSpot Quotequotetemplateassociationtype and a Hubspot Dealcontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a Hubspot Dealcontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - Hubspot Dealcontactassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Quotequotetemplateassociationtype to Hubspot Quotecompanyassociationtype
--------------------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a Hubspot Quotecompanyassociationtype.

Once a link between a HubSpot Quotequotetemplateassociationtype and a Hubspot Quotecompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a Hubspot Quotecompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - Hubspot Quotecompanyassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Quotequotetemplateassociationtype to Hubspot Quotecontactassociationtype
--------------------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a Hubspot Quotecontactassociationtype.

Once a link between a HubSpot Quotequotetemplateassociationtype and a Hubspot Quotecontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a Hubspot Quotecontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - Hubspot Quotecontactassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Quotequotetemplateassociationtype to Hubspot Quotedealassociationtype
-----------------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a Hubspot Quotedealassociationtype.

Once a link between a HubSpot Quotequotetemplateassociationtype and a Hubspot Quotedealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a Hubspot Quotedealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - Hubspot Quotedealassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Ticketcompanyassociationtype to Hubspot Dealcompanyassociationtype
--------------------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a Hubspot Dealcompanyassociationtype.

Once a link between a HubSpot Ticketcompanyassociationtype and a Hubspot Dealcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a Hubspot Dealcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     - Hubspot Dealcompanyassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Ticketcompanyassociationtype to Hubspot Dealcontactassociationtype
--------------------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a Hubspot Dealcontactassociationtype.

Once a link between a HubSpot Ticketcompanyassociationtype and a Hubspot Dealcontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a Hubspot Dealcontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     - Hubspot Dealcontactassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Ticketcompanyassociationtype to Hubspot Quotecompanyassociationtype
---------------------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a Hubspot Quotecompanyassociationtype.

Once a link between a HubSpot Ticketcompanyassociationtype and a Hubspot Quotecompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a Hubspot Quotecompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     - Hubspot Quotecompanyassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Ticketcompanyassociationtype to Hubspot Quotecontactassociationtype
---------------------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a Hubspot Quotecontactassociationtype.

Once a link between a HubSpot Ticketcompanyassociationtype and a Hubspot Quotecontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a Hubspot Quotecontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     - Hubspot Quotecontactassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Ticketcompanyassociationtype to Hubspot Quotedealassociationtype
------------------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a Hubspot Quotedealassociationtype.

Once a link between a HubSpot Ticketcompanyassociationtype and a Hubspot Quotedealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a Hubspot Quotedealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     - Hubspot Quotedealassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"


HubSpot Ticketcompanyassociationtype to Hubspot Quotequotetemplateassociationtype
---------------------------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a Hubspot Quotequotetemplateassociationtype.

Once a link between a HubSpot Ticketcompanyassociationtype and a Hubspot Quotequotetemplateassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a Hubspot Quotequotetemplateassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     - Hubspot Quotequotetemplateassociationtype Property
     - Hubspot Data Type
   * - label
     - label
     - "string"

