from utils.common_web import get_title, get_driver
from web.web_user_actions import WebActions
from datetime import datetime, timedelta


def create_random_auction():
    show_title = get_title('Auto_R_A')
    do = WebActions(get_driver())
    end_time = datetime.now() + timedelta(days=1)
    do.login_flow(show_title)
    do.run_forever(end_time, do.random_auction())
    do.after_test()
