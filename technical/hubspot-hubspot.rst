====================
HubSpot to  Dataflow
====================

Generated: 2023-11-30 00:01:11

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to  Company
---------------------------
Before any synchronization can take place, a link between a HubSpot Company and a  Company must be established.

A HubSpot Company will merge with a  Company if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Company Property
   * - id
     - id

Once a link between a HubSpot Company and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Company:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Company Property
     -  Data Type
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


HubSpot Contact to  Contact
---------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a  Contact must be established.

A HubSpot Contact will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Contact Property
   * - id
     - id
   * - properties.email
     - properties.email

Once a link between a HubSpot Contact and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a  Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Contact Property
     -  Data Type
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


HubSpot Contact to  Contactcompanyassociation
---------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a  Contactcompanyassociation must be established.

A HubSpot Contact will merge with a  Contactcompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Contactcompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Contact and a  Contactcompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a  Contactcompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Contactcompanyassociation Property
     -  Data Type
   * - id
     - id
     - "integer"


HubSpot Contactcompanyassociation to  Contact
---------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a  Contact.

If a matching  Contact already exists, the HubSpot Contactcompanyassociation will be merged with the existing one.
If no matching  Contact is found, a new  Contact will be created.

A HubSpot Contactcompanyassociation will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     -  Contact Property
   * - id
     - id

Once a link between a HubSpot Contactcompanyassociation and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a  Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     -  Contact Property
     -  Data Type


HubSpot Contactcompanyassociation to  Contactcompanyassociation
---------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contactcompanyassociation and a  Contactcompanyassociation must be established.

A HubSpot Contactcompanyassociation will merge with a  Contactcompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     -  Contactcompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Contactcompanyassociation and a  Contactcompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a  Contactcompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     -  Contactcompanyassociation Property
     -  Data Type
   * - id
     - id
     - "integer"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "integer"


HubSpot Deal to  Deal
---------------------
Before any synchronization can take place, a link between a HubSpot Deal and a  Deal must be established.

A HubSpot Deal will merge with a  Deal if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     -  Deal Property
   * - id
     - id

Once a link between a HubSpot Deal and a  Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a  Deal:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     -  Deal Property
     -  Data Type


HubSpot Deal to  Dealcompanyassociation
---------------------------------------
Before any synchronization can take place, a link between a HubSpot Deal and a  Dealcompanyassociation must be established.

A HubSpot Deal will merge with a  Dealcompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     -  Dealcompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Deal and a  Dealcompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a  Dealcompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     -  Dealcompanyassociation Property
     -  Data Type
   * - id
     - id
     - "string"
   * - properties.hubspot_owner_id
     - toObjectId (Dependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypes)
     - "string"


HubSpot Deal to  Dealcontactassociation
---------------------------------------
Before any synchronization can take place, a link between a HubSpot Deal and a  Dealcontactassociation must be established.

A HubSpot Deal will merge with a  Dealcontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     -  Dealcontactassociation Property
   * - id
     - id

Once a link between a HubSpot Deal and a  Dealcontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a  Dealcontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     -  Dealcontactassociation Property
     -  Data Type
   * - id
     - id
     - "string"
   * - properties.hubspot_owner_id
     - toObjectId (Dependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypes)
     - "string"


HubSpot Dealcompanyassociation to  Deal
---------------------------------------
Before any synchronization can take place, a link between a HubSpot Dealcompanyassociation and a  Deal must be established.

A HubSpot Dealcompanyassociation will merge with a  Deal if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     -  Deal Property
   * - id
     - id

Once a link between a HubSpot Dealcompanyassociation and a  Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a  Deal:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     -  Deal Property
     -  Data Type
   * - toObjectId (Dependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypes)
     - properties.hubspot_owner_id
     - "string"


HubSpot Dealcompanyassociation to  Dealcompanyassociation
---------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Dealcompanyassociation and a  Dealcompanyassociation must be established.

A HubSpot Dealcompanyassociation will merge with a  Dealcompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     -  Dealcompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Dealcompanyassociation and a  Dealcompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a  Dealcompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     -  Dealcompanyassociation Property
     -  Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Dealcompanyassociation to  Dealcontactassociation
---------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Dealcompanyassociation and a  Dealcontactassociation must be established.

A HubSpot Dealcompanyassociation will merge with a  Dealcontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     -  Dealcontactassociation Property
   * - id
     - id

