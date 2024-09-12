================================
Tidsbanken to Tripletex Dataflow
================================

Generated: 2024-09-12 13:14:11

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Tripletex Contact
--------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a Tripletex Contact must be established.

A Tidsbanken Ansatt will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Tripletex Contact Property
   * - Epost
     - email

Once a link between a Tidsbanken Ansatt and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - Etternavn
     - lastName
     - "string"
   * - Fornavn
     - firstName
     - "string"
   * - Mobil
     - phoneNumberMobile
     - N/A


Tidsbanken Ansatt to Tripletex Customer person
----------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a Tripletex Customer person must be established.

A Tidsbanken Ansatt will merge with a Tripletex Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Tripletex Customer person Property
   * - Epost
     - email

Once a link between a Tidsbanken Ansatt and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Tripletex Customer person Property
     - Tripletex Data Type
   * - Adresse
     - deliveryAddress.addressLine1
     - "string"
   * - Adresse
     - physicalAddress.addressLine1
     - "string"
   * - Adresse
     - postalAddress.addressLine1
     - "string"
   * - Id
     - id
     - "integer"
   * - Mobil
     - phoneNumberMobile
     - "string"
   * - Navn
     - name
     - "string"
   * - Postnummer
     - deliveryAddress.postalCode
     - "string"
   * - Postnummer
     - physicalAddress.postalCode
     - "string"
   * - Postnummer
     - postalAddress.postalCode
     - "string"
   * - Poststed
     - deliveryAddress.city
     - "string"
   * - Poststed
     - physicalAddress.city
     - "string"
   * - Poststed
     - postalAddress.city
     - "string"


Tidsbanken Kunde to Tripletex Customer person
---------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Kunde and a Tripletex Customer person must be established.

A new Tripletex Customer person will be created from a Tidsbanken Kunde if it is connected to a Tidsbanken Prosjekt that is synchronized into Tripletex.

Once a link between a Tidsbanken Kunde and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Tripletex Customer person Property
     - Tripletex Data Type
   * - Gateadresse
     - deliveryAddress.addressLine1
     - "string"
   * - Gateadresse
     - physicalAddress.addressLine1
     - "string"
   * - Gateadresse
     - postalAddress.addressLine1
     - "string"
   * - Id
     - id
     - "integer"
   * - LevPostNr
     - deliveryAddress.postalCode
     - "string"
   * - LevPostNr
     - physicalAddress.postalCode
     - "string"
   * - LevPostNr
     - postalAddress.postalCode
     - "string"
   * - LevPoststed
     - deliveryAddress.city
     - "string"
   * - LevPoststed
     - physicalAddress.city
     - "string"
   * - LevPoststed
     - postalAddress.city
     - "string"
   * - Leveringsadresse
     - deliveryAddress.addressLine1
     - "string"
   * - Leveringsadresse
     - physicalAddress.addressLine1
     - "string"
   * - Leveringsadresse
     - postalAddress.addressLine1
     - "string"
   * - Leveringsadresse2
     - deliveryAddress.addressLine2
     - "string"
   * - Leveringsadresse2
     - physicalAddress.addressLine2
     - "string"
   * - Leveringsadresse2
     - postalAddress.addressLine2
     - "string"
   * - Postadresse
     - deliveryAddress.addressLine2
     - "string"
   * - Postadresse
     - physicalAddress.addressLine2
     - "string"
   * - Postadresse
     - postalAddress.addressLine2
     - "string"
   * - Postnr
     - deliveryAddress.postalCode
     - "string"
   * - Postnr
     - physicalAddress.postalCode
     - "string"
   * - Postnr
     - postalAddress.postalCode
     - "string"
   * - Poststed
     - deliveryAddress.city
     - "string"
   * - Poststed
     - physicalAddress.city
     - "string"
   * - Poststed
     - postalAddress.city
     - "string"


Tidsbanken Ansatt to Tripletex Employee
---------------------------------------
Every Tidsbanken Ansatt will be synchronized with a Tripletex Employee.

If a matching Tripletex Employee already exists, the Tidsbanken Ansatt will be merged with the existing one.
If no matching Tripletex Employee is found, a new Tripletex Employee will be created.

A Tidsbanken Ansatt will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Tripletex Employee Property
   * - Epost
     - email
   * - Id
     - employeeNumber
   * - Personnummer
     - nationalIdentityNumber

