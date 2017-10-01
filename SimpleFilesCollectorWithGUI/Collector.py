import os
from tkinter import *

import shutil
type_of_file = 'start'

root = Tk()

root.geometry('310x310')
root.title = ('smth')
#canvas = Canvas(root, width=310, height=310, bg='#002')
label_cp = Label(root, text='Enter path for collecting: ')
label_cp.place(x=0, y=10)
label_tof = Label(root, text='Enter type of file: ')
label_tof.place(x=0, y=30)
label_sf = Label(root, text='Enter saving folder: ')
label_sf.place(x=0, y=50)

entry_cp = Entry(root)
entry_cp.place(x=150, y=10)
entry_tof = Entry(root)
entry_tof.place(x=150, y=30)
entry_sf = Entry(root)
entry_sf.place(x=150, y=50)

btn_collect = Button(root, text='Collect')
btn_collect.bind('<Button-1>', lambda event: collect(entry_cp.get(), entry_tof.get(), entry_sf.get()))
btn_collect.place(x=150, y=70)

root.mainloop()

def collect(collecting_path, type_of_file, saving_folder):
    if not os.path.isdir(saving_folder):
        os.makedirs(saving_folder)
    list_of_types = [type_of_file]

    for path, package, files in os.walk(top=collecting_path):
        for file in files:
            index = file.rindex('.')
            name = file[index+1:]
            if name in list_of_types:
                shutil.copy(path + '\\' + file, saving_folder)




#collecting_path = input('Enter path for collecting: ')
# list_of_types = []
# while type_of_file != 'stop':
#     type_of_file = input('Enter type of file or \'stop\': ')
#     list_of_types.append(type_of_file)

# def collect(collecting_path, type_of_file, saving_folder):
#     if not os.path.isdir(saving_folder):
#         os.makedirs(saving_folder)
#     list_of_types = [type_of_file]
#
#     for path, package, files in os.walk(top=collecting_path):
#         for file in files:
#             index = file.rindex('.')
#             name = file[index+1:]
#             if name in list_of_types:
#                 shutil.copy(path + '\\' + file, saving_folder)

