
import datetime

month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

current_datetime = datetime.datetime.now()

curr_year = current_datetime.year
curr_month = month_list[current_datetime.month - 1]
curr_day = current_datetime.day

print(f'{curr_day} - {curr_month} - {curr_year}')