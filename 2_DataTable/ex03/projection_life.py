from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def format_thousands(value: float, pos: int) -> str:
    '''
    Format y-axis labels in thousands.
    '''
    res = f"{int(value / 1_000)}k" if value >= 1_000 else str(int(value))
    return res


def validate_dataframe(df, name: str, column: str) -> str | None:
    """
    Check that the dataframe is usable.
    Returns an error message, or None if everything looks fine.
    """
    if df is None:
        return f"Error: could not load {name}."

    if "country" not in df.columns:
        return f"Error: '{name}' missing 'country' column."

    if column not in df.columns:
        return f"Error: '{name}' missing '{column}' column."

    return None


def main():
    '''
    Program loads two data filles and
    '''

    year = '1900'
    df_le = load("life_expectancy_years.csv")
    df_gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    error = validate_dataframe(df_le, "life expectancy data", year)
    if error:
        print(error)
        return

    error = validate_dataframe(df_gdp, "gdp data", year)
    if error:
        print(error)
        return

    # Filter the dataframes to only include the year of interest
    line_le = df_le[["country", year]]
    line_gdp = df_gdp[["country", year]]

    # Merge the two dataframes on the 'country' column
    df_year = line_le.merge(line_gdp, on="country", suffixes=("_le", "_gdp"))

    if df_year.empty:
        print("Error: no matching countries between the two datasets.")
        return

    x = df_year[f"{year}_gdp"]
    y = df_year[f"{year}_le"]
    legend = df_year["country"].values

    fig, ax = plt.subplots()
    sc = ax.scatter(x, y)

    # Annotation box, hidden until we hover over a point
    annot = ax.annotate(
        "",
        xy=(0, 0),
        xytext=(15, 15),
        textcoords="offset points",
        bbox=dict(boxstyle="round", fc="w"),
        arrowprops=dict(arrowstyle="->"),
    )
    annot.set_visible(False)

    def update_annot(index):
        pos = sc.get_offsets()[index]
        annot.xy = pos
        annot.set_text(legend[index])

    def on_hover(event):
        visible = annot.get_visible()
        if event.inaxes == ax:
            contains, info = sc.contains(event)
            if contains:
                index = info["ind"][0]
                update_annot(index)
                annot.set_visible(True)
                fig.canvas.draw_idle()
                return
        if visible:
            annot.set_visible(False)
            fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", on_hover)

    ax.set_xscale("log")
    ax.set_xticks([300, 1000, 10000])
    ax.xaxis.set_major_formatter(FuncFormatter(format_thousands))

    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.title(year)
    plt.show()


if __name__ == "__main__":
    main()