Once a link between a HubSpot Dealcompanyassociation and a  Dealcontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a  Dealcontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     -  Dealcontactassociation Property
     -  Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Dealcontactassociation to  Deal
---------------------------------------
Before any synchronization can take place, a link between a HubSpot Dealcontactassociation and a  Deal must be established.

A HubSpot Dealcontactassociation will merge with a  Deal if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     -  Deal Property
   * - id
     - id

Once a link between a HubSpot Dealcontactassociation and a  Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a  Deal:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     -  Deal Property
     -  Data Type
   * - toObjectId (Dependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypesDependant on having wd:Q16869121 in sesam_simpleAssociationTypes)
     - properties.hubspot_owner_id
     - "string"


HubSpot Dealcontactassociation to  Dealcompanyassociation
---------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Dealcontactassociation and a  Dealcompanyassociation must be established.

A HubSpot Dealcontactassociation will merge with a  Dealcompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     -  Dealcompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Dealcontactassociation and a  Dealcompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a  Dealcompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     -  Dealcompanyassociation Property
     -  Data Type
   * - id
     - id
     - "string"
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Dealcontactassociation to  Dealcontactassociation
---------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Dealcontactassociation and a  Dealcontactassociation must be established.

A HubSpot Dealcontactassociation will merge with a  Dealcontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     -  Dealcontactassociation Property
   * - id
     - id

Once a link between a HubSpot Dealcontactassociation and a  Dealcontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a  Dealcontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     -  Dealcontactassociation Property
     -  Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Lineitem to  Lineitem
-----------------------------
Before any synchronization can take place, a link between a HubSpot Lineitem and a  Lineitem must be established.

A HubSpot Lineitem will merge with a  Lineitem if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     -  Lineitem Property
   * - id
     - id

Once a link between a HubSpot Lineitem and a  Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a  Lineitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     -  Lineitem Property
     -  Data Type


HubSpot Lineitem to  Lineitemquoteassociation
---------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitem and a  Lineitemquoteassociation must be established.

A HubSpot Lineitem will merge with a  Lineitemquoteassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     -  Lineitemquoteassociation Property
   * - id
     - id

Once a link between a HubSpot Lineitem and a  Lineitemquoteassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a  Lineitemquoteassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     -  Lineitemquoteassociation Property
     -  Data Type
   * - id
     - id
     - "string"


HubSpot Lineitemdealassociation to  Lineitemdealassociation
-----------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitemdealassociation and a  Lineitemdealassociation must be established.

A HubSpot Lineitemdealassociation will merge with a  Lineitemdealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     -  Lineitemdealassociation Property
   * - id
     - id

Once a link between a HubSpot Lineitemdealassociation and a  Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a  Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     -  Lineitemdealassociation Property
     -  Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Lineitemdealassociation to  Lineitemquoteassociation
------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitemdealassociation and a  Lineitemquoteassociation must be established.

A HubSpot Lineitemdealassociation will merge with a  Lineitemquoteassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     -  Lineitemquoteassociation Property
   * - id
     - id

Once a link between a HubSpot Lineitemdealassociation and a  Lineitemquoteassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a  Lineitemquoteassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     -  Lineitemquoteassociation Property
     -  Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Lineitemquoteassociation to  Lineitem
---------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitemquoteassociation and a  Lineitem must be established.

A HubSpot Lineitemquoteassociation will merge with a  Lineitem if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     -  Lineitem Property
   * - id
     - id

Once a link between a HubSpot Lineitemquoteassociation and a  Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a  Lineitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     -  Lineitem Property
     -  Data Type


HubSpot Lineitemquoteassociation to  Lineitemdealassociation
------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitemquoteassociation and a  Lineitemdealassociation must be established.

A HubSpot Lineitemquoteassociation will merge with a  Lineitemdealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     -  Lineitemdealassociation Property
   * - id
     - id

Once a link between a HubSpot Lineitemquoteassociation and a  Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a  Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     -  Lineitemdealassociation Property
     -  Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q940607 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Lineitemquoteassociation to  Lineitemquoteassociation
-------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Lineitemquoteassociation and a  Lineitemquoteassociation must be established.

A HubSpot Lineitemquoteassociation will merge with a  Lineitemquoteassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     -  Lineitemquoteassociation Property
   * - id
     - id

