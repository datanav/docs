================================
Tripletex to Tidsbanken Dataflow
================================

Generated: 2024-09-21 00:01:13

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to Tidsbanken Ansatt
--------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a Tidsbanken Ansatt must be established.

A Tripletex Contact will merge with a Tidsbanken Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Tidsbanken Ansatt Property
   * - email
     - Epost

Once a link between a Tripletex Contact and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
   * - firstName
     - Fornavn
     - "string"
   * - lastName
     - Etternavn
     - "string"
   * - phoneNumberMobile
     - Mobil
     - "string"


Tripletex Customer to Tidsbanken Ansatt
---------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Tidsbanken Ansatt must be established.

A Tripletex Customer will merge with a Tidsbanken Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Tidsbanken Ansatt Property
   * - email
     - Epost

Once a link between a Tripletex Customer and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
   * - deliveryAddress.addressLine1
     - Adresse
     - "string"
   * - deliveryAddress.city
     - Poststed
     - "string"
   * - deliveryAddress.postalCode
     - Postnummer
     - "string"
   * - id
     - Id
     - "integer"
   * - name
     - Navn
     - "string"
   * - phoneNumberMobile
     - Mobil
     - "string"
   * - physicalAddress.addressLine1
     - Adresse
     - "string"
   * - physicalAddress.city
     - Poststed
     - "string"
   * - physicalAddress.postalCode
     - Postnummer
     - "string"
   * - postalAddress.addressLine1
     - Adresse
     - "string"
   * - postalAddress.city
     - Poststed
     - "string"
   * - postalAddress.postalCode
     - Postnummer
     - "string"


Tripletex Customer to Tidsbanken Kunde
--------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Tidsbanken Kunde must be established.

A new Tidsbanken Kunde will be created from a Tripletex Customer if it is connected to a Tripletex Project that is synchronized into Tidsbanken.

A Tripletex Customer will merge with a Tidsbanken Kunde if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Tidsbanken Kunde Property
   * - email
     - Epost
   * - customerNumber
     - Id
   * - organizationNumber
     - Organisasjonsnummer

Once a link between a Tripletex Customer and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type
   * - customerNumber
     - sesam_kundeId
     - "string"
   * - deliveryAddress.addressLine1
     - Gateadresse
     - "string"
   * - deliveryAddress.addressLine1
     - Leveringsadresse
     - "string"
   * - deliveryAddress.addressLine2
     - Leveringsadresse2
     - "string"
   * - deliveryAddress.addressLine2
     - Postadresse
     - "string"
   * - deliveryAddress.city
     - LevPoststed
     - "string"
   * - deliveryAddress.city
     - Poststed
     - "string"
   * - deliveryAddress.postalCode
     - LevPostNr
     - "string"
   * - deliveryAddress.postalCode
     - Postnr
     - "string"
   * - email
     - Epost
     - "string"
   * - id
     - Id
     - "string"
   * - name
     - Navn
     - "string"
   * - organizationNumber
     - Organisasjonsnummer
     - "string"
   * - phoneNumber
     - Telefon
     - "string"
   * - phoneNumberMobile
     - Mobil
     - "string"
   * - physicalAddress.addressLine1
     - Gateadresse
     - "string"
   * - physicalAddress.addressLine1
     - Leveringsadresse
     - "string"
   * - physicalAddress.addressLine2
     - Leveringsadresse2
     - "string"
   * - physicalAddress.addressLine2
     - Postadresse
     - "string"
   * - physicalAddress.city
     - LevPoststed
     - "string"
   * - physicalAddress.city
     - Poststed
     - "string"
   * - physicalAddress.postalCode
     - LevPostNr
     - "string"
   * - physicalAddress.postalCode
     - Postnr
     - "string"
   * - postalAddress.addressLine1
     - Gateadresse
     - "string"
   * - postalAddress.addressLine1
     - Leveringsadresse
     - "string"
   * - postalAddress.addressLine2
     - Leveringsadresse2
     - "string"
   * - postalAddress.addressLine2
     - Postadresse
     - "string"
   * - postalAddress.city
     - LevPoststed
     - "string"
   * - postalAddress.city
     - Poststed
     - "string"
   * - postalAddress.postalCode
     - LevPostNr
     - "string"
   * - postalAddress.postalCode
     - Postnr
     - "string"
   * - website
     - Url
     - "string"


