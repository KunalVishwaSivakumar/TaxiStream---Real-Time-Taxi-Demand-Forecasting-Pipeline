import pandas as pd

df = pd.read_parquet('data/raw/yellow_tripdata_2025-01.parquet')
df.head(500).to_csv('data/raw/nyc_taxi_sample.csv', index=False)
print("Sample saved!")
