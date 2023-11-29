import numpy as np
import scipy.special as sc

class Henze:
    def __C0(self, Y, a, n):
        sum = 0
        for k in range(n):
            for j in range(n):
                sum += 1. / (Y[j] + Y[k] + a)
        return 1. / n * sum

    def __C1(self, Y, a, n):
        sum = 0
        for j in range(n):
            sum += np.exp(Y[j] + a) * sc.exp1(Y[j] + a)
        return sum

    def __C2(self, Y, a, n):
        result = n * (1.0 - a * np.exp(a) * sc.exp1(a))
        return result


    def MainHenze(self, Y, a, n):
        HE = self.__C0(Y, a, n) - self.__C1(Y, a, n) + self.__C2(Y, a, n)
        return HE