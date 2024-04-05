import requests
from bs4 import BeautifulSoup
from config import Config
from text_sender import TextSender


if __name__ == '__main__':
    r = requests.get('https://glastonbury.seetickets.com/content/extras')
    # r = requests.get('http://127.0.0.1:5000/')
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup)

    finder_status = True
    search_phrase = 'unbalance'
    xs = soup.find_all('p')
    for idx, content in enumerate(xs):
        # print(idx, content)
        if search_phrase in str(content):
            # print('sold OUT')
            break
        else:
            # print('NOT sold out')
            finder_status = False

    if finder_status:
        print(f"keyword: '{search_phrase}' found on site")
    else:
        config = Config.get_config()
        print(f"keyword: '{search_phrase}' NOT found on site .... send warning text message")
        TextSender.send_text(config)
