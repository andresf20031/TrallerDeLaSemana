nombre = input("digite su nombre: ")
Edad = float(input("digite su edad: "))

if Edad > 5:
    print("1 suma/ 2 resta / 3 multiplicacion / 4 division")
    tipoOpe = float(input("que tipo de operacion desea realizar: "))
    num1 = float(input("digite el primer numero: "))
    num2 = float(input("digite el segundo numero / en caso de division digite el dividendo: "))
    if tipoOpe == 1:
        solucion = num1 + num2
        print(f"el resultado es: {solucion}")
    elif tipoOpe == 2:
        solucion = num1 - num2
        print(f"el resultado es: {solucion}")
    elif tipoOpe == 3:
        solucion = num1 * num2
        print(f"el resultado es: {solucion}")
    elif tipoOpe == 4:
        if num2 ==0:
            print(f"no se puede realizar la division ya que el dividendo no puede ser 0: ")
        else:
            solucion = num1 / num2
        print(f"el resultado es: {solucion}")

else:
    print("usted no puede usar el programa")
    
