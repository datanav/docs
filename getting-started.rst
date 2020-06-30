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

.. _getting-started-import-data:

Import data
===========

Before we describe how to import data into your node, we need to emphasize an important issue. If you will work on a Sesam node that already contains configurations and data, you should NOT import data through uploading the training-config.json as described below. This is because **uploading a config replaces the existing one**. You then need to create each pipe and the system found in the training-config.json file manually. Go to the Pipes-view, create pipe, post one of the pipes found in the json file and repeat the process. The pipes (or system) in the json file are identified by the "_id" attribute. Copy the pipe's content and its curly bracket { } wrapper. The pipes to copy and create are **"hr-person"**, **"crm-person"**, **"difi-postnummer"**, **"erp-person"**, **"global-location"**, **"global-person"**, **"person-crm"**, **"salesforce-consent"** and **"salesforce-userprofile"**. The **"datahotel"** config is a system that you copy and create in the Systems-view.

When you are setting up your node for the first time your Sesam node might contain many different :ref:`pipes <concepts-pipes>` and :ref:`systems <concepts-systems>` depending on your needs and wishes. However, as of yet we do not have any data to work with. For this purpose, we have made available a practice datahub which contains several pipes and systems which we will use in this getting started guide. As this guide progresses, we will talk more about the what a pipe and a system is. For now, the first thing you need to do is to download the `training-config.json <https://raw.githubusercontent.com/sesam-community/wiki/master/training-config.json>`__ and save it locally on your computer (left click url and "Save Link As...").

Go into you 'Dev Node'. Click on **Datahub** in the left menu and select the **Tools tab**.

.. image:: images/getting-started/importdata.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Upload the file. As seen on picture above, make sure you check the box "**Force upload (ignore validation errors)**".

We have created some test data for you. Go to the **Variables** tab and paste the code below inside the curly brackets.

::

  "node-env": "test"

You should now have several pipes available. Pipes are available in the **pipes** tab. Click on a pipe in the list to see details on how it's configured.

As a sanity check you can select **Pipes** in the menu on the left. Select the crm-person pipe and go to the **Config** tab. Preview the pipe by hitting **ctrl + Enter**. Previewing a pipe is useful when you want to check result of logic without having to run pipe to check output. The **config** contains the actual data transformations and pumps. In the top right corner press **Start** then **Refresh**. It should look like the picture below. Notice that it says "Processed 10 last run" next to the **Start** button. You can also check the **Output** tab to see the entities. 

.. image:: images/getting-started/running_pipe.gif
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Repeat these steps for **hr-system**, **erp-person**, **salesforce-userprofile** and **difi-postnummer** pipes.

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

For more details on how to use the templates when making a new pipe from scratch, please click here LINK.

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
                  ["substring",0,4,"_S.FirstName"]], 
              ["add", "fullname-lower-case", 
                  ["concat","_T.Firstname-lower"," ","_S.LastName"]], 
              ["remove", "Username"] 
          ] 
        } 
    } 

The above DTL snippet displays the :ref:`add <dtl_transform-add>` function as well as the  :ref:`concat <concat_dtl_function>`, :ref:`add <lower_dtl_function>`, :ref:`substring <substring_dtl_function>` and the :ref:`remove <dtl_transform-remove>` function inside the transform. 

  * The first **["add"]** creates a new property named **"Type"** that has the value **"customer"**.

  * The second **["add"]** creates a new property named **"Firstname"** which is constructed by using the function concatenate (**["concat"]**).

  * The third **["add"]** uses the function **["lower"]** to make all characters lower case.

  * The fourth **["add"]** uses the function **["substring"]** to make a substring of the **"FirstName"**.

  * The fifth **["add"]** uses the function **["concat"]** to combine the lower cased first name with the last name.

  * The **["remove"]** function removes the selected property.

Notice the **"_S.[property1]"** and **"_T.[property2]"**. The **_S** and **_T** are called variables, and refer to the source and the target respectively.

Lab 1-2
^^^^^^^^
The :ref:`Labs section <getting-started-labs>` helps us get more hands on with Sesam. Head over there and do the first two labs to get more experience transforming data. 


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

**"Coalesce"** means to join or combine. In SQL it is commonly used together with "is-null" to return the first non-null value in a list. In DTL, when we need to prioritize which keys we want to use to pick a value, we use **"Coalesce"**. So, when is this useful and how is it used?

Say we want to add a property or a key called "lastname". This key-value is found in three different systems. We want to make sure we use the most trusted value, we use **"Coalesce"** to state order which Sesam checks for values. If the hr-person "lastname" is null, **"Coalesce"** gives us the opportunity to choose which is the next best option.

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


