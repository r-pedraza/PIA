# PIA

Repositorio de entregas de tareas del ciclo IA + Big Data.

Contiene **solo entregas**: una carpeta por tarea con su documento y su PDF. Las
herramientas y los scripts viven fuera, en el monorepo.

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

```bash
git add -A
git commit -m "tareaNN: descripción corta"
git push
```

Para ramas por tarea y por ejercicio, ver `NORMATIVA.md`.

## Entorno

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # cuando exista
```

`.venv/` está en `.gitignore`, nunca se sube.
