import schedule
import time as t
import requests

def print_str(str, time=10):
    print("IT JUST FOR TEST!")
    print("about (5+your input time) seconds later your str will printed")
    t.sleep(5)
    schedule.every(time).seconds.do(lambda: print_job(str))
    while True:
        schedule.run_pending()
        t.sleep(1)

def url_request_by_time(url, time=10):
    
    print("YOUR INPUT URL IS:",url)
    print("YOUR INPUT TIME IS:",str(time))

    while True:
        user_answer = (input("IS IT OK? Y/N")).upper()
        if user_answer == "N":
            print("BYE")
            t.sleep(3)
            return 0
        elif user_answer == "Y":
            print("URL REQUEST WILL BE START")
            break
        else:
            print("PLEASE ENTER Y OR N: ")
    
    schedule.every(time).seconds.do(lambda: request_url(url))
    while True:
        schedule.run_pending()
        t.sleep(1)

def url_request_by_day_period(url, hour=0, min=0):
    print("YOUR INPUT URL IS:",url)
    if hour<10:
        hour_str = "0"+str(hour)
    else:
        hour_str = str(hour)
    if min<10:
        min_str = "0"+str(min)
    else:
        min_str = str(min)
    period = hour_str + ":" + min_str
    print("YOUR INPUT PERIOD IS:",str(period))

    while True:
        user_answer = (input("IS IT OK? Y/N : ")).upper()
        if user_answer == "N":
            print("BYE")
            t.sleep(3)
            return 0
        elif user_answer == "Y":
            print("URL REQUEST WILL BE START")
            break
        else:
            print("PLEASE ENTER Y OR N: ")
    
    schedule.every().day.at(period).do(lambda: request_url(url))
    while True:
        schedule.run_pending()
        t.sleep(1)

def print_job(str):
    now = t.localtime()
    now_pretty = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    print(now_pretty)
    print(str)
    
def request_url(url):
    now = t.localtime()
    now_pretty = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    response = requests.get(url)
    print("["+now_pretty+"]response status code: "+str(response.status_code))
