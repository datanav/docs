.. _getting-started:

===============
Getting started
===============


.. contents:: Table of Contents
   :depth: 2
   :local:


Introduction
------------
Welcome to this introduction to Sesam! This is a basic course that will guide you through what Sesam is, what it does and how it works.

Sesam is an Integration Platform that uses a unique Datahub approach for collection, connecting and sharing of data. The platform is optimized for collecting or receiving data from source systems, transforming data and pushing or providing data to target systems.

If you want to jump straight into Sesam and get hands-on, you can go right  to the :ref:`Labs section <getting-started-labs>`.


.. _getting-started-setting-up-our-sesam-node:

Setting up our Sesam instance
-----------------------------
You must sign up using the `Sesam Portal <https://portal.sesam.io/unified/auth/login?redirect=dashboard>`__ to purchase new or access existing Sesam instances. The default instance type is cloud based, but it's also possible to install Sesam on-premise or in a local cloud environment. If you consider this option, please be free to contact us on info@sesam.io for further information). This document assumes a cloud based installation. You can also access an existing Sesam instance by registering in the `Sesam Portal <https://portal.sesam.io/unified/auth/login?redirect=dashboard>`__ and obtaining an invitation from someone with management permissions for the existing installation. 

The following guide requires the use of Python 3.5.x/3.4.x and a Git client.

.. _getting-started-sign-up:

Sign up
=======

Go to the `Sesam Portal <https://portal.sesam.io/unified/auth/login?redirect=dashboard>`__ and sign up.

Once you've signed up you'll see this page. Click on Request private trial.

.. image:: images/getting-started/dashboard-view.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Once you get the access from the Sesam team you'll get your own Dev Node card in the Dashboard.

.. _getting-started-upload-config:

Upload config
=============

Please note that uploading a config as described below **will overwrite** any config already on the node. You should have a node dedicated for the purpose if you are going set it up for this guide and its labs. 

Download the :download:`getting-started-config.json<files/getting-started-config.json>` and save it locally on your computer.

Go to your 'Dev Node' on the Sesam portal. Click on **Datahub** in the left menu and select the **Tools tab**.

.. image:: images/getting-started/importdata.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Upload the getting-started-config.json file through the drag & drop interface. Then go to the **Variables** tab and paste the below code as environment variables.

::

  {
    "node-env": "test",
    "pump-mode": "manual",
    "udir-baseurl": "https://data-nxr-fellestjeneste.udir.no/api/%s"
  }

You should now have several pipes available in the **pipes** tab. Select all pipes and click the **Enable** and **Start** buttons. This will first populate the input pipes' datasets with test data and then subsecuently the rest of the pipes will run to make the data flow downstream and populate the node. You can click on a pipe in the list to see details on how it's configured.

Config contents
^^^^^^^^^^^^^^^

The config, and now our node, contains seven input pipes. Five of them have embedded person data, one has postal codes and the last one has embedded orders from a webshop. In addition there is a a merge pipe for person data, two global pipes, and example pipes for modelling and exporting person address data. Have a look at how the pipes are connected by navigating between them through their Graph-tabs. The "merged-person" pipe is a good place to start.

.. _getting-started-sesam-overview:

Sesam overview
--------------
We will now give a short overview of the Sesam machinery and the Sesam portal, before we start learning and applying the different concepts. 

In the image above we see five main tabs under the "Training Node" section on the left-hand side. The **Overview** tab shows the current systems you have active, as well as their corresponding inbound and outbound pipes. The :ref:`Datasets <concepts-datasets>`  tab shows the datasets you are currently using is this particular node. The tab :ref:`Pipes <concepts-pipes>` displays the different pipes you have created in your node and the tab :ref:`Systems <concepts-systems>` displays the different :ref:`microservices <getting-started-microservices>` and source systems you employ. The tab **Flows** gives you an overview of your pipes and their connections to other pipes and systems.

The following picture shows the general setup of a Sesam node.


.. image:: images/getting-started/sesam_overview.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

The data is supplied to our pipe via different :ref:`sources <concepts-sources>`. These sources might be databases such as SQL or CSV files. Sometimes, the data available might not be compatible with the Sesam requirements, or you might wish to extract data from an API. The Python scrips performing these tasks are called microservices, and they act as **Systems** in the Sesam node. Since not all sources have their data updated at the same time, every pipe has a :ref:`pump <concepts-pumps>` which tells the pipe how often to run send the data from the source to a :ref:`sink <concepts-sinks>`. A **Sink** writes the final result to a target.  

The picture below shows the different tabs when working on a pipe.   

.. image:: images/getting-started/pipe_tabs.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

The first five tabs are the most used ones, and the ones we will focus on in this section.

The **Dashboard** tab gives you an overview of the different pipes connected to this specific pipe. The **Config** tab displays the **DTL** code in which we transform the data into the performed format and setup. The **Input** and **Output** tabs shows the data before and after being sent through the pipe, respectively. The **Execution log** is a helpful tool when debugging your code. This tab will display the different error messages. 

.. _getting-started-glossary:

Glossary
========
:ref:`Datasets <concepts-datasets>`: Sesam stores its data as datasets consisting of entities. Datasets are used as sources for data transformation and stored as new datasets and sources for delivering data to target systems (endpoints).

:doc:`Entities <entitymodel>`: Sesam uses an entity data model as the core representation of data. Each entity is a dictionary of key-value pairs. Each key is a string and the value can be either a literal value, a list or another dictionary.

:ref:`Pipes <concepts-pipes>`: Defines the flow of data in Sesam. They consist of a source and can also have a list of transformations and a sink. In addition, every pipe has a pump that is scheduled to run at selected intervals and pull data entities from the source, through the transformations and put the results into the sink.

:ref:`Pumps <concepts-pumps>`: A scheduler that handles the mechanics of sending data from a source to a sink. It runs periodically or on a 'cron' schedule and reads entities from a data source and writes them to a data sink.

:ref:`Sinks <concepts-sinks>`: Sinks are at the receiving end of pipes and are responsible for writing entities into an internal dataset or a target system.

:ref:`Sources <concepts-sources>`: Sources consist of data entities and they come in many different formats. A source can provide data as datasets, SQL databases, CSV-files, RDF files such as XML, JSON data, REST APIs and others.

:ref:`Systems <concepts-systems>`: A system component represents a computer system that can provide data entities. Its task is to provide common properties and services that can be used by several data sources, such as connection pooling, authentication settings, communication protocol settings and so on.

:ref:`Transformations <concepts-transforms>`: These are described using the Data Transformation Language (DTL). It is here you transform your data from many datasets to construct new entities into new datasets.


.. _getting-started-naming-conventions:

Naming conventions
==================
To ensure we have a structured set of pipes that stay manageable in a bigger system we need to stick to a convention when naming them. Below is our recommended way of naming pipes.

General rules
^^^^^^^^^^^^^
  * Lower case letters
  * Use dash **-** as delimiter

Systems
^^^^^^^
  * Name the system after the service you integrate with, not the technology used (e.g. **salesforce** instead of **mysql**).
  * If multiple systems are required to talk to a system, postfixc them with a qualifier (e.g. **salesforce-out**).

Pipes
^^^^^
  * Name input pipes with the system they read from, and postfix with the type of content (e.g. **salesforce-sale**).
  * Do not use plural names (e.g. **crm-store**, not **crm-stores**).
  * Prefix merge pipes with **merged-** (e.g. **merged-person**).
  * Prefix global pipes with **global-** (e.g. **global-person**).
  * Name intermediate output pipes with the type of the content and the name of the system to send to (e.g. **sale-bigquery**).
  * Name outgoing pipes by postfixing the intermediate output with **-endpoint** (e.g. **sale-bigquery-endpoint**).

Datasets
^^^^^^^^
  * Name them the same as the pipe that produced it (the default).
  
.. _getting-started-pipes:

Pipes
-----
In this section we will go further into what pipes are, how they work and what we can do with them. 

When we analyse the different data available to us, we discover many opportunities to use it and increase its value. For example, we might not have the need for all of it. Some of that data might be abundant due to multiple occurrences, i.e. the name of an employee occurring in several sources. Some data might have to be split up into different categories, i.e. the personal vs public information of an employee. In other instances we wish to display all the data about a specific object in one place, thus we need to join data from different sources, or enrich data either by adding new properties, or by adding properties existing in different datasets. The pipes are responsible for the transformation of the source data (either from one or several sources) from one setup to another, with the purpose of adding structure to the data. These pipes generate new datasets with new and transformed data ready to be used by other systems.

.. image:: images/getting-started/pipe-struckture.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

As seen above a pipe in Sesam typically consists of five blocks and each block is available as a template to make writing pipes easier and quicker. For source and targets we can choose available systems and press replace to add values to pipe. Same with pump and transforms.

.. image:: images/getting-started/templates.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

The data is typically structured as a list of entities. An entity is a dictionary with key-value pairs and is identified through its '_id' tag. This data might be a list of employees, with the '_id' tag corresponding to their personal employee number.  

For more details on how to use the templates when making a new pipe from scratch, please click :ref:`here <management-studio-new-pipe>`.

.. _getting-started-basic-dtl-functions:

Basic DTL and functions
=======================
Sesam utilizes :ref:`DTL <concepts-dtl>` (Data Transformation Language) which enables the user to easily apply logical operations on the data. In this section we will go through the most common functions available in DTL. For a more extensive walk-through, visit the :ref:`DTL reference guide <DTLReferenceGuide>`.

DTL scripts are written inside the config tab when selecting a pipe in your Sesam node. The scripts consist of five sections: 

  * **System**: We initialize the DTL scripts in Sesam by specifying the **_id** and **type** of the script. The **_id** is the name of the script, and the type is simply just **pipe**.
  * **Provider**: We need to tell DTL which source/sources to get the data from. 
  * **Transform**: Next we need to specify the rules with which we wish to transform the data.
  * **Pump**: We need to add a pump in order to schedule the pumping of data from a source to a **Sink**.
  * **Sink**: Finally we need to specify a **Sink** which writes the data to the target.

Next, let us briefly explain key-value pair. It is quite simply a property with a value. E.g.:

    ``"firstname": "Ole"``

.. image:: images/getting-started/key_value_pair.png
    :width: 600px
    :align: center
    :alt: Generic pipe concept



.. _getting-started-transformations:

Transformations
===============
There are many different ways of transforming the source data. In this section will will encounter some of the more frequently used operations. For a full technical overview of the available operations visit the :ref:`DTL reference guide <DTLReferenceGuide>`.   

::

  "transform": { 
      "type": "dtl", 
      "rules": { 
          "default": [ 
              ["copy", "*"], 
              ["add", "Type", "customer"], 
              ["add", "Fullname", 
                  ["concat","_S.FirstName"," ","_S.LastName"]], 
              ["add","Firstname-lower", 
                  ["lower","_S.FirstName"]], 
              ["add", "part-of-string", 
                  ["substring", 0, 4,"_S.FirstName"]], 
              ["add", "fullname-lower-case", 
                  ["concat","_T.Firstname-lower"," ","_S.LastName"]], 
              ["remove", "Username"] 
          ] 
        } 
    } 

The above DTL snippet displays the :ref:`add <dtl_transform-add>` function as well as the  :ref:`concat <concat_dtl_function>`, :ref:`add <lower_dtl_function>`, :ref:`substring <substring_dtl_function>` and the :ref:`remove <dtl_transform-remove>` function inside the transform. 

  * The first ``["add"]``  creates a new property named **"Type"** that has the value **"customer"**.

  * The second ``["add"]`` creates a new property named **"Fullname"** which is constructed by using the function concatenate (``["concat"]``).

  * The third ``["add"]`` uses the function ``["lower"]`` to make all characters lower case.

  * The fourth ``["add"]`` uses the function ``["substring"]`` to make a substring of the **"FirstName"**.

  * The fifth ``["add"]`` uses the function``["concat"]`` to combine the lower cased first name with the last name.

  * The ``["remove"]`` function removes the selected property.

