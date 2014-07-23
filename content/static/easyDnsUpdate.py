import httplib, base64

def getPublicIPAddr():
	getip = httplib.HTTPConnection( 'ipv4.icanhazip.com' )

	getip.request( 'GET', '/' )

	ip = getip.getresponse()

	ipstr = ip.read().strip()

	getip.close()
	
	return ipstr

def updateEasyDNS( domain ):
	username = "jhood06"
	password = "!blah!1337"
	base64encode = base64.encodestring( '%s:%s' % (username, password)).replace( '\n', '' )

	con = httplib.HTTPConnection( 'api.cp.easydns.com' )

	headers = { 'Authorization': "Basic %s" % base64encode } 
	con.request( 'GET', '/dyn/dynsite.php?hostname=%s&myip=%s' % (domain,getPublicIPAddr()) , "", headers)

	respn = con.getresponse().read()

	con.close()

	return respn


updateEasyDNS( 'jonathanandalexis.org' )
updateEasyDNS( 'wedding.jonathanhood.org' )
updateEasyDNS( 'jonathanhood.org' )

