def gaussian_elimination(M: list, S: list):
    """Gibt die Lösung von ein system mit 3 unbekannt. Es nutzt die Gaußsche Eliminierungsmethode
    
    Args:
        - {list} M : Matrix mit Koeffizienten
        - {list} S : Matrix mit Nummer
    """
    # Zeilen der Matrix
    R_1 = M[0]
    R_2 = M[1]
    R_3 = M[2]

    # Erster Schritt
    if R_1[0] == 0:
        # tauscht die Zeilen aus, wenn der pivot 0 ist
        R_1, R_2 = R_2, R_1
        S[0], S[1] = S[1], S[0]
    else:
        p = R_1[0] # pivot
        S[1] = S[1]-R_2[0]/p*S[0]
        S[2] = S[2]-R_3[0]/p*S[0]
        R_2 = [R_2[i]-(R_2[0]/p)*R_1[i] for i in range(3)]
        R_3 = [R_3[i]-(R_3[0]/p)*R_1[i] for i in range(3)]

    # Zweite Schritt
    if R_2[1] == 0:
        # tauscht die Zeilen aus, wenn der pivot 0 ist
        R_2, R_3 = R_3, R_2
        S[1], S[2] = S[2], S[1]
    else:
        p = R_2[1] # pivot
        # ändern die Lösungsmatrix
        S[2] = S[2]-R_3[1]/p*S[1]
        R_3 = [R_3[i]-(R_3[1]/p)*R_2[i] for i in range(3)]

    # Lösungsschritt
    z = S[2]/R_3[2]
    y = (S[1]-R_2[2]*z)*1/R_2[1]
    x = (S[0]-R_1[1]*y-R_1[2]*z)*1/R_1[0]

    # --- Lösungen --- #
    return f"\033[38;5;9mDie Lösung vom System ist:\n\033[38;5;1mx = {x}\n\033[38;5;2my = {y}\n\033[38;5;12mz = {z}"

M = [[1, 2, -1], [2, 3, 1], [1, 1, 1]]
S = [4, 17, 9]
print(gaussian_elimination(M, S))