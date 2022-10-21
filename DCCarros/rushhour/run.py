from board import Board
from solver import Solver
from solver2 import Solver2
import sys

solver = None
board = None
if sys.argv[1] == "astar" and len(sys.argv) == 5:
    heuristic = sys.argv[3]
    # Revisamos que la heuristica sea valida
    if heuristic not in ["blockingcars", "zero"]:
        print("Invalid heuristic")
        exit(1)
    weight = sys.argv[4]
    # Revisamos que el peso sea valido
    if not weight.replace('.', '', 1).isdigit():
        print("Invalid weight")
        exit(1)
    # Cargamos el tablero
    board = Board.readFromfile(sys.argv[2])
    print("Board inicial:")
    print(board.prettify(board.cars))
    # Inicializamos el solver
    solver = Solver(board, heuristic, float(weight))
    # Resolvemos el tablero
    final_node = solver.search()
    # Revisamos si se encontro una solucion
    if final_node is None:
        print("No solution")
    else:
        moves = final_node.trace()

elif sys.argv[1] == "solver2" and len(sys.argv) == 4:
    # Cargamos el tablero inicial
    board = Board.readFromfile(sys.argv[2])
    print("Board inicial:")
    print(board.prettify(board.cars))
    # Cargamos el tablero final
    final_board = Board.readFromfile(sys.argv[3])
    print("Board final:")
    print(final_board.prettify(final_board.cars))
    # Inicializamos el solver
    solver = Solver2(board, final_board)
    # Resolvemos el tablero
    moves = solver.search()
    # Revisamos si se encontro una solucion
    if moves is None:
        print("No solution")
else:
    print("Uso para A* : python rushhour/run.py astar <board> <heuristic> <weight>")
    print("Uso para solver2 : python rushhour/run.py solver2 <board> <final_board>")
    exit(1)

# Imprimimos los movimientos
print(solver.solution(board, moves))
print('Time: {} seconds'.format(solver.end_time - solver.start_time))
print('Expansions: {}'.format(solver.expansions))