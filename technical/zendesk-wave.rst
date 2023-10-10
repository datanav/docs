========================
Zendesk to Wave Dataflow
========================

Generated: 2023-10-10 20:59:49

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organisations to Wave Customer person
---------------------------------------------
Before any synchronization can take place, a link between a Zendesk Organisations and a Wave Customer person must be established.

A new Wave Customer person will be created from a Zendesk Organisations if it is connected to a Zendesk Users, or Organisations that is synchronized into Wave.

Once a link between a Zendesk Organisations and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organisations and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Zendesk Organisations Property
     - Wave Customer person Property
     - Wave Data Type


Zendesk Organisations to Wave Customer
--------------------------------------
Every Zendesk Organisations will be synchronized with a Wave Customer.

Once a link between a Zendesk Organisations and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organisations and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Zendesk Organisations Property
     - Wave Customer Property
     - Wave Data Type
   * - name
     - name
     - "if","or","is-empty","_."],"eq","","_."]],"-","_."]
   * - url
     - website
     - "string"


Zendesk Organizations to Wave Customer person
---------------------------------------------
Before any synchronization can take place, a link between a Zendesk Organizations and a Wave Customer person must be established.

A new Wave Customer person will be created from a Zendesk Organizations if it is connected to a Zendesk Users, or Organisations that is synchronized into Wave.

Once a link between a Zendesk Organizations and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - Wave Customer person Property
     - Wave Data Type


Zendesk Organizations to Wave Customer
--------------------------------------
Before any synchronization can take place, a link between a Zendesk Organizations and a Wave Customer must be established.

A new Wave Customer will be created from a Zendesk Organizations if it is connected to a Zendesk Users, or Organisations that is synchronized into Wave.

Once a link between a Zendesk Organizations and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - Wave Customer Property
     - Wave Data Type


Zendesk Users to Wave Customer
------------------------------
Every Zendesk Users will be synchronized with a Wave Customer.

Once a link between a Zendesk Users and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Wave Customer Property
     - Wave Data Type

