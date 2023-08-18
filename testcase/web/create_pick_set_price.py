from utils.common_web import get_title, get_driver
from web.web_user_actions import WebActions
from datetime import datetime, timedelta


def create_pick_set_price():
    show_title = get_title('Auto_P_S')
    do = WebActions(get_driver())
    end_time = datetime.now() + timedelta(days=1)
    do.login_flow(show_title)
    do.run_forever(end_time, do.p_s_flow())
    do.after_test()
