from data.created_show import show_name


class LocatorInfo:
    def __init__(self, by_type=None, locator=None):
        self.type = by_type
        self.locator = locator


"Login"

login = LocatorInfo('link text', 'Sign in')
username = LocatorInfo('id', 'user_email_or_username')
user_password = LocatorInfo('id', 'user_password')
sign_in = LocatorInfo('id', 'submit-button')

"Home page"
schedule_a_show = LocatorInfo('class name', 'fanatics-button--large')
search_streams = LocatorInfo(locator="//*[@id='live_stream_search']/input")
edit_show = LocatorInfo(locator=f"//*[contains(text(), {show_name})]/../../footer//*[@title='Edit']")

"Schedule page"
title = LocatorInfo('id', 'stream-title')
upload = LocatorInfo('id', 'cover_image_upload')
date = LocatorInfo('id', 'startsAtDate')
time = LocatorInfo('id', 'startsAtTime')
channel = LocatorInfo('id', 'live_stream-form_channel_id')
creator = LocatorInfo('id', 'live_stream-form_staffers_0_id')
breaker = LocatorInfo('id', 'live_stream-form_staffers_1_id')
add_listing = LocatorInfo(locator='//*[@id="live_stream-form"]/button')

'''Listing page'''
save_draft = LocatorInfo(locator='//*[@id="phx-F3kPodRmbxV3l21B"]/div/header/div/a/button')
publish = LocatorInfo(locator='//header/div/button')
listing_title = LocatorInfo('id', 'create-listing-form_title')
select_an_option = LocatorInfo('id', 'create-listing-form_break_template_id')
random_spot = LocatorInfo(locator="//*[@class='row'][2]/fieldset[1]/div/label[1]")
pick_your_spot = LocatorInfo(locator="//*[@class='row'][2]/fieldset/div/label[2]")
price_per_spot = LocatorInfo('id', 'create-listing-form_price_in_cents')
set_price = LocatorInfo(locator="//*[@class='row'][2]/fieldset[2]/div/label[1]")
auction = LocatorInfo(locator="//*[@class='row'][2]/fieldset[2]/div/label[2]")
assign_price = LocatorInfo('id', 'open-assign-price-modal')
save_listing = LocatorInfo(locator="//*[contains(text(), ' Save listing and add another')]")
assign_list = LocatorInfo(locator="//*[@class='dollar-input']/input")
assign_prices = LocatorInfo('id', 'assign-prices-button')
close_assign_prices = LocatorInfo('id', 'close-spot-pricing-modal')
min_bid = LocatorInfo('id', 'create-listing-form_minimum_bid_in_cents')

'''Detail page'''
camera_1 = LocatorInfo('id', 'primarySourceInputListIVS')
camera_2 = LocatorInfo('id', 'secondarySourceInputListIVS')
camera_3 = LocatorInfo('id', 'securitySourceInputListIVS')
audio = LocatorInfo('id', 'audioSourceInputListIVS')
go_live = LocatorInfo(locator="//*[contains(text(), 'Go live')]")
end_stream = LocatorInfo(locator="//*[contains(text(), 'End show')]")
listings_list = LocatorInfo(locator="//*[@class='listing']")
create_listing = LocatorInfo(locator="//*[contains(text(), 'Create new listing')]")
start_ripping = LocatorInfo(locator="//*[contains(text(), 'Start ripping')]")
overlays = LocatorInfo(locator="//*[contains(text(), 'Overlays')]")
fire = LocatorInfo(locator="//*[contains(text(), 'Fire')]")
to_the_moon = LocatorInfo(locator="//*[contains(text(), 'To the moon')]")
confetti = LocatorInfo(locator="//*[contains(text(), 'Confetti')]")
giveaway = LocatorInfo(locator="//*[contains(text(), 'Giveaway')]")
randomize = LocatorInfo(locator="//*[contains(text(), 'Randomize')]")
one_up_auction = LocatorInfo(locator="//*[@class='card']/button//*[contains(text(), 'Auction')]")

'''create listing'''
close_create = LocatorInfo(locator="//*[contains(text(), 'Create a listing')]/button")

'''random set price'''
randomize_all_spot = LocatorInfo(locator="//*[@class='break-details']/div/button")
start_next_listing = LocatorInfo(locator="//*[contains(text(), 'Start next listing')]")
end_listing = LocatorInfo(locator="//*[contains(text(), 'End listing')]")

'''giveaway'''
giveaway_title = LocatorInfo('id', 'giveaway-form_title')
all_viewers = LocatorInfo(locator="//*[@id='giveaway-form']//fieldset[2]/div/label[1]")
followers_only = LocatorInfo(locator="//*[@id='giveaway-form']//fieldset[2]/div/label[2]")
launch_giveaway = LocatorInfo(locator="//*[@id='giveaway-form']//*[contains(text(), 'Launch')]")

'''random auction'''
begin_auction = LocatorInfo(locator="//*[@id='auction-details']/div/button")
auction_failed = LocatorInfo(locator="//*[@id='break-status']/p/text()[2]")
