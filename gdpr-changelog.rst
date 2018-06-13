Changelog
=========


2018-06-13
----------
* Added a new "``GDPR operations``" role for non-admin users that will be uploading or downloading access request spreadsheets

2018-06-12
----------
* Added a new "``gdpr-version-tag``" environment variable that can have the values "latest", "nightly", "weekly" or "weekly-prod". This will control how often the GDPR platform templates (pipes) are updated. The default value is "nightly". You should only use "latest" with care as it might be unstable during a day. Production systems should always use "weekly" or "weekly-prod" values.
