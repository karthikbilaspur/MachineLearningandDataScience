# differentiation_formulas.py

import sympy as sp

def power_rule(x: sp.Symbol, n: int):
    """Differentiates x^n with respect to x"""
    return n * x ** (n - 1)

def logarithmic_rule(x: sp.Symbol):
    """Differentiates ln(x) with respect to x"""
    return 1 / x

def exponential_rule(x: sp.Symbol, a: float):
    """Differentiates a^x with respect to x"""
    return a ** x * sp.log(a)

def trigonometric_rules(func: str, x: sp.Symbol):
    """Differentiates trigonometric functions with respect to x"""
    if func == 'sin':
        return sp.cos(x)
    elif func == 'cos':
        return -sp.sin(x)
    elif func == 'tan':
        return sp.sec(x) ** 2
    elif func == 'sec':
        return sp.sec(x) * sp.tan(x)
    elif func == 'cosec':
        return -sp.cosec(x) * sp.cot(x)
    elif func == 'cot':
        return -sp.csc(x) ** 2

def inverse_trigonometric_rules(func: str, x: sp.Symbol):
    """Differentiates inverse trigonometric functions with respect to x"""
    if func == 'sin_inv':
        return 1 / sp.sqrt(1 - x ** 2)
    elif func == 'cos_inv':
        return -1 / sp.sqrt(1 - x ** 2)
    elif func == 'tan_inv':
        return 1 / (1 + x ** 2)
    elif func == 'sec_inv':
        return 1 / (sp.Abs(x) * sp.sqrt(x ** 2 - 1))
    elif func == 'cosec_inv':
        return -1 / (sp.Abs(x) * sp.sqrt(x ** 2 - 1))
    elif func == 'cot_inv':
        return -1 / (1 + x ** 2)

def main():
    x = sp.symbols('x')
    print("Differentiation Formulas:")
    print("-------------------------")
    print("Power Rule: d(x^n)/dx =", power_rule(x, 2))
    print("Logarithmic Rule: d(ln(x))/dx =", logarithmic_rule(x))
    print("Exponential Rule: d(a^x)/dx =", exponential_rule(x, 2))
    print("Trigonometric Rules:")
    print("d(sin(x))/dx =", trigonometric_rules('sin', x))
    print("d(cos(x))/dx =", trigonometric_rules('cos', x))
    print("Inverse Trigonometric Rules:")
    print("d(sin_inv(x))/dx =", inverse_trigonometric_rules('sin_inv', x))
    print("d(cos_inv(x))/dx =", inverse_trigonometric_rules('cos_inv', x))

if __name__ == "__main__":
    main()