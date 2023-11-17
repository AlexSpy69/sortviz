import tkinter as tk
import tkinter.ttk as ttk

import time, threading
import sortviz.util as util

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
                    tk.Frame(bg=self.colors[1], width=500/columns,
                             height=500/rows).grid(row=rows-i, column=j, sticky="nwes")
                else:
                    tk.Frame(bg=self.colors[0], width=500/columns,
                             height=500/rows).grid(row=rows-i, column=j, sticky="nwes")

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Sorting Algorithm Visualizer")
        self.geometry("500x500")
        self.grid = Grid()
        self.grid.grid(sticky="nwes")
        
        self.iter_count = 0
        self.sleeptime = 0

    def start(self, alg, sequence: list, single_iter=False):
        self.iter_count = 0
        if not single_iter:
            def proc():
                self.grid.set_sequence(sequence)
                time.sleep(1)
                alg(sequence)
        else:
            def proc():
                self.grid.set_sequence(sequence)
                time.sleep(1)
                while not util.is_sorted(sequence):
                    alg(sequence, len(sequence), self.iter_count)
                    self.update(sequence)
                
        threading.Thread(target=proc).start()

    def update(self, sequence: list):
        self.iter_count += 1
        self.title(f"{self.iter_count} iterations")
        self.grid.set_sequence(sequence)
        time.sleep(self.sleeptime)
        