Notice the ``["_S.[property1]"`` and ``["_T.[property2]"``. The **_S** and **_T** are called variables, and refer to the source and the target entity respectively.

Rules
^^^^^

In each pipe there is one mandatory rule where most of functions to apply transforms to source data is added; **"default"**.The other rules can be applied via the ``["apply"]``,  and ``["apply-hops"]`` DTL functions. This means that most of the logic applied to the entities of the source data, will be added inside **"default"**. That can be ``["add"]``,  ``["remove™]``, ``["filter"]`` and ``["copy"]`` to name a few examples. 

It is important to remember the *order of the functions is significant*. This means Sesam can use output from a previous function (by using the variable ``["_T"]`` ) in a transform step further down within the default rule. The rules applied to the ``["apply"]``  and ``["apply-hops"]`` , are stated outside the default rule, but within the curly brackets of **{"rules"}**. 

Let us have a look at an example of a global pipe to try to highlight some of this:

As we can see in "default" several ``["add"]`` have been listed. When adding "fullname” The order is important as this is based on "firstname" and "lastname" which was already added. Also ``["filter"]`` used for **"consents"** which is added straight after **"consents"** was added via ``["hops"]`` function. Filters are often added at the start of "default rule", e.g. if you only want to process entities that meet certain requirements. And in some cases at the end of the "default rule" as in this example the filter checks if "consents" contain data, in which case the entity is included in further processing.

In our example we have one rule in addition to the "default rule". As we can see it is the rule is called **"location"** which is called on by ``["apply-hops"]`` in the default rule. This rule specifies what output is to be returned. In this case "kommunenavn" and "poststed" is copied from "global-location".

::

   {
    "_id": "global-person",
    "type": "pipe",
    "source": {
      "type": "merge",
      "datasets": ["erp-person ep", "greg-crm-person gcp", "hr-person hp", "salesforce-userprofile sup"],
      "equality": [
        ["eq", "gcp.SSN", "ep.SSN"],
        ["eq", "gcp.SSN", "hp.SSN"],
        ["eq", "gcp.EmailAddress", "sup.EmailAddress"]],
      "identity": "first",
      "strategy": "default",
      "version": 2
    },
    "transform": [{
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*"],
          ["add", "zipcode",
            ["coalesce",
              ["list", "_S.hr-person:ZipCode", "_S.greg-crm-person:PostalCode", "_S.erp-person:ZipCode"]]],
          ["add", "email",
            ["coalesce", "_S.EmailAddress"]],
          ["add", "firstname",
            ["coalesce",
              ["list", "_S.erp-person:Firstname", "_S.hr-person:GivenName", "_S.greg-crm-person:FirstName"]]],
          ["add", "lastname",
            ["coalesce",
              ["list", "_S.erp-person:Lastname", "_S.greg-crm-person:LastName", "_S.hr-person:Surname"]]],
          ["add", "fullname",
            ["concat", "_T.firstname", " ", "_S.erp-person:MiddleInitial", " ", "_T.lastname"]],
          ["add", "active-subscriptions",
            ["apply", "filter-subscriptions", "_S.erp-person:subscriptions"]],
          ["add", "consents",
            ["hops", {
              "datasets": ["global-consent gc"],
              "where": [
                ["eq", "_S.salesforce-userprofile:Username", "gc.Username"]],
              "return": "gc.title"
            }]],
          ["filter",
            ["is-not-empty", "_T.consents"]],
          ["merge",
            ["apply-hops", "location", {
              "datasets": ["global-location gl"],
              "where": ["eq", "_S.ZipCode", "gl.postnummer"]
            }]],
        "location": [
          ["copy", "kommunenavn"],
          ["copy", "poststed"]]
      }
    }],
    "metadata": {
      "global": true
    }
  }

Merging sources
^^^^^^^^^^^^^^^
Merging gives us an aggregated representation of two or more datasets​​. We can create an aggregated dataset source that contains all the data from multiple datasets by using the source type "merge". With this merge type we will join datasets through properties that have corresponding values across different datasets. The resulting aggregated dataset will contain entities with all the properties from the different datasets. 

.. image:: images/getting-started/db-table-after-merge.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

When merging datasets we need to combine entities through identical values across datasets. In the image above we merge datasets A and B through their "lastname" properties, and B and C through their "email" properties. As we can see, the resulting dataset will have "null" values in the fields that cannot be populated through entities with matching values.

This way you can for example, combine a customer dataset with another customer dataset through the **"lastname"** property and work with an entity that contains more customer info. In the configuration below we have given the datasets **aliases** in the source config. This is for easy referencing later in the source configuration. We see the alisases 
here:

**["customerA a", "customerB b"]**

In the equality rule we simply put **"a.lastname" and "b.lastname"** to specify which dataset and which key we use. IF we were not using aliases, it would look like this **"customerA.lastname", "customerB.lastname"** so aliases make it easier and tidier to write DTL.

::
 
  "source": { 
      "type": "merge", 
      "datasets": ["customerA a", "customerB b"], 
      "equality": [ 
      ["eq", "a.lastname", "b.lastname"] 
      ], 
      "identity": "first", 
      "version": 2 
  }

With the :ref:`equality <eq_dtl_function>` property of the source we set the joining condition for the merge. The join expression **["eq", "a.lastname", "b.lastname"]** will combine entities where the lastname from **”customer A”** matches the **”lastname”** from **"customer B”** . Our source dataset will after the merge contain entities with data from both the customers.

The **“identity”** property specifies the ID of the resulting entity. Set to **“first”** it will use a single ID value from one dataset. This ID will be copied from the first dataset that contains one, in the order that the datasets are listed in the **“source”** property. Set to **“composite”** it will instead make a custom id composed of all the different IDs in the datasets.

The **”version”** property refers to the version of the merge source. The default value is 1, but version 1 is deprecated. Set this to **2**.

Coalesce, list and other useful DTL functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**"Coalesce"** means to join or combine. In SQL it is commonly used together with ``["is-null"]`` to return the first non-null value in a list. In DTL, when we need to prioritize which keys we want to use to pick a value, we use **"Coalesce"**. So, when is this useful and how is it used?

Say we want to add a property or a key called "lastname". This key-value is found in three different systems. We want to make sure we use the most trusted value, we use ``["Coalesce"]`` to state the order which Sesam checks for values. If the hr-person "lastname" is null, ``["Coalesce"]`` gives us the opportunity to choose which is the next best option.

::

  ["comment", "Below code will first check "lastname" in hr-person 
              dataset ,if it is null then it goes to crm-person dataset and so 
              on. basically, we prioritize the order on most trusted values"], 
              ["add", "zipcode", 
                  ["coalesce", ["list", "_S.hr-person:lastname", 
                  "_S.crm-person:name", "_S.erp-person:surname"] 
              ] 
          ] 
  ] 


``["Coalesce"]`` is used together with ``["list"]`` function, which basically is a list of values. We need ``["list"]``  to list the order of which keys to pick values from. 

If you need a list of key-value pairs, in other words a list of properties *and* values, you need to make a dictionary using the ``["dict"]``  function.

To illustrate the difference let us look at some DTL in a pipe


::
  
  {
  "_id": "global-person",
  "type": "pipe",
  "source": {
  "type": "merge",
  "datasets": ["erp-person ep", "crm-person cp", "salesforce-userprofile su", "hr-person hr"],
  "equality": [
      ["eq", "ep.SSN", "cp.SSN"],
      ["eq", "ep.SSN", "hr.SSN"],
      ["eq", "ep.Username", "su.Username"]
    ],
    "identity": "first",
    "version": 2
  },
  "transform": {
    "type": "dtl",
    "rules": {
      "default": [
        ["copy", "*"],
        ["add", "firstname",
          ["coalesce",
            ["list", "_S.crm-person:FirstName", "_S.erp-person:Firstname", "_S.hr-person:GivenName"]
          ]
        ],
        ["add", "lastname",
          ["coalesce",
            ["list", "_S.crm-person:LastName", "_S.erp-person:Lastname", "_S.hr-person:Surname"]
          ]
        ],
  ["add", "fields",
          ["dict", "SSN", "_S.ssn", "contact", "_S.emailaddress", 
  "Origin", "_S.birth_place "]
        ]

As seen in pipe above, the dictionary contains key and where to access value i.e. **["dict","SSN", "_S.ssn"].** A list could be a list of items separated by commas i.e.  **["list","_S.crm-person:FirstName", "_S.erp-person:Firstname", "_S.hr-person:GivenName"].**

The ``["if"]``  condition is a function in DTL that works by evaluating a statement and by performing different actions depending on the outcome of the evaluation. 

In everyday life we might say "if you're 50 years old or older, then you're entitled to a longer vacation". If not, then you have the standard number of weeks set aside for vacation. 

In DTL this would be utilized in the following way:

First we need to be able to assort the different people into two separate groups, e.g. group_1 is the group containing people with normal vacation (under 50 years of age) and group_2 is the group with people with extended vacation. Now let's assume that every person has an attribute named "age". Assuming that the person entity is the source entity we could define our evaluating statement as the following: ["gte", "_S.age", "50"], which will be true if the person is 50 years old or older, and false otherwise. We use the ``["gte"]``  function which is used to get values greater than or equal to. In comparison ``["gt"]``  simply means greater than. Now we can construct our complete if-statement:

::

  ["if",
      ["gte", "_S.age", "50"], 
      ["add", "age_group", "group_1"],
      ["add", "age_group", "group_2"]
  ]

The third line is activated if the statement is true, and the fourth line if the statement is false.

Another handy function is ``["return"]``  which allows us to specify which values we want returned from source when doing hops. Please see code example below

Config:

::

  ["add", "FirstName",
    ["first",
      ["hops", {
        "datasets": ["users u"],
        "where": [
          ["eq", "_S.Username", "u.Username"]
         
        "return": "u.FirstName"
      }]
    ]
  ]

  This example will make a hops to the 'users' dataset based on the Username properties, and if a match is found, return the value of the 'FirstName' property. If the value of that property is 'John', the resulting output would be:

  {
    "FirstName": "John"
  }

``["Tuples"]`` is mainly used when we need to make several equalities between two datasets in one hops. Let us say you have two properties in dataset A that will match two properties in dataset B, it will be done as follows:

::

  ["eq",
    ["tuples", "A.prop1", "A.prop2"],
    ["tuples", "B.prop1", "B.prop2"]
  ]

**Filters** they can be used in many contexts, but one typical case we use ``["filter"]``  for is on out from globals to filter in correct entities (typically on rdf: type) to be processed further.

When we need to filter data, there is a ``["filter"]`` function. This can be used in several ways and in various combinations with other functions. Below are some examples:

- To stop processing, simply use ``["filter"]``

- Continue processing only if the source entity's age is greater than say 42, use  ``["filter", ["gt", "_S.age", 42]]``

- Continue processing only if the source entity's doctype is report, use ``["filter", ["eq", "_S.doctype", "report"]]``

- If you wish to process only if doctype *isn't* report, then use ``[["filter", ["neq", "_S.doctype", "report"]]``

- If you have more than one type, continues processing if source entity has doctypes either report, letter or budget, you can combine with ``["or"]``


::

  ["filter",
           ["or",
             ["eq", "_S.doctype", "report"],
             ["eq", "_S.doctype", "letter"],
             ["eq", "_S.doctype", "budget"]
 
If we don't need exact match, we can use ``["intersects"]`` instead; it will continue  to process if we get overlap.

::

  ["filter",
            ["intersects", "_S.doctype",
              ["list", "report", "letter", "budget"]
            ]
          ]


Global datasets
^^^^^^^^^^^^^^^
Global datasets are key to getting the most out of using Sesam. We combine data from sources with logically linked information to provide one common place to then retrieve this data from when needed. This will reduce the total number of pipes needed compared to a system where you get data from the original sources each time.
You can read more about global datasets; what they are, how to use them and how to develop them :ref:`here <best-practice-global>`.

Namespace identifiers
^^^^^^^^^^^^^^^^^^^^^
A namespaced identifier consists of two parts; a namespace and an identifier. The namespace part can consist of any character, including colons. The identifier part can consist of any character except colons (:).

Example of an entity with namespaces:

::

   { 
   "_id": "users:123", 
   "user:username": "erica", 
   "user:firstname": "Erica", 
   "user:manager": "~:users:101" 
   } 

Namespace identifiers are recommended way for referring datasets for matching properties during transformations. Suppose, if you have three different person datasets and you want to merge on some common properties, like e-mail or SSN, then we should use namespace identifiers. The code below will add a namespace identifier, based on common SSN properties between datasets **"crm-person"** and **"erp-person"** during transformation inside DTL of **"crm-person"**. Same way, we need to create a namespace identifier between **"hr-person"** and **"erp-person"** datasets so that we can refer them during merging.

::

  ["make-ni", "erp-person", "SSN"],

This will produce the following output:

::

  "crm-person:SSN-ni": "~:erp-person:23072451376",

Now, you have unique namespace identifiers based on SSN, which you can refer now.

::

   {
    "_id": "global-person", 
    "type": "pipe", 
    "source": { 
        "type": "merge", 
        "datasets": ["crm-person cp", "hr-person hp", "erp-person ep"], 
        "equality": [ 
            ["eq", "cp.SSN-ni", "ep.$ids"], 
            ["eq", "hp.SSN-ni", "ep.$ids"] 
        ], 
        "identity": "first", 
        "version": 2 
    }

In the above code we are connecting the foreign keys, **"SSN-ni"** of **"hr-person"** and **"crm-person"** with the primary key, **"$ids"**, of **"erp-person"**. You do not need to add the third equality between **"hr-person"** and **"crm-person"** as it will happen automatically.


Merging with DTL
^^^^^^^^^^^^^^^^
We can merge entities in the DTL transform section with the :ref:`merge <dtl_transform-merge>` function. This will combine its input properties (for example Age, CellNumber and salary) into the target dataset.

::

        ["merge", 
            ["list", { 
                "Age": 40 
            }, { 
                "CellNumber": 7854216, 
                "Salary": 400000 
            }] 
        ] 

We will later see the use of the ``["merge"]`` function in combination with functions that fetch entities from other datasets.

Apply
=====
The :ref:`apply <apply_function>` operation applies an own-specified rule to an entity. I.e. the call ["apply", "SomeRule", "_S.orders"] applied the rule "SomeFunc" to the source "_S.orders".  

Hops
====
The :ref:`hops <hops_function>` function joins two datasets and returns the entities where the specified parameters match:

::
 
  "transform": {​
       "type": "dtl",​
        "rules": {​ 
            "default": [​ 
                ["copy", "*"],​
                ["add", "order-data"​, 
                    ["hops", {​ 
                        "datasets": ["global-orders glo"],​ 
                        "where": [​ 
                            ["eq", "_S.custno", "glo.custno"]​
                        ]​ 
                    } 
                ]​
             ]​ 
         } 
     } 


In this transform we first copy everything from the source dataset into the target. To do a ``["hops"]``  you first add a new property to the target dataset. Then, inside that ``["add"]``  you call on the ``["hops"]``  function to fetch entities from the specified dataset, in this example (**"global-orders"**).


Apply-hops
==========
There is also the function :ref:`apply-hops <apply_hops_function>`, which is a combined ``["apply"]``  and ``["hops"]``  function. This adds another **"rule"** in the DTL configuration in which we can specify how to implement the entities fetched with the hops. You can read more about the ``["apply"]``  function :ref:`here <hops_function>` 

::

  "transform": { 
      "type": "dtl", 
      "rules": { 
          "default": [ 
              ["copy", "*"], 
              ["merge", 
                  ["apply-hops", "order", { 
                      "datasets": ["orders o"], 
                      "where": 
                      ["eq", "_S._id", "o.cust_id"] 
                  }] 
              ] 
          ], 
          "order": [ 
              ["add","ID","_S._id"] 
          ] 
      } 
  }

This will retrieve orders through the hops expression and then add them using the order transformation rule. The output is a dataset where the ID of all orders are added to the customers from the source dataset.



Should I "add" or "merge" an apply-hops?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
As you can see in the examples below we want to add the "City" and "Municipality" from another dataset to the source. In the two examples we have the same source but the difference is in how we use the ``["apply-hops"]`` . In the first case we ``["add"]``  a new property called "difi-data" which you can see in the results creates a dictionary containing "City" and "Municipality" in **"difi-data"**.

 When adding "City" and "Municipality" from another dataset we need to specify which *sources* and *entities* we want to match on. This is done by adding ``["_S"]``  in front of name of dataset and entity.  It looks like this: **_S.hr-person:ZipCode**

  **"_S"** is a built-in variable in **DTL**. Read more about Variables :ref:`here <variables>`.


::

 "transform": { 
    "type": "dtl", 
    "rules": { 
        "default": [ 
            ["copy", "*"], 
            ["add","difi-data", 
                ["apply-hops", "foobar", { 
                    "datasets": ["difi-postnummer dip"], 
                    "where": [ 
                        ["or", 
                            ["eq", "_S.hr-person:ZipCode", "dip.postnummer"], 
                            ["eq", "_S.crm-person:PostalCode", "dip.postnummer"] 
                        ] 
                    ] 
                }] 
            ], 
            ["comment", "Below code will first check zipcode in hr-person 
            dataset, if it is null then it goes to crm-person dataset and so on. 
            Basically we prioritize the order on most trusted values"], 
            ["add", "zipcode", 
                ["coalesce", 
                    ["list", "_S.hr-person:ZipCode", "_S.crm-person:PostalCode", 
                    "_S.erp-person:ZipCode"] 
                ] 
            ] 
        ], 
        "foobar": [ 
            ["add", "Municipality", "_S.kommunenavn"], 
            ["add", "City", "_S.poststed"] 
        ] 
    } 
 }

.. image:: images/getting-started/add_applyhops.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

In the second example, instead of adding the ``["apply-hops"]`` , we use ``["merge"]`` . This will add the "City" and "Municipality" as properties in the target.

::

  "transform": { 
      "type": "dtl", 
      "rules": { 
          "default": [ 
              ["copy", "*"], 
              ["merge", 
                  ["apply-hops", "foobar", { 
                      "datasets": ["difi-postnummer dip"], 
                      "where": [ 
                          ["or", 
                              ["eq", "_S.hr-person:ZipCode", "dip.postnummer"], 
                              ["eq", "_S.crm-person:PostalCode", "dip.postnummer"] 
                          ] 
                      ] 
                  }] 
              ], 
              ["comment", "Below code will first check zipcode in hr-person 
              dataset ,if it is null then it goes to crm-person dataset and so 
              on. basically, we prioritize the order on most trusted values"], 
              ["add", "zipcode", 
                  ["coalesce", ["list", "_S.hr-person:ZipCode", 
                  "_S.crm-person:PostalCode", "_S.erp-person:ZipCode"] 
              ] 
          ] 
      ],  
      "foobar": [ 
          ["add", "Municipality", "_S.kommunenavn"], 
          ["add", "City", "_S.poststed"] 
      ] 
  } 
 } 

.. image:: images/getting-started/merge_applyhops.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept


.. _getting-started-Dependency-tracking-and-resetting-a-pipe:

Dependency-tracking and resetting a pipe
========================================

We have now started to create dependencies between datasets. In :ref:`Lab 5 <getting-started-labs-5>` you created a pipe called **<your_name>-global-person** and in :ref:`Lab 6 <getting-started-labs-6>` you created hops to **difi-postnummer**. This means that entities from **<your_name>-global-person** should change when the data in the source datasets (crm-person, erp-person, hr-person and salesforce-userprofile) changes, in addition to when the relevant data in difi-postnummer changes. We could of course check through every entity in difi-postnummer for changes, but this would also mean we need to reprocess every entity in the source datasets to check for changes when they connect to **difi-postnummer**.

In order to make sure that only entities that has changed since the last time the integration ran are updated, Sesam utilizes **“dependency tracking”**. **Dependency tracking** ensures that Sesam recognizes changes in connected data, and not only changes in the pipe’s sources, and acts accordingly. For further information regarding dependency tracking visit :ref:`here <concepts-dependency_tracking>`.

We will try to explain the workings of dependency tracking with a different example, and then apply this information to the current situation in :ref:`Lab 9 <getting-started-labs-9>`.

Let us assume you have a dataset in your Sesam node concerning all the employees in a company. This dataset may contain information regarding the employee’s names, employee numbers, age, length of employment and so on. In another dataset you have information regarding which projects the employees have worked on as well as the employee number. You now wish to combine these datasets to generate a new dataset that includes both the employees name, employee number and the different projects this employee has worked on. This could be done using the :ref:`hops <hops_function>` function. 

If we start with the dataset containing employee information, we may combine the data from the employee dataset with the project dataset based on matching employee numbers. Should an employee change their name, Sesam will pick up a change in the source entity and reprocess that entity to update the results. However, the project dataset in not the source entity in this case, but registering the changes in this dataset is just as vital as registering changes in the source dataset, as they both combine to make the resulting dataset in this use-case. This is where dependency tracking comes into play. 

Dependency tracking tracks all the data this pipe, as well as the dataset it is connected to, such that changes to data outside the source dataset are registered and reprocessed in the pipe. 

So far in the labs we have only covered changes outside the pipe we are working on. But, what about changes in the pipe itself? If we add lines in our DTL config, how does Sesam know that the entities should be reprocessed? The source or the dependent data has no changes, and therefore no entities will be reprocessed as Sesam thinks nothing has changed. In short, Sesam does not recognize this automatically. Entities are only reprocessed in Sesam if there are changes in the data coming into the pipe. If we make changes in a Sesam pipe, changes that will affect the end result (such as adding extra data), the entities that has already been processed will not by them self be reprocessed, thus only changed data or new data will be populated with the extra information. 

To remedy this, every time we make changes in a pipe that will affect the output data, and if we want all old entities to have that extra information, we must manually **reset** and **start** the pipe. When we reset a pipe, all the entities from the source will be reprocessed. This can be done by clicking on the three dots next to the pipe name at the top of your pipe.

.. image:: images/pipesmenu.png
    :width: 600px
    :align: center
    :alt: DataSet


Some of the alternatives presented are **“Restart”**, **“Start”** and **“Reset”**. **“Restart”** is simply a combination of **“Reset”** followed by **“Start”**. This will send all the entities from the source dataset through the pipe and populate them with the extra data you have specified through your DTL config. 

In many cases, we do not wish to reprocess all the entities, but only some of the them. E.g. imagine you have a dataset of 5 million entities, tracing back many years. In your DTL config, you have added logic that yields extra data if the entities are two months old or newer. Reprocessing entities older than two month makes no sense now, since they will not be populated with the new data either way. In these situations, press **"..."** at end of pipe name and on the menu choose **“Update last seen”** . This functionality could be more efficient. In this case, we choose which entities should be reprocessed, which greatly decreases the computational time. 

Similarly, imagine you work on a global pipe which merges data from 3 different sources. Two of these sources contain millions of entities, and one only a few. Let’s say you wish to change the output containing data from the source with only a few entities. Resetting the whole pipe in this case is unnecessary since we only need to reprocess a few entities, The **Update last seen** option also supports resetting the data from several sources at different times, thus if you need to reprocess the entities from the "small" dataset, you may do so without sending through all the other million entities, which will in either case be unaffected by your DTL changes. 

There are other reasons both to reprocess all the data and only some of it, but the main point is to assess every situation individually.

Go to the :ref:`Labs section <getting-started-labs>` and do :ref:`Lab 9 <getting-started-labs-9>` for examples and to play around with data and see how it works.

.. _getting-started-sinks:

Sinks
-----

Sinks are at the receiving end of pipes and are responsible for writing entities into an internal dataset or a target system.

Sinks can support :ref:`batching <pipe_batching>` by implementing specific methods and accumulating entities in a buffer before writing the batch. The size of each batch can be specified using the batch_size property on the pipe. See the section on batching for more information. We also recommend that you read about 
:ref:`the sinks <best-practice-output-pipes>` in the documentation and "Best practice" for best ways of working with them :ref:`here <best-practice-output-pipes>`.

.. _getting-started-csv-endpoint:

CSV endpoint sink
=================
We will first look at setting up a sink to expose the output for a .csv (comma separated values) file. The CSV endpoint sink does not support pumping and the batching explained above. The only way to have entities flow through the pipe is by requesting the output as explained below.

::

 "sink": {
   "type": "csv_endpoint",
   "columns": ["_id", "lastname", "address"],
 }

The sink config can include more parameters, but their default values are OK for our example and do not need to be listed and changed. For example **"delimiter"** is set as **","** by default. Look up other parameters in the documentation if needed. The values listed in **"columns"** correspond to values in the output of the DTL.

After creating a pipe with a CSV endpoint sink you can go to the **"Output"** tab of the pipe. Here you can download the entity output. Select the number of entities you want to include and click "Download" to get a .csv file with the same name as the pipe. This can be viewed in a text editor to see the result, or you can open the file in e.g. Microsoft Excel. In Excel open a document, go to the "Data" tab and click "From Text/CSV".

You can also download the output by copying the cURL and creating your .csv file in a CLI like curl or Git Bash. Paste the cURL into you CLI and add " > my_file.csv" at the end. This will create the file at your current location. You can remove the entity limit and get all entities by removing "?limit=X" from the curl.


SQL database to CSV file output step by step
============================================
In this next chapter we will walk you through the steps of using a SQL database as a source and create a CSV endpoint. First, if you don't have access to a SQL server you can sign up at `ElephantSQL <https://www.elephantsql.com>`__ and select a free trial.

Once you've set up your account click on details in the left menu. It should look like this: 

.. image:: images/getting-started/Elephant_SQL.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Now you are ready to create a new system. In **Sesam** go to Systems and select **New system**. In the **Choose template** select **postgresql prototype** (Because we're using ElephantSQL. Will be different for other sources).

To fill in the **"database"**, **"host"**, **"password"** and **"username"** go to your *ElephantSQL* and select **details**. From the figure above you'll see that you have the **Server**, **User & Default database** and **Password**.

In the **"_id"** you'll create the name of the system (the same as creating a pipe).

  * **"type"**: "system:postgresql"
  * **"database"**: User & Default database
  * **"host"**: Server
  * **"password"**: Password
  * **"username"**: User & Default database 

Using secrets
^^^^^^^^^^^^^
.. image:: images/getting-started/new_system3.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

As you can see, we are using :ref:`secrets <secrets_manager>` for the database, password and username. To do this go into the **Secrets** tab, click **Add secret**, give it a name (e.g. "password" for the password and "username" for the username) and paste the values from ElephantSQL. Read more about secrets `here <https://docs.sesam.io/security.html>`__.

Creating a table in the database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Until now your database has been empty. If you are not familiar with SQL, do not worry. We have created some sample data for you. In ElephantSQL, click on **browser** in the left menu.

.. image:: images/getting-started/elephantQuery.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept


Copy/paste the following

::

  CREATE TABLE EmployeeTable ( 
  id SERIAL PRIMARY KEY, 
  firstname varchar(40), 
  lastname varchar(40), 
  DateOfBirth varchar(10), 
  Address varchar(40), 
  Salary int, Department varchar(40) 
  );

Then click on **Execute**

Delete the old text and copy/paste the following:

::
 
  INSERT INTO EmployeeTable (id, firstname ,lastname ,DateOfBirth ,address,Salary,Department) 
  VALUES (1,'Larry','Johnson','27-05-1989','Country road 1',58000,'Sales'), 
  (2,'Mike', 'Jensen','05-27-1989','Upper street 3',62000, 'Marketing'), 
  (3,'Hannah', 'Jackson','10-12-1982','East road 5',60000,'Production'), 
  (4,'Phillip', 'Blackstone','08-02-1978','Sourt Street 23',49000,'Sales'), 
  (5,'Otto', 'Greene','03-20-1969','North street 65',48000,'HR'), 
  (6,'Siri', 'Stone','03-05-1989','Middle street 5',62000, 'Marketing'), 
  (7,'Olav', 'Olsen','11-30-1989','Down street 2',54000, 'Accounting');

Then click on **Execute**. We have now created a sample table with some properties with values.

Head back to your Dev node. Now you can create a new pipe that pulls this table from the database.

.. image:: images/getting-started/new-pipe-db.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Should **Provider** -> **employeetable** not pop up automatically just type in the necessary lines manually as shown in the picture above.

You are now free to transform the data as you want, but it is not needed and will be omitted here.

Creating out CSV sink
^^^^^^^^^^^^^^^^^^^^^
.. image:: images/getting-started/csv-endpoint.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

There are multiple ways of viewing the data. The simplest is to download the file and opening it with Excel or any text editor. (If you are familiar with cURL you can copy the link and past it in terminal/command.)

.. image:: images/getting-started/csv-sink.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Click **Download**. Open a new Excel document. Go to **Data** then select **From text**. Find the CSV-file and click **Get Data**.

Select as shown in figures below:

.. image:: images/getting-started/csv-test.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept


SQL sink example configuration
==============================
The outermost object would be your pipe configuration, which is omitted here for brevity:

::

  { 
      "sink": { 
          "type": "sql", 
          "system": "my-mssql-system", 
          "table": "customers" 
          } 
  } 

Each object is on the form:

::

 {
    "source_property": "name_of_property",
    "name": "name_of_column",
    "type": "string|integer|decimal|float|bytes|datetime|date|time|uuid|boolean",
    "max_size|max_value": 1234,
    "min_size|min_value": 1234,
    "precision": 10,
    "scale": 2,
    "allow_null": true|false,
    "primary_key": true|false,
    "index": true|false,
    "default": "default-value"
 }

Let's look at an example:

::

 {
  "_id": "employeetable-endpoint",
  "type": "pipe",
  "source": {
    "type": "dataset",
    "dataset": "db-employee"
  },
  "sink": {
    "type": "sql",
    "system": "employee",
    "batch_size": 50,
    "bulk_operation_queue_size": 3,
    "bulk_operation_timeout": 600,
    "create_table_if_missing": true,
    "keep_failed_bulk_operation_files": false,
    "primary_key": ["id"],
    "schema": "dbo",
    "schema_definition": [{
      "type": "integer",
      "name": "id",
      "default": 1,
      "allow_null": false,
      "index": false,
      "max_value": 1000,
      "min_value": -1,
      "primary_key": true,
      "source_property": "id"
    }, {
      "type": "string",
      "name": "firstname",
      "default": "",
      "allow_null": true,
      "index": false,
      "max_size": 20,
      "min_size": 0,
      "primary_key": false,
      "source_property": "firstname"
    }, {
      "type": "string",
      "name": "lastname",
      "default": "",
      "allow_null": true,
      "index": false,
      "max_size": 50,
      "min_size": 0,
      "primary_key": false,
      "source_property": "lastname"
    }, {
      "type": "string",
      "name": "dateofbirth",
      "default": "",
      "allow_null": true,
      "index": false,
      "max_size": 50,
      "min_size": 0,
      "primary_key": false,
      "source_property": "dateofbirth"
    }, {
      "type": "string",
      "name": "department",
      "default": "",
      "allow_null": true,
      "index": false,
      "max_size": 50,
      "min_size": 0,
      "primary_key": false,
      "source_property": "department"
    }, {
      "type": "integer",
      "name": "salary",
      "default": "",
      "allow_null": true,
      "index": false,
      "max_value": 10000000,
      "min_value": 0,
      "primary_key": false,
      "source_property": "salary"
    }, {
      "type": "string",
      "name": "address",
      "default": "",
      "allow_null": true,
      "index": false,
      "max_size": 50,
      "min_size": 0,
      "primary_key": false,
      "source_property": "address"
    }],
    "table": "db-test-emlpoyee",
    "timestamp": "time_added",
    "truncate_table_on_first_run": false,
    "use_bulk_operations": false
  },
  "transform": {
    "type": "dtl",
    "rules": {
      "default": [
        ["copy",
          ["list", "id", "firstname", "lastname", "dateofbirth", "department", "salary", "address"]
        ]
      ]
    }
  },
  "pump": {
    "mode": "manual"
  },
  "metadata": {
    "tags": ["test"]
  },
  "remove_namespaces": true
 }

This sink configuration creates an SQL table containing data from the **"db-employee"** dataset.

HTTP-endpoint and retrieving data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We can expose the entities of a dataset in Sesam through an HTTP-endpoint and fetch them with an HTTP Get-request.

Exposing datasets with HTTP-endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To expose a dataset from Sesam we create an HTTP-endpoint pipe in our Sesam node. Below is the configuration for a pipe called "person-crm-endpoint", which exposes the dataset 'person-crm'.

**Replace the dataset** in the "source" with the dataset you want data from and **name the pipe** accordingly in the **"_id"**. We recommend setting the **"_id"** of the pipe as **"name-of-dataset-endpoint"**.

::

 {
  "_id": "person-crm-endpoint",
  "type": "pipe",
  "source": {
    "type": "dataset",
    "dataset": "person-crm"
  },
  "sink": {
    "type": "http_endpoint"
  }
 }

Fetch data
^^^^^^^^^^
To get hold of the data we have exposed in our HTTP-endpoint we send HTTP Get-requests from our client. Provided below are templates for implementing this in Python, Java or C# .Net.

**Python**

We will use Python's HTTP library Requests. This can be installed by running **pip install requests** in our Python interpreter.

::

 import requests

 url = "https://DATAHUB-URL.sesam.cloud/api/publishers/ENDPOINT-ID/entities"
 JWT = "YOUR-JWT-TOKEN"

 r = requests.get(url, headers={'Authorization': 'bearer '+JWT})
 entities = r.text

 print(entities)

**Java**

We will use Apache HttpClient to create a GET request and will need the following Maven dependency:

::

 <dependency>
    <groupId>org.apache.httpcomponents</groupId>
    <artifactId>httpclient</artifactId>
    <version>4.5.4</version>
 </dependency> 

**Java class**:

::

 package sesam;

 import java.io.BufferedReader;
 import java.io.IOException;
 import java.io.InputStreamReader;
 import org.apache.http.HttpResponse;
 import org.apache.http.client.methods.HttpGet;
 import org.apache.http.impl.client.CloseableHttpClient;
 import org.apache.http.impl.client.HttpClientBuilder;

 public class ApacheHttpClientGet {

    public static void main(String[] args) throws IOException {

        String entities = getEntities();
        System.out.println(entities);
    }

    private static String getEntities() throws IOException {

        try (CloseableHttpClient client = HttpClientBuilder.create().build()) {

            String url = "https://DATAHUB-URL.sesam.cloud/api/publishers/ENDPOINT-ID/entities";
            String JWT = "YOUR-JWT-TOKEN";

            HttpGet request = new HttpGet(url);
            request.addHeader("Authorization", "Bearer "+JWT);
            HttpResponse response = client.execute(request);

            if (response.getStatusLine().getStatusCode() != 200) {
                // handle as preferred
                return null;
            }

            BufferedReader bufReader = new BufferedReader(new InputStreamReader(
                    response.getEntity().getContent()));

            return bufReader.readLine();
        }
    }
 }

**C#.Net**

::

 using System;
 using System.Net.Http;
 using System.Net.Http.Headers;
 using System.Threading.Tasks;

 namespace Sesam
 {
   class Program
   {
       static void Main(string[] args)
       {
           var entities = GetEntities().Result;
           Console.WriteLine($"Entities: {entities}");
           Console.ReadLine();
       }

       private static async Task<String> GetEntities()
       {
           var url = "https://DATAHUB-URL.sesam.cloud/";
           var apiUrl = $"/api/publishers/ENDPOINT-ID/entities";
           string jwt = "YOUR-JWT-TOKEN";

           using (var client = new HttpClient() { BaseAddress = new Uri(url) })
           {
               client.BaseAddress = new Uri(url);
               client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
               client.DefaultRequestHeaders.Add("Authorization", $"Bearer {jwt}");

               using (var response = await client.GetAsync(apiUrl))
               {
                   if (response.StatusCode == System.Net.HttpStatusCode.OK)
                       return await response.Content.ReadAsStringAsync();

                   else return null;
               }
           }
       }
   }
 }

**Adaptation**
To make these code implementations work with our HTTP endpoint we have to replace the capitalized parts of the URL and the JWT-token creation.

  1. **Replace DATAHUB-URL** with the URL of our Sesam datahub. This URL is found just below the Sesam logo at the top-left corner of the page when logged into our node in the Sesam portal.

  2. **Replace** the **ENDPOINT-ID** part of the URL with the **"_id"** of the endpoint pipe we want data from.

  3. **Replace YOUR-JWT-TOKEN** with a JWT-token from our Sesam subscription. This is to provide authorization to access the HTTP-endpoint. The token is not retrievable through Sesam, but we might have already stored it somewhere for later use. We can find our JWT-token inside our .syncconfig-files if we have previously created these to support storing Sesam-configs locally. If we don't have access to our existing JWTs, we can create a new one in the Sesam portal under "Subscription" -> "JWT".

  * Optionally we can add **?limit=x** or **?since=x** to the end of the URL in our get-call. Limit has to be an integer and specifies the maximum number of entities to get. Adding since will give you only the entities that have a higher value of "_updated" than the value you give since. The "_updated" property of the entities are either an integer or a timestamp, but since is treated as a string. When using since to only fetch entities that have been added since our previous request, we need to keep track the "_updated" value of the last entity fetched client side to have it available for the next call.

The complete URL could look like this ``https://datahub-425aagcte.sesam.cloud/api/publishers/person-crm-httpendpoint/entities?since=255``:

All of these templates provide the data from the HTTP endpoint as a JSON-formatted string object named **entities**. We can now replace the printing of this string with our own implementation to make use of the data.

.. _getting-started-pumps:

Pumps
-----
The pumps specify the schedule with which the pipe runs. This can be done through a scheduled interval specified either pr.seconds, hours, days, weeks or months. A pump can be added to a pipe through the **Schedule** template. 

Dead letters
============

"Pump" is also the part of the pipe where more advanced settings for keeping control of dead letters are configured.

A general definition of "dead letter" is a letter sent to unknown address, in other words "failed delivery". Transferring this to Sesam, a dead letter is an entity in a dataset that fails to write when a pipe runs. Hence a "failed delivery" to the target system it is supposed to be written to. 

If a pipe fails, Sesam provides a function which allows failed entities to be written to a "dead letter" dataset. If the entities can be transferred later on, they are flagged as "ok" in the dead letter dataset. Sesam can be configured to keep trying to write the entities to appropriate dataset.

Once pipe has run, go into **Dataset**. On top go to column **"Origin"** and click **"system"**. This filter shows on the systems datasets and it is here you will find you dead letter datasets. So for pipes configurated to use **dead letters**, a dataset prefix ``system:dead-letter:`` followed by the pipe name will be generated. If no entities failed, the dataset will be empty. Those entities that failed, will be listed in this dataset.

.. image:: images/how-to-dl-dataset.png
    :width: 600px
    :align: center
    :alt: DataSet


.. image:: images/dl-dataset.png
    :width: 600px
    :align: center
    :alt: DataSet

Now we have a list of datasets that failed and you can do more configuration to pump to say when to retry to write the failed entities, how often, max number of times Sesam should try to re-write them and delay when try to re-write. For more detail on how to use the various options, please read more about configuring :ref:`pumps <pump_section>`

::

  {
    "_id": "crm-person-endpoint",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "person-cmm"
    },
    "sink": {
      "type": "json",
      "system": "cmm",
      "url": "person"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*"],
          ["add", "timestamp",
            ["datetime-format", "%Y-%m-%d",
              ["now"]
            ]
          ]
        ]
      }
    },
    "pump": {
      "max_consecutive_write_errors": 1000,
      "max_retries_per_entity": 3,
      "max_write_errors_in_retry_dataset": 10000,
      "track_dead_letters": true,
      "use_dead_letter_dataset": true,
      "write_retry_delay": "~f0.1"
    }
  }

.. _getting-started-microservices:

Microservices
-------------
The DTL in Sesam is a powerful tool to transform our data. But sometimes we need to do something with our data that is outside the scope of the DTL. We can then create a microservice that does what we need and run it inside Sesam to serve those needs. We can also use a microservice when we need to connect to an external system where the connection point is not compatible with the Sesam source systems. The microservice can be made according to our preferences and in any language.

.. image:: images/getting-started/MS-types.jpg
    :width: 800px
    :align: center
    :alt: Generic pipe concept

As shown above, irrespective of nature or technologies of external system, we can easily connect with them using microservices to read, write and update data. Microservices add flexibility to do more with data than may be possible with DTL.

Workflow
========
Microservices in Sesam run in docker containers. These containers run on our Sesam-node in what we call a system. Below is a visual representation of the flow of hosting our microservice in Sesam.

.. image:: images/getting-started/workflow-ms.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

We start by building a Docker image from our microservice. A Docker image is the blueprint for creating a container with our microservice. 

The Docker image is then pushed up to a repository on Docker Hub (or any Docker platform. When hosted in the repository the image can be pulled by anyone with access.

Finally, we pull the image from our Docker Hub repository (although private repositories are also supported) and spin up a container on our Sesam node. The container is created from the image and started. The Docker-commands for this are performed by Sesam. We simply specify the location of the image on Docker Hub in our Sesam system configuration and the container is spun up automatically. Once the Docker image location is defined in the System config Sesam will spin up the correponding container automatically. Finally to transfer data between Sesam datahub and the microservice, we need an input pipe or endpoint pipe depending on solution. For example a SQL database sends data to a Sesam pipe via a default microservice available inside your Sesam node, and similarly for data going out of Sesam to target systems. 

Microservices with Docker
=========================

First you need to sign up on `Docker <https://www.docker.com>`__ and create a new repository.

.. image:: images/getting-started/Docker-repo.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Then download `Docker Desktop <https://www.docker.com/get-started>`__.

You now need to download Python. Here we're using Python 3.6 but you can use any version after 3.5. Then install pip and Flask.

Flask is a web framework used by Pything to develop web services nad pip is a de facto standard package-management system used to install and manage software packages written in Python. If you need help with this, follow the instructions `here <https://pip.pypa.io/en/stable/installing/>`__ for pip and `here <http://flask.pocoo.org/docs/1.0/installation/>`__ for Flask.

.. image:: images/getting-started/flaskInstall.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

First things first, we need to decice which IDE (integrated development environment) you want to use. In this exercise we will use *Pycharm*, but there are various other options so if you are currently using another one, that is not a problem.

You are now ready to create the microservice. We will generate a folder and a couple of files that a microservice always need to run. Firstly we need to create a **Dockerfile**. A `Dockerfile <https://docs.docker.com/develop/develop-images/dockerfile_best-practices/>`__ is a text file that Docker reads in from top to bottom. It contains instructions which informs Docker *how* the Docker image should get built. To read more about Docker, Docker image, Docker build, it is helpful to browse the `Docker documentation <https://docs.docker.com>`__ . In addition we need to generate the actual program which is stored in a python file (.py). 

This is the program that actually runs inside Sesam and tells the system that it is connected to what needs to be done. In this example, it only sends 3 entities with embedded order data. In other cases, the MS must contain authentication to the system (eg basic auth or sql database), or in some cases we have to extract the data in the correct format (such as retrieving OData). All of these .py files (must not be .py, these are only python programs. It could have been .java for java programs, for example) are the "programs" that are running.

In addition we need requirements.txt file which tells the microservice file which libraries this program needs to run. In our example, we only run Flaks so we simply write it in in the following format:

`Flask==1.1.2``

If you want to know more about requirements.txt files, please click `here <https://pip.pypa.io/en/stable/user_guide/#requirements-files>`__ 


Now let us go through this step by step.

First thing we need is to create a new project in Pycharm. Name your project “Demo_MicroserviceProject”. The files we need to create the Microservices, will be stored inside the project. 

Once we have this, we can start by adding the **"Dockerfile"**. 

Inside your Demo_MicroserviceProject folder create a new file called "Dockerfile" and paste:

::

  FROM python:3-alpine 
  
  RUN apk update 
  
  RUN pip install --upgrade pip 
  
  COPY ./service/requirements.txt /service/requirements.txt 
  RUN pip install -r /service/requirements.txt 
  COPY ./service /service 
  
  EXPOSE 5000 
  
  CMD ["python3", "./service/DemoMicroservice.py"]

Once Dockerfile is ready, we create a new folder called "service" inside your project root folder.

.. image:: images/getting-started/MSproject.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Next step is to create the "requirements.txt" inside the "service" folder and paste the following text inside it:

::

 Flask==1.0.2

 If you have a newer version of Flask, you put that in instead of 1.0.2.

Final part is the actual program. For this we create a python file, also in the "service" folder, named "DemoMicroservice.py" with the following code:

::

  from flask import Flask, jsonify 

  app = Flask(__name__) 

  orders = [ 
  { 
      'id': 1, 
      'Username': u'Unjudosely', 
      'Orders': u'Thinkpad', 
      'TotalSum': 8000 
      }, 
      { 
      'id': 2, 
      'Username': u'Wimen1979', 
      'Orders': u'MacbookPro', 
      'TotalSum': 12000 
      }, 
      { 'id': 3, 
      'Username': u'Gotin1984', 
      'Orders': u'Chormebook', 
      'TotalSum': 10000 
      } 

  ] 

  @app.route('/api/orders', methods=['GET']) 
  def get_orders(): 
      return jsonify({'orders': orders}) 


  if __name__ == '__main__': 
      app.run(debug=True, host='0.0.0.0', port=5000)

.. image:: images/getting-started/DemoService.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Create an image of the microservice in PyCharm's terminal window or any other CLI that you prefer:

::

 docker build -t <docker_username>/<your_repository_name>:<tagname> .

To check that the you have created image run the command:

::

 docker images

Testing
^^^^^^^

To test that you can run a container from your image locally you can run it directly in the terminal. First we need to login to Docker. Run the command docker login and enter your Docker Hub **username** and **password** when prompted.

Next we'll need to run the image to create the container.

To check that you have created the image run the command:

::

  docker run -p <local_port>:<container_port> <docker_username>/<your_repository_name>:<tagname>

Set **local_port** to 5000 and the container_port to the same as the one you specified in the Dockerfile.

Now you can either go to the url in the browser or do:

::

 curl -v http://localhost:5000/api/orders 

in terminal to see if the the container runs.

To stop the container running locally you can run: 

::

 docker stop <container name> or docker stop <container_id>  


Push to Docker Hub
^^^^^^^^^^^^^^^^^^
Now we need to push the image to the repository:

To check that the you have created image run the command:

::

 docker push <docker_username>/<your_repository_name>:<tagname>

Go to hub.docker.com and check that you can see the tagname in you repository.

.. image:: images/getting-started/docker-push.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Import to Sesam node
^^^^^^^^^^^^^^^^^^^^

Now that the Docker image has been pushed to our Docker platform we need to spin up the container in our Sesam node. 

Create a new system in your node. Choose **microservice prototype** as template. Give it a proper name. Inside the **"docker"** parameter write:

::

 "docker": { 
    "image": "<docker_username>/<your_repository_name>:<tagname>", 
    "port":5000 
 } 

.. image:: images/getting-started/systemconfigms.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Save it and click on **Status**. Click **Pull** and **restart**, then **Refresh** and **Check health**. You can also hit **Refresh** in the log so you see that it's running as it should.

.. image:: images/getting-started/system-microservice.gif
    :width: 800px
    :align: center
    :alt: Generic pipe concept

The final step is to create an input pipe to get all the data from our microservice into Sesam datahub. Because our dataset does not have an **"_id"** property we need to add that. We could just use a normal **["add"]** function, but as you can see from the microservice, we’ve actually just created one property as a dictionary. We really want these as three entities and that reason we use this function:

::

  ["create", 
      ["apply", "create-entity", "_S.orders"]] 

This creates a new rule where we can add the **"_id"**. Since the **"id"** in the microservice is an integer and Sesam only accepts string values for the **"_id"** we convert it with the **["string"]** function.

.. image:: images/getting-started/remade-pipe.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

.. image:: images/getting-started/pipe-orders-ms-output.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept


.. _getting-started-microservices-restAPI:

REST APIs
=========
Sometimes we have to connect to a websites API to extract data for our pipe. A website's API is a code that allows our program to communicate with the website, to either extract information, or to post information. A REST (Representational State Transfer), or RESTful, API is an API which uses HTTP requests to POST, GET PUT and DELETE data. 

We will be using the `flask <https://flask.palletsprojects.com/en/1.1.x/>`__ library as well as the `requests <https://2.python-requests.org/en/master/>`__ library in Python to display how we might communicate with a websites API. 

.. _getting-started-microservices-restAPI-Authentication:

Authentication
^^^^^^^^^^^^^^
Often when we wish to communicate with an API, we need to establish who we are, and what we are allowed to do. There as many different ways of doing this, and the way forward depends on the API you wish to communicate with. Most APIs have easily accessible documentation which explain how to authenticate and authorize for that specific API. For these specific websites, you can access the information only after you have authenticated yourself. 

.. _getting-started-microservices-restAPI-JWT:

JSON Web Tokens
^^^^^^^^^^^^^^^
When we authenticate ourselves to a server, we often utilize something called a **JSON Web Token** (**JWT**). A JWT is a string that consists of a **header**, a **payload** and a **signature** to form the string **header.payload.signature**.

  * **Header**: The header describes what sort of object it is, in this case a JWT. It also describes the specific algorithm needed to create the JWT signature component.
  * **Payload**: The payload contains the user information, such as the user ID and the rights of the user.
  * **Signature**: The signature makes sure the JWT is securure during transport. The signature is the hashed version of the header and the payload, combined with a secret. The secret uses the algorithm specified in the header to hash the data.      

A JWT is used when we need to make sure that the sent data actually originates from an authentic source, to make sure no secondhand party has tempered with the data. When we sign into an app, i.e. google we first communicate with the app's authentication server. This server sends us a JWT back which we can use to communicate with the app's API. 

.. figure:: images/getting-started/JWT.png
    :width: 800px
    :align: center

.. _getting-started-microservices-restAPI-requests:

Requests methods
^^^^^^^^^^^^^^^^
When communicating with the API we use requests methods such as **GET**, **POST**. For more request methods read `this <https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods>`__.

  * **GET**: The GET method request a representation of the data from a web resource, i.e. it reads data.
  * **POST**: The POST method request that the web resource accepts the data in the request, i.e. it writes data.

.. _getting-started-labs:

Labs
----

To do these labs you will need to have a Sesam node set up with the :download:`getting-started-config.json<files/getting-started-config.json>` configuration. If you have set up your datahub following the :ref:`guide <getting-started-upload-config>` you are ready to do these labs.

| **Naming pipes**
| As explained in this guide and our :ref:`Best Practice documentation <best-practice-naming-conventions>` we encourage creating pipe names from the type of object the pipe contains and the external system the data is imported from or to be exported to, i.e. "salesforce-user" or "event-bigquery". For some of the pipes we will create in these labs it can be difficult to give proper names as the pipes can be arbitrary and have no target system. In these cases it is OK to use the topic of the task as the pipe's object and simply "labs" as the target system when naming the pipe, i.e. "string-logic-labs".

| **Developer Guide**
| `The Developer Guide <https://docs.sesam.io/developer-guide.html>`__ section of the documentation will be an important resource when doing these labs, the tree first sub-sections of Service Configuration, Entity Data Model and Data Transformation Language in particular.

.. _getting-started-labs-basics:

Basics
======

Lab 1
^^^^^

**Copy from source**

If a pipe has no transform config it will copy all the attributes of an the entity from the source, but if it does then that config must specify which attributes to copy from the source. In many cases we want to keep all attributes from the source entity, but other times we might want a subset of the attributes or we want to make some changes to the attributes before we add them to the target entity. In most cases we want to keep the entity ID from the source dataset, so we also copy the ``_id`` system attribute. We can choose not to copy the ``_id`` if we want to handle entity ID in a different way, but all entities must have an ``_id`` of type string.

Task
++++

- Create a pipe with ``"_id": "order-anonymized-labs"``.
- Set source to be of type "dataset" and the dataset to "webshop-order".
- In the transform section, copy all properties from source except the ``customerId`` and ``customerId-ni`` attributes.
- Start the pipe and check the results in the "Output"-tab of the pipe. 

Tips

  - You can create a downstream pipe (a pipe that uses the dataset of the pipe you're currently viewing as its source) from the pipe menu. Click the three dots to the right of the pipe name to open the menu.
  - The templates avaiable on the pipe's "Config"-tab can help ease and speed up config creation. Add a transform config with the "Add DTL transform" button.
  - You can look up how the ``copy`` transform function in DTL works in the :ref:`documentation <dtl-transforms>`. You'll notice that like many other DTL functions it is more flexible than it looks:

    * ``["copy", "foo"]`` will copy the "foo" attribute.
    * ``["copy", "*"]`` will copy all attributes.
    * ``["copy", "*", "foo"]`` will copy all attributes except "foo".
    * ``["copy", ["list", "foo", "bar"]]`` will copy only the "foo" and "bar" attributes.
    * ``["copy", "*", ["list", "foo", "bar"]]`` will copy all attributes except "foo" and "bar".
    * ``["copy", "foo*"]`` will copy all attributes that have "foo" at the start of their name.

Lab 2
^^^^^

| **Add and remove attributes**
| **Variables _S and _T**
| **Sequential execution**

In the transform config part of the pipe config we can create new attributes in our resulting (target) entities with the ``add`` transform function and remove attributes with  the ``remove`` transform function. To refer to attributes on the source or target entity we can prefix the attribute with ``_S.`` or ``_T.`` respectively. 

Task
++++

- Create a pipe downstream from **crm-person** and copy only the ``_id`` from the source entity. 
- Add an attribute named ``address-from-source`` and populate it with the address found in **crm-person** using the ``_S.`` variable. 
- Then add ``address-from-target`` using the ``_T.`` variable to refer to the address attribute you just made.
- Finally remove the ``address-from-source`` attribute.

Tips

  - You can preview how a transform config will affect an entity using ``CTRL`` + ``Enter`` when in the editor of the "Config"-tab. Use the arrow buttons to navigate to a fitting entity, or enter its ``_id`` in the "Search ID" textbox.
  - There are other variables than the commonly used ``_S`` and ``_T`` variables. These can be looked up in the :ref:`documentation <variables>`.

Import data
===========

Lab 3
^^^^^

**Create a system**

A system in Sesam represents a computer system that can provide or receive data entities. Its task is to provide common properties and services that can be used by several data sources, such as connection pooling, authentication settings, communication protocol settings and so on. There are many different types of systems available in Sesam. And if we need a more customized system we can use a microservice from https://github.com/sesam-community or create a new one to run as a custom microservice system.

We are going to import data containing county and municipality information for Norway from an API (https://ws.geonorge.no/kommuneinfo/v1/fylkerkommuner) using a URL system in our Sesam node.

Task
++++

- Create a URL-system that connects to geonorge with the base URL "https://ws.geonorge.no/" as its ``url_pattern``. 
- Name the system "geonorge".

Tips

  - All systems are :ref:`documented <system_section>`.
  - You can select the "url prototype" system type template when creating the system config to help populate it.
  - The rest of the URL will be appended at the end of the ``url_pattern`` from an ``url`` parameter in the source of the input pipe. 
  - You can see whether the system is able to connect to the target on the "Status"-tab.

Lab 4
^^^^^

**Environment variables and secrets**

We can save environment variables and secrets in the hub through the 'Variables'-tab on the Datahub settings page. Variables and secrets saved there are globally accessible with syntax ``"$ENV(variable-name)"`` and ``"$SECRET(variable-name)"``. We can also store secrets that are exclusively accessible to a specific systen in that system's 'Secrets'-tab.

Task
++++

- Save the base URL of the geonorge-system as an environment variable in the datahub, and change the geonorge-system's ``url_pattern`` attribute to refer to that environment variable.

Lab 5
^^^^^

**Input pipe**

In an input pipe we specify where to get data from and through which system. And we often have to specify which attribute's value to use as our internal ``_id`` system attribute, which has to be a unique string per entity. We also add an attribute named ``rdf:type`` to each entity describing where the data comes from and what it is, which we use for filtering later downstream. But we will omit the ``rdf:type`` for now and come back to that later.

Task
++++

- Create an input pipe with ``_id`` "geonorge-county" that imports county data using the newly made "geonorge"-system. 
- Give the pipe a JSON source config and set its ``url`` to "kommuneinfo/v1/fylkerkommuner". 
- As there is no automatically identifiable ID in the data you will have to add a transform config in your pipe and in it ``add`` the ``_id`` attribute from the source data's "fylkesnummer" attribute (county number).
- ``copy`` all attributes from the source.

Tips

  - You can find the JSON source documented under Service Configuration in the Developer Guide section of the ducumentation.
  - The imported entities can be viewed in the "Output"-tab of the pipe and in the dataset of the same name. There should be 11 counties.
  - Check the "Execution Log"-tab to see whether the pipe ran successfully. It contains helpful information if you need to figure out why the pipe run did not yield the expected outcome.


Lab 6
^^^^^

**Conditional source**

We should be able to use the same exact pipe-configs on Sesam nodes in different environments. To support this in input pipes we use a conditional source with two alternative configs named "prod" and "test". We refer to the environment variable ``node-env`` as the condition to determine which source to use, which is set as either "prod" or "test" depending of the environment the node runs in. The source config for test should be an embedded type with a few test entities while the source config for prod refers to the external source system. See the **udir-postalcode** pipe for an example of this. We have set our ``node-env`` environment varible as "test" as we prepared for these labs.

Task
++++

- Make the source config for **geonorge-county** conditional and supply a few counties as embedded entities. The entities to embed can be taken from the output of the pipe as it previously ran with the production source, but to save time creating entities that match our person test data from other pipes we have created a :download:`list of entities <files/geonorge-county-test-data.json>` to embed. 
- Run the pipe and verify that it now outputs the embedded entities.

Tips

  - Always make sure to anonymize the test data and replace sensitive information.
  - Create embedded entities that will match and connect with test data from other input pipes. 
  - Try setting the ``node-env`` environment variable to "prod" and run both **geonorge-county** and **udir-postalcode**. Observe that they now import the full datasets from the external source. Set ``node-env`` back to "test" and run the pipes again to keep working with just test data.


Lab 7
^^^^^

**Global dataset**

We want to put all data in the datahub into a fitting global dataset, so there's a logical place to find it when needed. Our newly imported data represents counties, with their municipalities, and fits well in the **global-location** dataset.

Task
++++

- Add the new county data to the **global-location** dataset by adding the county dataset in the global's source datasets list. Note that the datasets listed need to have an alias as well, i.e. "udir-postalcode upc". Run the global pipe after adding the new dataset in its config.
- Create a new global pipe named **global-transaction**. Use a merge source and put **webshop-order** in its dataset property list. Remember to give the dataset an alias. Add a metadata config to the pipe's config at root level as ``"metadata": {"global": true}`` to give the pipe a global icon in the "Graph"-tab view.

Tips

  - Study **global-location** to create **global-transaction**, or even copy its config and change what you need.
  


Data Modelling
==============

Lab 8
^^^^^

| **Filtering entities**  
| **Global dataset as pipe source**
| **Pipe reset**

As explained in our :ref:`Best Practices <best-practice>` we want to use a global dataset as our data source when preparing data for export to another system. When we use a global dataset as a pipe's source we have to specify what data from that global dataset we want to use. We use the DTL transform function ``filter``, to select only the entities we want. The most common filtering we do is filter on ``rdf:type``, an attribute we add to the data as it enters Sesam to tag which system it comes from and what it contains. A filter on rdf:type can look like this:
::

  ["filter",
    ["in", "~:hr:person", "_S.rdf:type"]
  ]

This means an entity will be sent to the sink only if "~:hr:person" is found in the ``rdf:type`` attribute. Entities that do not have "~:hr:person" in the rdf:type will be excluded from our resulting data.

Something to note when we change the transform config of a pipe is that data previously processed by the pipe will remain unchanged unless we pump it through the pipe again with the new transform config. We need to reset the pipe if we want all data output to be processed the same way. The "Restart"-option in the pipe menu conveniently triggers both a "Reset" and a "Start" command on the pipe.

Task
++++

1. Create a pipe with **global-person** as the source dataset. Do not include a transform section in the pipe. 
2. Observe that the pipe outputs all the same entities as **global-person** in its "Output"-tab.
3. Add a transform to the pipe config with ``["copy, "*"]`` and ``["filter", ["in", "~:hr:person", "_S.rdf:type"]]``. 
4. Restart the pipe. Observe that there are now only 10 entities in the output, and that they all contain data from "hr-person".
5. Change the filter to keep only entities that have data from the **crm-person** dataset.
6. Restart the pipe and observe that you now have 10 entities which all have data from **crm-person**. This should not be the exact same 10 entities as before.

Tips

  - The entities you find in the "Output"-tab of the pipe are the same as the entities in the dataset with the same name. The entities in the "Latest" category is the current dataset. In "Latest w/ deleted" you will also find the hr-person entities som the first pipe run. In the "All" category you will find previous versions of all entities as well as the current and deleted entities.
  - The number of previous entities to keep is two by default and can be changed with a :ref:`compaction <pipe_compaction>` config.
  - When in the config editor use ``Alt`` + ``.`` to reformat the config and display it with correct line breaks and whitespace for improved readability.

Lab 9
^^^^^

**Namespaces**

By default attributes in Sesam have a namespace as a prefix to the attribute name, separated with a colon. This namespace is a string that by default contains the name of the pipe where the attribute was created. For data that we import from external systems this means the name of the input pipe. We can use this namespace to distinguish between attributes with the same name that originate from different sources.

Task
++++

- Create a pipe downstream from **global-person**. 
- Copy only the ``_id`` and ``hr-person:StreetAddress``.
- Add one attribute containing ``StreetAddress`` from **erp-person** and another with ``Address`` from **crm-person**.
- Note that the namespace of the added attributes refer to the new pipe. This is different from attributes that are copied from the source dataset, which keep their original namespace from the source.  

Lab 10
^^^^^^

**Lists**

Lists are a common collection type to work with in Sesam. Source data can contain lists, merges can result in joined attributes becoming lists and we can structure data in lists through DTL to provide as output or to use as input in other DTL-functions.

Task
++++

- Create a pipe with the config provided below.

::

  {
    "_id": "list-labs",
    "type": "pipe",
    "source": {
      "type": "embedded",
      "entities": [{
        "_id": "1"
      }]
    }
  }

- Give it a transform config and ``add`` a list containing strings "a", "b", "c" and "d" using the ``list`` function.
- Use this list for the following sub-tasks in which you create new attributes containing:

  - the first string element in the list.
  - the 3rd string element in the list.
  - the number of elements in the list.
  - the original list, but with the string "e" inserted as the second element.
  - the same list as in the previous sub-task, but sorted alphabetically.

Tips

  - All the functions needed for this lab, and many more, are found in the docs' :ref:`DTL Reference Guide <DTLReferenceGuide>` under "Values/collections".


Lab 11
^^^^^^

**Golden records**

In globals we often have data from different sources describing the same characteristic of an object. To avoid having to research which data is most reliable every time we need to use that data, we can create a golden record which is populated with the most reliable version of that data that is available on the object in the global. We can later use that golden record attribute downstream and not have to make the same prioritization each time we need that data.

Task
++++

- Create a new golden record attribute named ``email`` in **global-person** where you rank the data quality of the email address from **crm-person** the highest, **salesforce-userprofile** the 2nd most and **hr-person** the least.

Tips

  - Look up the ``coalesce`` function in the docs or look at its use in **global-person**.
  - Restart pipes after making changes to their transform config if you want its dataset to reflect the new config.

Lab 12
^^^^^^

| **Casting**
| **Number logic**    
| **Nested functions**

We can cast an attribute as different types, like integer, string, datetime and others described in the docs. 

When working with numbers we have a set of functions and operators that we can apply to the numeric values. These are documented in the DTL Reference Guide under "Math". Different functions for casting can be found under "Numbers", "Strings" and other headers regarding data types. 

To do successive actions on a value we nest functions within eachother. We use the result of one function as an input parameter of another, like so:

::

  ["add", "foo",
    ["first",
      ["split", "-", "bar-bell"]
    ]
  ]

To follow a value through complex logic you often read the config from right to left. I.e. we have a string of "bar-bell". We then split the string at the hyphen to get two strings in a list (``["bar", "bell"]``). Then we select the first object in the list and we add that as ``foo`` to end up with a key + value pair of ``"foo": "bar"``.

Task
++++

- Create a pipe with **erp-person** data. Make the pipe downstream from **erp-person** or preferrably downstream from **global-person** and filter the entities that do not contain **erp-person** data (filter on ``rdf:type``).
- Imagine a new order has come in for everyone in this dataset, and increase the number of ``TimesOrdered`` by one. As this attribute is a string in the source data it needs to be cast to integer before we can increase the value. Cast the result back to string and add it to the entity as a new ``TimesOrdered`` attribute which will get its namespace from the new pipe.

Lab 13
^^^^^^

**String logic**

In Sesam's DTL there are many functions available for working with :ref:`strings <string_dtl_function>`. Let's try working wuth some of them. 

Task
++++

- Create a pipe with **hr-person** data. 
- Create an attribute for each of the subtasks below containing:

  - only the prefix of the email address. Look up the ``split`` and ``first`` functions. 
  - the person's surname in only capital letters. Look up ``upper`` in the docs.
  - the date of birth of the person in the format of "dd.mm.yy" extrapolated from ``SSN``. Look up ``substring`` and ``concat`` or ``join`` in the docs.
  - the title of the person without any punctuation at the end. Look up the use of the ``strip`` functions.

Tips

  - The first two digits of a SSN represent the day, the next two digits represent the month and then the next two represent the year.


Lab 14
^^^^^^

**Datetime logic**

Sesam provides a toolkit for working with date and time values, just like it does for string and number logic. These DTL-functions can be found in the docs too! With ``datetime-parse"`` we can translate strings to datetime values, while ``datetime-format`` translates datetime values to strings. ``datetime-diff``, ``datetime-plus`` and ``datetime-shift`` lets us do calculation and manipulation of datetime values.

Task
++++

- Create a pipe containing the entities from **webshop-orders**. 
- Use datetime logic on the ``orderPlaced`` attribute from source, to create additional attributes containing
  
  - ``orderPlaced`` as a datetime value.
  - ``orderPlaced`` as a string containing its date in the "dd.mm.yyyy" format.
  - a datetime value of 72 hours after the order was placed.
  - the number of days since the order was placed.

Tip

  - For the last task use the ``now`` function when calculating how much time has passed.


Lab 15
^^^^^^

| **If**
| **Comparisons**

With DTL we can perform logic with checks and comparisons as well. Let's look at the ``if`` function and the comparison functions we have available.

Task
++++

- Create a pipe that checks entities from **erp-person** using the ``if`` function to see if they have a 10 000 or higher spending according to their ``MoneyUsed`` attribute. Add the attribute ``big-spender`` as a boolean true or false depending on the result.

Tips

  - Look up the ``if`` function and the various comparisons in the :ref:`docs <eq_dtl_function>`.
  - You will have to cast the ``MoneyUsed`` value to a numeric type, i.e. integer, to get a correct result from the comparison.
  - You can perform more than one action as the result of an ``if`` by placing them within square brackets to make it a list of actions in the then or else argument of an if. Test it by adding another attribute along with ``big-spender``, like ``"foo": "bar"``.

Lab 16
^^^^^^

**Filter**

There are two ``filter`` functions in Sesam's DTL. In this task and when we filter entities on ``rdf:type`` we use the transform function. Transform functions are the functions that can add or remove attributes to the entities, which in this case adds an internal system attribute (``"_filtered": true``) to the entity. The other filter function is found under Values/Collections in the docs and is used to filter values that do not match a certain criteria when we perform logic on data within a transfom function.

If we use the ``filter`` transform function without any input parameter we filter out the entitiy we're currently processing unconditionally. We can provide a function as an "unless"-condition, and the entity will only be filtered if that function returns true. We have already used this filter function to filter entities from a global dataset source based on ``rdf:type``. ``["filter", ["in", "~\:hr:person", "_S.rdf:type"]]`` reads "Filter, unless '~:hr:person' is in the 'rdf:type'-list".

Task
++++

- Create a pipe with **global-person** as its source.
- Use the filter function to keep only the females.
- Add another filter, or add another condition in the first filter, that filters out anyone who does not have "dayrep.com" as their email postfix.

Tips

- The ``discard`` transform function is similar to the ``filter`` transform function. But ``discard`` will drop the entity completely and not send it to the sink at all, while the ``filter`` function adds ``_filtered`` as true to the entity and lets the entity pass to the sink. If an entity already exists in the pipe's dataset from previous runs, but is updated with ``"_filtered": true`` it will be deleted from the dataset (receive ``"_deleted": true``). With ``discard`` that same entity would stay unchanged in the pipe's dataset. If a filtered entity does not alreay exist in the dataset it will not be written to the dataset by the sink.

Lab 17
^^^^^^

**Apply**

The transform section of a pipe config contains a ``default`` rule. The logic in this rule will execute on the pipe's source entity. We can make additional rules and in the default rule select data to pass through those custom named rules with an ``apply`` function. By passing entities or lists through a rule we can achieve a loop-like behavior where the transforms of the rule is applied to each item of the entity or list individually. Additional rules can also help section and organize a long pipe config.

Task
++++

- Create a pipe with the config provided below. 

::

  {
    "_id": "apply-labs",
    "type": "pipe",
    "source": {
      "type": "embedded",
      "entities": {
        "_id": "1",
        "list": ["some string", false, "another string", 45678908765, "abcd", "STRING", true, null, "132456"]
      }
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*"]
        ]
      }
    }
  }

- Expand the transform config. Use ``apply`` with a ``merge-union`` transform function to run the ``list`` items through another rule. 
- Have that rule keep the string-objects and not save anything else. Within that rule the data sent to it is accessible through ``_S``. Use ``if`` to check the object with ``is-string``. Keep a string by adding it with ``["add", "result", "_S."]`` if ``is-string`` returns true. The rule you call with the apply must exist inside the ``rules`` dictionary of the pipe config, just like the ``default`` rule does.

Tips

  - Try swapping ``merge-union``  with ``merge`` or ``add`` to see the difference in how the resulting data is structured as it is returned and added to the target entity.

Lab 18
^^^^^^

| **Create-child**
| **Emit_children**
| **Chained transforms**

We can emit new, standalone entities from a set of values on an entity. This can be done either with the ``create`` or ``create-child`` transform functions. ``create`` will emit and send the new standalone entities to the pipe's sink, while ``create-child`` will add them in a ``$children`` attribute on the original entity. We can then pass the original entity through an ``emit_children`` transform to write them as standalone entities to a dataset. The new entities must have their own valid ``_id``. 

So far we have only been using a ``DTL`` transform in our pipes. There are other :ref:`transforms <transform_section>` that do different things. The emit children transform will produce standalone entities from the contents of ``$children`` attribute of an entity and discard the original entity. The HTTP transform can send the entities to an external HTTP endpoint for transformation and recieve data back. You can have a conditional transform just like we have conditional source, and you can chain multiple transforms in one pipe.

The counties we imported from geonorge earlier in these labs each include a list of municipalities. Let's emit these municipalities as their own entities using ``create-child`` and an emit children transform that we chain after the DTL transform where we create the ``$children``.

Task
++++

- Make a pipe downstream from geonorge-county and name it geonorge-municipality.
- Give it a chained transform with a DTL transform first and an emit children transform second. 
- In hte DTL transform first add ``["filter", ["neq", "_S._deleted", true]]`` to remove ``_deleted`` entities, as the emit children transform would also emit children from those. 
- As the municipalities listed in the counties do not have an "_id" already we need to add that before put them in ``$children``. In the DTL transform have a ``create-child`` transform function take the results of an ``apply`` as its argument. The ``apply`` function should pass the list-attribute "_S.kommuner" (municipalities) through a rule in which we build our new entities. In that rule 

  - copy all attributes that are passed to the rule in the "kommuner" list object with ["copy", "*"]
  - add "_id" from "_S.kommunenummer" (municipality number)
  - add "rdf:type" as ["ni", "geonorge", "municipality"] to use for filtering downstream when we are to use this data later.
- Run the pipe and confirm that it outputs municipalities.
- Finaly, add the new municipality dataset to **global-location**'s' source dataset list and run the global pipe.

Lab 19
^^^^^^

**Namespaced Identifiers**

To make it easier to join data from different datasets we add a namespaced identifier based on an attribute is equal to the _id in the other dataset. This can be viewed as similar to setting a foreign key in one table that relates to the primary key of another table in an SQL-database. If we make a namespaced identifier (NI) on a ``customer-id`` attribute of an entity in an orders dataset we can then use that NI attribute when obtaining data from that order's customer when joining data using hops. 

We have seen the NI attribute ``rdf:type`` on all the entities in our Sesam hub in these labs. This attribute is used to filter entities downstream, like we have been doing.

Look up the ``ni`` function in the Developer Guide. You can also read more about namespaced identifiers in the :ref:`Best Practice <best-practice-namespaced-identifiers>` section of the docs.

Task
++++

- Add a NI as ``municipality-ni`` in **udir-postalcode** based on the ``municipality`` attribute in the postalcode entity. In the ``ni`` function supply the namespace string "geonorge-municipality" and refer to the ``municipality`` attribute for the value.
- Add ``rdf:type`` using the ``ni`` function in geonorge-county.

Tips

  - Once we have made a NI attribute that refers to an entity in another dataset we can look up that entity when browsing its dataset by pasting the NI-attribute value as id to search in the dataset browser (or the "Output"-tab of the dataset's pipe).

Lab 20
^^^^^^

**Hops**

With the ``hops`` function we can reach data outside of the entity we're currently processing. The function takes a dictionary as its only argument, the hops spec. In that dictionary we specify which datasets to join on which attributes. We can also specify what attribute or expression we want returned from the hops, if not the whole entity is returned. If a pipe joins data from multiple datasets Sesam builds an index on the specified properties. You can read more about hops and how joins work in the :ref:`Developer Guide <path_expressions_and_hops>`. It is considered good practice to hop to a global dataset when possible, instead of other datasets that contain the data we need. 

Task
++++

- Create a pipe containing the people from **erp-person**.
- Use the ``hops`` function to access the **webshop-order** data through the **global-transaction** dataset and from that add a list of IDs of items the person has ordered. The ``where`` parameter of the hops spec shoould be an ``eq`` comparison between ``$ids`` of the pipe's source and the ``customerId-ni`` of the order dataset.
- Specify the item ID attribute of the order in the hops spec's ``return`` parameter.

Tips

  - Look up ``hops`` in the Developer Guide. The hops spec has many optional parameters, only ``datasets`` and ``where`` are required.
  - You can see an example of hops in use in the **person-address-csv** pipe in your datahub.
  - If you set **erp-person** as the source of your pipe you can join the datasets on erp-person's ``_id`` and webshop-order's ``customer-id``. But if you set **global-person** as your pipe source and used filter to get only the erp-person entities (as is recommended) those entities' ``_id`` may not be the ``_id`` of **erp-person**, and the comparison will fail. However, on the **global-person** entity there is a ``$ids`` attribute containing all ``_id``\s of the merged person entities in a list of namespaced identifiers. Base the join expression of the ``where`` parameter on ``$ids`` when possible when working with merged entities.

Lab 21
^^^^^^

**Apply-hops**

In some cases we want to apply some transforms to the results of a hops before we return it to the root entity. We can use the ``apply-hops`` function to run the results from the hops through a specified rule before returning. This can be used to traverse a list or entity, for example to filter the elements of the list that are not relevant. Within the rule called by the apply we can also do new hops to join data from other datasets based on the data returned from the initial hops.

Task
++++

- Create a pipe with **global-person** as its source. Make a ``merge`` transform function with an ``apply-hops`` to the **global-location** dataset. Set the join expression ``eq`` function to compare ``global-person:zipcode`` and ``udir-postalcode:postalcode``.
- In the rule called by the ``apply-hops``, add an attribute named "location" which should be a concatinated string that states the number of the municipality in which the postal city is located, i.e. "Oslo is located in municipality number 0301".
- Inside the newly made custom rule ``merge`` another ``apply-hops`` to the related **geonorge-municipality** entity in **global-location**. Since we have already made ``municipality-ni`` in **udir-postalcode** we can compare that to the ``$ids`` of the **global-location** municipalities in the join expression.
- Check if the municipality is located north of the arctic cirle by checking if the last number, the latitude, in ``punktIOmrade.coordinates`` (pointInArea) is 66.33 or bigger. Add ``arctic-municipality`` as true or false.

Export data
===========

How we export data from Sesam depends on the target system. For many databases, APIs and other targets there are ready-made connectors in Sesam. These are available as systems and can be created using templates which you fill in with the required connection info to serve as your connection to the external system. Previously in these labs we set up a URL-system in our Sesam node to import data from geonorge.no. If a system in Sesam is connected to an external system that we can write to, we can reference that system in an output pipe's sink to use it for writing data. If we need to connect to a system that is not supported out-of-the-box or do operations that are not supported we can create and run a custom microservice as a system, used with a JSON push sink. You can find open-source, community developed microservices at https://github.com/sesam-community. We can also expose data directly in an HTTP publisher endpoint as JSON, CSV or XML without any system, just using a sink.

You will find documentation for the systems and sinks on the Developer Guide's :ref:`Service Configuration <configuration>` page.


Lab 22
^^^^^^

**CSV endpoint**

Task
++++

- Create a preperation pipe, a pipe with entities that will be exported or exposed in an output pipe downstream. Populate the preperation pipe with entities of your choosing. Make sure to stick to naming conventions and name it after the type of object it contains and the target system (in this case the system is simply "csv") i.e. "orders-csv".
- Create an output pipe downstream with a CSV sink. Name this pipe the same as its preperation pipe, but with an "-endpoint" postfix, i.e. "orders-csv-endpoint".
- Download the .csv file from the pipe's "Output"-tab and verify its content.

Tips

  - You can find the sink config template under the "Target" header in templates. Choose system "system:sesam-node" and sink "csv_endpoint prototype".
  - Note that you can retrieve the entities with the cURL provided in the Output-tab. This cURL contains a JWT (JSON Web Token) for authentication. You can also create a shareable link for use without access to the Sesam portal. 

Lab 23
^^^^^^

| **HTTP endpoint**
| **JWT**

Task
++++

- Create a similar data flow as in the previous lab, but this time use an HTTP sink in the output pipe. Stick to naming conventions.
- Create a JWT of your own in the datahub's subscription page. Using this bearer token as authentication, retrieve the data through a GET-request to the ".../entities"-URL exposed by the http-sink.

Tips

  - You can send the GET-request with cURL, Postman (or your favorite alternative), write a microservice that fetches the data or import the data from another service or system capable of sending HTTP-requests that you may be looking to integrate with Sesam.
  - The "Output"-tab of the output pipe provides what's needed to retrieve the data.


Lab 24
^^^^^^

**Export to SQL-database**

SQL databases are common target systems for data export from Sesam. There are a few different SQL systems available in sesam and all of them are used togother with the SQL sink when exporting data. For the following task you need an SQL database to write to. If you don't have one at hand there are free online database services where you can set up a database using a trial account. https://www.elephantsql.com/ is one where you can set up a postgresql database.

Task
++++

Write entities to a table in an SQL database. Follow the steps below:

1. Create an SQL system in Sesam that is of the same type as your database and supply the connection info needed in the template system config. Put passwords or auth tokens for your system in the datahub's secrets and refer to those in your system config. In many cases it is advisable to store other connection info values as environment variables in the datahub. You can verify that the system is able to connect on its Status-tab.

2. Create a person table in your database with columns as specified in the SQL query below:

::

  CREATE TABLE person (
  _id varchar(50) PRIMARY KEY,
  firstname varchar(50),
  lastname varchar(50),
  address varchar(100)
  );

3. Create a preperation pipe downstream from **global-person** and have it copy this list of attributes: ``["list", "_id", "global-person:firstname", "global-person:lastname", "global-person:address"]``.

4. Create an output pipe downstream from the preperation pipe with an SQL sink that refers to the newly created system and the "person" table. Make sure to add a pump config in which ``"mode"`` is set to ``"ENV(pump-mode)"``, which in turn is set to "manual" in the datahub environment variables.

5 Send your data to the database table by starting the output pipe. Check the execution log of the pipe to see how it ran. These logs are the first place to look for clues of what went wrong in a failed run. Verify that the entities have been written to the table in your database. If you need to run a query to view the data in the database, you can run ``select * from person;``.

Tips

  - The system config will be different depending on what type of database you are connecting to. Selecting a template will help with config creation. The Developer Guide also have full descriptions of the possible parameters of your system config. In many cases copying the "Example config" from the docs or selecting a config template and filling in the values to match your database server and authentication will be sufficient.
  - The SQL sink also has a lot of parameters for customizing your SQL operations, like the possibility to define a table's columns in ``schema_definition`` and creating the table on a first run or a reset of the output pipe. Only the parameters "type", "system" and "table" are required.
  - The ``pump-mode`` environment variable is used to make sure an output pipe in a non-production environment does not export data unless the pipe is started manually. In a production environment ``pump-mode`` would be set as "scheduled" and the pipe's pump config would include a "cron-expression" or "schedule_interval" that specifies when to run. 


Lab 25
^^^^^^

**Export to API**

API's are another common external system type that Sesam integrates with. Let's try posting some data to jsonplaceholder.typicode.com, which is a API containing test data that we can also post data to. The data will not actually be saved and stored, but the status codes that the API returns are the same as if it did. The operation we want to imitate is described on this page https://jsonplaceholder.typicode.com/guide.html under "Create a resource".

Task
++++

- POST entities to an API. Follow the steps below:

1. Create a URL system in Sesam named "typicode" with the base url ``"https://sonplaceholder.typicode.com/%s"`` as its ``url_pattern``. Store the url as an environment variable and refer to that in the system config.

2. Create a preparation pipe with some entities. You can for example copy the config of the preparation pipe of the previous task. Just remember to have the newly created system in the pipe name.

3. Create an output pipe with a JSON push sink. The sink needs to refer to the ``"typicode"`` system and have``"posts"`` as the ``url`` to append to the ``url_pattern`` of the system. Remember to set the pump's mode to the ``pump-mode`` encvironment variable.

4. Run the output pipe and make sure you get a "pump-completed" entry in the execution log of the pipe.

Tips

  - The URL system has more available parameters than we need for this test, i.e. for authentication. The REST system further expands the ability to customize our integrations with APIs.

Learn more
==========

We encourage you to play around and test more imports, transformations, enrichment and exports of data. Here are a few suggestions for what to do next.


- Get the data you exported back from your SQL database.
- Import some of the test data available at http://jsonplaceholder.typicode.com.
- Create an item dataset related to the webshop-orders in an input pipe with embedded source. Give some of the items IDs that correspond to the webshop-order dataset. Find or create a suitable global dataset to put the items in. Create payloads that combine data from people or orders with data from the item-entities.
- Export data to an external system you have access to and can test with.
- Try more DTL-functions like
  
  - ``dict``
  - ``case``
  - ``case-eq``
  - ``matches``
  - ``intersects/intersection``
  - ``map``
  - ``key-values``
  - ``discard``
  - ``default``
  - ``rename``
  - ``make-ni``
  - ``ni-is and ni-id``
  - ``all and any``
  - ``and and or``
  - ``encrypt``
  - ``path``

Solution examples
=================

As with most programming there are usually more ways than one to reach a certain outcome. Below are suggestions for how to solve the labs in this guide, but keep in mind other approaches might be just as viable.

Lab 1
^^^^^
Pipe config:
::

  {
    "_id": "order-anonymized-labs",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "webshop-order"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*", "customerId*"],
          ["comment", "Alternative solutions that produce the same results are shown in the comments below"],
          ["comment",
            ["copy", "*",
              ["list", "customerId", "customerId-ni"]
            ]
          ],
          ["comment",
            ["copy",
              ["list", "_id", "id", "itemId", "orderPlaced", "quantity"]
            ]
          ],
          ["comment",
            ["copy", "_id"],
            ["copy", "id"],
            ["copy", "itemId"],
            ["copy", "orderPlaced"],
            ["copy", "quantity"]
          ]
        ]
      }
    }
  }

Result:

.. image:: images/getting-started/labs/lab-copy-from-source.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab

Lab 2
^^^^^
Pipe config:
::

  {
    "_id": "add-remove-labs",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "crm-person"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "_id"],
          ["add", "address-from-source", "_S.Address"],
          ["add", "address-from-target", "_T.address-from-source"],
          ["remove", "address-from-source"]
        ]
      }
    }
  }

Result:

.. image:: images/getting-started/labs/lab-add-remove.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab

Lab 3
^^^^^
System config:
::

  {
    "_id": "geonorge",
    "type": "system:url",
    "url_pattern": "https://ws.geonorge.no/%s",
    "verify_ssl": true
  }

Lab 4
^^^^^
System config:
::

  {
    "_id": "geonorge",
    "type": "system:url",
    "url_pattern": "$ENV(geonorge-baseurl)",
    "verify_ssl": true
  }

Environment variables:
::

  {
    "geonorge-baseurl": "https://ws.geonorge.no/%s",
    "node-env": "test",
    "pump-mode": "manual",
    "udir-baseurl": "https://data-nxr-fellestjeneste.udir.no/api/%s"
  }

Effective system config:
::

  {
    "_id": "geonorge",
    "connect_timeout": 60,
    "read_timeout": 1800,
    "type": "system:url",
    "url_pattern": "https://ws.geonorge.no/%s",
    "verify_ssl": true
  }

Lab 5
^^^^^
::

  {
    "_id": "geonorge-county",
    "type": "pipe",
    "source": {
      "type": "json",
      "system": "geonorge",
      "url": "kommuneinfo/v1/fylkerkommuner"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*"],
          ["add", "_id", "_S.fylkesnummer"]
        ]
      }
    }
  }

.. image:: images/getting-started/labs/lab-input-pipe.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab

Lab 6
^^^^^
::

  {
    "_id": "geonorge-county",
    "type": "pipe",
    "source": {
      "type": "conditional",
      "alternatives": {
        "prod": {
          "type": "json",
          "system": "geonorge",
          "url": "kommuneinfo/v1/fylkerkommuner"
        },
        "test": {
          "type": "embedded",
          "entities": [{...},{...}]
          }]
        }
      },
      "condition": "$ENV(node-env)"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*"],
          ["add", "_id", "_S.fylkesnummer"]
        ]
      }
    }
  }

The embedded entities are removed in this code snippet for brevity. They are found in the lab task text.

.. image:: images/getting-started/labs/lab-conditional-source.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab

Lab 7
^^^^^
::

  {
    "_id": "global-location",
    "type": "pipe",
    "source": {
      "type": "merge",
      "datasets": ["udir-postalcode upc", "geonorge-county gnc"],
      "identity": "first",
      "version": 2
    },
    "metadata": {
      "global": true
    }
  }

::

  {
    "_id": "global-transaction",
    "type": "pipe",
    "source": {
      "type": "merge",
      "datasets": ["webshop-order wo"],
      "identity": "first",
      "version": 2
    },
    "metadata": {
      "global": true
    }
  }

Lab 8
^^^^^
::

  {
    "_id": "filter-entities-labs",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "global-person"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*"],
          ["filter",
            ["in", "~:crm:person", "_S.rdf:type"]
          ]
        ]
      }
    }
  }

