# Ejercicios para practicar Python 🐍

Son ejercicios simples y practicos para practicar un poco coneptos basicos de programacion en Pyhton.

Los ejercicios estan inspirados en cursos que eh tomado para practicar, y junto las soluciones que les di. Si te ayuda a tener este material en español para practicar, compartelo a otros que tambien les pueda servir.

Los ejercicios los dividi en basicos e intermedios, dado que la soluciones pueden desarrollarse sin necesidad de usar funciones.

Claro que si eres mas avanzado puedes usarlas y compartir tu proceso.

---

## 📚 Índice

- [Ejercicios Básicos](#-ejercicios-básicos)
  - [Ejercicio 1: ...](#ejercicio-1-)
  - [Ejercicio 2: ...](#ejercicio-2-)
  - [Ejercicio 3: ...](#ejercicio-3-)
  - [Ejercicio 4: ...](#ejercicio-4-)
  - [Ejercicio 5: ...](#ejercicio-5-)
- [Ejercicios Intermedios](#-ejercicios-intermedios)
  - [Ejercicio 1: ...](#ejercicio-1-)
  - [Ejercicio 2: ...](#ejercicio-2-)
  - [Ejercicio 3: ...](#ejercicio-3-)
- [Cómo contribuir](#-cómo-contribuir)

---

## 🟢 Ejercicios Básicos

### Ejercicio 1: Calcula el area de un circulo

**Descripción:**  
Calcula el area de un circulo. El usuario te dara el radio.

**Dificultad:** ⭐ Fácil

**Pistas:**

- Usa `input()` para pedir los números
- La formula para obtener el area es: A = pi r^2
- En pyhton para elevar un numero al cuadraro es n\*\*2

**Prueba:**

- Entrada: 5
- Salida esperada: 78.55

### Ejercicio 2: Ordena una lista de manera ascendente

**Descripción:**  
Ordena un lista de numeros dada por el usuario, el usuario puede insertar N numeros en la misma linea. Debes ordenarlos de forma ascendente y muestra el resultado en una linea.

**Dificultad:** ⭐ Fácil

**Pistas:**

- Usa `input()` para pedir los números
- `.split()` te puede ayudar a separar los valores de la cadena introducida
- `sorted()` te puede ayudar en este caso

**Prueba:**

- Entrada: 1 9 5 7 3
- Salida esperada: 1 3 5 7 9

### Ejercicio 3: Calcula el factorial de un numero

**Descripción:**  
El factorial es la multiplicacion de todos los numeros hasta un numero determinado.

Solicita al usuario un numero N y calcula el factorial desde 1 hasta N e imprime el resultado

**Dificultad:** ⭐ Fácil

**Pistas:**

- La estructura de un for es `for (variable o _) in (Rango)`. Recordando que el rango va de 0 a N-1

**Prueba:**

- Entrada: 8
- Salida esperada: 40320

### Ejercicio 4: Contando caracters

**Descripción:**  
Realiza una funcion que reciba un numero y cuente la cantidad de digitos que conforman el numero.

\*Nota:este ejercicio puedes jugar con numeros flotantes y validaciones, igual con cadenas de texto y quitando los espacios

**Dificultad:** ⭐ Fácil

**Pistas:**

- la funcion `len()` permite el conteo de caracteres dentro de una cadena

**Prueba:**

- Entrada: 156
- Salida esperada: 3

### Ejercicio 5: Cuantos años tiene un perro

**Descripción:**  
Calcula la edad de un perro, acorde a las siguientes caracteristicas:

- El primer año del perro equivale a 15 años humanos
- El segundo año equivale a 9 años humanos
- Del tercer año al sexto año, cada uno equivale a 4 años humanos
- A partir del 7mo cada año equivale a 5 años humanos

Introduce la edad del perro y calcula su equivalente en años humanos.

**Dificultad:** ⭐ Fácil

**Pistas:**

- `If` suele usarse para condiciones

**Prueba:**

- Entrada: 10
- Salida esperada: 60

## 🟢 Ejercicios Intermedios

### Ejercicio 1: Anagrama

**Descripción:**  
Se considera anagrama aquella cadena que tenga los mismos caracteres que otra aunque esten desordenados. Ejemplo:

- amor:roma
- 582:258
- gato:toga
- 16:61

Introduce dos numeros e identifica si son anagramas.

Puedes aumentar la dificultad del reto:

- Opcion1: Que el usuario introduzca cuantas cadenas quiere introducir y cuenta cuantas de esas cadenas son anagramas
- Opcion2: El usuario puede introducir tanto numeros como palabras para encontrar si son anagramas

La solucion de este ejercicio representa la Opcion 1

**Dificultad:** ⭐⭐ Medio

**Pistas:**

- `sorted()` es un aliado para acomodar numeros

**Prueba:**

- Entrada: 546 645
- Salida esperada: True

Opcion 1 (La solucion que se da es para la opcion 1):

- Entrada:
  3
  548 854
  4567 6574
  2345 2874
- Salida esperada: 2

Opcion 2:

- Entrada:
  2
  roma amor
  2345 2874
- Salida esperada: 1

### Ejercicio 2: Ataque del caballo

**Descripción:**  
En ajedrez el caballo se mueve en L.

El usuario introducira la posicion del caballo y despues la posicion de las piezas del oponente, calcula cuales piezas son atacadas por tu caballo.

Teniendo un tablero de a-h (columnas) y a-8 (filas)

**Dificultad:** ⭐⭐ Medio

**Pistas:**

- `abs()` te permite obtener un entero
- `ord()` te permite pasar letras a su equivalente numerico
- El caballo siempre se movera dos casillas al frente y una al lado
- Piensalo como posiciones enteras y la diferencia que puede haber

**Prueba:**

- Entrada:
  d 4 Posicion de tu caballo en el tablero
  6 Fichas de tu contrincante
  c 2 posicion de cada ficha
  e 6
  a 1
  f 5
  d 5
  b 3
- Salida esperada: 4

### Ejercicio 3: Propagacion

**Descripción:**  
En un vecindario representado como una cuadrícula de casas de altura H y ancho W, algunas casas empiezan pintadas de gris.

Cada mes ocurre lo siguiente:
Todas las casas que estén justo al lado (arriba, abajo, izquierda o derecha) de una casa ya pintada de gris, se pintan también de gris.
Este proceso se repite mes tras mes.

Dada la cantidad total de casas que se quieren pintar de gris (N) y las posiciones de las casas que ya están grises al inicio, calcula cuántos meses se necesitan para que al menos N casas estén pintadas de gris.
Entrada:

- Primera línea: dos números enteros H y W (altura y ancho del vecindario).
- Segunda línea: un número entero N (cantidad de casas grises que se desean alcanzar).
- Tercera línea: un número entero M (cantidad de casas que ya están grises al inicio).
- Las siguientes M líneas: dos números X e Y que indican la fila y la columna de cada casa ya pintada de gris (las posiciones empiezan en 1).

Cada mes se propaga, cuantos meses se tardara en tener N casas grises

**Dificultad:** ⭐⭐ Medio

**Pistas:**

- Es un problema de propagacion, considera que debes tener el vecindario base con las primeras casas pintadas, una que se modifique acorde a la propacacion.
- Ten cuidado al realizar la propagacion no actualizes el vecindario sobre el calculo o se seguira propagando.

**Prueba:**

- Entrada:
  2 3
  4
  1
  1 1
- Salida esperada: 2

## 🤝 Cómo contribuir

¡Las contribuciones son bienvenidas! Puedes ayudar de las siguientes formas:

- Añadir nuevos ejercicios (básicos, intermedios o avanzados)
- Mejorar los enunciados o añadir más pistas
- Corregir errores
- Añadir ejemplos adicionales de entrada/salida
- Mejorar este README

### Pasos para contribuir:

1. Haz un **Fork** de este repositorio
2. Crea una nueva rama:

   ```bash
   git checkout -b nombre-de-tu-rama

   ```

3. Realiza tus cambios y haz commit:
   add .
   git commit -m "Añadí ejercicio de ..."

4. Sube tus cambios:
   push origin nombre-de-tu-rama

5. Abre un Pull Request explicando qué añadiste o modificaste.

Si tienes dudas o quieres proponer un ejercicio, puedes abrir un Issue.
