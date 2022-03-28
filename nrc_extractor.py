import re
import json

regex_file = open('regex.json')
r_data = json.load(regex_file)

#[State Number]/[District]([NAING/N])[Registered No]

def get_nrc_data(string, state = True):
    nrc = re.findall(r_data['nrc'], string)
    # print(nrc)
    if state == True:
        state = ' '.join(nrc).split('/')[0]
        state = check_state(state)
        return ' '.join(nrc), state
    else:
        return ' '.join(nrc)

nrc_data = open("nrc_data.json")
state_data = json.load(nrc_data)

def check_state(num, lang = 'en'):
    state_name = state_data['state'].keys()
    # print(state_name)
    if num in state_name:
        # print(num)
        # print(nrc_data['state'])
        state_name = state_data['state'][num]
        # isvalid =  True
        return state_name
    else:
        # isvalid = False
        return "invalid state"
