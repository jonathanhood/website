How-to Generate a CSR
=====================

:category: Notes

I recently found myself in need of a csr for work project, and found the documentation a bit lacking.  Here is how I accomplished that task.  I'm going to make the following assumptions:


- You are using Debian 5.0 Lenny
- You have apache2 installed, and SSL configured with a self-signed certificate.


A CSR is the request you send to a CA for a signed certificate. Generating one is straight forward, first we have to generate a private key::

    > cd /etc/ssl/private
    > openssl genrsa -out private.key 2048
    > chmod 600 private.key

Now that we have generated a private key, we can generate the CSR. It is going to ask a bunch of questions, answer with the same values used whenever you created the account with your CA::

    > openssl req -new -key private.key -out request.csr

Give that CSR to the CA, and they will generate you an SSL certificate. I'll cover giving that certificate to apache in a later article.