Once a link between a HubSpot Lineitemquoteassociation and a  Lineitemquoteassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a  Lineitemquoteassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     -  Lineitemquoteassociation Property
     -  Data Type


HubSpot Owner to  User
----------------------
Before any synchronization can take place, a link between a HubSpot Owner and a  User must be established.

A HubSpot Owner will merge with a  User if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Owner Property
     -  User Property
   * - userId
     - Id
   * - email
     - email

Once a link between a HubSpot Owner and a  User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Owner and a  User:

.. list-table::
   :header-rows: 1

   * - HubSpot Owner Property
     -  User Property
     -  Data Type
   * - email
     - email
     - "string"


HubSpot Quote to  Quote
-----------------------
Before any synchronization can take place, a link between a HubSpot Quote and a  Quote must be established.

A HubSpot Quote will merge with a  Quote if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     -  Quote Property
   * - id
     - id

Once a link between a HubSpot Quote and a  Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a  Quote:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     -  Quote Property
     -  Data Type


HubSpot Quote to  Quotecompanyassociation
-----------------------------------------
Before any synchronization can take place, a link between a HubSpot Quote and a  Quotecompanyassociation must be established.

A HubSpot Quote will merge with a  Quotecompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     -  Quotecompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Quote and a  Quotecompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a  Quotecompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     -  Quotecompanyassociation Property
     -  Data Type
   * - associations.companies.results.id
     - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - "string"
   * - associations.contacts.results.id
     - toObjectId (Dependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypes)
     - "string"
   * - id
     - id
     - "string"


HubSpot Quote to  Quotecontactassociation
-----------------------------------------
Before any synchronization can take place, a link between a HubSpot Quote and a  Quotecontactassociation must be established.

A HubSpot Quote will merge with a  Quotecontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     -  Quotecontactassociation Property
   * - id
     - id

Once a link between a HubSpot Quote and a  Quotecontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a  Quotecontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     -  Quotecontactassociation Property
     -  Data Type
   * - associations.companies.results.id
     - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - "string"
   * - associations.contacts.results.id
     - toObjectId (Dependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypesDependant on having wd:Q760086 in sesam_simpleAssociationTypes)
     - "string"
   * - id
     - id
     - "string"


HubSpot Quote to  Quotedealassociation
--------------------------------------
Before any synchronization can take place, a link between a HubSpot Quote and a  Quotedealassociation must be established.

A HubSpot Quote will merge with a  Quotedealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     -  Quotedealassociation Property
   * - id
     - id

Once a link between a HubSpot Quote and a  Quotedealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a  Quotedealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     -  Quotedealassociation Property
     -  Data Type
   * - id
     - id
     - "string"


HubSpot Quote to  Quotequotetemplateassociation
-----------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quote and a  Quotequotetemplateassociation must be established.

A HubSpot Quote will merge with a  Quotequotetemplateassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     -  Quotequotetemplateassociation Property
   * - id
     - id

Once a link between a HubSpot Quote and a  Quotequotetemplateassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a  Quotequotetemplateassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     -  Quotequotetemplateassociation Property
     -  Data Type
   * - id
     - id
     - "string"


HubSpot Quotecompanyassociation to  Quote
-----------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecompanyassociation and a  Quote must be established.

A HubSpot Quotecompanyassociation will merge with a  Quote if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     -  Quote Property
   * - id
     - id

Once a link between a HubSpot Quotecompanyassociation and a  Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a  Quote:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     -  Quote Property
     -  Data Type


HubSpot Quotecompanyassociation to  Quotecompanyassociation
-----------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecompanyassociation and a  Quotecompanyassociation must be established.

A HubSpot Quotecompanyassociation will merge with a  Quotecompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     -  Quotecompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecompanyassociation and a  Quotecompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a  Quotecompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     -  Quotecompanyassociation Property
     -  Data Type


HubSpot Quotecompanyassociation to  Quotecontactassociation
-----------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecompanyassociation and a  Quotecontactassociation must be established.

A HubSpot Quotecompanyassociation will merge with a  Quotecontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     -  Quotecontactassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecompanyassociation and a  Quotecontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a  Quotecontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     -  Quotecontactassociation Property
     -  Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Quotecompanyassociation to  Quotedealassociation
--------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecompanyassociation and a  Quotedealassociation must be established.

