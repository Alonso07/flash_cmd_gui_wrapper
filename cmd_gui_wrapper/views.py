
import tkinter as tk
from .controller import Controller


class Views(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        content = tk.Frame(parent)
        #frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=400, height=400)
        frame = tk.Frame(content, borderwidth=5, width=400, height=400)
        
        titlelbl = tk.Label(content, text="Title")
        titlelbl.grid(column=0, row=0, columnspan=5)

        self.imgobj = tk.PhotoImage(file='./assets/DSA_64x40.png')
        imageLabel = tk.Label(content, image = self.imgobj)
        imageLabel.grid(column=4, row=0, columnspan=1)

        subtitlelbl = tk.Label(content, text="Subtitle")
        subtitlelbl.grid(column=0, row=1, columnspan=6)

        content.grid(column=0, row=0)
        frame.grid(column=0, row=0, columnspan=5, rowspan=12)

        action = tk.StringVar()

        act1 = tk.Radiobutton(content, text='act1', variable=action, value="act1")
        act2 = tk.Radiobutton(content, text='act2', variable=action, value="act2")
        act3 = tk.Radiobutton(content, text='act3', variable=action, value="act3")
        act4 = tk.Radiobutton(content, text='act4', variable=action, value="act4")
        act5 = tk.Radiobutton(content, text='act5', variable=action, value="act5")
        
        act1.grid(column=0, row=2)
        act2.grid(column=1, row=2) 
        act3.grid(column=2, row=2)
        act4.grid(column=3, row=2) 
        act5.grid(column=4, row=2)

        """
        name = ttk.Entry(content)

        onevar = BooleanVar(value=True)
        twovar = BooleanVar(value=False)
        threevar = BooleanVar(value=True)

        one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
        two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
        three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
        ok = ttk.Button(content, text="Okay")
        cancel = ttk.Button(content, text="Cancel")

        
        name.grid(column=3, row=1, columnspan=2)
        one.grid(column=0, row=3)
        two.grid(column=1, row=3)
        three.grid(column=2, row=3)
        ok.grid(column=3, row=3)
        cancel.grid(column=4, row=3)
        """

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def save_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.save(self.email_var.get())

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''
        
        
        
if __name__ == '__main__':
    window = tk.Tk()
    views = Views(window)

    window.mainloop()    
          