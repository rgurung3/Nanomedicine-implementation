import pandas as pd

def load_dataset(path: str):
    df = load_dataset("data/raw/nano_tumor.csv")
    print(f"Dataset loaded with shape: {df.shape}")
    return df