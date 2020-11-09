numero = float(input())

t_celsius = (numero-32) * 5/9
t_kelvin = t_celsius + 273.15

print("Convertendo", numero, "graus Fahrenheit temos:")
print(t_celsius, "graus Celsius e", t_kelvin, "Kelvin")