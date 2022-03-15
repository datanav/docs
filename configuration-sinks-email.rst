
.. _mail_sink:

Email Message sink
------------------

The mail message sink is capable of sending mail messages based on the entities it receives. The message to send can be
constructed either by inline templates or from templates read from disk. These templates are assumed to be ``Jinja
templates`` (https://palletsprojects.com/p/jinja/) with the entities properties available to the templating context. The template file
name can either be embedded in the configuration or in the input entity. The mail server settings have to
be registered in a :ref:`SMTP system <smtp_system>` component in advance and its ``_id`` put in the ``system``
property of the sink.

Prototype
^^^^^^^^^

::

    {
        "type": "mail",
        "system": "smtp-system-id",
        "body_template": "static jinja template as a string",
        "body_template_property": "id-of-property-to-get-as-a-body-template",
        "text_body_template": "static text only jinja template as a string",
        "text_body_template_property": "id-of-property-to-get-as-a-text-body-template",
        "subject_template": "static jinja template as a string",
        "subject_template_property": "id-of-property-to-get-as-a-subject-template",
        "recipients": "static,comma,separated,list,of,email,addresses",
        "recipients_property": "id-of-property-to-get-recipients-from",
        "mail_from": "static@email.address"
    }

Properties
^^^^^^^^^^

The configuration must contain at most one of ``body_template`` or ``body_template_property``. The same applies to
``subject_template`` and ``subject_template_property``.

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
     - The id of the :ref:`SMTP system <smtp_system>` to use.
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
       (i.e for inlining the templates in the entities). It should not be used at the same time as ``body_template``.
     - "body_template"
     -

   * - ``subject_template``
     - String
     - Should contain a ``Jinja template`` to use for constructing subjects for the email messages. The template
       will have access to all entity properties by name
     -
     - Yes

   * - ``subject_template_property``
     - String
     - Should contain a ``id`` of a property of the incoming entity to use for looking up the ``Jinja template``
       (i.e for inlining the templates in the entities). It should not be used at the same time as ``subject_template``.
     - "subject_template"
     -

   * - ``text_body_template``
     - String
     - Should contain a ``Jinja template`` to use for constructing plain-text messages. The template will have access to all entity properties by name.
     -
     -

   * - ``text_body_template_property``
     - String
     - Should contain a ``id`` of a property of the incoming entity to use for looking up the ``Jinja template``
       (i.e for inlining the templates in the entities) used to construct plain text messages. It should not be used at the same time as ``text_body_template``
     - "text_body_template"
     -

   * - ``recipients``
     - String
     - Should contain a comma-separated list of email addresses to send the message constructed to. If this is not
       inlined in the entities via ``recipients_property`` (see below) this property is mandatory.
     -
     - Yes

   * - ``recipients_property``
     - String
     - Should contain the id of the property to look up the recpients from the entity itself (i.e for inlining the
       recpients). If ``recipients`` (see abowe) is not specified, this property is mandatory and the propery
       referenced by it must exists and be valid for all entities.
     - "recipients"
     -

   * - ``mail_from``
     - String
     - An email address to use as the sender of all messages
     -
     - Yes

   * - ``unhandled_template_variable_replacement``
     - String
     - Specifies how unhandled variables in the templates are handled. debug: the '{{variable_name}}'-string is kept.
       empty_string: {{variable_name}} is replaced with an empty string. strict: an error is raised.
       The default is 'debug'.
     - "debug"
     -



Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "mail",
            "system": "our-smtp-server",
            "body_template": "Mail message body: {{ message_prop_id }}",
            "subject_template": "Subject: {{ subject_prop_id }}",
            "recipients": "foo@bar.com,info@example.com",
            "mail_from": "all@of.us"
        }
    }

In the above example the entities sent to the sink should have at least the properties ``subject_prop_id`` and ``message_prop_id``, i.e.:

::

    {
        "_id": "message_id",
        "message_prop_id": "This is the message to send",
        "subject_prop_id": "This is the subject of the message to send",
        "some_other_property": "Some other value"
    }

A note on multi-part messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To send multi-part email messages containing both a HTML and a plain-text version, you should provide templates for both
``body_template`` (or ``body_template_property``) and ``text_body_template`` (or ``text_body_template_property``).
The former should then contain your HTML message and the latter your plain-text version. If you omit the ``text_*``
properties and the body template contains HTML, the sink will attempt to extract a text-only version of the HTML
on a best-effort basis; i.e. this might not preserve the information contained in the HTML in the desired way.
