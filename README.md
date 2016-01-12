evepilots
=========
Designed as a replacment/update to EVE Who with added features from Dotlan EVE
Pilots is a web service for viewing details about capsuleers, corporations and
alliances within New Eden. Both services offer great products but Dotlan is
esigned primarily as a mapping service and EVE Who is lacking a lot of features
that EVE Pilots tries to add.

The primary goal of EVE Oilots is to offer a one stop service for looking up
information (except kills, zKillbaord covers that well enough) on capsuleers,
corporations, and alliances.

Features EVE Pilots tries to add ontop of the basic information that EVE Who
offers is graphs of security status for capsuleers, graphs of member counts for
corporations and alliances, a better search, and hopefully much more over time.

This application is in the early stages of development and not ready for public
use yet.

TODO
====

Backend:
* Move corporation utilities to a corporations service
* Add an update corporations command
* Add alliances
* Add an update alliances command
* Add a daily calculation of a corporations member count
* Add a daily calculation of a alliances corporation count
* Add a daily calculation of a alliances member count
* Track a corporations alliance history
* Track a capsuleers sec status history
* Calculate a corporations retention some how
* Scrape for new capsuleers

Frontend:
* Add search for capsuleers, corporations, alliances
* Show top corporations and alliances in member count
* Add a details page for corporations
* Add a details page for alliances
* Add employment history to the capsuleer details page
* Add current corporation to capsuleer details page
* Add current alliance to capsuleer details page
* Corporation details should list average sec status
* Corporation details should show average sec status over time
* Pick a corporation and a date and see where all of the members of that
corporation at that time are now.
* 

Environment Variables
=====================
* EPI_SECRET_KEY: Secret key used by Flask for securing cookies and such. Might
remote this as no feature currently needs it. Leaving for now since it's a basic
config of most web apps and might need it later.
* EPI_SQLA_URI: URI to a valid SQLAlchemy backend. Postgress is used in dev and
the recommended backend.
* EPI_CELERY_BROKER_URL: URL to the celery broker for processing tasks such as
updating capsuleer information or calculating daily corporation member counts.
* 

Manage Commands
===============
* update_capsuleers: 
* load_capsuleers: 
* update_corporations: 