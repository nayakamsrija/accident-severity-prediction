# Accident Severity Prediction (US Accidents)

Multiclass (Severity 1–4) and binary (LOW vs HIGH) prediction using the US Accidents dataset.

## Data

This project uses the Kaggle dataset `sobhanmoosavi/us-accidents` (file: `US_Accidents_March23.csv`).
The raw CSV is **not** committed; download locally or use `src/data/download_data.py` with Kaggle credentials.

## Repository layout

- `src/` — data loader and feature helpers
- `models/` — trained artifacts (multiclass / binary subfolders and exported pickles)
- `output-plot/` — EDA and evaluation figures
- `tableau_binary/`, `tableau_multiclass/` — CSV exports for Tableau dashboards
- `streamlit_app.py` — interactive predictor UI
- `save_models_for_streamlit.py` — export pickles for the app

## Quick start

1. Python 3.10+ recommended; create a virtual environment.
2. Install dependencies: `pip install -r models/requirements.txt` (and add `pandas`, `scikit-learn`, `streamlit`, `kagglehub` as needed for your environment).
3. Run dataset loader: `python -m src.data.download_data` (from repo root, with `PYTHONPATH=.` or install package in editable mode).
4. Launch app: `streamlit run streamlit_app.py` (requires trained models under `models/`).

## Team

DATA 230 — Team 5 (Spring 2025).
