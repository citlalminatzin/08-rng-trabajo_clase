[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Y59lTQr6)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23693676)
# Experimento de Miaunty-Hall

## Integrantes

-Herrera Barrera Joyce


## Ejercicio

Un gato hambriento enfrenta tres cajas: solo una guarda un pescado
fresco, las otras esconden pepinos. Después de que el gato selecciona una
de las cajas el humano abre una caja sin pescado y le ofrece la opción de
cambiar. ¿El gato debería seguir su instinto inicial o cambiar su
selección?

Las probabilidades de elegir cada caja son:

-Caja con un pepino 1/3

-Caja con un pepino 1/3

-Caja con el pescado 1/3

Elegir alguna de las cajas nos da 1/3 de probabilidad de ganar, sin embargo, al decidir cambiar de elección, estamos tomando 2/3 de probabilidad de elegir la caja ganadora.
También esta la otra probabilidad de elegir la caja ganadora y no cambiar en primera instancia, pero la probabilidad es de 1/3.

 Por ello, la mejor opción es que el gato decida cambiar de caja para que tenga más oportunidad de ganar.

Esto lo podemos ver tras ejecutar el código:

success_change=0.632 

success_stay=0.339

Si aumentaramos el número de iteraciones, estos números se acercarían más a 0.666 y 0.333 repectivamente.