A HubSpot Quotecompanyassociation will merge with a  Quotedealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     -  Quotedealassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecompanyassociation and a  Quotedealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a  Quotedealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     -  Quotedealassociation Property
     -  Data Type
   * - id
     - id
     - "string"


HubSpot Quotecompanyassociation to  Quotequotetemplateassociation
-----------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecompanyassociation and a  Quotequotetemplateassociation must be established.

A HubSpot Quotecompanyassociation will merge with a  Quotequotetemplateassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     -  Quotequotetemplateassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecompanyassociation and a  Quotequotetemplateassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a  Quotequotetemplateassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     -  Quotequotetemplateassociation Property
     -  Data Type
   * - id
     - id
     - "string"


HubSpot Quotecontactassociation to  Quote
-----------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecontactassociation and a  Quote must be established.

A HubSpot Quotecontactassociation will merge with a  Quote if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     -  Quote Property
   * - id
     - id

Once a link between a HubSpot Quotecontactassociation and a  Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a  Quote:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     -  Quote Property
     -  Data Type


HubSpot Quotecontactassociation to  Quotecompanyassociation
-----------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecontactassociation and a  Quotecompanyassociation must be established.

A HubSpot Quotecontactassociation will merge with a  Quotecompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     -  Quotecompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecontactassociation and a  Quotecompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a  Quotecompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     -  Quotecompanyassociation Property
     -  Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Quotecontactassociation to  Quotecontactassociation
-----------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecontactassociation and a  Quotecontactassociation must be established.

A HubSpot Quotecontactassociation will merge with a  Quotecontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     -  Quotecontactassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecontactassociation and a  Quotecontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a  Quotecontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     -  Quotecontactassociation Property
     -  Data Type


HubSpot Quotecontactassociation to  Quotedealassociation
--------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecontactassociation and a  Quotedealassociation must be established.

A HubSpot Quotecontactassociation will merge with a  Quotedealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     -  Quotedealassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecontactassociation and a  Quotedealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a  Quotedealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     -  Quotedealassociation Property
     -  Data Type
   * - id
     - id
     - "string"


HubSpot Quotecontactassociation to  Quotequotetemplateassociation
-----------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotecontactassociation and a  Quotequotetemplateassociation must be established.

A HubSpot Quotecontactassociation will merge with a  Quotequotetemplateassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     -  Quotequotetemplateassociation Property
   * - id
     - id

Once a link between a HubSpot Quotecontactassociation and a  Quotequotetemplateassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a  Quotequotetemplateassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     -  Quotequotetemplateassociation Property
     -  Data Type
   * - id
     - id
     - "string"


HubSpot Quotedealassociation to  Quote
--------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotedealassociation and a  Quote must be established.

A HubSpot Quotedealassociation will merge with a  Quote if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     -  Quote Property
   * - id
     - id

Once a link between a HubSpot Quotedealassociation and a  Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a  Quote:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     -  Quote Property
     -  Data Type


HubSpot Quotedealassociation to  Quotecompanyassociation
--------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotedealassociation and a  Quotecompanyassociation must be established.

A HubSpot Quotedealassociation will merge with a  Quotecompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     -  Quotecompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Quotedealassociation and a  Quotecompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a  Quotecompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     -  Quotecompanyassociation Property
     -  Data Type
   * - id
     - id
     - "string"


HubSpot Quotedealassociation to  Quotecontactassociation
--------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotedealassociation and a  Quotecontactassociation must be established.

A HubSpot Quotedealassociation will merge with a  Quotecontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     -  Quotecontactassociation Property
   * - id
     - id

Once a link between a HubSpot Quotedealassociation and a  Quotecontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a  Quotecontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     -  Quotecontactassociation Property
     -  Data Type
   * - id
     - id
     - "string"


HubSpot Quotedealassociation to  Quotedealassociation
-----------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotedealassociation and a  Quotedealassociation must be established.

A HubSpot Quotedealassociation will merge with a  Quotedealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     -  Quotedealassociation Property
   * - id
     - id

Once a link between a HubSpot Quotedealassociation and a  Quotedealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a  Quotedealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     -  Quotedealassociation Property
     -  Data Type


HubSpot Quotedealassociation to  Quotequotetemplateassociation
--------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotedealassociation and a  Quotequotetemplateassociation must be established.

A HubSpot Quotedealassociation will merge with a  Quotequotetemplateassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     -  Quotequotetemplateassociation Property
   * - id
     - id

