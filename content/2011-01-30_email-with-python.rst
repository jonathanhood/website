How-To Send Email with Python
#############################

Sending email from a script is a very useful tool. On a linux machine, you can setup a mta to get mail from any cron jobs, but there are alot of situations where that functionality may not be available. This happened to me the other day, and I found the fantastic smtplib that exists in the python standard library. So, you need to send a message? Its super easy, first import smtplib and connect to a server

.. sourcecode:: python
  
  import smtplib
  server = smtplib.SMTP( "your.smtp.address" )

At this point there may or may not be a few extra steps to perform. My test server is configured for STARTTLS and authentication. I'll detail the steps for that here.

.. sourcecode:: python
  
  server.starttls()
  server.ehlo()
  server.login( "username", "password" )

Now, build your message. The primary downside to smtplib is that you have to build the header yourself. As it turns out, that is pretty trivial.

.. sourcecode:: python

  mailto = "test.email@foo.com"
  mailfrom = "otheremail@foo.com"
  subject = "Test Email"
  head = "From: " + mailfrom + "\r\nTo: " + mailto 
       + "\r\nSubject: " + subject + "\r\n\r\n"

The rest of the message is just plain text.

.. sourcecode:: python

  body = "Hello world!"

Now, put the two together and send the message.

.. sourcecode:: python

  msg = head + body
  server.sendmail( mailfrom, mailto, msg )

I wrote a function to encapsulate this behavior, maybe it will be useful for you.

.. sourcecode:: python

  def sendEmail( mailfrom, mailto, subject, body, servername, username, password ):
    import smtplib
    server = smtplib.SMTP( servername )
    server.starttls()
    server.ehlo()
    server.login( username, password )
    msg = "From: " + mailfrom + "\r\nTo: " + mailto 
          + "\r\nSubject: " + subject + "\r\n\r\n" + body
    server.sendmail( mailfrom, mailto, msg )


