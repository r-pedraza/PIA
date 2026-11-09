# Dataset · Predicting Credit Card Fraud (Playground Series S6E11)

Contenido del dataset descargado de la competición, tal cual lo entrega Kaggle. Se sube al
repositorio porque la rúbrica del apartado 3 pide «descargar el dataset … y subir su contenido al
repositorio Github» (1,25 puntos).

| Dato | Valor |
|---|---|
| Competición | [Predicting Credit Card Fraud](https://www.kaggle.com/competitions/playground-series-s6e11) |
| Serie | Playground Series · Season 6 Episode 11 (`playground-series-s6e11`) |
| Licencia | Attribution 4.0 International (CC BY 4.0) |
| Objetivo | probabilidad de fraude (`is_fraud`) para cada `id` de test |
| Métrica | ROC AUC |

## Ficheros

| Fichero | Filas | Columnas | Bytes |
|---|---:|---:|---:|
| `train.csv` | 699 960 | 26 (25 variables + `is_fraud`) | 98 533 176 |
| `test.csv` | 299 984 | 25 (sin la variable objetivo) | 41 068 069 |
| `sample_submission.csv` | 299 984 | 2 (`id`, `is_fraud`) | 8 399 564 |
| **Total** | | | **148 000 809** (≈148 MB) |

Cabecera: `id, amount_usd, hours_since_last_txn, txn_count_last_24h, distance_from_home_km,
card_age_months, customer…` hasta 25 variables de entrada.

## Procedencia

1. Pestaña **Data** de la competición → **Download All**, que genera
   `playground-series-s6e11.zip` (30,9 MB comprimido).
2. Se descomprime y se suben los tres CSV sin modificar: ni filtrado de filas, ni cambio de
   cabeceras, ni renombrado de columnas.

Los pasos están documentados con pantallazos en [`../kaggle.pdf`](../kaggle.pdf) y
[`../capturas/`](../capturas/).
