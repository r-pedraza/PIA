# PIA · Tarea 1 · Apartado 3 · Kaggle

Cuenta en Kaggle, entrada en una competición activa y descarga del dataset, con
pantallazos del proceso. El documento que se ve en el repositorio es
[kaggle.pdf](kaggle.pdf); las imágenes sueltas están en `capturas/`.

## Ficha de la competición

| Dato | Valor |
|---|---|
| Competición | Predicting Credit Card Fraud |
| Serie | Playground Series · Season 6 Episode 11 (`playground-series-s6e11`) |
| URL | https://www.kaggle.com/competitions/playground-series-s6e11 |
| Organiza | Kaggle |
| Objetivo | Predecir la probabilidad de fraude (`is_fraud`) en cada identificador del conjunto de test |
| Métrica | ROC AUC (área bajo la curva) |
| Etiquetas | Beginner · Tabular · Roc Auc Score |
| Ficheros | `train.csv`, `test.csv`, `sample_submission.csv` |
| Tamaño total | 148 MB · 3 ficheros · 53 columnas |
| Licencia | Attribution 4.0 International (CC BY 4.0) |
| Participación al capturar | 912 equipos · 24 días de plazo restante |

Los datos de la tabla salen de las propias capturas (pestañas Overview y Data de
la competición) y de la ficha pública del enlace.

## Qué hace falta para que puntúe

La rúbrica del apartado 3 son 2 puntos:

| Criterio | Puntos | Dónde se demuestra |
|---|---:|---|
| Se crea una cuenta en Kaggle | 0,75 | `01` a `03` |
| Se accede a una competición y se descarga el dataset, con pantallazos del proceso y del dataset | 1,25 | `04` a `10` |

## Capturas

| # | Fichero | Qué demuestra |
|---|---|---|
| 01 | `01-punto-de-partida.jpg` | Kaggle antes de crear la cuenta: la cabecera ofrece *Login* y *Sign Up* |
| 02 | `02-registro-formulario.jpg` | Formulario de alta: pestaña *Register*, con *Register with Google* y *Register with Email* |
| 03 | `03-cuenta-creada.jpg` | Sesión iniciada como *Raul Pedraza*: la cuenta existe y está verificada |
| 04 | `04-competiciones-activas.jpg` | Listado de competiciones con el filtro **Active** aplicado |
| 05 | `05-competicion-overview.jpg` | Página de la competición: título, plazo, métrica y número de equipos |
| 06 | `06-inscripcion-competicion.jpg` | **Inscripción**: la competición aparece en *Your Work* con un envío puntuado (6,1) y el puesto sobre 915 equipos |
| 07 | `07-dataset-ficheros.jpg` | Pestaña Data: los 3 ficheros, 148 MB y el botón *Download All* |
| 08 | `08-descarga-dataset.jpg` | Descripción del dataset y descarga en curso (`playground-series-s6e11.zip`, 30,9 MB) |
| 09 | `09-dataset-descargado.jpg` | Finder: el `.zip` y la carpeta extraída en Descargas |
| 10 | `10-dataset-contenido.jpg` | Contenido del dataset descargado: `train.csv`, `test.csv`, `sample_submission.csv` |

## Regenerar el PDF

El generador vive fuera de este repositorio (NORMATIVA.md: aquí solo van
entregas, no herramientas):

```sh
sh /Users/raul/.hermes/profiles/academico/scripts/pia_kaggle_pdf.sh
```

Toma las capturas de `capturas/`, les pone pie y compone `kaggle.pdf` con Chrome
en modo headless.

## Notas

- El dataset no se sube al repositorio: el enunciado pide un documento **con
  pantallazos** del proceso y del dataset, no los datos. Un `.csv` de 148 MB no
  tiene sitio en un repo de entregas.
- Las capturas se tomaron el 2026-11-06 a las 15:51.
