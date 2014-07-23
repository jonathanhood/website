Signed SSL Cert on Debian Lenny
===============================

This is a follow up to the previous post, where I showed how-to generate a CSR. Now, I'm going to assume that you have a signed certificate and a CA bundle. Configuring apache to use these items is a relatively simple affair. First, copy them to the proper place on your server::

    > mv public.crt /etc/ssl/certs/public.crt
    > mkdir /etc/apache2/ssl.cert
    > mv bundle.ca-bundle /etc/apache2/ssl.cert/bundle.ca-bundle

Now, configure apache to use these certificate files. You'll need to give apache 3 files.


1. Your private key.
2. The public certificate.
3. The CA bundle.


The 1st item was generated before you created the CSR, the second 2 are provided by your CA.  I'll assume that the default ssl configuration for apache is in use::

    > vim /etc/apache2/sites-enabled/default-ssl

There, find the following keys and set them to the proper values::

    SSLCertificateFile /etc/ssl/certs/public.crt
    SSLCertificateKeyFile /etc/ssl/private/private.key
    SSLCACertificateFile /etc/apache2/ssl.cert/bundle.ca-bundle

Now, just need to reload apache::

    > /etc/init.d/apache2 reload 

That should be it. You should now stop seeing certificate warnings whenever you visit an SSL page.

