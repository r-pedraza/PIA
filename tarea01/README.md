# PIA · Tarea 1

Tarea de la unidad 1 de Programación de Inteligencia Artificial. Tres apartados:

| Apartado | Contenido | Puntos |
|---|---|---:|
| 1 | Cuenta en GitHub y primer repositorio, con el proceso explicado | 2 |
| 2 | Tres problemas de Python | 6 |
| 3 | Cuenta en Kaggle, competición y dataset | 2 |

## Contenido de la carpeta

```
tarea01/
├── README.md           este fichero
├── enunciado.md        fuente editable del apartado 1 (Markdown)
├── entrega.pdf         apartado 1 entregado en Avanza
├── Pedraza_Leon_Raul_PIA01_Tarea.txt   fichero que se sube a Avanza (solo la URL)
├── kaggle/             apartado 3: cuenta, competición y dataset
│   ├── README.md           ficha de la competición y lista de capturas
│   ├── kaggle.pdf          documento con los pantallazos
│   └── capturas/           capturas numeradas 01..10
└── src/
    ├── problema1.py        lista de enteros: quita negativos, duplica y ordena
    ├── problema2.py        frecuencia de palabras en un fichero de texto
    ├── problema3.py        intersección, unión y diferencia simétrica con sets
    ├── test_problema1.py   tests del problema 1
    ├── test_problema2.py   tests del problema 2
    └── test_problema3.py   tests del problema 3
```

Normas de código: identificadores en
inglés, docstrings en inglés, mensajes al usuario en español y compatibilidad con
Python 3.9.

## Qué hace cada problema

**Problema 1 · `clean_list(numbers)`**
Devuelve una lista nueva sin negativos, sin repetidos y ordenada.
`[4, -1, 2, 4, 3, -5, 2] → [2, 3, 4]`. Rechaza valores que no sean enteros con
`TypeError` y no modifica la lista de entrada.

**Problema 2 · `count_frequencies(words, path)`**
Cuenta cuántas veces aparece cada palabra de la lista en el fichero. Quita
puntuación, pasa a minúsculas y normaliza tildes, así que `Programación` y
`PROGRAMACION` cuentan como la misma palabra. Devuelve todas las palabras de la
lista, aunque aparezcan 0 veces. `print_sorted()` las muestra por orden
alfabético.

**Problema 3 · `compare_sets(first, second)`**
Con `set`, calcula intersección (`&`), unión (`|`) y diferencia simétrica (`^`)
de dos listas de enteros, y devuelve un diccionario con las tres, ordenadas para
que la salida sea estable.

## Apartado 3 · Kaggle

Cuenta creada y competición consultada: **Predicting Credit Card Fraud**
(Playground Series S6E11), dataset de 148 MB en tres CSV. El proceso está
documentado en `kaggle/kaggle.pdf`; los detalles y la lista de capturas, en
`kaggle/README.md`.

## Estado

- Apartado 3 completo: `kaggle/kaggle.pdf` con las diez figuras (cuenta,
  competición, inscripción y dataset).
