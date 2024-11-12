
def insertion_sort(elements):
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        # Shift elements of the sorted segment to the right to make room for the key
        while j >= 0 and elements[j] > key:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key  # Place the key in its correct position

if __name__ == '__main__':
    elements = [1, 8, 2, 7, 3, 9, 0]
    insertion_sort(elements)
    print(elements)
