from datetime import datetime

def get_current_time_stamp()->str:
    return f"{datetime.now().strftime('%Y-%m-%d--%H-%M-%S')}"

current_time_stamp=get_current_time_stamp()
#print(current_time_stamp)