Tripletex Department to Tidsbanken Avdeling
-------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a Tidsbanken Avdeling must be established.

A new Tidsbanken Avdeling will be created from a Tripletex Department if it is connected to a Tripletex Contact, Project, Employee, or Customer-person that is synchronized into Tidsbanken.

A Tripletex Department will merge with a Tidsbanken Avdeling if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Tidsbanken Avdeling Property
   * - departmentNumber
     - Id

Once a link between a Tripletex Department and a Tidsbanken Avdeling is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Tidsbanken Avdeling:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Tidsbanken Avdeling Property
     - Tidsbanken Data Type
   * - departmentNumber
     - sesam_avdelingId
     - "string"
   * - isInactive
     - Synlig
     - "string"
   * - name
     - Navn
     - "string"


Tripletex Employee to Tidsbanken Ansatt
---------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a Tidsbanken Ansatt must be established.

A Tripletex Employee will merge with a Tidsbanken Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Tidsbanken Ansatt Property
   * - email
     - Epost
   * - employeeNumber
     - Id
   * - nationalIdentityNumber
     - Personnummer

Once a link between a Tripletex Employee and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
   * - address.addressLine1
     - Adresse
     - "string"
   * - address.city
     - Poststed
     - "string"
   * - address.postalCode
     - Postnummer
     - "string"
   * - dateOfBirth
     - Fodt
     - "string"
   * - department.id (Dependant on having wd:Q29415492 in  )
     - Aktiv
     - "boolean"
   * - department.id (Dependant on having wd:Q2366457 in  )
     - AvdelingId
     - "string"
   * - email
     - Epost
     - "string"
   * - employeeNumber
     - sesam_ansattId
     - "integer"
   * - firstName
     - Fornavn
     - "string"
   * - id
     - Id
     - "integer"
   * - lastName
     - Etternavn
     - "string"
   * - phoneNumberHome
     - TlfPrivat
     - "string"
   * - phoneNumberMobile
     - Mobil
     - "string"
   * - sesam_employment_status
     - Aktiv
     - "boolean"


Tripletex Supplier to Tidsbanken Kunde
--------------------------------------
Before any synchronization can take place, a link between a Tripletex Supplier and a Tidsbanken Kunde must be established.

A Tripletex Supplier will merge with a Tidsbanken Kunde if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - Tidsbanken Kunde Property
   * - email
     - Epost
   * - organizationNumber
     - Organisasjonsnummer

Once a link between a Tripletex Supplier and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type
   * - deliveryAddress.addressLine1
     - Gateadresse
     - "string"
   * - deliveryAddress.addressLine1
     - Leveringsadresse
     - "string"
   * - deliveryAddress.addressLine2
     - Leveringsadresse2
     - "string"
   * - deliveryAddress.addressLine2
     - Postadresse
     - "string"
   * - deliveryAddress.city
     - LevPoststed
     - "string"
   * - deliveryAddress.city
     - Poststed
     - "string"
   * - deliveryAddress.postalCode
     - LevPostNr
     - "string"
   * - deliveryAddress.postalCode
     - Postnr
     - "string"
   * - email
     - Epost
     - "string"
   * - id
     - Id
     - "string"
   * - name
     - Navn
     - "string"
   * - organizationNumber
     - Organisasjonsnummer
     - "string"
   * - phoneNumber
     - Telefon
     - "string"
   * - phoneNumberMobile
     - Mobil
     - "string"
   * - physicalAddress.addressLine1
     - Gateadresse
     - "string"
   * - physicalAddress.addressLine1
     - Leveringsadresse
     - "string"
   * - physicalAddress.addressLine2
     - Leveringsadresse2
     - "string"
   * - physicalAddress.addressLine2
     - Postadresse
     - "string"
   * - physicalAddress.city
     - LevPoststed
     - "string"
   * - physicalAddress.city
     - Poststed
     - "string"
   * - physicalAddress.postalCode
     - LevPostNr
     - "string"
   * - physicalAddress.postalCode
     - Postnr
     - "string"
   * - postalAddress.addressLine1
     - Gateadresse
     - "string"
   * - postalAddress.addressLine1
     - Leveringsadresse
     - "string"
   * - postalAddress.addressLine2
     - Leveringsadresse2
     - "string"
   * - postalAddress.addressLine2
     - Postadresse
     - "string"
   * - postalAddress.city
     - LevPoststed
     - "string"
   * - postalAddress.city
     - Poststed
     - "string"
   * - postalAddress.postalCode
     - LevPostNr
     - "string"
   * - postalAddress.postalCode
     - Postnr
     - "string"
   * - url
     - Url
     - "string"