.. image:: images/getting-started/labs/lab-filter-entities.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab

Lab 9
^^^^^
::

  {
    "_id": "namespace-labs",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "global-person"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy",
            ["list", "_id", "hr-person:StreetAddress"]
          ],
          ["add", "erp-address", "_S.erp-person:StreetAddress"],
          ["add", "crm-address", "_S.crm-person:Address"]
        ]
      }
    }
  }

.. image:: images/getting-started/labs/lab-namespaces.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab

Lab 10
^^^^^^
::

  {
    "_id": "list-labs",
    "type": "pipe",
    "source": {
      "type": "embedded",
      "entities": [{
        "_id": "1"
      }]
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "_id"],
          ["add", "list",
            ["list", "a", "b", "c", "d"]
          ],
          ["add", "first-item",
            ["first", "_T.list"]
          ],
          ["add", "3rd-item",
            ["nth", 2, "_T.list"]
          ],
          ["add", "count",
            ["count", "_T.list"]
          ],
          ["add", "inserted-item",
            ["insert", 1, "_T.list", "e"]
          ],
          ["add", "sorted",
            ["sorted", "_T.inserted-item"]
          ]
        ]
      }
    }
  }

.. image:: images/getting-started/labs/lab-list.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab

Lab 11
^^^^^^
::

  {
    "_id": "global-person",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "merged-person"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*"],
          ["add", "firstname",
            ["coalesce",
              ["list", "_S.hr-person:GivenName", "_S.crm-person:FirstName", "_S.erp-person:GivenName"]
            ]
          ],
          ["add", "middle-initial",
            ["coalesce",
              ["list", "_S.hr-person:MiddleInitial", "_S.crm-person:MiddleInitial", "_S.erp-person:MiddleInitial"]
            ]
          ],
          ["add", "lastname",
            ["coalesce",
              ["list", "_S.hr-person:Surname", "_S.crm-person:LastName", "_S.erp-person:Surname"]
            ]
          ],
          ["add", "fullname",
            ["join", " ",
              ["list", "_T.global-person:firstname",
                ["if",
                  ["is-not-null", "_T.global-person:middle-initial"],
                  ["concat", "_T.global-person:middle-initial", "."]
                ], "_T.global-person:lastname"]
            ]
          ],
          ["add", "address",
            ["coalesce",
              ["list", "_S.crm-person:Address", "_S.hr-person:StreetAddress", "_S.erp-person:StreetAddress"]
            ]
          ],
          ["add", "zipcode",
            ["coalesce",
              ["list", "_S.hr-person:ZipCode", "_S.crm-person:PostalCode", "_S.erp-person:ZipCode"]
            ]
          ],
          ["add", "country",
            ["coalesce",
              ["list", "_S.hr-person:Country", "_S.erp-person:Country"]
            ]
          ],
          ["add", "gender",
            ["coalesce",
              ["list", "_S.hr-person:Gender", "_S.crm-person:Gender", "_S.erp-person:Gender"]
            ]
          ],
          ["add", "email",
            ["coalesce",
              ["list", "_S.crm-person.EmailAddress", "_S.salesforce-userprofile:EmailAddress", "_S.hr-person:EmailAddress"]
            ]
          ]
        ]
      }
    },
    "metadata": {
      "global": true
    }
  }


