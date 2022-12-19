from twilio.rest import Client 
#import os
account_sid = 'AC464749a7c1346141b1c373b53c1785d1'
auth_token = 'f6ad194dfb5833536a15f85000259a1f'
#account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
#auth_token = os.environ.get('TWILIO_ACCOUNT_TOKEN')
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='yes, it is working as expected',      
                              to='whatsapp:+916360595319' 
                          ) 
 
print(message.sid)
