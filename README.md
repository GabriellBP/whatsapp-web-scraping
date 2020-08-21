# Whatsapp Web Scraping
Just a simple whatsapp web scraping to collect data from conversations.

## To run:
 - Download [ChromeDriver](https://chromedriver.chromium.org/downloads "ChromeDriver") and put it on the utils folder, if you prefer you can intall it and add it to the PATH System
 - Install all dependencies with the command `pip install requirements.txt`
 - After that run the command `python main.py` and wait the page to open and show the whatsapp-web interface
 - Use the QR Code to connect with your whatsapp and just after that press enter on the command line
 - Wait the program runs and enjoy your collected data ^^
 
## Know troubles:
 Can occurr that the whatsapp change the css classes name the it uses, if it occurrs the program won't be able to get the contact list, scroll the side-pane or get the messages. To solve that you must have to look for the current css class name and change in the code. To help in that, below there are some prints indicating the css classes used

<kbd><img src="readme/image_1.png" /></kbd>
<kbd><img src="readme/image_2.png" /></kbd>
<kbd><img src="readme/image_3.png" /></kbd>
<kbd><img src="readme/image_4.png" /></kbd>
