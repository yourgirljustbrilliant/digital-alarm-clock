from playsound import playsound 
import time 

CLEAR = "\033[2J"
CLEAR_AND_RETURN ="\033[H"

def alarm(seconds):
    time_elapsed = 0 
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1) #means wait for 1 secound then continue
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        secounds_left = time_left % 60 

        print(f"{CLEAR_AND_RETURN}ALARM WILL SOUND IN:{minutes_left:02d}:{secounds_left:02d}")


minutes = int(input("How many minutes to wait: "))
seconds = int(input("how many seconds to wait: "))
total_seconds = minutes * 60 * seconds
playsound("sound.wav")
alarm(total_seconds)
