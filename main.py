from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


# you can set the chromedriver path on the system path and remove this variable
CHROMEDRIVER_PATH = 'utils/chromedriver.exe'
global SCROLL_TO, SCROLL_SIZE


# test sending a message
def send_a_message(driver):
    name = input('Enter the name of a user')
    msg = input('Enter your message')

    # saving the defined contact name from your WhatsApp chat in user variable
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    # name of span class of contatct
    msg_box = driver.find_element_by_class_name('_3uMse')
    msg_box.send_keys(msg)
    sleep(5)


def scroll(dr, last_element):
    global SCROLL_TO, SCROLL_SIZE

    print('>>> scrolling')
    side_pane = dr.find_element_by_id('pane-side')
    print('.')
    dr.execute_script('arguments[0].scrollTop = '+str(SCROLL_TO), side_pane)
    sleep(3)
    SCROLL_TO += SCROLL_SIZE


def main():
    global SCROLL_TO, SCROLL_SIZE
    SCROLL_SIZE = 600
    SCROLL_TO = 600

    options = Options()
    options.add_argument('user-data-dir=./User_Data')  # saving user data so you don't have to scan the QR Code again
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
    driver.get('https://web.whatsapp.com/')
    input('Enter after scanning QR code or after the page has fully loaded')
    # send_a_message(driver)
    # retrieving the contacts
    print('>>> getting contact list')
    contacts = set()
    length = 0
    while True:
        contacts_sel = driver.find_elements_by_class_name('_357i8')  # get just contacts ignoring groups
        contacts.update(set([j.text for j in contacts_sel]))
        if length == len(contacts):
            break
        else:
            length = len(contacts)
        scroll(driver)
    print(len(contacts), "contacts retrieved")
    for i in contacts:
        print(i)


if __name__ == "__main__":
    main()
