.. _talk_wave:

Wave
====

`Wave <https://waveapps.com>`_ provides financial software and services for small businesses, with services include direct bank data imports, invoicing and expense tracking, customizable chart of accounts, and journal transactions.


.. panels::
    :body: text-left
    :container: container-lg pb-3
    :column: col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2

    **Making Wave Talk**

    Easily synchronise valuable data between Wave and your other systems.
    

    .. link-button:: https://wave.sesam.io
        :type: url
        :text: Try for free
        :classes: btn-primary btn-block

Frequently Asked Questions
--------------------------

How can I synchronise my contact persons to a Wave customer? 
***********************************************************
Wave has no contact of a person concept, but rather integrates this information directly on the customer object. In order for this information to flow between your Wave account and other connected systems, we infer a contact person object to the Wave customer object. This means, as long as we have either a **Firstname**, **lastname**, **phone number** or an **email** a contact person will be created based on these attributes and syncronized to the connected system/systems.

The side effects of this are:

#. A Wave customer's contact information can not be removed by simply removing it from Wave, you also have to remove it from other conencted systems first.
#. Changing a Wave customer's email could result in the merging of contacts on other systems. You can never change the contact entity through Wave GUI, only update it's metadata.
