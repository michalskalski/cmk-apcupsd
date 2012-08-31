[cmk-apcupsd](http://github.com/aikinaro/cmk-apcupsd) Check_MK package for monitoring UPS managed by apcupsd
=========

Description
---------

This is package for Check_MK which allow to checks status of ups managed by apcupsd demon. 
Package contain plugin for check_mk linux agent, templates for pnp4nagios and perfometer plugins.
You can monitor:
* UPS status
* battery charge
* load capacity
* internal temperature
* input, output and battery voltage level
* remaining runtime on battery

Avaliable checks are dependet on which model of ups you have. Package was tested on APC Smart-UPS 2200 RM. 
 

Requirements
---------

1. [Check_MK](http://mathias-kettner.de/check_mk_download.html) (tested on 1.2.0p1 and 1.2.0p2) + [pnp4nagios >= 0.6.x](http://docs.pnp4nagios.org/pnp-0.6/start)
2. [Apcupsd](http://www.apcupsd.org/)

Installation
-----------

1. Dowload mpk file on host where check_mk is installed and run:
   ```
   check_mk -P install cmk-apcupsd-[VERSION].mpk
   ```
2. On host which run apcupsd install check_mk_agent, and put agents/plugins/apcupsd from this repo in check_mk_agent plugins directory (/usr/lib/check_mk_agent/plugins/)
3. Rescan services for monitored host

