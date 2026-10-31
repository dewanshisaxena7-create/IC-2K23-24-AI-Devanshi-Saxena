
import pandas as pd


def preprocess_data():
    """Clean a dataset by handling missing and duplicate values."""

    data = {
        "Name": ["Aman", "Riya", "Karan", "Neha", "Riya"],
        "Age": [20, 21, None, 22, 21],
        "Marks": [85, 90, 78, None, 90]
    }

    df = pd.DataFrame(data)

    print("Original Dataset:")
    print(df)

    print("\nMissing Values:")
    print(df.isnull().sum())

    # Fill missing numerical values with column means.
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

    # Remove duplicate records.
    df = df.drop_duplicates()

    print("\nCleaned Dataset:")
    print(df)

    print("\nMissing Values After Cleaning:")
    print(df.isnull().sum())


if __name__ == "__main__":
    preprocess_data()
