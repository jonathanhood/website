EasyDNS With Python
###################

I recently needed a simple dynamic DNS updater for the EasyDNS dns service. There was a linux client available, but it was written in C and required quite a bit of work to get working. So, I wrote a simple python library to do the job.

`[Download] <{filename}/static/easyDnsUpdate.py>`_

**Features**

* Retrieve your publicly available IP address using the service at icanhazip.com
* Update a domain in the EasyDNS service with the ip address of the current system.

**Requirements**

* Python 2.6.x, Python 2.7.x
* This *will not work* in Python 3.x

.. sourcecode:: python

  import ddns
  print ddns.getPublicIPAddr()
  ddns.username = 'username'
  ddns.password = 'password'
  ddns.updateEasyDNS( 'my.domain.com' )

