"""Esegue la pipeline completa: ingestion -> bronze -> silver.

    python -m pipeline.run_pipeline
"""
from . import bronze, ingestion, silver


def main():
    print("== ingestion ==")
    ingestion.ingest()
    print("== bronze ==")
    bronze.to_bronze()
    print("== silver ==")
    silver.to_silver()
    print("== fatto ==")


if __name__ == "__main__":
    main()