.. image:: images/getting-started/labs/lab-golden-record.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab

Lab 12
^^^^^^
::

  {
    "_id": "casting-labs",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "global-person"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["filter",
            ["in", "~:erp:person", "_S.rdf:type"]
          ],
          ["copy",
            ["list", "_id", "erp-person:*"]
          ],
          ["add", "TimesOrdered",
            ["string",
              ["plus", 1,
                ["integer", "_S.TimesOrdered"]
              ]
            ]
          ]
        ]
      }
    }
  }

.. image:: images/getting-started/labs/lab-casting.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab

Lab 13
^^^^^^
::

  {
    "_id": "string-logic-labs",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "global-person"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["filter",
            ["in", "~:hr:person", "_S.rdf:type"]
          ],
          ["copy",
            ["list", "_id", "hr-person:*"]
          ],
          ["add", "email-prefix",
            ["first",
              ["split", "@", "_S.hr-person:EmailAddress"]
            ]
          ],
          ["add", "capital-surname",
            ["upper", "_S.hr-person:Surname"]
          ],
          ["add", "date-of-birth",
            ["join", ".",
              ["list",
                ["substring", 0, 2, "_S.hr-person:SSN"],
                ["substring", 2, 4, "_S.hr-person:SSN"],
                ["substring", 4, 6, "_S.hr-person:SSN"]
              ]
            ]
          ],
          ["add", "title",
            ["rstrip", ".", "_S.hr-person:Title"]
          ]
        ]
      }
    }
  }

