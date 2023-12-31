import sortviz
import random
  
def bogo_sort(array):
    n = len(array)
    while not sorted(array) == array:
        random.shuffle(array)
        root.update(array)

root = sortviz.MainWindow()
root.start(bogo_sort, [9, 8, 7, 6, 5, 4, 3, 2, 1])
root.mainloop()
