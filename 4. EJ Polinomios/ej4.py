class Polinomio:
    def __init__(self, terminos=None):
        # terminos es un diccionario donde la clave es el exponente y el valor es el coeficiente
        if terminos is None:
            self.terminos = {}
        else:
            self.terminos = terminos

    def __str__(self):
        if not self.terminos:
            return "0"
        resultado = []
        for exp in sorted(self.terminos.keys(), reverse=True):
            coef = self.terminos[exp]
            if coef != 0:
                if exp == 0:
                    resultado.append(f"{coef}")
                else:
                    resultado.append(f"{coef}x^{exp}")
        return " + ".join(resultado)

    def restar(self, otro):
        resultado = Polinomio()
        for exp in self.terminos:
            resultado.terminos[exp] = self.terminos[exp]
        for exp in otro.terminos:
            if exp in resultado.terminos:
                resultado.terminos[exp] -= otro.terminos[exp]
            else:
                resultado.terminos[exp] = -otro.terminos[exp]
        # Eliminar términos con coeficiente 0
        for exp in list(resultado.terminos.keys()):
            if resultado.terminos[exp] == 0:
                del resultado.terminos[exp]
        return resultado

    def dividir(self, otro):
        if not otro.terminos:
            raise ValueError("No se puede dividir entre un polinomio vacío.")
        resultado = Polinomio()
        dividendo = Polinomio(self.terminos.copy())
        while dividendo.terminos and max(dividendo.terminos) >= max(otro.terminos):
            exp_dividendo = max(dividendo.terminos)
            exp_divisor = max(otro.terminos)
            coef_dividendo = dividendo.terminos[exp_dividendo]
            coef_divisor = otro.terminos[exp_divisor]
            nuevo_exp = exp_dividendo - exp_divisor
            nuevo_coef = coef_dividendo // coef_divisor
            resultado.terminos[nuevo_exp] = nuevo_coef
            # Restar el término correspondiente
            for exp in otro.terminos:
                exp_actual = exp + nuevo_exp
                coef_actual = otro.terminos[exp] * nuevo_coef
                if exp_actual in dividendo.terminos:
                    dividendo.terminos[exp_actual] -= coef_actual
                else:
                    dividendo.terminos[exp_actual] = -coef_actual
            # Eliminar términos con coeficiente 0
            for exp in list(dividendo.terminos.keys()):
                if dividendo.terminos[exp] == 0:
                    del dividendo.terminos[exp]
        return resultado

    def eliminar_termino(self, exponente):
        if exponente in self.terminos:
            del self.terminos[exponente]

    def existe_termino(self, exponente):
        return exponente in self.terminos