Continuation
============

Continuation (also known as incremental loading) involves extracting only the data that has changed since the last extraction cycle.

Implementing continuation in a connector
----------------------------------------

See the section on :ref:`continuation support <continuation_support>`.


Example: system config with continuation
----------------------------------------

::

   "<datatype>-list": {
      "method": "GET",
      "page_size": 100,
      "url": "https://api.example.com/v1/data?updated_at_min={{since}}"
    }

* corresponding pipe must have ``"supports_since": true`` in the source.