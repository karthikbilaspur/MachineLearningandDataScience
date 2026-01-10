# partial_derivatives.py

import sympy as sp

def partial_derivative(func, var):
    """Computes the partial derivative of a function with respect to a variable"""
    return sp.diff(func, var)

def main():
    x, y = sp.symbols('x y')
    
    # Define a function of two variables
    f = x**2 * y + 2*x*y**2
    
    print("Function: f(x, y) =", f)
    print("Partial Derivative with respect to x: ∂f/∂x =", partial_derivative(f, x))
    print("Partial Derivative with respect to y: ∂f/∂y =", partial_derivative(f, y))

    # Define another function of two variables
    g = sp.sin(x*y) + x**2 * y
    
    print("\nFunction: g(x, y) =", g)
    print("Partial Derivative with respect to x: ∂g/∂x =", partial_derivative(g, x))
    print("Partial Derivative with respect to y: ∂g/∂y =", partial_derivative(g, y))

    # Compute higher-order partial derivatives
    f_xx = partial_derivative(partial_derivative(f, x), x)
    f_xy = partial_derivative(partial_derivative(f, x), y)
    f_yx = partial_derivative(partial_derivative(f, y), x)
    f_yy = partial_derivative(partial_derivative(f, y), y)

    print("\nHigher-Order Partial Derivatives of f(x, y):")
    print("∂²f/∂x² =", f_xx)
    print("∂²f/∂x∂y =", f_xy)
    print("∂²f/∂y∂x =", f_yx)
    print("∂²f/∂y² =", f_yy)

if __name__ == "__main__":
    main()