Once a link between a HubSpot Quotedealassociation and a  Quotequotetemplateassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a  Quotequotetemplateassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     -  Quotequotetemplateassociation Property
     -  Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Quotequotetemplateassociation to  Quote
-----------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotequotetemplateassociation and a  Quote must be established.

A HubSpot Quotequotetemplateassociation will merge with a  Quote if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     -  Quote Property
   * - id
     - id

Once a link between a HubSpot Quotequotetemplateassociation and a  Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a  Quote:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     -  Quote Property
     -  Data Type


HubSpot Quotequotetemplateassociation to  Quotecompanyassociation
-----------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotequotetemplateassociation and a  Quotecompanyassociation must be established.

A HubSpot Quotequotetemplateassociation will merge with a  Quotecompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     -  Quotecompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Quotequotetemplateassociation and a  Quotecompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a  Quotecompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     -  Quotecompanyassociation Property
     -  Data Type
   * - id
     - id
     - "string"


HubSpot Quotequotetemplateassociation to  Quotecontactassociation
-----------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotequotetemplateassociation and a  Quotecontactassociation must be established.

A HubSpot Quotequotetemplateassociation will merge with a  Quotecontactassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     -  Quotecontactassociation Property
   * - id
     - id

Once a link between a HubSpot Quotequotetemplateassociation and a  Quotecontactassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a  Quotecontactassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     -  Quotecontactassociation Property
     -  Data Type
   * - id
     - id
     - "string"


HubSpot Quotequotetemplateassociation to  Quotedealassociation
--------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotequotetemplateassociation and a  Quotedealassociation must be established.

A HubSpot Quotequotetemplateassociation will merge with a  Quotedealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     -  Quotedealassociation Property
   * - id
     - id

Once a link between a HubSpot Quotequotetemplateassociation and a  Quotedealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a  Quotedealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     -  Quotedealassociation Property
     -  Data Type
   * - id
     - id
     - "string"
   * - toObjectId
     - toObjectId (Dependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypes)
     - "string"


HubSpot Quotequotetemplateassociation to  Quotequotetemplateassociation
-----------------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotequotetemplateassociation and a  Quotequotetemplateassociation must be established.

A HubSpot Quotequotetemplateassociation will merge with a  Quotequotetemplateassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     -  Quotequotetemplateassociation Property
   * - id
     - id

Once a link between a HubSpot Quotequotetemplateassociation and a  Quotequotetemplateassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a  Quotequotetemplateassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     -  Quotequotetemplateassociation Property
     -  Data Type


HubSpot Ticket to  Ticket
-------------------------
Before any synchronization can take place, a link between a HubSpot Ticket and a  Ticket must be established.

A HubSpot Ticket will merge with a  Ticket if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticket Property
     -  Ticket Property
   * - properties.hs_pipeline
     - properties.hs_pipeline

Once a link between a HubSpot Ticket and a  Ticket is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticket and a  Ticket:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticket Property
     -  Ticket Property
     -  Data Type
   * - properties.hubspot_owner_id
     - properties.hubspot_owner_id
     - "string"
   * - properties.subject
     - properties.subject
     - "string"


HubSpot Ticketcompanyassociation to  Ticketcompanyassociation
-------------------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Ticketcompanyassociation and a  Ticketcompanyassociation must be established.

A HubSpot Ticketcompanyassociation will merge with a  Ticketcompanyassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociation Property
     -  Ticketcompanyassociation Property
   * - id
     - id

Once a link between a HubSpot Ticketcompanyassociation and a  Ticketcompanyassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociation and a  Ticketcompanyassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociation Property
     -  Ticketcompanyassociation Property
     -  Data Type


HubSpot User to  User
---------------------
Before any synchronization can take place, a link between a HubSpot User and a  User must be established.

A HubSpot User will merge with a  User if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     -  User Property
   * - Id
     - Id
   * - email
     - email

Once a link between a HubSpot User and a  User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a  User:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     -  User Property
     -  Data Type
   * - email
     - email
     - "string"


HubSpot Company to  Contact
---------------------------
Before any synchronization can take place, a link between a HubSpot Company and a  Contact must be established.

A new  Contact will be created from a HubSpot Company if it is connected to a HubSpot Quote, Quotedealassociation, Quotecompanyassociation, Quotecontactassociation, or Quotequotetemplateassociation that is synchronized into .