Tripletex Customer (organisation data) to Tidsbanken Kunde
----------------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Tidsbanken Kunde.

Once a link between a Tripletex Customer (organisation data) and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer (organisation data) and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer (organisation data) Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type
   * - deliveryAddress.addressLine1
     - Gateadresse
     - "string"
   * - deliveryAddress.addressLine1
     - Leveringsadresse
     - "string"
   * - deliveryAddress.addressLine2
     - Leveringsadresse2
     - "string"
   * - deliveryAddress.addressLine2
     - Postadresse
     - "string"
   * - deliveryAddress.city
     - LevPoststed
     - "string"
   * - deliveryAddress.city
     - Poststed
     - "string"
   * - deliveryAddress.postalCode
     - LevPostNr
     - "string"
   * - deliveryAddress.postalCode
     - Postnr
     - "string"
   * - id
     - Id
     - "string"
   * - physicalAddress.addressLine1
     - Gateadresse
     - "string"
   * - physicalAddress.addressLine1
     - Leveringsadresse
     - "string"
   * - physicalAddress.addressLine2
     - Leveringsadresse2
     - "string"
   * - physicalAddress.addressLine2
     - Postadresse
     - "string"
   * - physicalAddress.city
     - LevPoststed
     - "string"
   * - physicalAddress.city
     - Poststed
     - "string"
   * - physicalAddress.postalCode
     - LevPostNr
     - "string"
   * - physicalAddress.postalCode
     - Postnr
     - "string"
   * - postalAddress.addressLine1
     - Gateadresse
     - "string"
   * - postalAddress.addressLine1
     - Leveringsadresse
     - "string"
   * - postalAddress.addressLine2
     - Leveringsadresse2
     - "string"
   * - postalAddress.addressLine2
     - Postadresse
     - "string"
   * - postalAddress.city
     - LevPoststed
     - "string"
   * - postalAddress.city
     - Poststed
     - "string"
   * - postalAddress.postalCode
     - LevPostNr
     - "string"
   * - postalAddress.postalCode
     - Postnr
     - "string"


Tripletex Customer to Tidsbanken Kunde
--------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Tidsbanken Kunde.

Once a link between a Tripletex Customer and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type


Tripletex Department to Tidsbanken Avdeling
-------------------------------------------
Every Tripletex Department will be synchronized with a Tidsbanken Avdeling.

Once a link between a Tripletex Department and a Tidsbanken Avdeling is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Tidsbanken Avdeling:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Tidsbanken Avdeling Property
     - Tidsbanken Data Type


Tripletex Employee to Tidsbanken Ansatt
---------------------------------------
Every Tripletex Employee will be synchronized with a Tidsbanken Ansatt.

Once a link between a Tripletex Employee and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
   * - email
     - Epost
     - "string"


Tripletex Project to Tidsbanken Prosjekt
----------------------------------------
Every Tripletex Project will be synchronized with a Tidsbanken Prosjekt.

Once a link between a Tripletex Project and a Tidsbanken Prosjekt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a Tidsbanken Prosjekt:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     - Tidsbanken Prosjekt Property
     - Tidsbanken Data Type
   * - customer.id
     - KundeId
     - "string"
   * - department.id
     - AvdelingId
     - "string"
   * - endDate
     - AvsluttetDato
     - N/A
   * - isClosed
     - Avsluttet
     - "string"
   * - isInternal
     - InterntProsjekt
     - "string"
   * - name
     - Navn
     - "string"
   * - projectManager.id
     - AnsvarligId
     - "integer"
   * - startDate
     - StartDato
     - N/A

