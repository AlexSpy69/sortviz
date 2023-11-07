import sortviz

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        r = quicksort(left) + [pivot] + quicksort(right)
        root.update(r)
        return r

root = sortviz.MainWindow()
root.start(quicksort, [9, 8, 7, 6, 5, 4, 3, 2, 1])
root.mainloop()
