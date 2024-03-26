import csv
from tkinter import *


class GUI:
    def __init__(self, window):
        """
        - The code provided is meant to guide you on the dimensions used and variable names standards.
        - Add the widgets responsible for the name, status, and save button.
        """
        self.window = window

        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Name')
        self.entry_name = Entry(self.frame_name)
        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=5, side='left')
        self.frame_name.pack(anchor='w', pady=10)  # anchor='w' helps to change the frame position from center to west.

        self.frame_age = Frame(self.window)
        self.label_age = Label(self.frame_age, text='Age')
        self.entry_age = Entry(self.frame_age)
        self.label_age.pack(padx=5, side='left')
        self.entry_age.pack(padx=15, side='left')
        self.frame_age.pack(anchor='w', pady=15)  # anchor='w' helps to change the frame position from center to west.

        self.frame_status = Frame(self.window)
        self.status_name = IntVar()
        self.status_name.set(0)
        self.label_status = Label(self.frame_status, text='Status')
        self.label_status.pack(padx=4, side='left')
        self.status_student = Radiobutton(self.frame_status, text='Student', variable=self.status_name, value=1)
        self.status_staff = Radiobutton(self.frame_status, text='Staff', variable=self.status_name, value=2)
        self.status_both = Radiobutton(self.frame_status, text='Both', variable=self.status_name, value=3)
        self.status_student.pack(padx=3, side='left')
        self.status_staff.pack(padx=5, side='left')
        self.status_both.pack(padx=5, side='left')
        self.frame_status.pack(pady=3)
        self.status_student.deselect()

        self.button_save = Button(self.window, text='SAVE', command=self.clicked)
        self.button_save.pack(side='bottom', pady=15)

    def clicked(self):
        with open('records.csv', 'a', newline='') as csvfile:
            name = self.entry_name.get()
            age = int(self.entry_age.get())
            age *= 2
            status = self.status_name.get()

            content = csv.writer(csvfile, delimiter=',',
                                 escapechar=' ', quoting=csv.QUOTE_NONE)

            if status == 1:
                content.writerow([f'{name}'] + [f'{age}'] + ['Student'])

            elif status == 2:
                content.writerow([f'{name}'] + [f'{age}'] + ['Staff'])

            elif status == 3:
                content.writerow([f'{name}'] + [f'{age}'] + ['Both'])

            else:
                content.writerow([f'{name}'] + [f'{age}'])

        self.entry_name.delete(0, END)
        self.entry_age.delete(0, END)
        self.status_student.deselect()
        self.status_staff.deselect()
        self.status_both.deselect()

        """
        - This method should only be called when the save button is clicked.
        - Retrieve the name, age, and status values.
        - The age must be doubled (e.g. if someone entered 5 for age, their age would be stored as 10).
        - Determine the person status based off the value of the radio button selected.

        - Open the records.csv file and append the new person's details.
        - I suggest first viewing the csv file's contents to understand how your data should be sent to it.

        - Clear the name and age values that were entered in the GUI.
        - Make sure you clear the status value (i.e, No status value should be selected).
        """
