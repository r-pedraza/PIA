# Norma de trabajo con Git — entregas PIA

Regla única para preparar, versionar y entregar las tareas de **Programación de
Inteligencia Artificial**. Si algo no se cumple aquí, se para y se pregunta.

## 1. Qué es este repositorio y qué no

Este repositorio contiene **solo entregas**. No lleva herramientas, ni scripts
auxiliares, ni configuración de desarrollo.

| Elemento | Ruta |
|---|---|
| Repositorio de entregas | `/Volumes/WD Blue 1TB/IA+BD/PIA/works` |
| Remoto | `https://github.com/r-pedraza/PIA.git` (privado) |
| Rama por defecto | `main` |
| Material descargado de Avanza | `/Volumes/WD Blue 1TB/IA+BD/PIA/2-Unidad-N/` |
| Fuente editable de cada entrega | `Trabajos/` de su enunciado, o `ejercicios/` |
| Herramienta de Git | `tools/pia_git/` del monorepo (fuera de este repo) |

El trabajo se escribe **fuera** del repo (en `Trabajos/` del enunciado) y se copia
aquí solo cuando se va a versionar. Nunca se edita la carpeta de descarga del
conector.

## 2. Ramas

```
main                 tronco estable. Solo recibe merges --no-ff en verde.
└── tareaNN          una rama por tarea, nace en main
    └── tareaNN-ejNN una rama por ejercicio, nace en tareaNN
```

- `NN` siempre a dos dígitos: `tarea01`, `tarea01-ej02`.
- **Con guion, no con barra.** Git no permite que una rama sea prefijo de otra:
  `tarea01` y `tarea01/ej01` no pueden coexistir. El esquema `tareaNN/ejNN`
  falla con `cannot lock ref`.
- Una tarea puede tener varios ejercicios, y cada uno se cierra antes de abrir
  el siguiente.

## 3. Ciclo de trabajo

La herramienta está en el monorepo; se invoca con `--repo` apuntando aquí:

```sh
P=/Users/raul/miniconda3/bin/python
T=/Users/raul/Documents/docker-stack/ServerMonorepo/tools/pia_git/pia_git.py
R="/Volumes/WD Blue 1TB/IA+BD/PIA/works"

$P $T --repo "$R" start-task  01              # abre tarea01 desde main
$P $T --repo "$R" start-ex    01 01           # abre tarea01-ej01 desde tarea01
# ... trabajar, commitear con normalidad ...
$P $T --repo "$R" finish-ex   01 01           # merge --no-ff en tarea01
$P $T --repo "$R" finish-task 01 "Título"     # merge --no-ff en main + tag v0.01.0
$P $T --repo "$R" publish                     # push de main con tags
$P $T --repo "$R" status                      # dónde estoy
```

El resultado es una línea por comando (`✓ tarea01 mergeada en main con tag
v0.01.0`) y el siguiente paso sugerido.

## 4. Commits

- Mensajes en **español**, en minúsculas, formato `tareaNN-ejNN: qué has hecho`.
- Un commit = un cambio con sentido.
- **Un commit por criterio de la rúbrica** cuando la tarea sea larga.
- No se commitea nunca: `.env`, claves `*.pem`, `.venv/`, `__pycache__/`,
  `.DS_Store`. Ya están en `.gitignore`.

## 5. Cierre de tarea

1. Todo el trabajo está en `tareaNN`.
2. `finish-task NN "Título"` → merge `--no-ff` y tag anotado `v0.NN.0`.
3. `publish` → `git push origin main --follow-tags`.
4. Se comprueba que el tag aparece en GitHub.

El tag marca la entrega; si la tarea se corrige después, se sube otro commit a
`main`, **nunca se mueve el tag**.

## 6. Qué se guarda en cada tarea

```
tareaNN/
├── README.md        objetivo, contenido y cómo se generó
├── enunciado.md     fuente editable (Markdown) del documento entregado
├── entrega.pdf      el PDF exacto que se sube a Avanza
├── src/             código, si la tarea lo lleva
└── data/            datos pequeños (los grandes van fuera, ver .gitignore)
```

Los `.gitkeep` se borran en cuanto la carpeta tiene contenido real.

## 7. Errores que ya hemos visto y cómo se evitan

| Síntoma | Causa real | Solución |
|---|---|---|
| `could not read Username for 'https://github.com'` | sin credenciales | `gh auth login --web` y `gh auth setup-git` |
| `Permission denied (publickey)` | clave SSH no registrada | usar HTTPS con `gh` como credential helper |
| `git push` no crea el repo | push no crea remotos | crear el repo antes con `gh repo create` |
| `cannot lock ref 'tarea01/ej01'` | rama prefijo de otra | usar `tarea01-ej01` |
| `remote origin already exists` | remote ya configurado | comprobar con `git remote -v`, no re-añadir |
| `nothing to commit` al abrir tarea | la carpeta ya existía con `.gitkeep` | ya no aplica: la herramienta solo commitea si hay cambios |

## 8. Antes de dar una tarea por entregada

- [ ] `status` sin cambios pendientes ni ramas huérfanas
- [ ] Tag `v0.NN.0` visible en GitHub
- [ ] `main` sincronizada con `origin/main`
- [ ] El PDF subido a Avanza es el mismo que `tareaNN/entrega.pdf`