Once a link between a HubSpot Company and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Contact Property
     -  Data Type
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


HubSpot Contact to  Company
---------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a  Company must be established.

A new  Company will be created from a HubSpot Contact if it is connected to a HubSpot Quote, Quotedealassociation, Quotecompanyassociation, Quotecontactassociation, or Quotequotetemplateassociation that is synchronized into .

Once a link between a HubSpot Contact and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a  Company:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Company Property
     -  Data Type


HubSpot User to  Contact
------------------------
Every HubSpot User will be synchronized with a  Contact.

Once a link between a HubSpot User and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a  Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     -  Contact Property
     -  Data Type
   * - email
     - properties.email
     - "string"
   * - email
     - properties.work_email
     - "string"


HubSpot Dealcompanyassociationtype to  Dealcontactassociationtype
-----------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a  Dealcontactassociationtype.

Once a link between a HubSpot Dealcompanyassociationtype and a  Dealcontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a  Dealcontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     -  Dealcontactassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Dealcompanyassociationtype to  Quotecompanyassociationtype
------------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a  Quotecompanyassociationtype.

Once a link between a HubSpot Dealcompanyassociationtype and a  Quotecompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a  Quotecompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     -  Quotecompanyassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Dealcompanyassociationtype to  Quotecontactassociationtype
------------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a  Quotecontactassociationtype.

Once a link between a HubSpot Dealcompanyassociationtype and a  Quotecontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a  Quotecontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     -  Quotecontactassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Dealcompanyassociationtype to  Quotedealassociationtype
---------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a  Quotedealassociationtype.

Once a link between a HubSpot Dealcompanyassociationtype and a  Quotedealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a  Quotedealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     -  Quotedealassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Dealcompanyassociationtype to  Quotequotetemplateassociationtype
------------------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a  Quotequotetemplateassociationtype.

Once a link between a HubSpot Dealcompanyassociationtype and a  Quotequotetemplateassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a  Quotequotetemplateassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     -  Quotequotetemplateassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Dealcompanyassociationtype to  Ticketcompanyassociationtype
-------------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a  Ticketcompanyassociationtype.

Once a link between a HubSpot Dealcompanyassociationtype and a  Ticketcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a  Ticketcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     -  Ticketcompanyassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Dealcontactassociationtype to  Dealcompanyassociationtype
-----------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a  Dealcompanyassociationtype.

Once a link between a HubSpot Dealcontactassociationtype and a  Dealcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a  Dealcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     -  Dealcompanyassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Dealcontactassociationtype to  Quotecompanyassociationtype
------------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a  Quotecompanyassociationtype.

Once a link between a HubSpot Dealcontactassociationtype and a  Quotecompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a  Quotecompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     -  Quotecompanyassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Dealcontactassociationtype to  Quotecontactassociationtype
------------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a  Quotecontactassociationtype.

Once a link between a HubSpot Dealcontactassociationtype and a  Quotecontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a  Quotecontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     -  Quotecontactassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Dealcontactassociationtype to  Quotedealassociationtype
---------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a  Quotedealassociationtype.

Once a link between a HubSpot Dealcontactassociationtype and a  Quotedealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a  Quotedealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     -  Quotedealassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Dealcontactassociationtype to  Quotequotetemplateassociationtype
------------------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a  Quotequotetemplateassociationtype.

Once a link between a HubSpot Dealcontactassociationtype and a  Quotequotetemplateassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a  Quotequotetemplateassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     -  Quotequotetemplateassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Dealcontactassociationtype to  Ticketcompanyassociationtype
-------------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a  Ticketcompanyassociationtype.

Once a link between a HubSpot Dealcontactassociationtype and a  Ticketcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a  Ticketcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     -  Ticketcompanyassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Lineitem to  Lineitemdealassociation
--------------------------------------------
Every HubSpot Lineitem will be synchronized with a  Lineitemdealassociation.

If a matching  Lineitemdealassociation already exists, the HubSpot Lineitem will be merged with the existing one.
If no matching  Lineitemdealassociation is found, a new  Lineitemdealassociation will be created.

A HubSpot Lineitem will merge with a  Lineitemdealassociation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     -  Lineitemdealassociation Property
   * - id
     - id

