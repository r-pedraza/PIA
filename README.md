# PIA

Repositorio de entregas de tareas del ciclo IA + Big Data.

## Estructura

```
tarea01/   # enunciado, notebook/código y memoria
tarea02/
tarea03/
tarea04/
tarea05/
```

Cada carpeta contiene su propio material. Los ficheros `.gitkeep` solo existen para que git
registre las carpetas vacías; puedes borrarlos en cuanto pongas contenido real.

## Convención por tarea

```
tareaNN/
├── README.md        # breve explicación: objetivo, cómo ejecutar, resultados
├── enunciado.*      # opcional, copia del enunciado
├── src/             # o notebook(s) .ipynb
└── data/            # datos pequeños (los grandes, ver .gitignore)
```

## Flujo de trabajo

```bash
git add -A
git commit -m "tareaNN: descripción corta"
git push
```

## Entorno

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # cuando exista
```

`.venv/` está en `.gitignore`, nunca se sube.
