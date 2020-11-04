from Backtracking import Backtracking
from CSPBacktracking import CSPBacktracking

# back = Backtracking()
#
# solutions = back.back()
#
# keepGoing = True
#
# while keepGoing:
#     print("The obtained solutions are: ")
#     for i in range(len(solutions)):
#         print(str(i + 1) + " - " + str(solutions[i]))
#
#     opt = input("Choose solution to display (0 - exit): ")
#     if opt == "0":
#         keepGoing = False
#         print("Goodbye!")
#     else:
#         try:
#             optInt = int(opt)
#             back.plot_graph(solutions[optInt - 1])
#         except Exception as e:
#             print("Invalid input")

csp = CSPBacktracking()
solutions = csp.back(5)

for s in solutions:
    print(s.get_timestamp())
    s.plot_countries()
