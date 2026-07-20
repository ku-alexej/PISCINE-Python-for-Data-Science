from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

MIN_YEAR = 1800
MAX_YEAR = 2050


def parse_population(value: str) -> float | None:
    '''
    Convert population strings to numbers.
    '''
    try:
        value = str(value)

        if value.endswith("B"):
            return float(value[:-1]) * 1_000_000_000
        if value.endswith("M"):
            return float(value[:-1]) * 1_000_000
        if value.endswith("k"):
            return float(value[:-1]) * 1_000

        return float(value)

    except ValueError:
        return None


def format_millions(value: float, pos: int) -> str:
    '''
    Format y-axis labels in millions.
    '''
    return f"{int(value / 1_000_000)}M"


def get_country_series(df, country: str):
    '''
    Extract and clean a single country's population series.
    '''

    row = df.loc[df["country"] == country].iloc[0].drop("country")
    return row.apply(parse_population)


def validate_dataframe(df, countries) -> str | None:
    '''
    Check that the dataframe is usable.
    Returns an error message, or None if everything looks fine.
    '''
    if df is None:
        return "Error: could not load data."

    if "country" not in df.columns:
        return "Error: missing 'country' column."

    available = set(df["country"].values)
    for country in countries:
        if country not in available:
            return f"Error: {country} not found."

    return None


def main():
    '''
    Load population data and compare countries in COUNTRIES.
    '''

    countries = ("France", "Russia")
    min_year = 1800
    max_year = 2050

    df = load("population_total.csv")

    error = validate_dataframe(df, countries)
    if error:
        print(error)
        return

    # Load each country's series into a dict keyed by country name
    data = {country: get_country_series(df, country) for country in countries}

    try:
        years = data[countries[0]].index.astype(int)
    except ValueError:
        print("Error: invalid year format.")
        return

    # Filter years to the range of interest
    mask = (years >= min_year) & (years <= max_year)
    years = years[mask]
    for country in countries:
        data[country] = data[country][mask]

    if len(years) == 0:
        print("Error: no data in the specified year range.")
        return

    for country in countries:
        plt.plot(years, data[country], label=country)

    max_population = max(series.max() for series in data.values())

    plt.xticks(range(min(years), max(years) + 1, 40))
    plt.yticks(range(0, int(max_population) + 1, 20_000_000))
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))

    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population Projections")
    plt.legend(loc="lower right")
    plt.show()


if __name__ == "__main__":
    main()
