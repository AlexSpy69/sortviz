import src.sortviz as sort

def selection_sort(array):
    size = len(array)
    for s in range(size):
        min_idx = s
        for i in range(s + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[s], array[min_idx]) = (array[min_idx], array[s])
        root.update(array)

    return array

root = sort.MainWindow()
root.start(selection_sort, [9, 8, 7, 6, 5, 4, 3, 2, 1])
root.mainloop()

