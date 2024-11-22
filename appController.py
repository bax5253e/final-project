import tkinter as tk

from appModel import AppModel
from mainView import MainView
from addTransactionsView import AddTransactionsView
from viewTransactionsView import ViewTransactionsView
from reportsView import ReportsView

class AppController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Personal Finance Tracker")
        self.root.geometry("800x600")
        
        self.model = AppModel()

        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        for ViewClass in [MainView, AddTransactionsView, ViewTransactionsView, ReportsView]:
            frame = ViewClass(self.container, self)
            self.frames[ViewClass.__name__] = frame

        self.show_frame("MainView")

    def show_frame(self, view_name):
        frame = self.frames[view_name]
        frame.tkraise()

    def quit(self):
        self.root.quit()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = AppController()
    app.run()



    