**"Coalesce"** is used together with **"list"** function, which basically is a list of values. We need **"list"** to list the order of which keys to pick values from. 

If you need a list of key-value pairs, in other words a list of properties *and* values, you need to make a dictionary using the **"dict"** function.

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

The **"if"** condition is a function in DTL that works by evaluating a statement and by performing different actions depending on the outcome of the evaluation. 

In everyday life we might say "if you're 50 years old or older, then you're entitled to a longer vacation". If not, then you have the standard number of weeks set aside for vacation. 

In DTL this would be utilized in the following way:

First we need to be able to assort the different people into two separate groups, e.g. group_1 is the group containing people with normal vacation (under 50 years of age) and group_2 is the group with people with extended vacation. Now let's assume that every person has an attribute named "age". Assuming that the person entity is the source entity we could define our evaluating statement as the following: ["gte", "_S.age", "50"], which will be true if the person is 50 years old or older, and false otherwise. We use the **"gte"** function which is used to get values greater than or equal to. In comparison **"gt"** simply means greater than. Now we can construct our complete if-statement:

::

  ["if",
      ["gte", "_S.age", "50"], 
      ["add", "age_group", "group_1"],
      ["add", "age_group", "group_2"]
  ]

The third line is activated if the statement is true, and the fourth line if the statement is false.

Another handy function is "return" which allows us to specify which values we want returned from source when doing hops.

"Tuples" is mainly used when we need to make several equalities between two datasets in one hops. Let us say you have two properties in dataset A that will match two properties in dataset B, it will be done as follows:

::

  ["eq",
    ["tuples", "A.prop1", "A.prop2"],
    ["tuples", "B.prop1", "B.prop2"]
  ]

Global datasets
^^^^^^^^^^^^^^^
Global datasets are key to getting the most out of using Sesam. We combine data from sources with logically linked information to provide one common place to then retrieve this data from when needed. This will reduce the total number of pipes needed compared to a system where you get data from the original sources each time.

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

Labs 3
^^^^^^
Go to the :ref:`Labs section <getting-started-labs>` and do :ref:`Lab 3 <getting-started-labs-3>`.

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

We will later see the use of the **["merge"]** function in combination with functions that fetch entities from other datasets.

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


In this transform we first copy everything from the source dataset into the target. To do a **["hops"]** you first add a new property to the target dataset. Then, inside that **["add"]** you call on the **["hops"]** function to fetch entities from the specified dataset, in this example (**"global-orders"**).

Lab 4
^^^^^
Go to the :ref:`Labs section <getting-started-labs>` and do :ref:`Lab 4 <getting-started-labs-4>`.


Apply-hops
==========
There is also the function :ref:`apply-hops <apply_hops_function>`, which is a combined **["apply"]** and **["hops"]** function. This adds another **"rule"** in the DTL configuration in which we can specify how to implement the entities fetched with the hops. You can read more about the **["apply"]** function :ref:`here <hops_function>` 

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

Lab 5
^^^^^
Go to the :ref:`Labs section <getting-started-labs>` and do :ref:`Lab 5 <getting-started-labs-5>`.

Should I "add" or "merge" an apply-hops?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
As you can see in the examples below we want to add the "City" and "Municipality" from another dataset to the source. In the two examples we have the same source but the difference is in how we use the **["apply-hops"]**. In the first case we **["add"]** a new property called "difi-data" which you can see in the results creates a dictionary containing "City" and "Municipality" in **"difi-data"**.

 When adding "City" and "Municipality" from another dataset we need to specify which *sources* and *entities* we want to match on. This is done by adding **"_S"** in front of name of dataset and entity.  It looks like this: **_S.hr-person:ZipCode**

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

In the second example, instead of adding the **["apply-hops"]**, we use **["merge"]**. This will add the "City" and "Municipality" as properties in the target.

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

Lab 6
^^^^^
Go to the :ref:`Labs section <getting-started-labs>` and do :ref:`Lab 6 <getting-started-labs-6>`.

.. _getting-started-Dependency-tracking-and-resetting-a-pipe:

Dependency-tracking and resetting a pipe
========================================

We have now started to create dependencies between datasets. In :ref:`Lab 5 <getting-started-labs-5>` you created a pipe called **<your_name>-global-person** and in :ref:`Lab 6 <getting-started-labs-6>` you created hops to **difi-postnummer**. This means that entities from **<your_name>-global-person** should change when the data in the source datasets (crm-person, erp-person, hr-person and salesforce-userprofile) changes, in addition to when the relevant data in difi-postnummer changes. We could of course check through every entity in difi-postnummer for changes, but this would also mean we need to reprocess every entity in the source datasets to check for changes when they connect to **difi-postnummer**.

