# Raw data notes

- `vercel_models_text.csv` — primary models export (CC BY 4.0 Vercel).
- If the plain CSV is missing from a shallow clone due to size limits, decode:

```bash
base64 -d data/raw/vercel_models_text.csv.gz.b64.txt | gzip -d > data/raw/vercel_models_text.csv
```

- `vercel_labs_text.csv` may be provided similarly.
