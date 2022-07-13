import sys
from time import sleep
from pick import pick
# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')


title = 'Please choose an action: '

options = [ 'Restart target in Normal mode', \
            'Restart target in Download mode', \
            'Restart target in Development mode', \
            'Active WD_OFF', \
            'Disable WD_OFF', \
            'Exit' ]

def restart_target_normal_mode():
    print("Restart target in Normal mode")
    sleep(3)

def restart_target_download_mode():
    print("Restart target in Download mode")
    sleep(3)

def restart_target_dev_mode():
    print("Restart target in Development mode")
    sleep(3)

def active_WD_OFF():
    print("Active WD_OFF")
    sleep(3)

def disable_WD_OFF():
    print("Disable WD_OFF")
    sleep(3)

def exit_pro():
    print("Goodbye!")
    sleep(3)
    sys.exit(0)

fun_dic = { 0: restart_target_normal_mode, \
            1: restart_target_download_mode, \
            2: restart_target_dev_mode, \
            3: active_WD_OFF, \
            4: disable_WD_OFF, \
            5: exit_pro }


while 1:
    option, index = pick(options, title, indicator='>>>', default_index=(len(options) // 2) - 1) 
    try:
        #eval(option)()
        fun_dic[index]()
    except ValueError as e:
        print(f"There is no function {option}. Error detail {e}")




