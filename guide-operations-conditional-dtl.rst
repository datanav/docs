:orphan:

.. _guide_operations_conditional_dtl:

The Conditional DTL
===================

.. toctree::
   :maxdepth: 1
   :hidden:

   Conditional source <tutorial-operations-conditional-source>

In this guide we will show you how to use Conditional DTL configurations. 

Conditional DTL configurations allows you to create different behaviour in your Sesam instance depending on which environment runs the configuration. For example, you might wish your Sesam production environment to collect data from, or share data to, a production database, but your Sesam test environment should only communicate with a test database. Or, you might wish for a certain transformation in your Sesam develop environment, but a different one in your Sesam production environment.

In this guide we will demonstrate how define environment dependent DTL operations and how these may be used to create a safer and more flexible configuration setup.   

.. admonition::  Objectives:
   
   After you complete these tutorials you will have:

   #. Learned how to create a conditional DTL source
   #. Learned how to create a conditional DTL transform
   #. Learned how to create a conditional DTL sink

.. admonition:: Prerequisites
    
    You should familiarize youself with:

    - :doc:`What is Sesam <index-whatis>`
    - :doc:`Building Blocks in Sesam <developer-guide>`


|
|

.. panels::
    :column: col-lg-12 p-2 

    **The conditional DTL:** This guide includes 1 tutorial
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. dropdown:: **1. The conditional source**
        :open:

        :badge:`Estimated time: 15 min,badge-light`

        This tutorial will show you how to use a conditional DTL source.

        .. link-button:: tutorial_operations_conditional_source
            :type: ref
            :text: Start this tutorial
            :classes: tutorial-start
        
    ..
      .. dropdown:: **2. The conditional transform**
          :open:

          :badge:`Estimated time: 15 min,badge-light`

          This tutorial will show you how to use a conditional DTL transform.

          .. link-button:: tutorial_operations_conditional_transform
              :type: ref
              :text: Start this tutorial
              :classes: tutorial-start
    ..  
      .. dropdown:: **The conditional sink**
          :open:
          
          :badge:`Estimated time: 15 min,badge-light`

          This tutorial will show you how to use a conditional DTL sink.

              .. link-button:: tutorial_operations_conditional_sink
                  :type: ref
                  :text: Start this tutorial
                  :classes: tutorial-start