Once a link between a Tidsbanken Ansatt and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - Adresse
     - address.addressLine1
     - "string"
   * - Aktiv
     - department.id (Dependant on having wd:Q29415466 in  Dependant on having wd:Q29415492 in  )
     - N/A
   * - Aktiv
     - sesam_employment_status
     - "boolean"
   * - AvdelingId
     - department.id (Dependant on having wd:Q2366457 in  )
     - N/A
   * - Epost
     - email
     - "string"
   * - Etternavn
     - lastName
     - "string"
   * - Fodt
     - dateOfBirth
     - N/A
   * - Fornavn
     - firstName
     - "string"
   * - Id
     - id
     - "integer"
   * - Mobil
     - phoneNumberMobile
     - N/A
   * - Postnummer
     - address.postalCode
     - "string"
   * - Poststed
     - address.city
     - "string"
   * - TlfPrivat
     - phoneNumberHome
     - "string"
   * - sesam_ansattId
     - employeeNumber
     - "string"


Tidsbanken Avdeling to Tripletex Department
-------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Tripletex Department.

If a matching Tripletex Department already exists, the Tidsbanken Avdeling will be merged with the existing one.
If no matching Tripletex Department is found, a new Tripletex Department will be created.

A Tidsbanken Avdeling will merge with a Tripletex Department if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Tripletex Department Property
   * - Id
     - departmentNumber

Once a link between a Tidsbanken Avdeling and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - Avdelingsleder
     - departmentManager.id
     - "string"
   * - Navn
     - name
     - "string"
   * - Synlig
     - isInactive
     - "string"
   * - sesam_avdelingId
     - departmentNumber
     - "string"


Tidsbanken Kunde to Tripletex Customer
--------------------------------------
Every Tidsbanken Kunde will be synchronized with a Tripletex Customer.

If a matching Tripletex Customer already exists, the Tidsbanken Kunde will be merged with the existing one.
If no matching Tripletex Customer is found, a new Tripletex Customer will be created.

A Tidsbanken Kunde will merge with a Tripletex Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Tripletex Customer Property
   * - Epost
     - email
   * - Id
     - customerNumber
   * - Organisasjonsnummer
     - organizationNumber

Once a link between a Tidsbanken Kunde and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - Epost
     - email
     - "string"
   * - Gateadresse
     - deliveryAddress.addressLine1
     - "string"
   * - Gateadresse
     - physicalAddress.addressLine1
     - "string"
   * - Gateadresse
     - postalAddress.addressLine1
     - "string"
   * - Id
     - id
     - "integer"
   * - LevPostNr
     - deliveryAddress.postalCode
     - "string"
   * - LevPostNr
     - physicalAddress.postalCode
     - "string"
   * - LevPostNr
     - postalAddress.postalCode
     - "string"
   * - LevPoststed
     - deliveryAddress.city
     - "string"
   * - LevPoststed
     - physicalAddress.city
     - "string"
   * - LevPoststed
     - postalAddress.city
     - "string"
   * - Leveringsadresse
     - deliveryAddress.addressLine1
     - "string"
   * - Leveringsadresse
     - physicalAddress.addressLine1
     - "string"
   * - Leveringsadresse
     - postalAddress.addressLine1
     - "string"
   * - Leveringsadresse2
     - deliveryAddress.addressLine2
     - "string"
   * - Leveringsadresse2
     - physicalAddress.addressLine2
     - "string"
   * - Leveringsadresse2
     - postalAddress.addressLine2
     - "string"
   * - Mobil
     - phoneNumberMobile
     - "string"
   * - Navn
     - name
     - "string"
   * - Organisasjonsnummer
     - organizationNumber
     - N/A
   * - Postadresse
     - deliveryAddress.addressLine2
     - "string"
   * - Postadresse
     - physicalAddress.addressLine2
     - "string"
   * - Postadresse
     - postalAddress.addressLine2
     - "string"
   * - Postnr
     - deliveryAddress.postalCode
     - "string"
   * - Postnr
     - physicalAddress.postalCode
     - "string"
   * - Postnr
     - postalAddress.postalCode
     - "string"
   * - Poststed
     - deliveryAddress.city
     - "string"
   * - Poststed
     - physicalAddress.city
     - "string"
   * - Poststed
     - postalAddress.city
     - "string"
   * - Telefon
     - phoneNumber
     - "string"
   * - Url
     - website
     - "string"
   * - sesam_kundeId
     - customerNumber
     - "string"


Tidsbanken Prosjekt to Tripletex Project
----------------------------------------
Every Tidsbanken Prosjekt will be synchronized with a Tripletex Project.

Once a link between a Tidsbanken Prosjekt and a Tripletex Project is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Prosjekt and a Tripletex Project:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Prosjekt Property
     - Tripletex Project Property
     - Tripletex Data Type
   * - AnsvarligId
     - projectManager.id
     - "integer"
   * - AvdelingId
     - department.id
     - "integer"
   * - Avsluttet
     - isClosed
     - "string"
   * - AvsluttetDato
     - endDate
     - N/A
   * - InterntProsjekt
     - isInternal
     - "string"
   * - KundeId
     - customer.id
     - "integer"
   * - Navn
     - name
     - "string"
   * - StartDato
     - startDate
     - N/A

