# Python code to find the largest number in a list
def largest_in_list(a):
    maxno = a[0]
    for i in range(1, len(a)):
        if a[i] > maxno:
            maxno = a[i]
    print("Largest element is", maxno)

a1 = [10, 2, 5, 7, 8]
largest_in_list(a1)
