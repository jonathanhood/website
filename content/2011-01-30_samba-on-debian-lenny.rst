Samba on Debian Lenny
=====================

I've recently had to install the most simple of SAMBA setups.  The following setup is meant for the simplest of environments, where no authentication is required.  It is completely open in that anyone can read/write to the share.  Be warned: only use this in a situation where you are sure it is safe.  For me, it is great for a development server share or for sharing files on a home network. First, either login as root, or switch user to the root account.  To switch user::

    > su -

Now, install samba::

    >apt-get install samba

Now, we need to edit the samba configuration file::

    >pico /etc/samba/smb.conf

Look for the following key::

    #     security = user

And set to::

    security = share

Niow, at the end of the file, add this section::

    [SHARENAME]
         comment = Share Description
         path = /smb_share
         guest ok = yes
         browesable = yes
         create mask = 0777
         directory mask = 0777
         force user = nobody
         force group = nogroup
         writeable = yes

Create the directory we will be sharing::

    > mkdir /smb_share

And set permissions::

    > chmod a+rw /smb_share

Now, restart samba::

    > /etc/init.d/samba restart

And your done, the share should be up and going.

