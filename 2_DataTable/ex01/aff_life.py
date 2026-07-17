from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Function loads the life expectancy dataset and
    plots the life expectancy of France over the years.
    """
    try:
        df = load("life_expectancy_years.csv")
        if df is None:
            return

        france = df.loc[df["country"] == "France"].iloc[0]

        years = france.drop("country")
        x = years.index.astype(int)
        y = years.values

        # Prepare the plot and display it
        plt.plot(x, y)
        plt.xticks(range(min(x), max(x) + 1, 40))
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.title("France Life expectancy Projections")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