In order to make sure that only entities that has changed since the last time the integration ran are updated, Sesam utilizes **“dependency tracking”**. **Dependency tracking** ensures that Sesam recognizes changes in connected data, and not only changes in the pipe’s sources, and acts accordingly. For further information regarding dependency tracking visit `here <https://docs.sesam.io/concepts.html#dependency-tracking>`__ 

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

Sinks can support `batching <https://docs.sesam.io/configuration.html#batching>`__ by implementing specific methods and accumulating entities in a buffer before writing the batch. The size of each batch can be specified using the batch_size property on the pipe. See the section on batching for more information. We also recommend that you read about the sinks in the documentation and "Best practice" for  best ways of working with them.

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

Lab 7
^^^^^
Go to the :ref:`Labs section <getting-started-labs>` and do :ref:`Lab 7 <getting-started-labs-7>`.

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

**Jaca class**:

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

We start by building a Docker image from our microservice. A Docker image is the blueprint for creating a container with our microservice. We can create and run as many containers as we want from the same image.

The Docker image is then pushed up to a repository on Docker Hub. This repository can be private or made public. When hosted in the repository the image can be pulled by anyone with access.

Finally, we pull the image from our Docker Hub repository (although private repositories are also supported) and spin up a container on our Sesam-node. The container is created from the image and started. The Docker-commands for this are performed by Sesam. We simply specify the location of the image on Docker Hub in our Sesam system configuration and the container is spun up automatically. 

Microservices with Docker
==========================

First you need to sign up on `Docker <https://www.docker.com>`__ and create a new repository.

.. image:: images/getting-started/Docker-repo.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Then download `Docker Desktop <https://www.docker.com/get-started>`__.

You now need to download Python. Here we're using Python 3.6 but you can use any version after 3.5. Then install pip and Flask. If you need help with this, follow the instructions `here <https://pip.pypa.io/en/stable/installing/>`__ for pip and `here <http://flask.pocoo.org/docs/1.0/installation/>`__ for Flask.

.. image:: images/getting-started/flaskInstall.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Now you are ready to create the microservice.

Create a new project in Pycharm (or your preferred text editor). This tutorial will be using Pycharm. Name your project “Demo_MicroserviceProject”.

Inside your Demo_MicroserviceProject folder create a new file called Dockerfile and paste:

::

  FROM python:3-alpine 
  
  RUN apk update 
  
  RUN pip install --upgrade pip 
  
  COPY ./service/requirements.txt /service/requirements.txt 
  RUN pip install -r /service/requirements.txt 
  COPY ./service /service 
  
  EXPOSE 5000 
  
  CMD ["python3", "./service/DemoMicroservice.py"]

Then create a new folder called service inside your project root folder.

.. image:: images/getting-started/MSproject.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Create a text file named "requirements.txt" inside the "service" folder and paste the following text inside it:

::

 Flask==1.0.2

Then create a python file, also in the "service" folder, named "DemoMicroservice.py" with the following code:

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

To test that you can run a container from your image locally you can run it in command line/terminal. First we need to login to Docker. Run the command docker login and enter your Docker Hub **username** and **password** when prompted.

Next we'll need to run the image to create the container.

To check that the you have created image run the command:

::

  docker run -p <local_port>:<container_port> <docker_username>/<your_repository_name>:<tagname>

Set **local_port** to 5000 and the container_port should be the same as the you expose in the Dockerfile.

Then to check you can either go to the url in the browser or do:

::

 curl -v http://localhost:5000/api/orders 

in terminal

To stop the container running locally you can run: 

::

 docker stop container name or container id <

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
Now we need to spin up the container in our Sesam node.

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

Then create a new pipe. Because our dataset does not have an **"_id"** property we need to add that. We could just use a normal **["add"]** function, but as you can see from the microservice, we’ve actually just created one property as a dictionary. We really want these as three entities and that reason we use this function:

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
============
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
These tasks will make you familiar with the basics of data transformation with Sesam. We recommend keeping the `documentation <https://docs.sesam.io/DTLReferenceGuide.html>`__ at hand to look up syntax and concepts when needed.

To do these labs you will need to have a Sesam node set up with the `training config json <https://raw.githubusercontent.com/sesam-community/wiki/master/training-config.json>`__ configuration. If you have set up your node following the :ref:`Getting started <getting-started>` with Sesam guide you are ready to do these labs.

