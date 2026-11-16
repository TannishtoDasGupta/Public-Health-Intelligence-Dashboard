# Public Health Intelligence Dashboard

A public-health indicator API using clearly labelled synthetic regional observations. It includes indicator definitions, regional summaries, and data-completeness metadata.

## Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open /docs. API: GET /indicators, GET /indicators/{code}, GET /regions/summary?indicator=..., GET /data-quality.

## Data integrity
The bundled values are fictional and must not be represented as official statistics or used for clinical/public-policy decisions. For real data, retain source URLs, publication dates, denominator definitions, transformation logic, and domain validation. Completeness alone does not prove accuracy or comparability.
