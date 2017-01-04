from twilio.rest import TwilioRestClient 

# put your own credentials here 
ACCOUNT_SID = "ACc4ac9e116af5468d0dc6476c6c3947af" 
AUTH_TOKEN = "#############################" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
	to="+91 9075220047", 
	from_="+12017208731", 
	body="Hello ",  
) 

