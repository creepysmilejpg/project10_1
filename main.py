from gui import *


def main():
    """
    - Change the window title to 'Lab 10'.
    - Set its length to 250 and height to 180.
    - Make the window non-resizable.
    """
    window = Tk()
    widgets = GUI(window)
    window.title(string='Lab 10')
    window.geometry('250x180')
    window.resizable(False, False)
    window.mainloop()


if __name__ == '__main__':
    main()
