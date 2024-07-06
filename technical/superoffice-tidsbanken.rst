==================================
SuperOffice to Tidsbanken Dataflow
==================================

Generated: 2024-07-06 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Tidsbanken Kunde
---------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Tidsbanken Kunde must be established.

A SuperOffice Contact will merge with a Tidsbanken Kunde if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Tidsbanken Kunde Property
   * - Emails.Value
     - Epost

Once a link between a SuperOffice Contact and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type
   * - Address.Postal.Address1
     - Gateadresse
     - "string"
   * - Address.Postal.Address1
     - Leveringsadresse
     - "string"
   * - Address.Postal.Address1
     - Postadresse
     - "string"
   * - Address.Postal.Address2
     - Gateadresse
     - "string"
   * - Address.Postal.Address2
     - Leveringsadresse2
     - "string"
   * - Address.Postal.Address2
     - Postadresse
     - "string"
   * - Address.Postal.City
     - LevPoststed
     - "string"
   * - Address.Postal.City
     - Poststed
     - "string"
   * - Address.Postal.Zipcode
     - LevPostNr
     - "string"
   * - Address.Postal.Zipcode
     - Postnr
     - "string"
   * - Address.Street.Address1
     - Gateadresse
     - "string"
   * - Address.Street.Address1
     - Leveringsadresse
     - "string"
   * - Address.Street.Address1
     - Postadresse
     - "string"
   * - Address.Street.Address2
     - Gateadresse
     - "string"
   * - Address.Street.Address2
     - Leveringsadresse2
     - "string"
   * - Address.Street.Address2
     - Postadresse
     - "string"
   * - Address.Street.City
     - LevPoststed
     - "string"
   * - Address.Street.City
     - Poststed
     - "string"
   * - Address.Street.Zipcode
     - LevPostNr
     - "string"
   * - Address.Street.Zipcode
     - Postnr
     - "string"
   * - ContactId
     - Id
     - "string"
   * - Emails.Value
     - Epost
     - "string"
   * - Name
     - Navn
     - "string"
   * - OrgNr (Dependant on having NO in Country.TwoLetterISOCountryDependant on having NO in Country.TwoLetterISOCountryDependant on having wd:Q11994066 in Country.TwoLetterISOCountryDependant on having wd:Q11994066 in Country.TwoLetterISOCountry)
     - Organisasjonsnummer
     - "string"
   * - OrgNr (Dependant on having wd:Q852835 in Country.TwoLetterISOCountry)
     - sesam_kundeId
     - "string"
   * - Phones.Value
     - Telefon
     - "string"
   * - Urls.Value
     - Url
     - "string"


SuperOffice Person to Tidsbanken Ansatt
---------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Tidsbanken Ansatt must be established.

A SuperOffice Person will merge with a Tidsbanken Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Tidsbanken Ansatt Property
   * - Emails.Value
     - Epost

Once a link between a SuperOffice Person and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
   * - Address.Street.Address1
     - Adresse
     - "string"
   * - Address.Street.City
     - Poststed
     - "string"
   * - Address.Street.Zipcode
     - Postnummer
     - "string"
   * - BirthDate
     - Fodt
     - "string"
   * - Contact.ContactId
     - AvdelingId
     - "string"
   * - Contact.ContactId
     - Tittel
     - "string"
   * - Contact.ContactId
     - sesam_ansattId
     - "integer"
   * - Firstname
     - Fornavn
     - "string"
   * - Lastname
     - Etternavn
     - "string"
   * - MobilePhones.Value
     - Mobil
     - "string"
   * - PersonId
     - Id
     - "integer"
   * - PrivatePhones.Value
     - TlfPrivat
     - "string"


SuperOffice User to Tidsbanken Ansatt
-------------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a Tidsbanken Ansatt must be established.

A SuperOffice User will merge with a Tidsbanken Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Tidsbanken Ansatt Property
   * - personEmail
     - Epost

Once a link between a SuperOffice User and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
   * - contactId
     - AvdelingId
     - "string"
   * - contactId
     - Tittel
     - "string"
   * - contactId
     - sesam_ansattId
     - "integer"
   * - firstName
     - Fornavn
     - "string"
   * - lastName
     - Etternavn
     - "string"
   * - personEmail
     - Epost
     - "string"


SuperOffice Project to Tidsbanken Prosjekt
------------------------------------------
Every SuperOffice Project will be synchronized with a Tidsbanken Prosjekt.

Once a link between a SuperOffice Project and a Tidsbanken Prosjekt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Project and a Tidsbanken Prosjekt:

.. list-table::
   :header-rows: 1

   * - SuperOffice Project Property
     - Tidsbanken Prosjekt Property
     - Tidsbanken Data Type
   * - Associate.AssociateId
     - AnsvarligId
     - "integer"
   * - Name
     - Navn
     - "string"

