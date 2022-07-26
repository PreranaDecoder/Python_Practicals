class Complex():
    def initComplex(self):
        self.realPart = int(input("Enter the Real Part: "))
        self.imgPart = int(input("Enter the Imaginary Part: "))

    def display(self):
        print(self.realPart, "+", self.imgPart, "i", sep="")

    def sum(self, c1, c2):
        self.realPart = c1.realPart + c2.realPart
        self.imgPart = c1.imgPart + c2.imgPart

    def mul(self, c1, c2):
        self.realPart = c1.realPart * c2.realPart
        self.imgPart = c1.imgPart * c2.imgPart

    def sub(self, c1, c2):
        self.realPart = c1.realPart - c2.realPart
        self.imgPart = c1.imgPart - c2.imgPart

    def mul(self, c1, c2):
        self.realPart = c1.realPart * c2.realPart
        self.imgPart = c1.imgPart * c2.imgPart

    def ge(self, c1, c2):
        self.realPart = (c1.realPart**2) + (c2.realPart**2)
        self.imgPart = (c1.imgPart**2) + (c2.imgPart**2)
        print(self.realPart>=self.imgPart)
        print(self.realPart == self.imgPart)

c1 = Complex()
c2 = Complex()
c3 = Complex()
c4 = Complex()
c5 = Complex()
c6 = Complex()
print("Enter first complex number : ")
c1.initComplex()
print("First Complex Number : ", end="")
c1.display()
print("Enter second complex number : ")
c2.initComplex()
print("Second Complex Number : ", end="")
c2.display()
print("Sum of two complex numbers is : ", end="")

c3.sum(c1, c2)
c3.display()

c4.sub(c1, c2)
c4.display()

c5.mul(c1, c2)
c5.display()

c6.ge(c1, c2)
c6.display()
