import src.sortviz as sort

def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
        root.update(array)

    return array


root = sort.MainWindow()
root.start(insertion_sort, [9, 8, 7, 6, 5, 4, 3, 2, 1])
root.mainloop()
