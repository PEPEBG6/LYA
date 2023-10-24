NMAX = 8
MAX_CANDIDATES = NMAX

TRUE = 1
FALSE = 0
solution_count = 0

# Función que verifica si la solución parcial 'a' es una solución completa.
def is_a_solution(a, k, n):
    return k == n

def process_solution(a, k, input):
    result = [str(i) for i in range(1, k + 1) if a[i] == TRUE]
    print("{" + " ".join(result) + " }")

# Candidatos válidos para colocar en la posición 'k' del tablero.
def construct_candidates(a, k, n, c):
    in_perm = [False] * (NMAX + 1)
    candidates = 0

    # Marca las posiciones en el tablero que ya están ocupadas.
    for i in range(1, k):
        in_perm[a[i]] = True

    # Encuentra las posiciones no ocupadas y las agrega a la lista de candidatos.
    for i in range(1, n + 1):
        if not in_perm[i]:
            c[candidates] = i
            candidates += 1

    return candidates

# Backtracking 
def backtrack(a, k, input):
    c = [0] * MAX_CANDIDATES
    ncandidates = 0

    if is_a_solution(a, k, input):
        process_solution(a, k, input)
    else:
        k = k + 1
        ncandidates = construct_candidates(a, k, input, c)

        # Recursivamente prueba todas las combinaciones 
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

def nqueens(n):
    a = [0] * (NMAX + 1)
    global solution_count
    solution_count = 0
    backtrack(a, 0, n)
    print("n={} solution count={}".format(n, solution_count))

if __name__ == "__main__":
    n = 9
    nqueens(n)