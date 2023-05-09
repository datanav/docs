.. _system_dataverse:

.. rst-class:: center-title

===================
Microsoft Dataverse
===================
Data Verse is  is a cloud based storage and data management engine under Microsoft, that lets you securely store and manage data that's used by business applications.

Data types
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 80, 10,10

   * - Data type
     - Input
     - Output

   * - :ref:`Person <datatype_human>`
     - true
     - true

   * - :ref:`Location <datatype_location>`
     - true
     - false

   * - :ref:`Organisation <datatype_organisation>`
     - true
     - true

   * - :ref:`Task <datatype_task>`
     - false
     - true

Other :ref:`Enterprise application integration (EAI) <systemtypeeai>` Systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. panels::
    :body: text-left
    :container: container-lg pb-3
    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2 custom-card

    **Azure-service-bus**

    Azure Service Bus is a reliable cloud messaging as a service (MaaS) and simple hybrid integration
    .. link-button:: system/azure-service-bus
        :type: ref
        :text: Read more
        :classes: read-more
    ---
    **Apache Kafka**

    
    .. link-button:: system/kafka
        :type: ref
        :text: Read more
        :classes: read-more
    ---