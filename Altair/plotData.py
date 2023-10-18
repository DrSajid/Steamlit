from loadData import *
import altair as alt


def vegalite():
    st.vega_lite_chart(
        df,
        {
            "mark": {"type": "circle", "tooltip": True},
            "width": 650,
            "height": 500,
            "encoding": {
                "x": {"field": "duration", "type": "quantitative"},
                "y": {"field": "views", "type": "quantitative"},
                "size": {"field": "languages", "type": "quantitative"},
                "color": {"field": "languages", "type": "quantitative"},
            },
        },
    )


def LinePlot():
    df_copy = df.copy()
    # df_copy = df_copy[(df_copy["film_year"] == 1999)]
    #     (df_copy["film_year"] == 1999)
    #     | (df_copy["film_year"] == 2000)
    #     | (df_copy["film_year"] == 2021)
    # ]
    df_copy = df_copy[
        (df_copy["film_year"] == 1996)
        | (df_copy["film_year"] == 1997)
        | (df_copy["film_year"] == 1998)
        | (df_copy["film_year"] == 1999)
        | (df_copy["film_year"] == 2000)
        | (df_copy["film_year"] == 2001)
        | (df_copy["film_year"] == 2002)
        | (df_copy["film_year"] == 2003)
        | (df_copy["film_year"] == 2004)
        | (df_copy["film_year"] == 2005)
        | (df_copy["film_year"] == 2006)
    ]
    # st.write(df_copy)
    df_copy["film_date"] = pd.to_datetime(df_copy["film_date"])

    line = (
        alt.Chart(df_copy)
        .mark_line()
        .encode(x="film_date", y="views")
        .properties(width=650, height=500)
        .interactive()
    )

    st.altair_chart(line)


def BarChart():
    bar_data = df.sort_values(by="views", ascending=False)
    bar_data = bar_data.head(20)

    sort = st.checkbox("Sort", value=False, help="Sort data")

    if sort:
        chart = (
            alt.Chart(bar_data)
            .mark_bar()
            .encode(x=alt.X("event:N", sort="-y"), y="views")
            .properties(width=650, height=500)
            .interactive()
        )
    else:
        chart = (
            alt.Chart(bar_data)
            .mark_bar()
            .encode(x="event", y="views")
            .properties(width=650, height=500)
            .interactive()
        )
    st.altair_chart(chart)


def Scatter_plot():
    toggle = st.checkbox(
        "Toggle background", value=False, help="will change background"
    )
    if toggle:
        chart = (
            alt.Chart(df, background="maroon")
            .mark_point()
            .encode(
                x="duration",
                y="views",
                size="languages",
                color="languages",
                tooltip=["duration", "views", "comments", "languages"],
            )
            .properties(width=650, height=500)
            .interactive()
        )
    else:
        chart = (
            alt.Chart(df)
            .mark_point()
            .encode(
                x="duration",
                y="views",
                size="languages",
                color="languages",
                tooltip=["duration", "views", "comments", "languages"],
            )
            .properties(width=650, height=500)
            .interactive()
        )
    st.altair_chart(chart)


def Area_plot():
    df_copy = df[df["film_year"] == 2012]
    df_copy["film_date"] = pd.to_datetime(df_copy["film_date"])

    radio_button = st.radio("With or without line", ("line", "without line"))

    if radio_button == "line":
        chart = (
            alt.Chart(df_copy)
            .mark_area(color="maroon", line=True)
            .encode(x="film_date", y="views")
            .properties(width=650, height=500)
            .interactive()
        )
    else:
        chart = (
            alt.Chart(df_copy)
            .mark_area(color="maroon", line=False)
            .encode(x="film_date", y="views")
            .properties(width=650, height=500)
            .interactive()
        )

    st.altair_chart(chart)
