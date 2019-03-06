from Solver import solver

def main():

    print("Masukkan State Awal : ")
    StartStates = []
    for i in range(0, 3): 
        StartStates.append(list(map(int, input().split())))
    
    Solver = solver(StartStates, [1, 2, 3, 4, 5, 6, 7, 8, 0])

    print("Pilihan Algoritma :")
    print("1. DFS")
    print("2. DLS")
    print("3. BFS")
    print("4. Dijkstra")
    print("5. A*") 
    option = int(input())

    if(Solver.isSolvable()):
        if(option == 1):
            hasil = Solver.DFS()
            if(hasil):
                print("Total Cost :", hasil.cost)
                Solver.traverse(hasil)
            else:
                print("Cannot Be Solved ! 2")
        elif(option == 2):
            print("Maksimum Kedalaman : ")
            MaxDepth = input()
            hasil = Solver.DLS(MaxDepth)
            if(hasil):
                print("Total Cost :", hasil.cost)
                Solver.traverse(hasil)
            else:
                print("Cannot Be Solved ! 2")
        elif(option == 3):
            hasil = Solver.BFS()
            if(hasil):
                print("Total Cost :", hasil.cost)
                Solver.traverse(hasil)
            else:
                print("Cannot Be Solved ! 2")
        elif(option == 4):
            hasil = Solver.Dijkstra()
            if(hasil):
                print("Total Cost :", hasil.cost)
                Solver.traverse(hasil)
            else:
                print("Cannot Be Solved ! 2")
        elif(option == 5):
            hasil = Solver.ast()
            if(hasil):
                print("Total Cost :", hasil.cost)
                Solver.traverse(hasil)
            else:
                print("Cannot Be Solved ! 2")
    else:
        print("Cannot Be Solved ! 1")

if __name__ == "__main__":
    main()