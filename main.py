from Solutions.CSPBacktracking import  CSPBacktracking
from Solutions.CSPReduceNeighbourDomains import CSPReduceNeighbourDomains
from Solutions.CSPOrderByNeighbours import CSPOrderByNeighbours
from Solutions.CSPWithLimit import CSPWithLimit
from Utils.Utils import plot_graph

from Statistics.Statistics import plot_graph_comparisons, plot_time_comparisons

print("Hello!")
option = input("'1'-Plot search graph comparisons\n'2'-Plot time comparisons for one solution\n"
               "'3'-Plot time comparisons for 10 solutions\n'4'-Compute now\nOption: ")
optiont = option.strip()
if optiont == "1":
    plot_graph_comparisons()
elif optiont == "2":
    plot_time_comparisons(0)
elif optiont == "3":
    plot_time_comparisons(1)
elif optiont == "4":
    f = input("Choose graph:\n\t'1'-10 nodes\n\t'2'-4 nodes\n\t'3'-6 nodes\n\t'4'-100 nodes\nOption: ")
    ft = f.strip()
    file = ""
    if ft == "1":
        file = "Input/graph.txt"
    elif ft == "2":
        file = "Input/graph2.txt"
    elif ft == "3":
        file = "Input/graph3.txt"
    elif ft == "4":
        file = "Input/graph4.txt"

    if file == "":
        print("Invalid input")
    else:
        sol = input("Choose option:\n\t'1'-CSP Backtracking\n\t"
                    "'2'-CSP with reduced domains\n\t'3'-CSP with ordered nodes\n\t'4'-CSP with limit b'\nOption: ")
        solt = sol.strip()
        back = None
        if solt == "1":
            back = CSPBacktracking(file)
        elif solt == "2":
            back = CSPReduceNeighbourDomains(file)
        elif solt == "3":
            back = CSPOrderByNeighbours(file)
        elif solt == "4":
            back = CSPWithLimit(file)

        if back is None:
            print("Invalid input")
        else:
            try:
                max_sols = int(input("Give the desired number of solutions: "))
                solutions, graph = back.back(max_sols)

                alive = True
                while alive:
                    opt = input("'1'-Display search graph\n'2'-Search graph stats\n'3'-Plot a solution\n'0'-Exit\nOption: ")
                    optt = opt.strip()
                    if optt == "0":
                        alive = False
                    elif optt == "1":
                        try:
                            plot_graph(graph)
                        except Exception as e:
                            print(e)
                            print("Error plotting graph")
                    elif optt == "2":
                        print(str(graph.number_of_nodes()) + " States")
                    elif optt == "3":
                        sols = "Choose solution:\n"
                        for i in range(len(solutions)):
                            sols = sols + str(i) + '\n'
                        sols += "Solution number: "
                        try:
                            i = int(input(sols))
                            solutions[i].plot_countries()
                        except Exception as e:
                            print(e)
                            print("Invalid input")
            except Exception as e:
                print(e)
                print("Invalid input")

print("Goodbye!")
