class Show:
    def __init__(self, title=None, cover_image=None, date=None, time=None,
                 channel='joy test auction channel', description=None, creator='joy@57blocks.com', breaker=None):
        self.title = title
        self.cover_image = cover_image
        self.date = date
        self.time = time
        self.channel = channel
        self.description = description
        self.creator = creator
        self.breaker = breaker


class Listing:

    def __init__(self, title=None, option='books', assign_type=None, sell_type=None, assign_price=None,
                 min_bid=None, price_per_spot=None):
        self.title = title
        self.option = option
        self.assign_type = assign_type
        self.sell_type = sell_type
        self.assign_price = assign_price
        self.min_bid = min_bid
        self.price_per_spot = price_per_spot


login_url = "https://zerocool:XQZlx6iprxItlugXiiYcTp@dev.fanatics.live"
account = 'joy@57blocks.com'
password = 'joy159753ty,.'
manage_url = 'https://dev.fanatics.live/shops/fanatics-live/manage'
fake_device = 'fake_device_0'
fake_audio = 'Fake Default Audio Input'
