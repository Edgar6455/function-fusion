import math

from function_package import *


if __name__ == '__main__':
    sin = Sin()
    cos = Cos()
    tg = sin / cos
    arg = math.pi / 4
    print(f"When x = pi / 4:\n\t{str(tg)} = {tg(arg)}\n")  # 1.0

    tg_derivative = tg.derivative()
    arg = math.pi / 4
    print(f"When x = pi / 4:\n\t{str(tg_derivative)} = {tg_derivative(arg)}\n")  # 2.0

    x_2 = Polynomial(0, 0, 1)  # 0*1 + 0*x + 1*x^2
    arg = 12
    print(f"When x = {arg}:\n\t{str(x_2)} = {x_2(arg)}\n")  # 144

    sin_2 = x_2.apply(sin)  # sin^2 (x)
    arg = 3 * math.pi / 2
    print(f"When x = 3 * pi / 2:\n\t{str(sin_2)} = {sin_2(arg)}\n")  # 1.0

    cos_x_2 = cos.apply(x_2)  # cos(x^2)
    arg = -math.sqrt(math.pi)
    print(f"When x = -sqrt(pi):\n\t{str(cos_x_2)} = {cos_x_2(arg)}\n")  # -1.0
