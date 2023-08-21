import random
import threading
from selenium.webdriver.support.ui import Select
from data.web_params import *
from utils.common_web import get_image_path, get_date, get_time
from utils.find_element import get_element, get_element_by_xpath, get_elements_by_xpath
from web.web_locator_info import *
from time import sleep
from datetime import datetime

class WebActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def login(self):
        self.driver.get(login_url)
        self.driver.maximize_window()
        sleep(1)

    def sign_in(self):
        get_element(self.driver, login).click()
        get_element(self.driver, username).send_keys(account)
        get_element(self.driver, user_password).send_keys(password)
        get_element(self.driver, sign_in).click()
        self.driver.get(manage_url)

    def schedule_a_show(self, new_title):
        new_show = Show(title=new_title, cover_image=get_image_path(), date=get_date(), time=get_time())
        get_element(self.driver, schedule_a_show).click()
        get_element(self.driver, title).send_keys(new_show.title)
        # save_data(new_show.title)
        sleep(2)
        upload_file = get_element(self.driver, upload)
        upload_file.send_keys(new_show.cover_image)
        sleep(2)
        get_element(self.driver, date).send_keys(new_show.date)
        get_element(self.driver, time).send_keys(new_show.time)
        channel_dropdown = get_element(self.driver, channel)
        channel_dropdown.click()
        select = Select(channel_dropdown)
        select.select_by_visible_text(new_show.channel)
        creator_dropdown = get_element(self.driver, creator)
        creator_dropdown.click()
        select = Select(creator_dropdown)
        select.select_by_visible_text(new_show.creator)
        get_element_by_xpath(self.driver, add_listing).click()

    def common_create_steps(self, listing):
        sleep(5)
        get_element(self.driver, listing_title).send_keys(listing.title)
        option_dropdown = get_element(self.driver, select_an_option)
        # option_dropdown.click()
        select = Select(option_dropdown)
        select.select_by_visible_text(listing.option)
        sleep(2)
        get_element_by_xpath(self.driver, listing.assign_type).click()
        sleep(2)
        get_element_by_xpath(self.driver, listing.sell_type).click()
        if listing.min_bid is not None:
            get_element(self.driver, min_bid).send_keys(listing.min_bid)
        elif listing.assign_price is not None:
            get_element(self.driver, assign_price).click()
            sleep(1)
            spots = get_elements_by_xpath(self.driver, assign_list)
            for spot in spots:
                # spot.send_keys(listing.assign_price)
                spot.send_keys(random.randint(1, 99999))
                sleep(1)
            get_element(self.driver, assign_prices).click()
        elif listing.price_per_spot is not None:
            get_element(self.driver, price_per_spot).send_keys(listing.price_per_spot)
        sleep(2)
        get_element_by_xpath(self.driver, save_listing).click()

    def create_random_set_price_listing(self, num=1):
        i = 0
        while i < num:
            listing = Listing(title='random set price', assign_type=random_spot, sell_type=set_price,
                              price_per_spot=10000)
            self.common_create_steps(listing)
            i += 1

    def create_random_auction(self, num=1):
        i = 0
        while i < num:
            listing = Listing(title='random auction', assign_type=random_spot, sell_type=auction, min_bid=1000)
            self.common_create_steps(listing)
            i += 1

    def create_pick_spot_auction(self, num=1):
        i = 0
        while i < num:
            listing = Listing(title='pick auction', assign_type=pick_your_spot, sell_type=auction, min_bid=5000)
            self.common_create_steps(listing)
            i += 1

    def create_pick_spot_set_price(self, num=1):
        i = 0
        while i < num:
            listing = Listing(title='pick set price', assign_type=pick_your_spot, sell_type=set_price,
                              assign_price=1000)
            self.common_create_steps(listing)
            i += 1

    def publish(self):
        get_element_by_xpath(self.driver, publish).click()

    def search(self, new_title):
        get_element_by_xpath(self.driver, search_streams).send_keys(new_title)
        sleep(1)

    def edit(self):
        get_element_by_xpath(self.driver, edit_show).click()

    def show_detail(self, new_title):
        show_detail = LocatorInfo(locator=f"//*[contains(text(), '{new_title}')]/../../footer//*[@title='Details']")
        get_element_by_xpath(self.driver, show_detail).click()

    def set_media(self, item, option):
        # sleep(1)
        option_dropdown = get_element(self.driver, item, 15)
        # option_dropdown.click()
        select = Select(option_dropdown)
        select.select_by_visible_text(option)

    def set_inputs(self):
        sleep(5)
        self.set_media(camera_1, fake_device)
        self.set_media(camera_2, fake_device)
        self.set_media(camera_3, fake_device)
        self.set_media(audio, fake_audio)

    def go_live(self):
        sleep(0.5)
        on_live = False
        get_element_by_xpath(self.driver, go_live).click()
        while on_live is False:
            try:
                get_element_by_xpath(self.driver, end_stream)
                on_live = True
                break
            except:
                sleep(0.5)

    def end_stream(self):
        get_element_by_xpath(self.driver, end_stream).click()
        sleep(3)

    def add_listings(self):
        sleep(1)
        self.create_pick_spot_set_price()
        self.create_pick_spot_auction()
        self.create_random_set_price_listing()
        self.create_random_auction()

    def run_a_listing(self):
        sleep(1)
        get_elements_by_xpath(self.driver, listings_list)[0].click()

    def create_listing(self):
        get_element_by_xpath(self.driver, create_listing).click()

    def close_create(self):
        get_element_by_xpath(self.driver, close_create).click()

    def start_next_listing(self):
        get_element_by_xpath(self.driver, start_next_listing).click()

    def start_auction(self):
        get_element_by_xpath(self.driver, begin_auction, 30).click()

    def tap_start_ripping(self):
        get_element_by_xpath(self.driver, start_ripping).click()

    def find_ripping(self):
        try:
            get_element_by_xpath(self.driver, start_ripping, 1)
            return True
        except:
            return False

    def randomize_listing(self):
        sleep(5)
        get_element_by_xpath(self.driver, randomize_all_spot, 5).click()

    def run_overlays(self):
        i = random.randint(1, 3)
        try:
            get_element_by_xpath(self.driver, overlays).click()
            sleep(2)
            if i == 1:
                get_element_by_xpath(self.driver, fire).click()
            elif i == 2:
                get_element_by_xpath(self.driver, to_the_moon).click()
            else:
                get_element_by_xpath(self.driver, confetti).click()
        except:
            sleep(30)

    def overlay_thread(self):
        while True:
            self.run_overlays()
            sleep(30)

    def run_overlays_thread(self):
        thread = threading.Thread(target=self.overlay_thread)
        thread.start()

    def run_giveaway(self):
        try:
            get_element_by_xpath(self.driver, giveaway).click()
            get_element(self.driver, giveaway_title).send_keys("This is a test")
            sleep(2)
            get_element_by_xpath(self.driver, all_viewers).click()
            sleep(2)
            get_element_by_xpath(self.driver, launch_giveaway).click()
            sleep(300)
        except:
            sleep(10)

    def giveaway_thread(self):
        while True:
            self.run_giveaway()

    def run_giveaway_thread(self):
        thread = threading.Thread(target=self.giveaway_thread)
        thread.start()

    def threads_flow(self):
        event1 = threading.Event()

        def thread1_func():
            self.run_giveaway()
            event1.set()

        def thread2_func():
            event1.wait()
            i = 0
            while i < 10:
                self.run_overlays()
                i += 1

        thread1 = threading.Thread(target=thread1_func)
        thread2 = threading.Thread(target=thread2_func)
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()

    def all_threads_flow(self):
        while True:
            self.threads_flow()

    def run_threads_flow(self):
        thread = threading.Thread(target=self.all_threads_flow)
        thread.start()

    def login_flow(self, show_title, listing_type):
        self.login()
        self.sign_in()
        self.schedule_a_show(show_title)
        if listing_type == 'rs':
            self.create_random_set_price_listing()
        elif listing_type == 'ra':
            self.create_random_auction()
        elif listing_type == 'ps':
            self.create_pick_spot_set_price()
        else:
            self.create_pick_spot_auction()
        self.publish()
        self.search(show_title)
        self.show_detail(show_title)
        self.set_inputs()
        self.run_a_listing()
        self.go_live()
        self.run_giveaway_thread()
        sleep(10)
        self.run_overlays_thread()

    def after_test(self):
        self.driver.close()
        self.driver.quit()

    def run_forever(self, end_time, func):
        is_forever = True
        while is_forever:
            current_time = datetime.now()
            if current_time > end_time:
                self.end_stream()
                break
            func()

    def pick_auction(self):
        auction_sold_out = False
        while auction_sold_out is not True:
            try:
                self.start_auction()
            except:
                if self.find_ripping() is True:
                    auction_sold_out = True
                else:
                    pass
        self.tap_start_ripping()
        self.create_listing()
        self.create_pick_spot_auction()
        self.close_create()
        self.start_next_listing()
        try:
            self.tap_start_ripping()
            self.start_next_listing()
        except:
            pass

    def p_s_flow(self):
        try:
            self.tap_start_ripping()
            self.create_listing()
            self.create_pick_spot_set_price()
            self.close_create()
            self.start_next_listing()
            try:
                self.tap_start_ripping()
                self.start_next_listing()
            except:
                raise
        except:
            print('Listing not sold out yet')

    def random_auction(self):
        auction_sold_out = False
        while auction_sold_out is not True:
            try:
                self.start_auction()
            except:
                if self.find_ripping() is True:
                    auction_sold_out = True
                else:
                    pass
        self.tap_start_ripping()
        self.create_listing()
        self.create_random_auction()
        self.close_create()
        self.start_next_listing()
        try:
            self.tap_start_ripping()
            self.start_next_listing()
        except:
            pass

    def random_set_price(self):
        try:
            self.randomize_listing()
            self.create_listing()
            self.create_random_set_price_listing()
            self.close_create()
            self.start_next_listing()
            try:
                self.tap_start_ripping()
                self.start_next_listing()
            except:
                raise
        except:
            print('Listing not sold out yet')
