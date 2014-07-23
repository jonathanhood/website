Virtual Email Domains with Postfix and Courier
##############################################

I've recently had to setup postfix and courier on a server that hosts multiple domains. Setting up the two for this task isn't hard, but proper documentation and tutorials can be hard to come by. We won't be using any extra services like MySQL to store the users and mailbox mappings. It works great for a small number of domains. I'm going to assume that Postfix and Courier are already set up and work for email addresses at your server's hostname. This how-to was tested on Debian Lenny. For our example, we will be creating the mail@foobar.org email address.

.. sourcecode:: shell
 
 > pico /etc/postfix/main.cf

There, you are going to add a few configuration keys to the end of the file.

.. sourcecode:: shell

  virtual_mailbox_domains = foobar.org
  virtual_mailbox_base = /var/mail
  virtual_mailbox_maps = hash:/etc/postfix/vmail
  virtual_uid_maps = static:6000
  virtual_gid_maps = static:6000

Now, lets create the /etc/postfix/vmail file. This is where we will list the mailboxes and their directory to be stored

.. sourcecode:: shell
 
  > pico /etc/postfix/vmail
  #Insert these values
  mail@foobar.org          /var/mail/foobar.org/mail/

Now, we need to create a user for postfix to use to put the mail into each mailbox

.. sourcecode:: shell
 
  > groupadd -g 6000 vmail
  > useradd -g vmail -u 6000

Now, create the mailbox directory and give permission to vmail.

.. sourcecode:: shell
 
  > mkdir -p /var/mail/foobar.org
  > chown vmail:vmail -R /var/mail

Now, create the hash of our vmail mapping file. This has to be done every time you adjust the /etc/postfix/vmail file. Then, we'll reload postfix and let it run the new config.

.. sourcecode:: shell
 
  > postmap /etc/postfix/vmail
  > postfix reload

Ok, postfix is set up. Now, lets setup courier. For courier, we will be using the userdb auth package for authentication. For that to work, we need to give it a list of users with their mail directory. Then we will assign a password to each user. The first step is to update the authdaemonrc configuration.

.. sourcecode:: shell
  
  > pico /etc/courier/authdaemonrc
  #Change this key
  authmodulelist="authpam"
  #to
  authmodulelist="authpam authuserdb"

Now, lets create the mail user in userdb. Whenever we create a user, we need to set uid=6000 and gid=6000 since this is the id of the vmail user used by postfix. The other variables point to the mailbox directory created by postfix.

.. sourcecode:: shell

  > userdb mail@foobar.org set uid=6000 gid=6000 home=/var/mail/foobar.org/mail \
    mail=/var/mail/foobar.org/mail
  > userdbpw -md5 | userdb mail@foobar.org set systempw

Every time we change userdb, we have to update it. To do so:

.. sourcecode:: shell

  > makeuserdb

Now, just reload authdaemonrc.

.. sourcecode:: shell

  > /etc/init.d/authdaemonrc reload

That should do it. Try logging in to the new email address. Note that you must use the full email address as the username.

Credit to dannorth.net_ for a lot of this information. In many cases these steps are verbatim, but some of them had to be corrected (hence the motivation for this page).

.. _dannorth.net: http://dannorth.net/2007/09/09/virtual-mailboxes-with-courier-imap-and-postfix

