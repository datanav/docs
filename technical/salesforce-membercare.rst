=================================
Salesforce to MemberCare Dataflow
=================================

Generated: 2024-09-25 00:34:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to MemberCare Countries
------------------------------------------
Every Salesforce Contact will be synchronized with a MemberCare Countries.

Once a link between a Salesforce Contact and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - MailingCountry
     - name
     - "string"


Salesforce Invoice to MemberCare Invoices
-----------------------------------------
Every Salesforce Invoice will be synchronized with a MemberCare Invoices.

Once a link between a Salesforce Invoice and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoice and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoice Property
     - MemberCare Invoices Property
     - MemberCare Data Type


Salesforce Order to MemberCare Countries
----------------------------------------
Every Salesforce Order will be synchronized with a MemberCare Countries.

Once a link between a Salesforce Order and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - BillingCountry
     - name
     - "string"
   * - BillingCountryCode
     - iso2Letter
     - "string"
   * - ShippingCountry
     - name
     - "string"
   * - ShippingCountryCode
     - iso2Letter
     - "string"


Salesforce Order to MemberCare Invoices
---------------------------------------
Every Salesforce Order will be synchronized with a MemberCare Invoices.

Once a link between a Salesforce Order and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - MemberCare Invoices Property
     - MemberCare Data Type


Salesforce Organization to MemberCare Companies
-----------------------------------------------
Every Salesforce Organization will be synchronized with a MemberCare Companies.

Once a link between a Salesforce Organization and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - MemberCare Companies Property
     - MemberCare Data Type


Salesforce Quote to MemberCare Countries
----------------------------------------
Every Salesforce Quote will be synchronized with a MemberCare Countries.

Once a link between a Salesforce Quote and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - BillingCountry
     - name
     - "string"
   * - BillingCountryCode
     - iso2Letter
     - "string"
   * - ShippingCountry
     - name
     - "string"
   * - ShippingCountryCode
     - iso2Letter
     - "string"


Salesforce Quote to MemberCare Invoices
---------------------------------------
Every Salesforce Quote will be synchronized with a MemberCare Invoices.

Once a link between a Salesforce Quote and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - MemberCare Invoices Property
     - MemberCare Data Type


Salesforce User to MemberCare Countries
---------------------------------------
Every Salesforce User will be synchronized with a MemberCare Countries.

Once a link between a Salesforce User and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - Country
     - name
     - "string"
   * - CountryCode
     - iso2Letter
     - "string"

