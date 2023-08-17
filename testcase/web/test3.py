
from time import sleep

from utils.common_web import get_title
from web.web_user_actions import WebActions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta

def test3():
    show_title = get_title('Auto_R_A')
    chrome_options = Options()
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    chrome_options.add_argument("--use-fake-device-for-media-stream")
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    do = WebActions(driver)
    start_time = datetime.now()
    end_time = start_time + timedelta(days=1)
    do.login()
    do.sign_in()
    do.schedule_a_show(show_title)
    do.create_random_auction()
    do.publish()
    do.search(show_title)
    do.show_detail(show_title)
    do.set_inputs()
    do.run_a_listing()
    do.go_live()
    do.run_giveaway_thread()
    sleep(10)
    do.run_overlays_thread()
    is_forever = True
    while is_forever:
        current_time = datetime.now()
        if current_time > end_time:
            do.end_stream()
            break
        auction_sold_out = False
        while auction_sold_out is not True:
            try:
                do.start_auction()
            except:
                if do.find_ripping() is True:
                    auction_sold_out = True
                else:
                    pass
        do.tap_start_ripping()
        do.create_listing()
        do.create_random_auction()
        do.close_create()
        do.start_next_listing()
        try:
            do.tap_start_ripping()
            do.start_next_listing()
        except:
            pass
    driver.close()
    driver.quit()