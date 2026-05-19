def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperatura_c = 25.0
resultado =  celsius_para_fahrenheit(temperatura_c)
print(f"{temperatura_c} graus Celsius equivalem {resultado} graus Fahrenheit.")