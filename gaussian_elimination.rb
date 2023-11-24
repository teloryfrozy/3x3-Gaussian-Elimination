require 'colorize'


def gaussian_elimination(m, s)
    # Returns the solution of a system with 3 unknowns. It utilizes the Gaussian elimination method.
    #
    # Arguments:
    #   - {Array} m : matrix with coefficients
    #   - {Array} s : matrix with numbers
    #

    # Rows of the matrix
    r_1 = m[0]
    r_2 = m[1]
    r_3 = m[2]

    # First step
    if r_1[0] == 0
        # swap rows if the pivot is 0
        r_1, r_2 = r_2, r_1
        s[0], s[1] = s[1], s[0]
    else
        p = r_1[0] # pivot
        s[1] = s[1]-r_2[0]/p*s[0]
        s[2] = s[2]-r_3[0]/p*s[0]
        
        # with_index (Ruby) <=> enumerate (Python)
        # value = r_2[i] (0...4).each do |i|
        r_2 = r_2.map.with_index {|value, i| value - (r_2[0] / p) * r_1[i]}
        r_3 = r_3.map.with_index {|value, i| value - (r_3[0] / p) * r_1[i]}
    end

    # second step
    if r_2[1] == 0
        # swaps the lines if the pivot is 0
        r_2, r_3 = r_3, r_2
        s[1], s[2] = s[2], s[1]
    else
        p = r_2[1] # pivot
        # change the solution matrix
        s[2] = s[2]-r_3[1]/p*s[1]
        r_3 = r_3.map.with_index {|value, i| value - (r_3[1] / p) * r_2[i]}
    end

    # solution step
    z = s[2]/r_3[2]
    y = (s[1]-r_2[2]*z)*1/r_2[1]
    x = (s[0]-r_1[1]*y-r_1[2]*z)*1/r_1[0]

    # --- solutions --- #
    solution = (
        "The solution of the system is:\n".colorize(:magenta) +
        "x = #{x}\n".colorize(:red) +
        "y = #{y}\n".colorize(:blue) +
        "z = #{z}".colorize(:yellow)
    )
    return solution
end 

m = [[1, 2, -1], [2, 3, 1], [1, 1, 1]]
s = [4, 17, 9]
puts gaussian_elimination(m, s)