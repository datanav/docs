Changelog
=========

2018-09-10
----------
* Added a :ref:`User Selectable Languages<gdpr_data_access_portal_user_selectable_languages>` config option to
  the Data Access Portal configuration.

2018-06-15
----------
* Added color pickers that can change the theming of the Data Access Portal. As of now, primary color will only change the header color.

2018-06-13
----------
* Added a new "``GDPR operations``" role for non-admin users that will be uploading or downloading access request spreadsheets

2018-06-12
----------
* Added a new "``gdpr-version-tag``" environment variable that can have the values "latest", "nightly", "weekly" or "weekly-prod". This will control how often the GDPR platform templates (pipes) are updated. The default value is "nightly". You should only use "latest" with care as it might be unstable during a day. Production systems should always use "weekly" or "weekly-prod" values.
