import pandas as pd


def load(path: str) -> pd.DataFrame:
    '''Function that loads a data file, prints it shape and returns a dataset object.'''

    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print(f"File '{path}' does not exist.")
        return None
    except IsADirectoryError:
        print(f"'{path}' is a directory.")
        return None
    except pd.errors.ParserError:
        print(f"'{path}' is not a valid data file.")
        return None
    except pd.errors.EmptyDataError:
        print(f"'{path}' is empty.")
        return None
    except Exception as e:
        print(f"Couldn't read '{path}': {e}")
        return None

    print(f"Loading dataset of dimensions {df.shape}")

    return df