.. image:: images/getting-started/labs/lab-strings.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab

Lab 14
^^^^^^
::

  {
    "_id": "datetime-labs",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "global-transaction"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["filter",
            ["in", "~:webshop:order", "_S.rdf:type"]
          ],
          ["copy",
            ["list", "_id", "orderPlaced"]
          ],
          ["add", "orderPlaced-datetime",
            ["datetime-parse", "%Y-%m-%d %H:%M:%S", "_S.orderPlaced"]
          ],
          ["add", "orderPlaced-date",
            ["datetime-format", "%d.%m.%Y", "_T.orderPlaced-datetime"]
          ],
          ["add", "orderPlaced-plus72h",
            ["datetime-plus", "hour", 72, "_T.orderPlaced-datetime"]
          ],
          ["add", "orderPlaced-days-since",
            ["datetime-diff", "day",
              ["now"], "_T.orderPlaced-datetime"]
          ]
        ]
      }
    }
  }

.. image:: images/getting-started/labs/lab-datetime.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab

Lab 15
^^^^^^
::

  {
    "_id": "comparison-labs",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "global-person"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["filter",
            ["in", "~:erp:person", "_S.rdf:type"]
          ],
          ["copy",
            ["list", "_id", "erp-person:*"]
          ],
          ["if",
            ["gte",
              ["integer", "_S.MoneyUsed"], 10000],
            [
              ["add", "big-spender", true],
              ["add", "foo", "bar"]
            ],
            [
              ["add", "big-spender", false],
              ["add", "foo", "bar"]
            ]
          ],
          ["comment", "alternative code below",
            ["add", "big-spender",
              ["if",
                ["gte",
                  ["integer", "_S.MoneyUsed"], 10000], true, false]
            ]
          ]
        ]
      }
    }
  }

