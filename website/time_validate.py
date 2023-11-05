import datetime
 
# Function to convert string to datetime
def convert(date_time):
    format = "%H:%M"
    datetime_str = datetime.datetime.strptime(date_time, format)
 
    return datetime_str
   
# Inputs:
# Start - "HH:MM"
# End - "HH:MM"
  # List - [ ("HH:MM", "HH:MM"), ... ]
def validator(time_1, time_2, list_of_tup_of_t):
    t_1 = convert(time_1)
    t_2 = convert(time_2)
#     buffer()
    for pairs in list_of_tup_of_t:
        if(t_1 <= convert(pairs[1]) and t_2 >= convert(pairs[0])):
            return 1
        elif(t_1 <= convert(pairs[0]) and t_2 >= convert(pairs[1])):
            return 1
    
    return 0
