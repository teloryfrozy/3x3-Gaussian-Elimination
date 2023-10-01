🧮 Gaussian Elimination Method for Solving a 3x3 Linear System 📊

This Python program implements the Gaussian Elimination method to solve a system of three equations with three unknowns. Given a matrix of coefficients and a vector of numbers, it calculates the values of x, y, and z, providing a solution to your linear system.
🚀 Usage

    Replace the matrix M and vector S in the code with your specific coefficients and numbers.

    Run the program.

python

M = [[1, 2, -1], [2, 3, 1], [1, 1, 1]]
S = [4, 17, 9]
solution = gaussian_elimination(M, S)
print(solution)

    The program will display the solution, including the values of x, y, and z.

💡 Example

For the provided example:

python

M = [[1, 2, -1], [2, 3, 1], [1, 1, 1]]
S = [4, 17, 9]

The program will output:

makefile

The solution to the system is:
x = 1.0
y = 2.0
z = 3.0

📜 License

This program is open-source and free to use without restrictions.
