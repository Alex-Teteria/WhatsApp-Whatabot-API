import network, urequests

def connect(ssid, passwd):
    wlan.disconnect()
    wlan.connect(ssid, passwd)
    while not wlan.isconnected():
        pass
    return wlan.ifconfig()

class Whatsapp_bot:
    """This is our Whatsapp bot"""
    
    def __init__(self, phone_number, api_key):
        self.phone_number = phone_number
        self.api_key = api_key
        
    def send_message(self, message):
        url = 'https://api.whatabot.net/whatsapp/sendMessage?apikey=' + self.api_key + '&text=' + message + '&phone=' + self.phone_number
        response = urequests.get(url)
        print('Message sent successfully!' if response.status_code == 200 else 'Error sending message!'+'\n'+response.text)

if __name__ == '__main__':
    wlan_id = 'your wi-fi ssid'
    wlan_pass = 'wi-fi password'
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print(connect(wlan_id, wlan_pass))

    phone_number = 'your phone number'
    api_key = 'your apikey'

# створюємо примірник класу Whatsapp_bot
    whatsapp_bot = Whatsapp_bot(phone_number, api_key)
# символ переноса рядка для Whatsapp - '%0a' !
    message = 'Тест повідомлення кирилицею%0aДеякі символи @ :) ! , ?%0aНорма!%0aЩе деякий текст%0aQwerty 1234567890'
    whatsapp_bot.send_message(message)
  
