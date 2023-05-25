
import tkinter as tk
import os
import platform

def search_kb():
    kb = kb_entry.get()
    version = platform.version()
    cmd = f'wusa /query /quiet /norestart /k:{kb} /version:{version}'
    result = os.system(cmd)
    if result == 0:
        status_label.config(text=f'{kb} is installed.')
    else:
        status_label.config(text=f'{kb} is not installed.')
        download_kb()

def download_kb():
    url = 'https://www.microsoft.com/en-us/download/details.aspx?id=123456'
    os.system(f'start {url}')

root = tk.Tk()
root.title('KB Checker')
root.geometry('300x200')

version_label = tk.Label(root, text=f'Windows Version: {platform.version()}')
version_label.pack(pady=10)

kb_label = tk.Label(root, text='KB:')
kb_label.pack(pady=10)

kb_entry = tk.Entry(root)
kb_entry.pack(pady=10)

search_button = tk.Button(root, text='Search', command=search_kb)
search_button.pack(pady=10)

status_label = tk.Label(root, text='')
status_label.pack(pady=10)

root.mainloop()

