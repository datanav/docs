Two step collect
================

All datatypes should use a minimum of two pipes for the collect pipe line. These are named ``-all`` and ``-collect``. This gives extensibility if webhook events if they will be added later. If also gives us the possibility to verify deletion tracked entities in the collect template.