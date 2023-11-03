# sortviz

A Tkinter GUI pacakge that visualizes sorting algorithms.


## Usage

This is an example of an implementation of the bubble sort algorithm.

```python
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
```

```python
import sortviz
```
Importing the package.

```python
def bubble_sort(array): [...]
```
The algorithm function - it takes an array
as a parameter and returns a sorted version of it.

```python
root = sortviz.MainWindow()
root.start(bubble_sort, [9, 8, 7, 6, 5, 4, 3, 2, 1])
root.mainloop()
```
root is an object of the class sortviz.MainWindow(), which is
a subclass of tkinter.Tk(). To start the event loop, you will need to run
mainloop at the end. The start method takes an algorithm function and an
unsorted array as parameters. Once you run it, the previously opened window
will visualize the sorting process. **It is important to call the update method
in the algorithm function after each iteration to update the window.**
