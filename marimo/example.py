import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import altair as alt
    import polars as pl

    return mo, alt, pl


@app.cell
def __(mo):
    mo.md("""
    # Climate Change Adaptation Dashboard

    Exploring temperature trends and adaptation measures across Europe
    """)
    return


@app.cell
def __(mo):
    country = mo.ui.dropdown(
        options=["Germany", "France", "Spain", "Italy", "Poland"],
        value="Germany",
        label="Select Country:",
    )
    country
    return (country,)


@app.cell
def __(country, mo, pl):
    # Sample climate data
    data = pl.DataFrame(
        {
            "year": list(range(2015, 2025)),
            "avg_temp_c": [9.2, 9.5, 9.8, 10.1, 10.3, 10.5, 10.8, 11.1, 11.3, 11.6],
            "heatwave_days": [5, 8, 12, 10, 15, 18, 22, 20, 25, 28],
            "adaptation_budget_million": [50, 55, 65, 70, 80, 95, 110, 125, 140, 160],
        }
    )

    mo.md(f"## Climate Data for {country.value}")
    return data


@app.cell
def __(data, mo):
    mo.ui.table(data)
    return


@app.cell
def __(data, mo, alt):
    # Temperature trend chart
    temp_chart = (
        alt.Chart(data.to_pandas())
        .mark_line(point=True, color="#e74c3c")
        .encode(
            x=alt.X("year:O", title="Year"),
            y=alt.Y("avg_temp_c:Q", title="Avg Temperature (°C)"),
        )
        .properties(title="Average Temperature Trend")
    )

    mo.ui.altair_chart(temp_chart)
    return (temp_chart,)


@app.cell
def __(data, mo, alt):
    # Adaptation budget chart
    budget_chart = (
        alt.Chart(data.to_pandas())
        .mark_bar(color="#27ae60")
        .encode(
            x=alt.X("year:O", title="Year"),
            y=alt.Y("adaptation_budget_million:Q", title="Budget (€ Million)"),
        )
        .properties(title="Climate Adaptation Budget")
    )

    mo.ui.altair_chart(budget_chart)
    return (budget_chart,)


@app.cell
def __(data, mo):
    # Calculate statistics
    latest = data.row(-1, named=True)
    avg_temp_increase = round(data["avg_temp_c"][-1] - data["avg_temp_c"][0], 1)

    mo.md(f"""
    ### Key Insights

    - **Temperature increase (2015–2024):** +{avg_temp_increase} °C  
    - **Heatwave days in 2024:** {latest['heatwave_days']} days  
    - **Current adaptation budget:** €{latest['adaptation_budget_million']} M
    """)
    return avg_temp_increase, latest


if __name__ == "__main__":
    app.run()
