import random
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

def bubble_sort(collection):
    ask = raw_input("Choose an option. -> = Increasing, <- = Decreasing")
    if ask == "->":

        length = len(collection)
        for i in range(length):
            swapped = False
            for j in range(length - 1):
                if collection[j].salary > collection[j + 1].salary:
                    swapped = True
                    collection[j], collection[j + 1] = collection[j + 1], collection[j]
            if not swapped: break
        for person in collection:
            print person.name, person.salary
        return collection
    if ask == "<-":
        length = len(collection)
        for i in range(length):
            swapped = False
            for j in range(length - 1):
                if collection[j].salary < collection[j + 1].salary:
                    swapped = True
                    collection[j], collection[j + 1] = collection[j + 1], collection[j]
            if not swapped: break
        for person in collection:
            print person.name,person.salary
        return collection

def quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
            quicksort(less)
            quicksort(pivot)
            quicksort(greater)
    for person in array:
        print person.salary


def main ():
    employees = []
    for i in range (0, 100):
        emp = Employee ("A"+str(i) ,random.randint (100, 300))
        employees.append(emp)
    bubble_sort(employees)
    #quicksort(employees)

main()
