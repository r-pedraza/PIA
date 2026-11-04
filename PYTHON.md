# Norma de código Python

Regla única para todo el Python que se entrega en PIA. Se aplica al código del
repositorio de entregas y a cualquier script que acabe en un PDF.

Si algo no está cubierto aquí, se aplica la [PEP 8](https://peps.python.org/pep-0008/)
y, si hay conflicto, manda esta norma.

## 1. Versión de Python

- **Objetivo: Python 3.11 como mínimo.** No se usa nada por debajo de 3.10 (sin
  `match/case`, sin tipos `X | Y` si hay que bajar de 3.10).
- Los ejercicios sencillos de clase funcionan también en **3.9**, porque el Python
  del sistema en el portátil y el del `.venv` es 3.9. Por eso:
  - `from typing import Dict, List, Optional` en lugar de `dict[str, int]` en
    las firmas si hay que bajar de 3.10.
  - Nada de `match`, de `zip(strict=True)` ni de `datetime.UTC`.
- Comprobación obligatoria antes de entregar:

  ```sh
  python3 --version          # la del sistema
  /Users/raul/miniconda3/bin/python --version   # la buena para trabajar
  ```

- Se declara la versión en `pyproject.toml` con `requires-python = ">=3.9"` y en
  el README de la tarea.

## 2. Idioma del código

- **Identificadores en inglés**: variables, funciones, clases, módulos y
  constantes. `count_frequencies`, no `contar_frecuencias`.
- **Comentarios y docstrings en inglés.** El código se comparte y se lee en
  cualquier sitio; los textos de cara al usuario pueden ir en español.
- **Mensajes al usuario y `print` de los programas: en español**, igual que los
  mensajes de error y las salidas de los ejercicios que se entregan.
- Los nombres del dominio (una palabra del enunciado, una variable de negocio)
  se pueden dejar en español si traducirlos las hace confusas. Se justifica en el
  docstring.
- Excepción razonable: los parámetros de entrada de los ejercicios de una
  asignatura en español pueden conservar el nombre del enunciado; la función se
  llama en inglés igualmente.

## 3. Estándares de estilo

- **PEP 8** + [PEP 257](https://peps.python.org/pep-0257/) (docstrings).
- **Líneas de 100 caracteres** como máximo (`line-length = 100`).
- **4 espacios**, nunca tabulaciones.
- **Nombres**:
  - `snake_case` para funciones, variables y módulos: `clean_list`.
  - `PascalCase` para clases: `WordCounter`.
  - `UPPER_SNAKE_CASE` para constantes de módulo: `MAX_WORDS`.
  - Sin nombres de una letra salvo contadores de bucle (`i`, `j`) y coordenadas.
  - Sin abreviaturas que no sean estándar (`tmp`, `buf` no; `num`, `idx` sí).
- **Orden dentro de un módulo**: docstring de módulo → imports → constantes →
  funciones → `if __name__ == "__main__":`.
- **Imports**: biblioteca estándar, luego terceros, luego locales, cada bloque
  separado por una línea en blanco y en orden alfabético dentro del bloque.
  Nunca `import *`.
- **F-strings** en lugar de `%` o `.format()`.

## 4. Clean code

Las reglas que de verdad se comprueban al revisar una entrega:

1. **Funciones cortas y con una sola responsabilidad.** Si necesita el
   conector «y», va partida en dos.
2. **Nombres que digan qué hace**, no cómo: `remove_negatives`, no `filter1`.
   Si un nombre necesita un comentario para entenderse, el nombre está mal.
3. **Sin efectos secundarios ocultos.** Una función que se llama `count_x` no
   imprime ni escribe ficheros por dentro.
4. **Separar cálculo de presentación.** La función devuelve datos; el
   `__main__` o una función `print_*` los muestra.
5. **Sin números mágicos.** Van a una constante con nombre: `MIN_EXCEDENTE = 500`.
6. **Sin anidamiento profundo.** Máximo dos niveles de `if`/`for`; el resto se
   delega en funciones auxiliares o se resuelve con `continue` temprano.
7. **Sin código muerto**: nada de variables que no se usan, imports huérfanos ni
   funciones comentadas.
8. **Sin duplicación.** Si un bloque aparece dos veces, se extrae.
9. **Errores explícitos**: se valida la entrada y se lanza una excepción con
   mensaje claro; no se devuelve `None` silencioso ni se traga el error con
   `except: pass`.
10. **Inmutabilidad cuando se pueda**: preferir devolver una lista nueva que
    modificar la del parámetro.
11. **Complejidad razonable**: si un `if` necesita leerlo dos veces, mala señal.
12. **Un cambio, un commit.**

## 5. Documentación

- **Docstring en todas las funciones públicas**: qué hace, qué recibe y qué
  devuelve. Las privadas (`_prefijo`) también, si no son obvias.
- Formato Google o reStructuredText, pero **el mismo en todo el repo**:

  ```python
  def severity(level: int) -> str:
      """Devuelve la etiqueta del nivel de severidad.

      Args:
          level: entero entre 1 y 5.

      Returns:
          La etiqueta del nivel («bajo», «medio», «alto»).

      Raises:
          ValueError: si `level` está fuera de rango.
      """
  ```

- Se documenta **por qué**, no qué: el `#` explica decisiones, no repite la
  línea.
- README de cada tarea con: objetivo, cómo ejecutar, salida esperada.

## 6. Tipos

- **Anotaciones de tipo obligatorias** en los parámetros y en el retorno de toda
  función pública.
- `Optional[X]` para `None`; nunca `= None` sin anotar.
- Se comprueba con `mypy` cuando el proyecto lo tenga disponible; si no, se
  revisan a mano.

## 7. Tests

- Cada ejercicio funcional lleva su `test_<modulo>.py` con `pytest`.
- Un test cubre el ejemplo del enunciado; como mínimo, un caso normal y un caso
  límite (lista vacía, fichero sin coincidencias, conjunto vacío).
- Nombres de test: `test_<qué hace>_<condición>`:
  `test_clean_list_removes_negatives`.
- Los tests no dependen del orden de ejecución ni de ficheros del disco.
- Todo en verde antes de commitear:

  ```sh
  python -m pytest tarea01/src -q
  ```

## 8. Dependencias y entorno

- Solo biblioteca estándar salvo que el enunciado pida otra cosa.
- Si hace falta una dependencia, se apunta en `requirements.txt` **con versión
  fijada** (`pandas==2.2.2`, no `pandas`).
- No se commitean entornos: `.venv/` está en `.gitignore`.
- Sin secretos en el código: claves, tokens y rutas personales van por
  variables de entorno o ficheros `.env` ignorados.

## 9. Comprobaciones antes de entregar

```sh
# 1. formato y estilo
python -m ruff check tareaNN/src          # E, F, I, B, UP
python -m ruff format --check tareaNN/src
# 2. tipos (si aplica)
python -m mypy tareaNN/src
# 3. tests
python -m pytest tareaNN/src -q
# 4. se ejecuta de verdad
python tareaNN/src/problema1.py
```

- [ ] Identificadores en inglés y comentarios en inglés
- [ ] Mensajes al usuario en español
- [ ] Docstrings en las funciones públicas
- [ ] Anotaciones de tipo
- [ ] Líneas de 100 caracteres o menos
- [ ] Sin números mágicos ni código muerto
- [ ] Tests en verde y salida del programa comprobada a mano
- [ ] Funciona con Python 3.9 si la tarea es de clase