Once a link between a HubSpot Lineitem and a  Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a  Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     -  Lineitemdealassociation Property
     -  Data Type
   * - id
     - id
     - "string"


HubSpot Lineitemdealassociation to  Lineitem
--------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a  Lineitem.

If a matching  Lineitem already exists, the HubSpot Lineitemdealassociation will be merged with the existing one.
If no matching  Lineitem is found, a new  Lineitem will be created.

A HubSpot Lineitemdealassociation will merge with a  Lineitem if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     -  Lineitem Property
   * - id
     - id

Once a link between a HubSpot Lineitemdealassociation and a  Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a  Lineitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     -  Lineitem Property
     -  Data Type


HubSpot Lineitemdealassociationtype to  Lineitemquoteassociationtype
--------------------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a  Lineitemquoteassociationtype.

Once a link between a HubSpot Lineitemdealassociationtype and a  Lineitemquoteassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a  Lineitemquoteassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     -  Lineitemquoteassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Lineitemquoteassociationtype to  Lineitemdealassociationtype
--------------------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a  Lineitemdealassociationtype.

Once a link between a HubSpot Lineitemquoteassociationtype and a  Lineitemdealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a  Lineitemdealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     -  Lineitemdealassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotecompanyassociationtype to  Dealcompanyassociationtype
------------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a  Dealcompanyassociationtype.

Once a link between a HubSpot Quotecompanyassociationtype and a  Dealcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a  Dealcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     -  Dealcompanyassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotecompanyassociationtype to  Dealcontactassociationtype
------------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a  Dealcontactassociationtype.

Once a link between a HubSpot Quotecompanyassociationtype and a  Dealcontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a  Dealcontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     -  Dealcontactassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotecompanyassociationtype to  Quotecontactassociationtype
-------------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a  Quotecontactassociationtype.

Once a link between a HubSpot Quotecompanyassociationtype and a  Quotecontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a  Quotecontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     -  Quotecontactassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotecompanyassociationtype to  Quotedealassociationtype
----------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a  Quotedealassociationtype.

Once a link between a HubSpot Quotecompanyassociationtype and a  Quotedealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a  Quotedealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     -  Quotedealassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotecompanyassociationtype to  Quotequotetemplateassociationtype
-------------------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a  Quotequotetemplateassociationtype.

Once a link between a HubSpot Quotecompanyassociationtype and a  Quotequotetemplateassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a  Quotequotetemplateassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     -  Quotequotetemplateassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotecompanyassociationtype to  Ticketcompanyassociationtype
--------------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a  Ticketcompanyassociationtype.

Once a link between a HubSpot Quotecompanyassociationtype and a  Ticketcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a  Ticketcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     -  Ticketcompanyassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotecontactassociationtype to  Dealcompanyassociationtype
------------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a  Dealcompanyassociationtype.

Once a link between a HubSpot Quotecontactassociationtype and a  Dealcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a  Dealcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     -  Dealcompanyassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotecontactassociationtype to  Dealcontactassociationtype
------------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a  Dealcontactassociationtype.

Once a link between a HubSpot Quotecontactassociationtype and a  Dealcontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a  Dealcontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     -  Dealcontactassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotecontactassociationtype to  Quotecompanyassociationtype
-------------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a  Quotecompanyassociationtype.

Once a link between a HubSpot Quotecontactassociationtype and a  Quotecompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a  Quotecompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     -  Quotecompanyassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotecontactassociationtype to  Quotedealassociationtype
----------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a  Quotedealassociationtype.

Once a link between a HubSpot Quotecontactassociationtype and a  Quotedealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a  Quotedealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     -  Quotedealassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotecontactassociationtype to  Quotequotetemplateassociationtype
-------------------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a  Quotequotetemplateassociationtype.

Once a link between a HubSpot Quotecontactassociationtype and a  Quotequotetemplateassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a  Quotequotetemplateassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     -  Quotequotetemplateassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotecontactassociationtype to  Ticketcompanyassociationtype
--------------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a  Ticketcompanyassociationtype.

Once a link between a HubSpot Quotecontactassociationtype and a  Ticketcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a  Ticketcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     -  Ticketcompanyassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotedealassociationtype to  Dealcompanyassociationtype
---------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a  Dealcompanyassociationtype.

Once a link between a HubSpot Quotedealassociationtype and a  Dealcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a  Dealcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     -  Dealcompanyassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotedealassociationtype to  Dealcontactassociationtype
---------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a  Dealcontactassociationtype.

