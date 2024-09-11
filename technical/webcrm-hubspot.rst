==========================
WebCRM to Hubspot Dataflow
==========================

Generated: 2024-09-11 07:47:14

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


WebCRM Opportunities to Hubspot Deal
------------------------------------
Every WebCRM Opportunities will be synchronized with a Hubspot Deal.

Once a link between a WebCRM Opportunities and a Hubspot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Opportunities and a Hubspot Deal:

.. list-table::
   :header-rows: 1

   * - WebCRM Opportunities Property
     - Hubspot Deal Property
     - Hubspot Data Type
   * - OpportunityCurrencyName
     - properties.deal_currency_code
     - "string"
   * - OpportunityCurrencySymbol
     - properties.description
     - "string"


WebCRM Products to Hubspot Product
----------------------------------
Every WebCRM Products will be synchronized with a Hubspot Product.

Once a link between a WebCRM Products and a Hubspot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a Hubspot Product:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - Hubspot Product Property
     - Hubspot Data Type
   * - ProductCostPrice
     - properties.hs_cost_of_goods_sold
     - "string"
   * - ProductPrice
     - properties.price
     - "string"


WebCRM Quotationline to Hubspot Lineitem
----------------------------------------
Every WebCRM Quotationline will be synchronized with a Hubspot Lineitem.

Once a link between a WebCRM Quotationline and a Hubspot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a Hubspot Lineitem:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - Hubspot Lineitem Property
     - Hubspot Data Type


WebCRM Users to Hubspot User
----------------------------
Every WebCRM Users will be synchronized with a Hubspot User.

Once a link between a WebCRM Users and a Hubspot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Users and a Hubspot User:

.. list-table::
   :header-rows: 1

   * - WebCRM Users Property
     - Hubspot User Property
     - Hubspot Data Type
   * - UserEmail
     - email
     - "string"

