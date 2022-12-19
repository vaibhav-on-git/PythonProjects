from twilio.rest import Client 
#import os
#account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
#auth_token = os.environ.get('TWILIO_ACCOUNT_TOKEN')
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='yes, it is working as expected',      
                              to='whatsapp:+916360595319' 
                          ) 
 
print(message.sid)
