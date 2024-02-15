class Recursive:
    def fibonacy(self, number: int):
        if number == 1:
            return 1
        if number == 0:
            return 0
        return self.fibonacy(number - 1) + self.fibonacy(number - 2)

    def factorical(self, number: int):
        if number == 0:
            return 1
        if number == 1:
            return 1
        return number * self.factorical(number - 1)


if __name__ == "__main__":
    print("Fibonacy of 8 is: ", Recursive().fibonacy(8))
    print("Factorical of 10 is: ", Recursive().factorical(10))
    # Fibonacy of 8 is:  21
    # Factorical of 10 is:  3628800
