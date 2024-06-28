===========================
Zendesk to ZohoCRM Dataflow
===========================

Generated: 2024-06-28 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to ZohoCRM Account
----------------------------------------
Every Zendesk Organizations will be synchronized with a ZohoCRM Account.

Once a link between a Zendesk Organizations and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - name
     - Account_Name
     - "string"
   * - url
     - Website
     - "string"

