from pyrubi import Client
from pyrubi.types import Message
from geopy.geocoders import Nominatim
client = Client("bog_bot")
geolocator = Nominatim(user_agent="geo_locator_bot")

# تابع برای دریافت مختصات جغرافیایی (عرض و طول)
def get_location(address):
    location = geolocator.geocode(address)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None
@client.on_message()    
def send_location(message:Message):
   
    address = message.text  # گرفتن متن وارد شده توسط کاربر
    guid =message.object_guid
    loc = get_location(address)  # دریافت مختصات جغرافیایی
    message.reply("درحال به دست اوردن اطلاعات مکان")
    if loc:
        
        
        # ارسال لوکیشن به کاربر
        client.send_location(guid,loc[0], loc[1])
        message.reply( f"مکان '{address}' ارسال شد.")
        
         
    else:
        
        message.reply("متاسفانه نتوانستم مکان را پیدا کنم. لطفاً آدرس یا مکان دیگری را امتحان کنید.") 

client.run()
