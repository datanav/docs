=============================
WebCRM to Unieconomy Dataflow
=============================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Organisations to Unieconomy Countries
--------------------------------------------
Every WebCRM Organisations will be synchronized with a Unieconomy Countries.

If a matching Unieconomy Countries already exists, the WebCRM Organisations will be merged with the existing one.
If no matching Unieconomy Countries is found, a new Unieconomy Countries will be created.

A WebCRM Organisations will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - Unieconomy Countries Property
   * - OrganisationCountryData.CodeISO
     - CountryCode

Once a link between a WebCRM Organisations and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - Unieconomy Countries Property
     - Unieconomy Data Type

