import SystemOfEquationsSolver as ses


def my_method(gmat : ses.GaussMatrix):
    gmat.row_multiplication(0, ses.Frac(4))
    print(gmat)
    gmat.row_multiplication(1, ses.Frac(5))
    print(gmat)
    gmat.row_addition(0, 1, ses.Frac(-1))
    print(gmat)
    gmat.row_multiplication(1, ses.Frac(3))
    print(gmat)
    gmat.row_multiplication(2, ses.Frac(5))
    print(gmat)
    gmat.row_multiplication(1, ses.Frac(7))
    print(gmat)
    gmat.row_multiplication(2, ses.Frac(9))
    print(gmat)
    gmat.row_addition(2, 1, ses.Frac(-4))
    print(gmat)
    gmat.row_multiplication(1, ses.Frac(-1))
    print(gmat)
    gmat.row_addition(1, 2, ses.Frac(-9))
    print(gmat)

mat = ses.GaussMatrix([[1, 2, -1, -1],
                       [-1, 1, -2, -5],
                       [2, 3, -1, 0]])
print(mat)

mat.solve()
# my_method(mat)