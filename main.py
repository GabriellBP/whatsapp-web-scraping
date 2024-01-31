import os
import pickle

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup


# you can set the chromedriver path on the system path and remove this variable
CHROMEDRIVER_PATH = 'utils/chromedriver'
global SCROLL_TO, SCROLL_SIZE


def pane_scroll(dr):
    global SCROLL_TO, SCROLL_SIZE

    print('>>> scrolling side pane')
    side_pane = dr.find_element_by_id('pane-side')
    dr.execute_script('arguments[0].scrollTop = '+str(SCROLL_TO), side_pane)
    sleep(3)
    SCROLL_TO += SCROLL_SIZE


def get_messages(driver, contact):
    global SCROLL_SIZE
    print('>>> getting messages')
    conversations = []
    # TODO(kevinsu): Pass in
    contact = "J Squared Friendmoon"

    user = driver.find_element_by_xpath('//span[contains(@title, "{}")]'.format(contact))
    user.click()
    sleep(3)
    conversation_pane = driver.find_element_by_xpath("//div[@class='_5kRIK']")

    count = 0
    scroll_count = 5
    messages = set()
    scroll = SCROLL_SIZE
    while count <= scroll_count:
        print(f"[{count}/{scroll_count}] scrolling!")
        driver.execute_script('arguments[0].scrollTop = -' + str(scroll), conversation_pane)
        sleep(2)
        scroll += SCROLL_SIZE
        count += 1
    soup = BeautifulSoup(conversation_pane.text, 'html.parser')
    lines = soup.text.strip().splitlines()

    long_names = {"Aulaire Naughton Pistilli", "Mun Yee Kelly", "Zepher Kaela Bree"}
    for text in lines:
        text = text.removeprefix("~")
        text = text.strip()
        if "+1" in text or \
                "PM" in text or \
                "AM" in text or \
                "0:" in text or \
                text.isnumeric() or \
                text == "Photo" or \
                text in long_names or \
                len(text.split(" ")) <= 2:
            continue
        print(text + "\n")
        messages.add(text)
    conversations.append(messages)
    filename = 'collected_data/conversations/{}.json'.format(contact)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'wb') as fp:
        pickle.dump(messages, fp)
    return conversations


def main():
    global SCROLL_TO, SCROLL_SIZE
    SCROLL_SIZE = 600
    SCROLL_TO = 600
    conversations = []

    options = Options()
    options.add_argument('user-data-dir=./User_Data')  # saving user data so you don't have to scan the QR Code again
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
    driver.get('https://web.whatsapp.com/')
    input('Press enter after scanning QR code or after the page has fully loaded\n')

    try:
        # retrieving the contacts
        print('>>> getting contact list')
        contacts = set()
        length = 0
        count = 1
        while count > 0:
            contacts = set(driver.find_elements_by_class_name('_21S-L'))
            conversations.extend(get_messages(driver, list(contacts)))
            contacts.update(contacts)
            if length == len(contacts) and length != 0:
                break
            else:
                length = len(contacts)
            pane_scroll(driver)
            count -= 1
        print(len(contacts), "contacts retrieved")
        print(len(conversations), "conversations retrieved")
        filename = 'collected_data/all.json'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'wb') as fp:
            pickle.dump(conversations, fp)
    except Exception as e:
        print(e)
        driver.quit()


if __name__ == "__main__":
    main()
