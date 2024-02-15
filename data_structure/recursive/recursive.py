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
