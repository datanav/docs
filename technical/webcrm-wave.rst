=======================
WebCRM to Wave Dataflow
=======================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Organisations to Wave Country
------------------------------------
Every WebCRM Organisations will be synchronized with a Wave Country.

If a matching Wave Country already exists, the WebCRM Organisations will be merged with the existing one.
If no matching Wave Country is found, a new Wave Country will be created.

A WebCRM Organisations will merge with a Wave Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - Wave Country Property
   * - OrganisationCountryData.CodeISO
     - code

Once a link between a WebCRM Organisations and a Wave Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a Wave Country:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - Wave Country Property
     - Wave Data Type


WebCRM Products to Wave Product
-------------------------------
Every WebCRM Products will be synchronized with a Wave Product.

Once a link between a WebCRM Products and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a Wave Product:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - Wave Product Property
     - Wave Data Type
   * - ProductPrice
     - unitPrice
     - "string"


WebCRM Users to Wave User
-------------------------
Every WebCRM Users will be synchronized with a Wave User.

Once a link between a WebCRM Users and a Wave User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Users and a Wave User:

.. list-table::
   :header-rows: 1

   * - WebCRM Users Property
     - Wave User Property
     - Wave Data Type

