def gaussian_elimination(M: list, S: list):
    """Returns the solution of a system with 3 unknowns. It utilizes the Gaussian elimination method.

    Args:
        - {list} M : Matrix with coefficients
        - {list} S : Matrix with numbers
    """

    # Rows of the matrix
    R_1 = M[0]
    R_2 = M[1]
    R_3 = M[2]

    # First step
    if R_1[0] == 0:
        # swap rows if the pivot is 0
        R_1, R_2 = R_2, R_1
        S[0], S[1] = S[1], S[0]
    else:
        p = R_1[0] # pivot
        S[1] = S[1]-R_2[0]/p*S[0]
        S[2] = S[2]-R_3[0]/p*S[0]
        R_2 = [R_2[i] - (R_2[0] / p) * R_1[i] for i in range(3)]
        R_3 = [R_3[i] - (R_3[0] / p) * R_1[i] for i in range(3)]

    # second step
    if R_2[1] == 0:
        # swaps the lines if the pivot is 0
        R_2, R_3 = R_3, R_2
        S[1], S[2] = S[2], S[1]
    else:
        p = R_2[1] # pivot
        # change the solution matrix
        S[2] = S[2]-R_3[1]/p*S[1]
        R_3 = [R_3[i]-(R_3[1]/p)*R_2[i] for i in range(3)]

    # solution step
    z = S[2]/R_3[2]
    y = (S[1]-R_2[2]*z)*1/R_2[1]
    x = (S[0]-R_1[1]*y-R_1[2]*z)*1/R_1[0]

    # --- solutions --- #
    solution = (
        "\033[35mThe solution of the system is:\n" +
        f"\033[31mx = {x}\n" +
        f"\033[34my = {y}\n" +
        f"\033[33mz = {z}"
    )
    return solution

M = [[1, 2, -1], [2, 3, 1], [1, 1, 1]]
S = [4, 17, 9]
print(gaussian_elimination(M, S))