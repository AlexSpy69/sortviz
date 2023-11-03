import sortviz

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        root.update(array) # update the window
        if already_sorted:
            break

    return array


root = sortviz.MainWindow()
root.start(bubble_sort, [9, 8, 7, 6, 5, 4, 3, 2, 1])
root.mainloop()
