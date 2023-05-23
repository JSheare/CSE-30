# make a generator
def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


def solve_queens(n_queens):
    q_elements = [i+1 for i in range(n_queens)]
    q_solutions = []
    for r_solution in all_perms(q_elements):
        valid_solution = True
        for i in range(len(r_solution)):
            current_horizontal = i+1
            current_vertical = r_solution[i]
            # Previous queens have been verified already so there's no need to check them redundantly
            for j in range(i+1, len(r_solution)):
                horizontal = j+1
                vertical = r_solution[j]
                if abs(current_horizontal-horizontal) == abs(current_vertical-vertical):
                    valid_solution = False
                    break

            if not valid_solution:
                break

        if valid_solution:
            q_solutions.append(r_solution)

    return q_solutions


if __name__ == '__main__':
    n = int(input('Enter a number of queens: \n'))
    solutions = solve_queens(n)
    print(f'The {n}-queens puzzle has {len(solutions)} solutions:')
    for solution in solutions:
        print(solution)
