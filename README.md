# WhatsApp-Whatabot-API
Personal WhatsApp Bot on MicroPython

Requires: Any microcontroller to send a message to execute a http GET.

## Contents

1. [Overview](./README.md#1-overview)
2. [Creating a WhatsApp Whatabot API](./README.md#2-creating)
3. [Install](./README.md#3-install)
4. [Quick start](./README.md#4-start)

## 1. Overview

[Whatabot API](https://whatabot.net/#about_section) is a service that allows you to send yourself messages in realtime. You only have to register your phone and take note of your api key! To send a message is nessesary to execute a http GET from your microcontroller. A module  [urequests](https://makeblock-micropython-api.readthedocs.io/en/latest/public_library/Third-party-libraries/urequests.html) is used to send GET requests. It's easy to use and you can receive realtime alterts in all your projects.

## 2. Creating a WhatsApp Whatabot API
How to get the necessary data to create WhatsApp Whatabot API:  
[Create the Whatabot contact](https://whatabot.net/#about_section)

## 3. Install
Download a code and unpack it into your project folder. Use Thonny IDE or other IDE for upload your code in microcontroller board.

## 4. Quick start
#### Typical Wi-Fi connection code for ESP board

import network, urequests

wlan_id = 'Mikro2'
wlan_pass = '196613036594'

phone_number = '380673820543'
api_key = '92941499'

def connect(ssid, passwd):
    wlan.disconnect()
    wlan.connect(ssid, passwd)
    while not wlan.isconnected():
        pass
    return wlan.ifconfig()

