

import tkinter as tk
from cmd_gui_wrapper.views import Views
from cmd_gui_wrapper.model import Model
from cmd_gui_wrapper.controller import Controller

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        print(type(self))
        self.title('Tkinter MVC Demo')

        # create a model
        model = Model('hello@pythontutorial.net')

        # create a view and place it on the root window
        views = Views(self)

        views.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = Controller(model, views)

        # set the controller to view
        views.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()            