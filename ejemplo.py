
# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

import math

try:
    a = float(input("Escribe el valor de a: "))
    b = float(input("Escribe el valor de b: "))
    c = float(input("Escribe el valor de c: "))
    if a == 0:
        print("No se puede calcular, denominador es cero")
    else:
        radicando = b*b-4*a*c
        if radicando < 0:
            print("No se puede calcular, el radicando es negativo")
        else:
            x1 = (-b+math.sqrt(radicando))/(2*a)
            x2 = (-b-math.sqrt(radicando))/(2*a)
            txt_salida = "Las soluciones a la ecuación "\
                "{0}X^2 + {1}X + {2} = 0 son: {3} y {4}"\
                .format(a, b, c, x1, x2)
            print(txt_salida)
except ValueError as val_error:
    print("Error: has introducido un valor no numérico")
    # print(val_error)