.. image:: images/getting-started/labs/lab-comparisons.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab

Lab 16
^^^^^^
::

  {
    "_id": "filter-labs",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "global-person"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*"],
          ["filter",
            ["and",
              ["eq", "_S.global-person:gender", "female"],
              ["eq",
                ["last",
                  ["split", "@", "_S.global-person:email"]
                ], "dayrep.com"]
            ]
          ]
        ]
      }
    }
  }

.. image:: images/getting-started/labs/lab-filter.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab


Lab 17
^^^^^^
::

  {
    "_id": "apply-labs",
    "type": "pipe",
    "source": {
      "type": "embedded",
      "entities": {
        "_id": "1",
        "list": ["some string", false, "another string", 45678908765, "abcd", "STRING", true, null, "132456"]
      }
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*"],
          ["merge-union",
            ["apply", "type-check", "_S.list"]
          ]
        ],
        "type-check": [
          ["if",
            ["is-string", "_S."],
            ["add", "result", "_S."]
          ]
        ]
      }
    }
  }

.. image:: images/getting-started/labs/lab-apply.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab

Lab 18
^^^^^^
::

  {
    "_id": "geonorge-municipalities",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "geonorge-county"
    },
    "transform": {
      "type": "chained",
      "transforms": [{
        "type": "dtl",
        "rules": {
          "default": [
            ["filter",
              ["neq", "_S._deleted", true]
            ],
            ["copy", "_id"],
            ["create-child",
              ["apply", "build-municipality", "_S.kommuner"]
            ]
          ],
          "build-municipality": [
            ["copy", "*"],
            ["add", "_id", "_S.kommunenummer"],
            ["add", "rdf:type",
              ["ni", "geonorge", "municipality"]
            ]
          ]
        }
      }, {
        "type": "emit_children"
      }]
    }
  }

