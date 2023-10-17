# WhatsApp-Whatabot-API
Personal WhatsApp Bot on MicroPython

Requires: Any microcontroller to send a message to execute a http GET.

## Contents

1. [Overview](./README.md#1-overview)
2. [Creating a WhatsApp Whatabot API](./README.md#2-Creating-a-WhatsApp-Whatabot-API)
3. [Install](./README.md#3-install)
4. [Quick start](./README.md#4-Quick-start)
5. [Some notes](./README.md#5-Some-notes-when-preparing-messages-for-sending)

## 1. Overview

[Whatabot API](https://whatabot.net/#about_section) is a service that allows you to send yourself messages in realtime. You only have to register your phone and take note of your api key! To send a message is nessesary to execute a http GET from your microcontroller. A module  [urequests](https://makeblock-micropython-api.readthedocs.io/en/latest/public_library/Third-party-libraries/urequests.html) is used to send GET requests. It's easy to use and you can receive realtime alterts in all your projects.

## 2. Creating a WhatsApp Whatabot API
How to get the necessary data to create WhatsApp Whatabot API:  
[Create the Whatabot contact](https://whatabot.net/#howtouse)

## 3. Install
Download a code and unpack it into your project folder. Use Thonny IDE or other IDE for upload your code in microcontroller board.

## 4. Quick start
#### Typical Wi-Fi connection code for ESP board (Station mode)

```python
import network

def connect(ssid, passwd):
    wlan.disconnect()
    wlan.connect(ssid, passwd)
    while not wlan.isconnected():
        pass
    return wlan.ifconfig()

if __name__ == '__main__':
    wlan_id = 'your wi-fi ssid'
    wlan_pass = 'your password'
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print(connect(wlan_id, wlan_pass))
```
#### Creating an object of the Whatsapp_bot class

```python
class Whatsapp_bot:
    """This will be our Whatsapp bot"""
    
    def __init__(self, phone_number, api_key):
        self.phone_number = phone_number
        self.api_key = api_key
        
    def send_message(self, message):
        url = 'https://api.whatabot.net/whatsapp/sendMessage?apikey=' + self.api_key + '&text=' + message + '&phone=' + self.phone_number
        response = urequests.get(url)
        print('Message sent successfully!' if response.status_code == 200 else 'Error sending message!'+'\n'+response.text)
```
#### Example to Send GET request API

```python
if __name__ == '__main__':
    import urequests

    phone_number = 'your phone number'
    api_key = 'your api key'

# створюємо примірник класу Whatsapp_bot
    whatsapp_bot = Whatsapp_bot(phone_number, api_key)
# символ переноса рядка для Whatsapp - '%0a' !
    message = 'Тестування надсилання кирилиці:%0aПросто деякий текст!.%0a Ще деякий текст!'
    whatsapp_bot.send_message(message)
```
## 5. Some notes when preparing messages for sending

There may be an error when sending some characters: "Status":"Error. Missing or incorrect number".  
Encoding should be used to send the following characters:  
|    Symbol   | Encoding |
| ----------- | -------- |
|     &       |    %26   |
|     #       |    %23   |
|  newline    |    %0a   |
|     ~       |    %7e   |
  
Symbols { } [ ] / \ ^ < > ! ? : ; . , - + = _ ( ) * " @ $ are sent normally 

