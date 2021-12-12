# python 3.10
# UTF-8
import argparse


from commandes import api_end_point, get_clean_command, get_date, get_news, get_time, help, show_info, site_search

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    print(args)