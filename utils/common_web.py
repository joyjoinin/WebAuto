from datetime import datetime
import os


def get_date():
    current_date = datetime.now().date()
    formatted_date = '00' + current_date.strftime("%Y%m%d")
    return formatted_date


def get_time():
    current_time = datetime.now().time()
    formatted_time = current_time.strftime("%I%M%p")
    return formatted_time


def get_image_path():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    new_path = script_dir.replace('utils', 'img.png')
    return new_path


def get_title(text):
    title = text + get_date() + get_time()
    return title


def save_data(show_name):
    with open('../../data/created_show.py', 'w') as output_file:
        output_file.write(f"show_name = '{show_name}' \n")
    output_file.close()


# def get_args_list():
#     import sys
#     if len(sys.argv) != 6:
#         return [1, 1, 1, 1, 1]
#     else:
#         run_round = int(sys.argv[1])
#         pick_set_listing_round = int(sys.argv[2])
#         pick_auction_listings_round = int(sys.argv[3])
#         random_set_listings_round = int(sys.argv[4])
#         random_auction_listings_round = int(sys.argv[5])
#         return [run_round, pick_set_listing_round, pick_auction_listings_round, random_set_listings_round, random_auction_listings_round]

