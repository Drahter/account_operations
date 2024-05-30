from funcs import *

data = get_data()
id_time = get_time(data)
five_latest_operations = get_five_latest(id_time)
check_operations(five_latest_operations, data)
