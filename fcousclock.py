import time

def pomodoro_timer(total_time, break_time):
    start_time = time.time()
    end_time = start_time + total_time
    
    while time.time() < end_time:
        remaining_time = end_time - time.time()
        
        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)
        
        time_format = "{:02d}:{:02d}".format(minutes, seconds)
        
        print("Remaining time: ", time_format, end="\r")
        time.sleep(1)
    
    print("\nTime's up! Take a break.")
    
    time.sleep(break_time)
    print("Break time is over. Restarting the timer...\n")
    
# 设置专注时间为25分钟，休息时间为5分钟
pomodoro_timer(25 * 60, 5 * 60)
