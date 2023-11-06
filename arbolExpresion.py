import math

class Nodo:
    def __init__(self, valor) :
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def evaluar_arbol_expresion(nodo, valores):
    if isinstance(nodo.valor, int):
        return nodo.valor
    
    if nodo.valor == 'x':
        return valores['x']
    
    if nodo.valor == '+':
        return evaluar_arbol_expresion(nodo.izquierdo, valores) + evaluar_arbol_expresion(nodo.derecho, valores)
    
    if nodo.valor == '-':
        return evaluar_arbol_expresion(nodo.izquierdo, valores) - evaluar_arbol_expresion(nodo.derecho, valores)
    
    if nodo.valor == '*':
        return evaluar_arbol_expresion(nodo.izquierdo, valores) * evaluar_arbol_expresion(nodo.derecho, valores)
    
    if nodo.valor == '/':
        
        derecha = evaluar_arbol_expresion(nodo.derecho, valores)
        
        if derecha ! = 0:
         return evaluar_arbol_expresion(nodo.izquierdo, valores) / evaluar_arbol_expresion(nodo.derecho, valores)
        
        else:
            ValueError("Division por cero")

arbol_expresion = Nodo('+')
arbol_expresion.izquierdo=Nodo('-')
arbol_expresion.izquierdo.izquierdo = Nodo('2')
arbol_expresion.izquierdo.derecho = Nodo('x')
arbol_expresion.izquierdo.izquierdo.izquierdo = Nodo('-1')
arbol_expresion.izquierdo.izquierdo.derecho = Nodo('3')
arbol_expresion.izquierdo.izquierdo.izquierdo.izquierdo = Nodo('1')
arbol_expresion.izquierdo.izquierdo.izquierdo.derecho = Nodo('x')
arbol_expresion.izquierdo.izquierdo.izquierdo.izquierdo.izquierdo = Nodo('-2')
arbol_expresion.izquierdo.izquierdo.izquierdo.izquierdo.derecho = Nodo('x')



while True:
    try:
        x = float(input("Ingresa un valor para x (o 'q' para salir):"))
        if x == 'q':
            break
        valores = {'x':x}
        resultado = evaluar_arbol_expresion(arbol_expresion, valores)
        print(f'El resultado de la expresion para x = {x} es:{resultado}')
    
    except ValueError as e:
        print(f"Error:"{e})
        break

    except KeyboardInterrupt:
        print("\nSaliendo del programa.")
        break







