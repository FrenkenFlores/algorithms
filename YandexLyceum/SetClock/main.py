import datetime
import sys
import schedule


start_day = datetime.datetime.today().day
last_hour = datetime.datetime.today().hour

phrase = sys.argv[1]
range = list(map(int, sys.argv[2].split('-')))


def job():
    global last_hour
    hour_now = datetime.datetime.today().hour
    if last_hour != hour_now and (hour_now < range[0] or hour_now > range[1]):
        print(phrase)
        last_hour = hour_now


def main():
    schedule.every(1).seconds.do(job)
    while datetime.datetime.today().day == start_day:
        schedule.run_pending()


if __name__ == "__main__":
    main()
