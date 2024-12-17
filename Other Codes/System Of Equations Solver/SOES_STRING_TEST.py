import SystemOfEquationsSolver as ses


while True:
    inp = input()
    if inp == "":
        break
    else:
        try:
            fr = ses.Frac(inp)
            print(f"The input was valid and the fraction {fr} was created.")
        except:
            print("The input was invalid.")