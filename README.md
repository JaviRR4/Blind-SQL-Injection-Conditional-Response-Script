# Blind-SQL-Injection-Conditional-Response-Script
Ejercicio academia s4vitar para portswigger lab

## conditional_blind_sqli.py

Este script automatiza un ataque de inyección SQL por fuerza bruta (blind SQL injection) para extraer la contraseña del usuario administrator en un sitio web vulnerable.

Descripción
sqli2.py realiza una enumeración carácter por carácter de la contraseña del administrador mediante inyección SQL en la cookie TrackingId. Utiliza la técnica de blind SQL injection para adivinar la contraseña de hasta 20 caracteres.

El script prueba letras minúsculas y dígitos, enviando solicitudes HTTP con un payload especialmente diseñado en la cookie para comprobar si un carácter específico coincide en una posición determinada. Cuando la respuesta del servidor contiene "Welcome back", el script deduce que el carácter probado es correcto y pasa al siguiente.

Características principales

Uso de la librería requests para hacer peticiones HTTP.

Manejo de señales para salir limpiamente con Ctrl+C.

Feedback visual con progreso en tiempo real usando pwn y termcolor.

Ataque específico para la extracción de contraseñas mediante inyección SQL ciega.

Aditional info




Uso
Ejecutar el script directamente:

python3 sqli2.py
El script iniciará el ataque y mostrará en pantalla el progreso y la contraseña encontrada en tiempo real.

![image](https://github.com/user-attachments/assets/9403e893-386e-4f66-9ad9-1df6a2d66025)


![image](https://github.com/user-attachments/assets/44b22a27-678a-44d0-8619-193abd05715e)

