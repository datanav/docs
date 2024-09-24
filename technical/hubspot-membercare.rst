==============================
HubSpot to MemberCare Dataflow
==============================

Generated: 2024-09-24 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to MemberCare Companies
---------------------------------------
Every HubSpot Company will be synchronized with a MemberCare Companies.

Once a link between a HubSpot Company and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - properties.name
     - companyName
     - "string"
   * - properties.website
     - url
     - "string"


HubSpot Contact to MemberCare Persons
-------------------------------------
Every HubSpot Contact will be synchronized with a MemberCare Persons.

Once a link between a HubSpot Contact and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - id
     - addresses.id
     - "string"
   * - properties.city
     - addresses.postalCode.city
     - "string"
   * - properties.country
     - addresses.country.id
     - "string"
   * - properties.date_of_birth
     - birthDate
     - "string"
   * - properties.email
     - socialSecurityNumber.number (Dependant on having wd:Q1273217 in socialSecurityNumber.iso2Letter)
     - "string"
   * - properties.firstname
     - firstname
     - "string"
   * - properties.lastname
     - lastname
     - "string"
   * - properties.zip
     - addresses.postalCode.zipCode
     - "string"


HubSpot Contactcompanyassociation to MemberCare Persons
-------------------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a MemberCare Persons.

Once a link between a HubSpot Contactcompanyassociation and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - MemberCare Persons Property
     - MemberCare Data Type


HubSpot Contactcompanyassociationtype to MemberCare Companycategories
---------------------------------------------------------------------
Every HubSpot Contactcompanyassociationtype will be synchronized with a MemberCare Companycategories.

Once a link between a HubSpot Contactcompanyassociationtype and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociationtype and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociationtype Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


HubSpot Deal to MemberCare Invoices
-----------------------------------
Every HubSpot Deal will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Deal and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - MemberCare Invoices Property
     - MemberCare Data Type


HubSpot Dealcompanyassociation to MemberCare Invoices
-----------------------------------------------------
Every HubSpot Dealcompanyassociation will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Dealcompanyassociation and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - MemberCare Invoices Property
     - MemberCare Data Type


HubSpot Dealcompanyassociationtype to MemberCare Companycategories
------------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a MemberCare Companycategories.

Once a link between a HubSpot Dealcompanyassociationtype and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


HubSpot Dealcontactassociation to MemberCare Invoices
-----------------------------------------------------
Every HubSpot Dealcontactassociation will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Dealcontactassociation and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - MemberCare Invoices Property
     - MemberCare Data Type


HubSpot Dealcontactassociationtype to MemberCare Companycategories
------------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a MemberCare Companycategories.

Once a link between a HubSpot Dealcontactassociationtype and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


HubSpot Lineitem to MemberCare Invoices
---------------------------------------
Every HubSpot Lineitem will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Lineitem and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - properties.description
     - invoiceItems.description
     - "string"
   * - properties.price
     - invoiceItems.unitPrice
     - "string"
   * - properties.quantity
     - invoiceItems.quantity
     - "string"


HubSpot Lineitemdealassociation to MemberCare Invoices
------------------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Lineitemdealassociation and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - toObjectId (Dependant on having wd:Q190581 in sesam_simpleAssociationTypes)
     - id
     - "string"


HubSpot Lineitemdealassociationtype to MemberCare Companycategories
-------------------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a MemberCare Companycategories.

Once a link between a HubSpot Lineitemdealassociationtype and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


HubSpot Lineitemquoteassociation to MemberCare Invoices
-------------------------------------------------------
Every HubSpot Lineitemquoteassociation will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Lineitemquoteassociation and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - toObjectId (Dependant on having wd:Q190581 in sesam_simpleAssociationTypes)
     - id
     - "string"


HubSpot Lineitemquoteassociationtype to MemberCare Companycategories
--------------------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a MemberCare Companycategories.

Once a link between a HubSpot Lineitemquoteassociationtype and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


HubSpot Product to MemberCare Products
--------------------------------------
Every HubSpot Product will be synchronized with a MemberCare Products.

Once a link between a HubSpot Product and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - MemberCare Products Property
     - MemberCare Data Type
   * - properties.name
     - name
     - "string"


HubSpot Quote to MemberCare Invoices
------------------------------------
Every HubSpot Quote will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Quote and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - MemberCare Invoices Property
     - MemberCare Data Type


HubSpot Quotecompanyassociation to MemberCare Invoices
------------------------------------------------------
Every HubSpot Quotecompanyassociation will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Quotecompanyassociation and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - MemberCare Invoices Property
     - MemberCare Data Type


HubSpot Quotecompanyassociationtype to MemberCare Companycategories
-------------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a MemberCare Companycategories.

Once a link between a HubSpot Quotecompanyassociationtype and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


HubSpot Quotecontactassociation to MemberCare Invoices
------------------------------------------------------
Every HubSpot Quotecontactassociation will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Quotecontactassociation and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - MemberCare Invoices Property
     - MemberCare Data Type


HubSpot Quotecontactassociationtype to MemberCare Companycategories
-------------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a MemberCare Companycategories.

Once a link between a HubSpot Quotecontactassociationtype and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


HubSpot Quotedealassociation to MemberCare Invoices
---------------------------------------------------
Every HubSpot Quotedealassociation will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Quotedealassociation and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - toObjectId (Dependant on having wd:Q190581 in sesam_simpleAssociationTypes)
     - id
     - "string"


HubSpot Quotedealassociationtype to MemberCare Companycategories
----------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a MemberCare Companycategories.

Once a link between a HubSpot Quotedealassociationtype and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


HubSpot Quotequotetemplateassociation to MemberCare Invoices
------------------------------------------------------------
Every HubSpot Quotequotetemplateassociation will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Quotequotetemplateassociation and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - toObjectId (Dependant on having wd:Q190581 in sesam_simpleAssociationTypes)
     - id
     - "string"


HubSpot Quotequotetemplateassociationtype to MemberCare Companycategories
-------------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a MemberCare Companycategories.

Once a link between a HubSpot Quotequotetemplateassociationtype and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


HubSpot User to MemberCare Persons
----------------------------------
Every HubSpot User will be synchronized with a MemberCare Persons.

Once a link between a HubSpot User and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - email
     - socialSecurityNumber.number (Dependant on having wd:Q28378282 in socialSecurityNumber.iso2Letter)
     - "string"


HubSpot Company to MemberCare Countries
---------------------------------------
Every HubSpot Company will be synchronized with a MemberCare Countries.

Once a link between a HubSpot Company and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - properties.country
     - name
     - "string"
   * - properties.industry
     - name
     - "string"
   * - properties.state
     - name
     - "string"
   * - properties.type
     - name
     - "string"

