.. _global-datasets:

:badge:`Free feature,badge-success badge-pill`

Global datasets
===============

A global dataset is a collection of data pertaining to the same concept from different sources. In other words, a global dataset combines data from sources that are semantically linked, to provide a comprehensive and logical grouping of this data into one :ref:`dataset <concepts-datasets>`. This will reduce the total number of :ref:`pipes <concepts-pipes>` needed compared to a system where you get data from the original sources each time. 

Global datasets can be populated by:

- Simply adding datasets to a global dataset without merging 
- Merging data from various sources without modifications  
- Selectively merge data, by selecting which properties to merge through transformations

It is important to remember that creating a global dataset requires either business knowledge or a sound understanding of the data entering Sesam from the different sources. 

Use case
========

Imagine three sources being ingressed in Sesam that each contain person data. Albeit, it is not immediately straight forward getting an overview of all the person metadata each of these sources contain. However, through the creation of a **global-person** dataset, information can be easily fetched from one single location instead of each of the three sources. Look at the below example to get an idea of how this could be done.

.. code-block:: python

  HR system
  {
    "_id": "hubspot-person:02023688018",
    "hubspot-person:EmailAddress": "IsakEikeland@teleworm.us",
    "hubspot-person:Gender": "male",
    "hubspot-person:Address": "Himmelberg Vei 11",
    "hubspot-person:PostCode": "0166",
    "hubspot-person:SSN": "02023688018",
    "rdf:type": "~:hubspot:Person"
  }

  CRM
  {
    "_id": "crm-person:100",
    "crm-person:EmailAddress": "IsakEikeland@teleworm.us",
    "crm-person:ID:”100”,
    "crm-person:SSN": "02023688018",
    "crm-person:SSN-ni": "~:hr-person:02023688018",
    "rdf:type": "~:crm:Person"
  }

  ERP
  {
    "_id": "erp-person:0202",
    "erp-person:SSN": "02023688018",
    "erp-person:SSN-ni": "~:hr-person:02023688018",
    "erp-person:Age": "43",
    "erp-person:Position": "Sales Manager",
    "erp-person:ID:”0202”,
    "erp-person:country":"NO",
    "rdf:type": "~:erp:Person"
  }

The dataset below is what a global dataset of the above three datasets would look after being merging on social security number (SSN).

.. code-block:: python

  {
    "$ids": [
      "~:crm-person:100",
      "~:hubspot-person:02023688018",
      "~:erp-person:0202"
    ],
    "_id": "crm-person:100",
    "hubspot-person:EmailAddress": "IsakEikeland@teleworm.us",
    "hubspot-person:Gender": "male",
    "hubspot-person:Address": "Himmelberg Vei 11",
    "hubspot-person:PostCode": "0166",
    "hubspot-person:SSN": "02023688018",
    "crm-person:EmailAddress": "IsakEikeland@teleworm.us",
    "crm-person:ID:”100”,
    "crm-person:SSN": "02023688018",
    "crm-person:SSN-ni": "~:hrsystem-person:02023688018",
    "erp-person:SSN": "02023688018",
    "erp-person:SSN-ni": "~:hr-person:02023688018",
    "erp-person:Age": "43",
    "erp-person:Position": "Sales Manager",
    "erp-person:ID:”0202”,
    "erp-person:country":"NO",
    "rdf:type": [
      "~:crm:Person",
      "~:hubspot:Person",
      "~:erp:Person"
    ]
  }

Key benefits
============

• By decoupling data from original sources, point-to-point integrations within Sesam can be avoided, thus fewer connections results in lower maintenance costs as integrated systems grow. In addition, data is available without concern of the original source
• Data in global datasets are re-used, which saves work and makes adding new integrations easier
• Only one look-up, instead of having to “look for data” in various datasets
• Inbound datasets can be kept raw and as identical to the real source as possible, independent of how the data will be used, thus avoiding “early binding”
• Adding additional integrations can further refine the global datasets and as such improve data quality

A model without global datasets might look like the figure below. This example consists of four sources and three target systems only. Generally, it will be a lot more complicated.

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

  As an example, an energy company has 700 000 customers, and each customer has a power meter connected to their home. When adding the historic data, which the company is required to store as well, the total data sums up to about 30 000 000 customers. One way of managing this large amount of data is to divide the data into different global datasets. In this case, the energy company might choose to store their historic data in one global dataset, and the current data in a different global dataset.
