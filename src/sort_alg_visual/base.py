import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

import time, threading

class Grid(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.colors = "black", "white"

    def set_sequence(self, sequence: list):
        rows = max(sequence)
        columns = len(sequence)

        for i in range(rows):
            for j in range(columns):
                if sequence[j] <= i:
                    tk.Frame(bg=self.colors[1], width=50,
                             height=50).grid(row=rows-i, column=j, sticky="nwes")
                else:
                    tk.Frame(bg=self.colors[0], width=50,
                             height=50).grid(row=rows-i, column=j, sticky="nwes")

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Sorting Algorithm Visualizer")
        self.grid = Grid()
        self.grid.grid(sticky="nwes")
        
        self.iter_count = 0
        self.sleeptime = 0

    def start(self, alg, sequence: list):
        def proc():
            self.grid.set_sequence(sequence)
            time.sleep(1)
            alg(sequence)
        threading.Thread(target=proc).start()

    def update(self, sequence: list):
        self.iter_count += 1
        self.title(f"{self.iter_count} iterations")
        self.grid.set_sequence(sequence)
        time.sleep(self.sleeptime)
        