.. image:: images/getting-started/labs/lab-create-child.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab

Lab 19
^^^^^^
::

  {
    "_id": "udir-postalcode",
    "type": "pipe",
    "source": {
      "type": "conditional",
      "alternatives": {
        "prod": {
          "type": "json",
          "system": "udir",
          "url": "v1/postnummerdata"
        },
        "test": {
          "type": "embedded",
          "entities": [{...},{...}]
        }
      },
      "condition": "$ENV(node-env)"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["comment", "The discard and renames in this pipe is done to simplify and translate the dataset for this guide"],
          ["discard",
            ["and",
              ["in", "_S.FylkeNummer",
                ["list", "03", "11", "15", "18", "30", "34", "38", "42", "46", "50", "54"]
              ],
              ["is-null", "_S.ArvtakerPostnummerDataIdListe"]
            ]
          ],
          ["add", "_id", "_S.PostNummer"],
          ["rename", "KommuneNummer", "municipality"],
          ["rename", "PostNummer", "postalcode"],
          ["rename", "PostSted", "city"],
          ["add", "rdf:type",
            ["ni", "udir", "postalcode"]
          ],
          ["add", "municipality-ni",
            ["ni", "geonorge-municipality", "_T.municipality"]
          ]
        ]
      }
    }
  }

