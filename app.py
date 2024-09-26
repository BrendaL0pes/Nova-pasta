import math

def calculate(lambda_, beta, x, y):
    cos = math.cos
    sin = math.sin
    beta_rad = math.radians(beta)  # Converte o ângulo beta de graus para radianos
    
    print("beta radianos = ", beta_rad)
    
    term1 = -2 * math.pi / lambda_
    eq_lambda = term1 * (cos(beta_rad) * x - sin(beta_rad) * y)
    
    print("cosBetaRad = ", cos(beta_rad))
    print("senBetaRad * y = ", sin(beta_rad) * y)
    print("equação lambda = ", eq_lambda)
    
    eq_geral = 2 + 2 * cos(eq_lambda)
    
    print("equação geral = ", eq_geral)
    
    return eq_geral