We recommend having a go at this by yourself, but there are clues provided below each lab on where to look for guidance if needed.

Good luck and have fun!

Lab 1
=====

.. _getting-started-labs-1:

Scope: Transforming data.

  * Create a new pipe​.
  * Use the **"crm-person"** as source.
  * Name it "[yourname]-crm-person".
  * Create a new property called "FullName" by using the functions **["add"]** and **["concat"]**.
  * Run pipe and look at ​dataset.

*If you need a hint on how to do this, look for the ["concat"] function in the "global-person" pipe.*

Lab 2
=====

.. _getting-started-labs-2:

Scope: Remove and add.

  * Create a new pipe.
  * Use a "person" source that contains the property "SSN".
  * Copy all the properties.
  * Remove the property "SSN".
  * By using the **["add"]** function, add a new property called "Birthday" by using the **["substring"]** function.

*Hint: Look up "remove" and "substring" in the documentation.*

Lab 3
=====

.. _getting-started-labs-3:

Scope: Merge multiple datasets in source to create a global.​

  * Create New pipe. Call this pipe <your_name>-global-person.
  * Select source system: system:sesam-node.
  * Select provider type: merge prototype.
  * List these four datasets in the source, with aliases: **"crm-person cp"**, **"erp-person ep"**, **"hr-person hp"** and **"salesforce-userprofile sup"**.
  * Use **["equality"]** to merge the datasets on matching values.
  * Set **"identity"** to **"first"**.
  * Set **"version"** to 2​.
  * Add transform​.
  * ["copy" , "*"]​.

*Hint: Look at the source section of the "global-person" pipe.*

Lab 4
=====
.. _getting-started-labs-4:

Scope: Hops

  * In the same pipe that we created in lab 3 we want to 'hop' to another dataset with the **["hops"]** function.
  * Add a new property called difi-data. Inside the add, use **["hops"]** to join on the "zipcode" from **hr-person** OR **"PostalCode"** from crm-person with **"postnummer"** of "difi-postnummer".

*Hint: Look up hops in the Getting started guide, the "person-crm" pipe or the documentation. You will also find the "or" function in the documentation.*

Lab 5
=====
.. _getting-started-labs-5:

Scope: Apply-hops

  * In the same pipe that we created in lab 3 we want to 'hop' to another dataset with the **["apply-hops"]** function.
  * Add a global property "City" and "Municipality" from "difi-postnummer" by using **["apply-hops"]**.
  * Try to use **["apply-hops"]** inside an **["add"]** and a **["merge"]**. See any difference?

*Hint: Look at the transform section of the "person-crm" pipe.*

Lab 6
=====
.. _getting-started-labs-6:

Scope: Creating global properties

  * In the global pipe we now want to create global properties for firstname, lastname, fullname, address, SSN, zipcode and customerid.
  * Use **["coalesce"]** and **["list"]** functions to prioritize which source you want to pick from first.

*Hint: Look at the transform section of the "global-person" pipe.*

Lab 7
=====
.. _getting-started-labs-7:

Scope: Enhancing the quality of data

  * Create new pipe, following naming conventions.
  * Copy these properties to the output dataset: CustomerId, firstname, lastname, FullName, Address, SSN, zipcode, City and Municipality.

*Hint: Look at the transform section of the "person-crm" pipe.*

Lab 8
=====
.. _getting-started-labs-8:

Scope : Publishing data to CSV-endpoint

  * Create new pipe. Source from lab 6. Add transform and sink.​

Hint: Look `here  <https://docs.sesam.io/getting-started.html#csv-endpoint-sink>`__ for help

Lab 9
=====
.. _getting-started-labs-9:

Start from your pipe from lab 5. 

* Add another property in the apply-hops rule and start the pipe again and look at the output. 

.. image:: images/getting-started/DT-03.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

* What can you see? Probably, you do not notice anything different, even though you just told the pipe to add another line with data to your entities. Why didn’t the outcome changes when you added a new property?

* In the outcome, locate an entity which has the properties "City" and "Municipality".

.. image:: images/getting-started/DT-05.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

*  Note down it’s sequence number (_updated value). 

* click on the three dots next to your pipe name and choose the option "Update last seen". Write down the sequency number you noted down and start the pipe again. 

.. image:: images/getting-started/DT-06.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

* Has the output changed? Why/why not? Did all the entities in the outcome change? Why/why not?
* What is the difference between the "Update last seen" option and the "Reset", "Restart" and "Start" options?

*Hint: check "Dependency-tracking and resetting a pipe"*

