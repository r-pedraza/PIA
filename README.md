# PIA

Repositorio de entregas de tareas del ciclo IA + Big Data.

Contiene **solo entregas**: una carpeta por tarea con su documento y su PDF. Las
herramientas y los scripts viven fuera, en el monorepo.

## Índice de entregas

| Tarea | Carpeta | Qué contiene | Puntos |
|---|---|---|---:|
| 1 · Unidad 1 | [tarea01/](tarea01/) | Apartado 1 GitHub ([entrega.pdf](tarea01/entrega.pdf)) · apartado 2 Python ([src/](tarea01/src/), 24 tests) · apartado 3 Kaggle ([kaggle.pdf](tarea01/kaggle/kaggle.pdf)) | 10 |
| 2 · Unidad 2 | [tarea02/](tarea02/) | pendiente | — |
| 3 · Unidad 3 | [tarea03/](tarea03/) | pendiente | — |

El fichero que se sube a Avanza en la tarea 1 es
[Pedraza_Leon_Raul_PIA01_Tarea.txt](tarea01/Pedraza_Leon_Raul_PIA01_Tarea.txt),
con la URL de este repositorio.

## Cómo comprobar una entrega en dos minutos

```bash
# 1. Documentos
open tarea01/entrega.pdf tarea01/kaggle/kaggle.pdf

# 2. Código: 24 tests y estilo
cd tarea01/src && python -m pytest . -q && python -m ruff check .
```

Los tests también corren solos en cada push (pestaña *Actions*, Python 3.9 y 3.13).

## Estructura

```
tarea01/   # README, enunciado.md, entrega.pdf y, si toca, src/ y data/
tarea02/
tarea03/
tarea04/
tarea05/
```

Norma de trabajo con Git: [NORMATIVA.md](NORMATIVA.md). Los ficheros `.gitkeep`
solo existen para que git registre las carpetas vacías; se borran en cuanto la
carpeta tiene contenido real.

## Convención por tarea

```
tareaNN/
├── README.md        # objetivo, contenido y cómo se generó
├── enunciado.md     # fuente editable (Markdown) del documento entregado
├── entrega.pdf      # el PDF exacto que se sube a Avanza
├── src/             # código, si la tarea lo lleva
└── data/            # datos pequeños (los grandes, ver .gitignore)
```

## Flujo de trabajo

Una rama por tarea; `main` solo recibe merges `--no-ff` (detalle en
`NORMATIVA.md`):

```bash
git checkout -b tareaNN
git commit -m "tareaNN-ejNN: qué se ha hecho"
git checkout main && git merge --no-ff tareaNN
git push origin main
```

## Entorno

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # cuando exista
```

`.venv/` está en `.gitignore`, nunca se sube.
