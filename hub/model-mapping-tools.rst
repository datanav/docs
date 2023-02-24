============
Data Mapping
============

Sesam Talk Data Model
---------------------
In this section we will describe how the Sesam Talk data model has been defined and applied, which provides a way for a company to apply their own data model.

Background
^^^^^^^^^^
In order to achieve a well-defined and unambiguous model, the Sesam Talk data model uses the Wikidata model as a base for the definition of items and properties. Items and properties that may provide valuable data across data providers are mapped to the Sesam Talk model. Here the items and properties in Sesam Talk that will be mapped, will inherit the corresponding Q- or P-value identifier from WikiData. This is to ensure a self-documented and standardized model. 
Please see Sesam Talk section for more on which systems are available in the model so far as well as which items and properties have been mapped.

Sesam Talk Definitions
^^^^^^^^^^^^^^^^^^^^^^

* Entity - an object in Sesam Talk containing metadata related to that object, e.g. a contact read from a system ("first_name": "John", "last_name": "Doe")
* Entity type - the type of an entity we get from an API from a provider, e.g. John Doe has a first name and a last name and is therefore a "contact" entity type
* Data type - the data type for a property, e.g. "first_name" and a "last_name" have the data type "string" as they require string values
* Property - a specific property on an entity type, e.g. "first_name"
* Global - a collection of entities across entity types withing the same data domain, e.g. "contact" and "employee" entity type are both withing the "person" domain as they both contain person data.

Columns used for mapping
------------------------

The actual data mapping is done in a table where we map the various types and source properties using the predefined vocabulary and this makes the data model. We use the following columns to define and build the various data types.

.. list-table::
   :header-rows: 1
   :widths: 20, 60

   * - Column name
     - Description
   * - ``System``
     - The source system
   * - ``Type``
     - entity type
   * - ``Name``
     - property name in source system, including full path when nested
   * - ``SubName``
     - property subname in source system
   * - ``Data type``
     - property name in source system
   * - ``Description``
     - description of property from source system
   * - ``Source property``
     - property where we are mapping from, combination of Name and SubName
   * - ``Global``
     - which ``Global`` the property is mapped to
   * - ``FilterValue``
     - if an entity type can be mapped to several ``Globals``, this column can be used to provide a filter on a property that defines which ``Global`` an entity should belong to
   * - ``Mapping``
     - the WikiData label and identifier of the property and global each source property is mapped to
   * - ``Target property``
     - the location of the source property's value when mapped to the Sesam Talk model
   * - ``SubMapping``
     - if additional context is needed, ``SubMapping`` is used
   * - ``SubProperty``
     - the location of the source property's submapped value when mapped to the Sesam Talk model
   * - ``Reference``
     - boolean value to identify references to other entities (namespaced identifier)
   * - ``Constant``
     - defines value of subMapping and is constant
   * - ``Variable``
     - defines value of subMapping based on value of context of data. This is not a constant hence a variable.
   * - ``Master``
     - master is used to set on one of the properties for an entity type to indicate which of the types is master. If an entity is to be added to, for example, global organisation, but also contains properties that are to be distinguished as separate entities in other globals (such as location or classification), one of the properties that indicates the organisation as global must be marked with true for master.
   * - ``Group``
     - used to group which properties belong together if several of the same type are to be separated as separate entities
   * - ``ReadOnly``
     - indicates whether a property is read-only and should only be read into Sesam Talk, and not written
   * - ``ReferenceTo``
     - used to specify the namespace where we create references to other entities

Mapping - Preparations
----------------------

The first step is to define which system contains high value data and are included in core processes in your business. This can be your ERP system, CRM system, HR system, asset management system etc. Defining these systems gives a foundation to defining which core entity types your business has and therefore should be part of your data model.
In the next steps the core entity types get defined and organised into their corresponding globals and the core source properties are mapped into the Sesam Talk model. For the human entity types (```Q5```), `the following model properties <https://docs.sesam.io/talk/entity types/human.html#model-properties>`_ are mapped.
Entities and a set of their properties are then linked to their corresponding global, e.g. ```Q5``` (Human). Each of these ```entities``` has a list of properties linked to them to give context and meaning. So for entities with entity type belonging to the global with entity type Q5, Human, the following properties are linked to it: https://docs.sesam.io/talk/entity types/human.html.

Single value or multi-value fields
----------------------------------

Properties can be either single value or multi value. Those with a single value are fairly easy to map, e.g., an entity with entity type "Human" has the source property "family_name". This is a single value field as there is only one family name; ```family name (P734)```.

Multi-value fields and properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Email address, on the other hand, is a multi-value field. The entity types *customer*, *employee* or *person* can have several types of email addresses such as work email, private email, official email etc. Instead of adding a hierarchy of various emails, we use sub-mapping to say what type of email address is this specific one. That is, we give an entity extra context: which type of email address is this. For this we have used a central property is called ```Type of reference (P3865)```. We add the value of email type in the ```Constant```. Examples of constants for an email address: business (Q4830453) and personal (Q67372736).
An e-mail address is an e-mail address of any type, but we refer to a given e-mail address for example business (Q4830453) or personal (Q67372736).

Each data type needs a unique ID which we in turn use to *merge* entities with in Sesam. We use this property from WIKIDATA: ```identity of subject in context (P4649)``.
To show an example; the entity type Customer has a property named "organisationNumber". This is a unique number which means entity types with the same "organisationNumber" linked to it, can be merged in Sesam as they are the same organisation. For the mapping, the target property becomes P4649. To add more context about this id, we generate a SubProperty called P4649 - P3865 which defines the type of reference and in ```Constant`` we find the specific "organisationNumber" which is ```Norwegian organisation number (Q11994066)```.

Another central property used to add type info on an entity, is called ```instance of (P31)``. In Sesam this type is called rdf:type or $type. The reason for adding this ```instance of (P31)`` on an entity, is to provide context to an entity of what type of data it is. This in turn is useful to use when you need to filter from large datasets. So ```instance of (P31)`` is used to define *the type of the entity* we are talking about. For example, data type Customer can have ```Property Participant (710)``. Mapping PP710 -P31 defines participant is of type. What the type is, is defined in the constant column and could be e.g., vendor (Q1762621) or customer (Q852835). to add type info on an entity.