Once a link between a HubSpot Quotedealassociationtype and a  Dealcontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a  Dealcontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     -  Dealcontactassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotedealassociationtype to  Quotecompanyassociationtype
----------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a  Quotecompanyassociationtype.

Once a link between a HubSpot Quotedealassociationtype and a  Quotecompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a  Quotecompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     -  Quotecompanyassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotedealassociationtype to  Quotecontactassociationtype
----------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a  Quotecontactassociationtype.

Once a link between a HubSpot Quotedealassociationtype and a  Quotecontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a  Quotecontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     -  Quotecontactassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotedealassociationtype to  Quotequotetemplateassociationtype
----------------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a  Quotequotetemplateassociationtype.

Once a link between a HubSpot Quotedealassociationtype and a  Quotequotetemplateassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a  Quotequotetemplateassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     -  Quotequotetemplateassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotedealassociationtype to  Ticketcompanyassociationtype
-----------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a  Ticketcompanyassociationtype.

Once a link between a HubSpot Quotedealassociationtype and a  Ticketcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a  Ticketcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     -  Ticketcompanyassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotequotetemplateassociationtype to  Dealcompanyassociationtype
------------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a  Dealcompanyassociationtype.

Once a link between a HubSpot Quotequotetemplateassociationtype and a  Dealcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a  Dealcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     -  Dealcompanyassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotequotetemplateassociationtype to  Dealcontactassociationtype
------------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a  Dealcontactassociationtype.

Once a link between a HubSpot Quotequotetemplateassociationtype and a  Dealcontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a  Dealcontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     -  Dealcontactassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotequotetemplateassociationtype to  Quotecompanyassociationtype
-------------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a  Quotecompanyassociationtype.

Once a link between a HubSpot Quotequotetemplateassociationtype and a  Quotecompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a  Quotecompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     -  Quotecompanyassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotequotetemplateassociationtype to  Quotecontactassociationtype
-------------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a  Quotecontactassociationtype.

Once a link between a HubSpot Quotequotetemplateassociationtype and a  Quotecontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a  Quotecontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     -  Quotecontactassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotequotetemplateassociationtype to  Quotedealassociationtype
----------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a  Quotedealassociationtype.

Once a link between a HubSpot Quotequotetemplateassociationtype and a  Quotedealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a  Quotedealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     -  Quotedealassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Quotequotetemplateassociationtype to  Ticketcompanyassociationtype
--------------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a  Ticketcompanyassociationtype.

Once a link between a HubSpot Quotequotetemplateassociationtype and a  Ticketcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a  Ticketcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     -  Ticketcompanyassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Ticketcompanyassociationtype to  Dealcompanyassociationtype
-------------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a  Dealcompanyassociationtype.

Once a link between a HubSpot Ticketcompanyassociationtype and a  Dealcompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a  Dealcompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     -  Dealcompanyassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Ticketcompanyassociationtype to  Dealcontactassociationtype
-------------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a  Dealcontactassociationtype.

Once a link between a HubSpot Ticketcompanyassociationtype and a  Dealcontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a  Dealcontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     -  Dealcontactassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Ticketcompanyassociationtype to  Quotecompanyassociationtype
--------------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a  Quotecompanyassociationtype.

Once a link between a HubSpot Ticketcompanyassociationtype and a  Quotecompanyassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a  Quotecompanyassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     -  Quotecompanyassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Ticketcompanyassociationtype to  Quotecontactassociationtype
--------------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a  Quotecontactassociationtype.

Once a link between a HubSpot Ticketcompanyassociationtype and a  Quotecontactassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a  Quotecontactassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     -  Quotecontactassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Ticketcompanyassociationtype to  Quotedealassociationtype
-----------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a  Quotedealassociationtype.

Once a link between a HubSpot Ticketcompanyassociationtype and a  Quotedealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a  Quotedealassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     -  Quotedealassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"


HubSpot Ticketcompanyassociationtype to  Quotequotetemplateassociationtype
--------------------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a  Quotequotetemplateassociationtype.

Once a link between a HubSpot Ticketcompanyassociationtype and a  Quotequotetemplateassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a  Quotequotetemplateassociationtype:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     -  Quotequotetemplateassociationtype Property
     -  Data Type
   * - label
     - label
     - "string"

