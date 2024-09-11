==========================
WebCRM to HubSpot Dataflow
==========================

Generated: 2024-09-11 07:56:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Organisations to Hubspot Company
---------------------------------------
Every Webcrm Organisations will be synchronized with a Hubspot Company.

Once a link between a Webcrm Organisations and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Organisations and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Webcrm Organisations Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - OrganisationCompanyDescription
     - properties.description
     - "string"
   * - OrganisationName
     - properties.name
     - "string"
   * - OrganisationTelephone
     - properties.phone
     - "string"


Webcrm Persons to Hubspot Contact
---------------------------------
Every Webcrm Persons will be synchronized with a Hubspot Contact.

Once a link between a Webcrm Persons and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Persons and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Webcrm Persons Property
     - Hubspot Contact Property
     - Hubspot Data Type
   * - PersonDirectPhone
     - properties.phone
     - "string"
   * - PersonFirstName
     - properties.firstname
     - "string"
   * - PersonLastName
     - properties.lastname
     - "string"
   * - PersonMobilePhone
     - properties.mobilephone
     - "string"
   * - document_number
     - properties.date_of_birth
     - "string"


Webcrm Users to Hubspot Contact
-------------------------------
Every Webcrm Users will be synchronized with a Hubspot Contact.

Once a link between a Webcrm Users and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Users and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Webcrm Users Property
     - Hubspot Contact Property
     - Hubspot Data Type
   * - UserMobilePhone
     - properties.mobilephone
     - "string"
   * - UserTelephone
     - properties.phone
     - "string"


WebCRM Opportunities to HubSpot Deal
------------------------------------
Every WebCRM Opportunities will be synchronized with a HubSpot Deal.

Once a link between a WebCRM Opportunities and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Opportunities and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - WebCRM Opportunities Property
     - HubSpot Deal Property
     - HubSpot Data Type
   * - OpportunityCurrencyName
     - properties.deal_currency_code
     - "string"
   * - OpportunityCurrencySymbol
     - properties.description
     - "string"


WebCRM Products to HubSpot Product
----------------------------------
Every WebCRM Products will be synchronized with a HubSpot Product.

Once a link between a WebCRM Products and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - HubSpot Product Property
     - HubSpot Data Type
   * - ProductCostPrice
     - properties.hs_cost_of_goods_sold
     - "string"
   * - ProductPrice
     - properties.price
     - "string"


WebCRM Quotationline to HubSpot Lineitem
----------------------------------------
Every WebCRM Quotationline will be synchronized with a HubSpot Lineitem.

Once a link between a WebCRM Quotationline and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - HubSpot Lineitem Property
     - HubSpot Data Type


WebCRM Users to HubSpot User
----------------------------
Every WebCRM Users will be synchronized with a HubSpot User.

Once a link between a WebCRM Users and a HubSpot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Users and a HubSpot User:

.. list-table::
   :header-rows: 1

   * - WebCRM Users Property
     - HubSpot User Property
     - HubSpot Data Type
   * - UserEmail
     - email
     - "string"

