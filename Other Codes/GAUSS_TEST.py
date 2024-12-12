import SystemOfEquationsSolver as ses


mat = ses.GaussMatrix([[-1, 2, -3],
                       [4, -5, 6]])
print(mat)

mat.solve()
# my_method(mat)