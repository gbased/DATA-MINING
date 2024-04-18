import numpy as np
import math
from scipy.optimize import curve_fit


class Reader:
    def __init__(self):
        self.x = []
        self.y = []
        self.err = []
        self.filename = None

    def read_file(self, filename: str):
        self.filename = filename
        with open(self.filename, 'r') as file:
            for line in file.readlines():
                tmp_values = list(map(float, line.split()))
                self.x.append(tmp_values[0])
                self.y.append(tmp_values[1])
                self.err.append(tmp_values[2])


class Distribution:
    def __init__(self):
        pass

    @staticmethod
    def weibull(x, a, b):
        if 0 < x < 1 and a > 0 and b > 0:
            return a*b*x**(b-1)*math.exp(-a*x**b)
        return None

    @staticmethod
    def gamma(x, a, b):
        if x > 0 and a > -1 and b > 0:
            return (x**a*math.exp(-x/b))/b**(a+1)*math.gamma(a+1)

    @staticmethod
    def x_square(x, n):
        if x > 0 and n > 0:
            return (1/2**(n/2)*math.gamma(n/2))*x**(n/2-1)*math.exp(-x/2)

def nonlinear_least_squares_analysis(x: (float, int), y: (float, int), initial_guesses = [(1, 1, 1), (1, 1, 1), (1, 1, 1)]) -> list:
    functions = [Distribution.weibull, Distribution.gamma, Distribution.x_square]

    best_params_list = []
    for func, initial_guess in zip(functions, initial_guesses):
        best_params, _ = curve_fit(func, x, y, initial_guess)
        best_params_list.append(best_params)

    return best_params_list
def main():
    reader = Reader
    #reader.read_file(filename='.venv\data7.txt')
    best_parameters = nonlinear_least_squares_analysis([1, 2, 3, 4, 5], [2.5, 3.5, 4.5, 5.5, 6.5])
    print(best_parameters)


if __name__ == '__main__':
    main()