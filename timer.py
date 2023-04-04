import time

def countdowntimer(seconds):
    while seconds>0:
        mins= int(seconds/60)
        sec= int(seconds%60)

        timer=f'{mins}:{sec}'

        print(timer,end='\r')
        time.sleep(1)
        seconds -= 1

    print("time up") 

seconds=input("enter time on seconds: ")
countdowntimer(int(seconds))