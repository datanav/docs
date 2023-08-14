=========================================
Powerofficego to PowerOfficeGov1 Dataflow
=========================================

Generated: 2023-08-14 08:48:58

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to PowerOfficeGov1. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Employee to PowerOfficeGov1 Employee
--------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Employee and a PowerOfficeGov1 Employee must be established.

A Powerofficego Employee will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employee Property
     - PowerOfficeGov1 Employee Property
   * - SocialSecurityNumber
     - SocialSecurityNumber
   * - SocialSecurityNumber
     - nationalIdentityNumber

Once a link between a Powerofficego Employee and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employee and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employee Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type


Powerofficego Product to PowerOfficeGov1 Product
------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Product and a PowerOfficeGov1 Product must be established.

A Powerofficego Product will merge with a PowerOfficeGov1 Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - PowerOfficeGov1 Product Property
   * - id
     - id

Once a link between a Powerofficego Product and a PowerOfficeGov1 Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a PowerOfficeGov1 Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - PowerOfficeGov1 Product Property
     - PowerOfficeGov1 Data Type


Powerofficego Product to PowerOfficeGov1 Productunit
----------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Product and a PowerOfficeGov1 Productunit must be established.

A Powerofficego Product will merge with a PowerOfficeGov1 Productunit if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - PowerOfficeGov1 Productunit Property
   * - unitOfMeasureCode
     - name

Once a link between a Powerofficego Product and a PowerOfficeGov1 Productunit is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a PowerOfficeGov1 Productunit:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - PowerOfficeGov1 Productunit Property
     - PowerOfficeGov1 Data Type


Powerofficego Vatcode to PowerOfficeGov1 Vatcode
------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Vatcode and a PowerOfficeGov1 Vatcode must be established.

A Powerofficego Vatcode will merge with a PowerOfficeGov1 Vatcode if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Vatcode Property
     - PowerOfficeGov1 Vatcode Property
   * - id
     - id

Once a link between a Powerofficego Vatcode and a PowerOfficeGov1 Vatcode is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Vatcode and a PowerOfficeGov1 Vatcode:

.. list-table::
   :header-rows: 1

   * - Powerofficego Vatcode Property
     - PowerOfficeGov1 Vatcode Property
     - PowerOfficeGov1 Data Type