Because the "municipality" attribute is a rename from a differently named attribute in the source we have used the "_T" variable to refer to it. Refering to "_S.KommuneNummer" would yield the same result.

.. image:: images/getting-started/labs/lab-municipality-ni.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab

::

  {
    "_id": "geonorge-county",
    "type": "pipe",
    "source": {
      "type": "conditional",
      "alternatives": {
        "prod": {
          "type": "json",
          "system": "geonorge",
          "url": "kommuneinfo/v1/fylkerkommuner"
        },
        "test": {
          "type": "embedded",
          "entities": [{...},{...}]
        }
      },
      "condition": "$ENV(node-env)"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*"],
          ["add", "_id", "_S.fylkesnummer"],
          ["add", "rdf:type",
            ["ni", "geonorge", "county"]
          ]
        ]
      }
    }
  }

.. image:: images/getting-started/labs/lab-rdf:type.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab

Lab 20
^^^^^^
::

  {
    "_id": "hops-labs",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "global-person"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["filter",
            ["in", "~:erp:person", "_S.rdf:type"]
          ],
          ["copy", "_id"],
          ["copy", "global-person:fullname"],
          ["add", "items",
            ["hops", {
              "datasets": ["global-transaction gt"],
              "where": ["eq", "_S.$ids", "gt.webshop-order:customerId-ni"],
              "return": "gt.webshop-order:itemId"
            }]
          ]
        ]
      }
    }
  }

.. image:: images/getting-started/labs/lab-hops.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab

Lab 21
^^^^^^
::

  {
    "_id": "apply-hops-labs",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "global-person"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "_id"],
          ["copy", "global-person:zipcode"],
          ["merge",
            ["apply-hops", "city-location", {
              "datasets": ["global-location gl"],
              "where": ["eq", "_S.global-person:zipcode", "gl.udir-postalcode:postalcode"]
            }]
          ]
        ],
        "city-location": [
          ["add", "location",
            ["concat", "_S.city", " is located in municipality number ", "_S.municipality"]
          ],
          ["merge",
            ["apply-hops", "latitude-check", {
              "datasets": ["global-location gl"],
              "where": ["eq", "_S.municipality-ni", "gl.$ids"]
            }]
          ]
        ],
        "latitude-check": [
          ["add", "arctic-municipality",
            ["if",
              ["gte",
                ["last", "_S.punktIOmrade.coordinates"], "~f66.33"], true, false]
          ]
        ]
      }
    }
  }

.. image:: images/getting-started/labs/lab-apply-hops.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab

Lab 22
^^^^^^
::

  {
    "_id": "person-csv",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "global-person"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "_id"],
          ["copy", "global-person:*",
            ["list", "firstname", "middle-initial", "lastname"]
          ]
        ]
      }
    }
  }

::

  {
    "_id": "person-csv-endpoint",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "person-csv"
    },
    "sink": {
      "type": "csv_endpoint",
      "columns": ["address", "country", "email", "fullname", "gender", "zipcode"]
    }
  }

Output:

::

  address,country,email,fullname,gender,zipcode
  Helmers vei 242,NO,torjussand@einrot.com,Torjus M. Sand,male,5031
  Frognerveien 60,NO,larsevjen@rhyta.com,Lars Evjen,male,3121
  Gydas gate 227,NO,siri@me.com,Siri Olsen,female,3733
  Nadderudåsen 186,NO,isakeikeland@teleworm.us,Isak E. Eikeland,male,9325
  Sommerfjøsvegen 143,NO,sebastianskjold@dayrep.com,Sebastian T. Skjold,male,7080
  Kongens gate 69,NO,caspiannygard@einrot.com,Caspian I. Nygård,male,0153
  Åsmostubben 19,NO,davidberntsen@superrito.com,David M. Berntsen,male,9011
  Fagerliveien 108,NO,lucaslie@cuvox.de,Lucas T. Lie,male,1605
  Zetlitzveien 241,,julieandersen@superrito.com,Julie I. Andersen,female,4017
  Kong Trygves vei 32,NO,camillawilhelmsen@dayrep.com,Camilla M. Wilhelmsen,female,3125
  Norderhovsgata 63,NO,RuneWold@armyspy.com,Rune E. Wold,male,3501
  Bøkleva 141,NO,WilliamFauske@jourrapide.com,William H. Fauske,male,1766
  Drengs 36,NO,,Aleksander M. Ommundsen,male,1390
  Tiurvegen vei,NO,,Erika L. Olsen,female,8657

Lab 23
^^^^^^
::

  {
    "_id": "person-http",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "global-person"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "_id"],
          ["copy", "global-person:*",
            ["list", "firstname", "middle-initial", "lastname"]
          ]
        ]
      }
    }
  }

::

  {
    "_id": "person-http-endpoint",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "person-http"
    },
    "sink": {
      "type": "http_endpoint"
    }
  }

.. image:: images/getting-started/labs/lab-jwt.png
    :width: 800px
    :align: center
    :alt: JWT creation on Subscription settings page

cURL command with newly created JWT:

::

  curl -H "Authorization: bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE1OTcyNjcyMzYuOTEwNTA2NywiZXhwIjoxNTk3NjEyMzgwLCJ1c2VyX2lkIjoiY2VlNDUxZDQtMDYwMC00NDk5LThkN2QtYjk3NGI4YTRlOTA1IiwidXNlcl9wcm9maWxlIjp7ImVtYWlsIjoicGFsLmFuZHJlYXNzZW5Ac2VzYW0uaW8iLCJuYW1lIjoiUFx1MDBlNWwgQW5kcmVhc3NlbiIsInBpY3R1cmUiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20vdjEuMC9tZS9waG90by8kdmFsdWUifSwidXNlcl9wcmluY2lwYWwiOiJncm91cDpFdmVyeW9uZSIsInByaW5jaXBhbHMiOnsiMTE3ZGNlYWEtZDY1OC00OTg2LTg5ZjktZDczOGIxMmMxNjlkIjpbImdyb3VwOkFkbWluIl19LCJhcGlfdG9rZW5faWQiOiIxOGEyNGQ0Mi0yOGVmLTQ0NGYtODM4NC1hOGVjMjEzM2FhOGQifQ.VT0PCDnEBraFk1pCSlO7d92zkD3MOhOvfdiLy7J6oAy6M77h1YbYKZRumzYUyg_XK8NXaginrK_pH563875S4nUZqINKiAnDJ0HYI9gQmABT2U8XQxeF-LlePpcxCI-UZarRiW_f2yQNYWqV_bJ3PmltodX2SUHjOmTcpqwVJvCqMSTqmCVqy6gPyQw6MTvzffP78MvmSb8fy8KcFP8H1rS4MilI9OnVWs9K3YaaXLs1SIxhAQrvjH2XlgwzMoCh05TpWPuiO1ph09fVI1U85uC59Q4e45bEpxMJmRuJ7RqEUdFR5RbSovqorB4Wxf8Cs0gFKMZxzj74eenMGjDJPg" https://datahub-117dceaa.sesam.cloud/api/publishers/person-http-endpoint/entities?limit=15

Output:

::

  [{"address": "Helmers vei 242", "country": "NO", "email": "torjussand@einrot.com", "fullname": "Torjus M. Sand", "gender": "male", "zipcode": "5031", "_id": "1", "_deleted": false, "_updated": 4, "_previous": null, "_ts": 1597266361399643, "_hash": "8a70306f3bcdb13714b62fa0dd5e8045"},{"address": "Frognerveien 60", "country": "NO", "email": "larsevjen@rhyta.com", "fullname": "Lars Evjen", "gender": "male", "zipcode": "3121", "_id": "2", "_deleted": false, "_updated": 5, "_previous": null, "_ts": 1597266361399655, "_hash": "821a5f4092874ae9d2b4e72819520ec5"},{"address": "Gydas gate 227", "country": "NO", "email": "siri@me.com", "fullname": "Siri Olsen", "gender": "female", "zipcode": "3733", "_id": "3", "_deleted": false, "_updated": 6, "_previous": null, "_ts": 1597266361399666, "_hash": "f8a5460cc0b8f25654e0581396fe9a8e"},{"address": "Nadderudåsen 186", "country": "NO", "email": "isakeikeland@teleworm.us", "fullname": "Isak E. Eikeland", "gender": "male", "zipcode": "9325", "_id": "100", "_deleted": false, "_updated": 7, "_previous": null, "_ts": 1597266361399677, "_hash": "f8a2aa8ef24b41ed18cbb9462790fa38"},{"address": "Sommerfjøsvegen 143", "country": "NO", "email": "sebastianskjold@dayrep.com", "fullname": "Sebastian T. Skjold", "gender": "male", "zipcode": "7080", "_id": "99", "_deleted": false, "_updated": 8, "_previous": null, "_ts": 1597266361399689, "_hash": "f576c6956daa30c4ab05192440117a4f"},{"address": "Kongens gate 69", "country": "NO", "email": "caspiannygard@einrot.com", "fullname": "Caspian I. Nygård", "gender": "male", "zipcode": "0153", "_id": "93", "_deleted": false, "_updated": 9, "_previous": null, "_ts": 1597266361399701, "_hash": "367cee1c0315ac189d0caccd76ab1a14"},{"address": "Åsmostubben 19", "country": "NO", "email": "davidberntsen@superrito.com", "fullname": "David M. Berntsen", "gender": "male", "zipcode": "9011", "_id": "91", "_deleted": false, "_updated": 10, "_previous": null, "_ts": 1597266361399712, "_hash": "b21ffc16fdfd6382d62a8b71d055d0d8"},{"address": "Fagerliveien 108", "country": "NO", "email": "lucaslie@cuvox.de", "fullname": "Lucas T. Lie", "gender": "male", "zipcode": "1605", "_id": "90", "_deleted": false, "_updated": 11, "_previous": null, "_ts": 1597266361399724, "_hash": "51266239e58e092fb537a0a0210242e6"},{"address": "Zetlitzveien 241", "country": null, "email": "julieandersen@superrito.com", "fullname": "Julie I. Andersen", "gender": "female", "zipcode": "4017", "_id": "80", "_deleted": false, "_updated": 12, "_previous": null, "_ts": 1597266361399735, "_hash": "109324caa77563a1f1a465ecc19f20fc"},{"address": "Kong Trygves vei 32", "country": "NO", "email": "camillawilhelmsen@dayrep.com", "fullname": "Camilla M. Wilhelmsen", "gender": "female", "zipcode": "3125", "_id": "81", "_deleted": false, "_updated": 13, "_previous": null, "_ts": 1597266361399747, "_hash": "8b5942cbc58a4f5dedc114234de95327"}]

Lab 24
^^^^^^

Postgres database connection info:

.. image:: images/getting-started/labs/lab-db-info.png
    :width: 800px
    :align: center
    :alt: The connection info to an example online database for used in this lab example solution

System config:

.. image:: images/getting-started/labs/lab-db-system.png
    :width: 800px
    :align: center
    :alt: A system config matching the connection info to the database in the previous image

Preperation pipe:

::

  {
    "_id": "person-elephantdb",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "global-person"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy",
            ["list", "_id", "global-person:firstname", "global-person:lastname", "global-person:address"]
          ]
        ]
      }
    }
  }

.. image:: images/getting-started/labs/lab-db-prep-pipe.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab

Output pipe:

::

  {
    "_id": "person-elephantdb-endpoint",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "person-elephantdb"
    },
    "sink": {
      "type": "sql",
      "system": "elephantdb",
      "table": "person"
    },
    "pump": {
      "mode": "$ENV(pump-mode)"
    }
  }

.. image:: images/getting-started/labs/lab-db-entries.png
    :width: 800px
    :align: center
    :alt: The person entities shown in the database browser after export

Lab 25
^^^^^^
System config:

::

  {
    "_id": "typicode",
    "type": "system:url",
    "url_pattern": "$ENV(typicode-baseurl)",
    "verify_ssl": true
  }

Preperation pipe:

::

  {
    "_id": "person-typicode",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "global-person"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy",
            ["list", "_id", "global-person:firstname", "global-person:lastname", "global-person:address"]
          ]
        ]
      }
    }
  }

.. image:: images/getting-started/labs/lab-api-prep-pipe.png
    :width: 800px
    :align: center
    :alt: Entity resulting from lab task as seen in the pipe's "Output"-tab

Output pipe:

::

  {
    "_id": "person-typicode-endpoint",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "person-typicode"
    },
    "sink": {
      "type": "json",
      "system": "typicode",
      "url": "posts"
    },
    "pump": {
      "mode": "$ENV(pump-mode)"
    }
  }

.. image:: images/getting-started/labs/lab-api-exec-log.png
    :width: 800px
    :align: center
    :alt: A "pump-completed" entry in the output pipe's execution log
