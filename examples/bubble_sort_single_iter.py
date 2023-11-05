import sortviz

def bubble_sort(array, n, i):
    for j in range(n - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

root = sortviz.MainWindow()
root.start(bubble_sort, [9, 8, 7, 6, 5, 4, 3, 2, 1], True)
root.mainloop()
