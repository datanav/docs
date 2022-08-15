.. _concepts-global-datasets:

Global datasets
===============

A global dataset is a collection of data pertaining to a same concept from different sources. In other words, a global dataset combines data from sources semantically linked to provide one single authoritative fresh data location to access when needed. This will reduce the total number of pipes needed compared to a system where you get data from the original sources each time. 

Global datasets can be populated by:

- Simply add datasets to a global dataset without merging 
- Merging data from various sources without modifications  
- Selectively merge data, by selecting which properties to merge through transformations

It is important to remember that a global dataset requires either business knowledge or a sound understanding of the data from the different sources. Global datasets will work to their fullest potential if they include all of the semantically linked data elements relating to the subject matter. 

**Example:**

There are three sources containing person data as shown below. If any target system wants data about this person, it would have to go through each root datasets every time. However, through the creation a **global-person** dataset, information can be easily fetched from one single location.

.. code-block:: python

  HR system
  {
    "_id": "hr-person:02023688018",
    "hr-person:EmailAddress": "IsakEikeland@teleworm.us",
    "hr-person:Gender": "male",
    "hr-person:SSN": "02023688018"
  }

  CRM
  {
    "_id": "crm-person:100",
    "crm-person:EmailAddress": "IsakEikeland@teleworm.us",
    "crm-person:ID:”100”,
    "crm-person:SSN": "02023688018",
    "crm-person:SSN-ni": "~:hr-person:02023688018"
  }

  ERP
  {
    "_id": "erp-person:0202",
    "erp-person:SSN": "02023688018",
    "erp-person:SSN-ni": "~:hr-person:02023688018",
    "erp-person:ID:”0202”,
    "erp-person:country":"NO"
  }

The dataset below is what a global dataset of the above three datasets looks like in Sesam when merging on equality of social security number (SSN).

.. code-block:: python

  {
    "$ids": [
      "~:crm-person:100",
      "~:hr-person:02023688018",
      "~:erp-person:0202"
    ],
    "_id": "crm-person:100",
    "hr-person:EmailAddress": "IsakEikeland@teleworm.us",
    "hr-person:Gender": "male",
    "hr-person:SSN": "02023688018",
    "crm-person:EmailAddress": "IsakEikeland@teleworm.us",
    "crm-person:ID:”100”,
    "crm-person:SSN": "02023688018",
    "crm-person:SSN-ni": "~:hrsystem-person:02023688018",
    "erp-person:SSN": "02023688018",
    "erp-person:SSN-ni": "~:hrsystem-person:02023688018",
    "erp-person:ID”:”0202”,
    "erp-person:country":"NO" 
  }

Key benefits
------------

• By decoupling data from original sources, point-to-point integrations within Sesam can be avoided, thus fewer connections results in lower maintenance costs. In addition, data is available without concern for the original source
• All logic related to connecting and enriching data is only done once 
• Data in Global datasets are re-used, which saves work and makes adding new integrations easier
• Only one look-up, instead of having to “look for data” in various datasets
• Input datasets can be kept raw and as similar to the real source as possible, independent of how the data will be used, thus avoiding “early binding”
• Adding additional integrations further refines the global datasets, and therefore continuously improves the data quality

A data model without global datasets might look like the figure below. This example consists of four sources and three target systems only. Generally, it will be a lot more complicated.

.. image:: ../images/best-practice/no-global.png
    :width: 80%
    :align: center
    :alt: Datamodel without global datasets

As shown in the figure below, a Sesam node containing global datasets results in fewer connections, making it both tidier and easier to manage.

.. image:: ../images/best-practice/global.png
    :width: 80%
    :align: center
    :alt: Generic pipe concept

.. admonition::  Good to remember:

  Global datasets will most likely grow and become large. If the configuration or logic is changed, this can in some cases mean that the whole dataset needs to be updated. This can potentially be a big job and will take time.

  As an example, an energy company has 700 000 customers, and each customer has a power meter connected to their home. When adding the historic data, the company is required to store as well, the total data objects sum up to 30 000 000. One way of managing this large data amount is to divide the data into different global datasets. In this case, the energy company chose to store their historic data in one global dataset, and the current data in a different global dataset.
