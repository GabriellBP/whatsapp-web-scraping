from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# you can set the chromedriver path on the system path and remove this variable
CHROMEDRIVER_PATH = 'utils/chromedriver.exe'


def send_a_message(driver):
    name = input('Enter the name of a user')
    msg = input('Enter your message')

    # saving the defined contact name from your WhatsApp chat in user variable
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    # name of span class of contatct
    msg_box = driver.find_element_by_class_name('_3uMse')
    msg_box.send_keys(msg)


def main():
    options = Options()
    options.add_argument('user-data-dir=./User_Data')
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
    driver.get('https://web.whatsapp.com/')
    input('Enter after scanning QR code or after the page has fully loaded')
    send_a_message(driver)


if __name__ == "__main__":
    main()
