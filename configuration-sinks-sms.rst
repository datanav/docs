
.. _sms_sink:

SMS message sink
----------------

The SMS message sink is capable of sending ``SMS`` messages based on the entities it receives. The message to send can be
constructed either by inline templates or from templates read from disk. These templates are assumed to be ``Jinja``
templates (https://palletsprojects.com/p/jinja/) with the entities properties available to the templating context. The template file
name can either be inlined in the configuration or embedded in the input entity. The SMS service to use must be
configured separately as a :ref:`system <system_section>` and its ``_id`` property given in the ``system`` property.
Currently, only the :ref:`Twilio provider <twilio_system>` is supported.

Prototype
^^^^^^^^^

::

    {
        "type": "sms",
        "system": "sms-system-id",
        "body_template": "static jinja template as a string",
        "body_template_property": "id-of-property-for-body-template",
        "recipients": "static,comma,separated,list,of,international,phonenumbers",
        "recipients_property": "id-of-property-to-get-recipients-from",
        "from_number": "static-international-phone-number-to-use-as-from-number",
    }

Properties
^^^^^^^^^^

The configuration must contain at most one of ``body_template`` or ``body_template_property``:

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`Twilio provider <twilio_system>` component to use.
     -
     - Yes

   * - ``body_template``
     - String
     - Should contain a ``Jinja template`` to use for constructing messages. The template will have access to all entity properties by name.
     -
     - Yes

   * - ``body_template_property``
     - String
     - Should contain a ``id`` of a property of the incoming entity to use for looking up the ``Jinja template``
       (i.e for inlining the templates in the entities). It should not be used at the same time as ``body_template``
       or ``body_template_file*``
     - "body_template"
     -

   * - ``recipients``
     - String
     - Should contain a comma-separated list of internationalised phone-numbers to send the message constructed to.
       If this is not inlined in the entities via ``recipients_property`` (see below) the property is required.
     -
     - Yes

   * - ``recipients_property``
     - String
     - Should contain the id of the property to look up the recipients from the entity itself (i.e for inlining the
       recpients). If ``recipients`` (see abowe) is not specified, this property is mandatory and the propery
       referenced by it must exists and be valid for all entities.
     - "recipients"
     - Yes

   * - ``from_number``
     - String
     - An international phone number to use as the sender of all messages
     -
     - Yes

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity. The
examples assume a :ref:`system component <system_section>` (i.e. a :ref:`Twilio service <twilio_system>`) has been
configured earlier:

::

    {
        "sink": {
            "type": "sms",
            "system": "twilio_service",
            "body_template": "SMS message: {{ message_prop_id }}",
            "recipients": "+4799887766,+4788776655",
            "from_number": "+4766554433"
        }
    }

In the above example the entities sent to the sink should have at least a single property ``message_prop_id``, i.e.:

::

    {
        "_id": "message_id",
        "message_prop_id": "This is the message to send",
        "some_other_property": "Some other value"
    }

An example where the template to use is included in the entity written to the sink:

::

    {
        "sink": {
            "type": "sms",
            "system": "twilio_service",
            "body_template_property": "body_template_property_id",
            "recipients": "+4799887766,+4788776655",
            "from_number": "+4766554433"
        }
    }

For the example above the entities sent to the sink should have at least a single property ``body_template_property_id``
and it also needs to have the properties references in the embedded template:

::

    {
        "_id": "message_id",
        "body_template_property_id": "SMS message: {{ message_prop_id }}",
        "message_prop_id": "This is the message to send",
        "some_other_property": "Some other value"
    }

You can also store the Jinja templates on disk and reference them in the same way via filenames instead of embedding
the templates in config or the entities themselves.

