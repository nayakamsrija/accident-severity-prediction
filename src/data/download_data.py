import kagglehub
from kagglehub import KaggleDatasetAdapter


def load_us_accidents_march23():
    return kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        "sobhanmoosavi/us-accidents",
        "US_Accidents_March23.csv",
    )


if __name__ == "__main__":
    df = load_us_accidents_march23()
    print(f"Dataset loaded: {df.shape[0]:,} rows x {df.shape[1]} columns")

