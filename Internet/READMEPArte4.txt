Practica 4

PokéAPI - Práctica con Postman

Descripción general de la API

- PokéAPI es una API REST pública y gratuita que proporciona información sobre el mundo de Pokémon. Permite consultar datos de Pokémon, habilidades, movimientos, tipos, evoluciones, objetos y regiones. La información se obtiene mediante solicitudes HTTP y se devuelve en formato JSON.

Solicitud 1

- Método HTTP utilizado: GET
- Endpoint: https://pokeapi.co/api/v2/pokemon/pikachu
- Parámetros o cuerpo de la solicitud: No requiere parámetros ni cuerpo de la solicitud.
- Descripción de la respuesta: Devuelve la información del Pokémon Pikachu, incluyendo su nombre, número de identificación, altura, peso y otros datos.

Ejemplo de respuesta:

```json
{
  "id": 25,
  "name": "pikachu",
  "height": 4,
  "weight": 60
}
```

- Código de estado obtenido: 200 OK.

---

Solicitud 2

- Método HTTP utilizado: POST
- Endpoint: https://pokeapi.co/api/v2/pokemon
- Parámetros o cuerpo de la solicitud: No se envió un cuerpo de la solicitud, ya que la PokéAPI no permite crear recursos mediante este método.
- Descripción de la respuesta: La API devuelve un error porque únicamente admite consultas mediante GET.

Ejemplo de respuesta:

```json
{
  "detail": "Not found."
}
```

- Código de estado obtenido: 404 Not Found.

---

Solicitud 3

- Método HTTP utilizado: PUT
- Endpoint: https://pokeapi.co/api/v2/pokemon/pikachu
- Parámetros o cuerpo de la solicitud: No se envió cuerpo de la solicitud. La PokéAPI no permite modificar información mediante este método.
- Descripción de la respuesta: La API responde con un error indicando que el recurso no admite solicitudes PUT.

Ejemplo de respuesta:

```json
{
  "detail": "Not found."
}
```

- Código de estado obtenido: 404 Not Found.

---

Qué aprendí del proceso

- Aprendí a utilizar Postman para realizar solicitudes HTTP a una API REST.
- Comprendí la diferencia entre los métodos GET, POST y PUT.
- Aprendí a interpretar los códigos de estado HTTP, como 200 OK y 404 Not Found.
- Observé cómo una API devuelve información en formato JSON.
- También entendí que existen APIs de solo lectura, como la PokéAPI, que únicamente permiten realizar consultas mediante el método GET.