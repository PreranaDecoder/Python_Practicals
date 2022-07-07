import cmath

# declare values
print("Quadratic equation --> ax**2 + bx + c = 0")
a,b,c = map(int,input("Enter the values of a, b, c : ").split())

# calculating the discriminant here
d = (b**2)-(4*a*c)

# finding two solutions of the quadratic equation
s1 = (-b - cmath.sqrt(d)) / (2*a)
s2 = (-b + cmath.sqrt(d)) / (2*a)

# printing the two solutions
print("The solutions are {0} and {1}".format(s1, s2))
