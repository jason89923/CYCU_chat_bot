date_range = set(['1', '2', '3', '4', '5'])
time_range = set(['1', '2', '3', '4', '5', '6', '7', '8', 'C', 'D', 'E', 'F'])
separator = set([' ', '\n', '\t', ','])

def get_token(input_msg: str):
    input_msg = input_msg.upper()
    date = ''
    time = ''
    while len(input_msg) > 0:
        first = input_msg[0]
        input_msg = input_msg[1:]
        if first in date_range:
            date = first
            break
            
    if date == '':
        return None, None
    
    while len(input_msg) > 0:
        first = input_msg[0]
        input_msg = input_msg[1:]
        if first == '-':
            break
        
    if len(input_msg) == 0:
        return None, None
    
    while len(input_msg) > 0:
        first = input_msg[0]
        input_msg = input_msg[1:]
        if first in time_range:
            time += first
        elif first in separator and time != '':
            break
        
    if time == '':
        return None, None
    
    time = set(time)
    time = ''.join(sorted(time))
    return f'{date}-{time}', input_msg

def get_time_conditions(input_msg: str):
    conditions = []
    while len(input_msg) > 0:
        token, input_msg = get_token(input_msg)
        if token is None:
            break
        conditions.append(token)
    return conditions