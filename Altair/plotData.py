from loadData import *


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


def Scatter_Matrics():
    chart = (
        alt.Chart(df)
        .mark_circle()
        .encode(
            alt.X(alt.repeat("column"), type="quantitative"),
            alt.Y(alt.repeat("row"), type="quantitative"),
            color="published_day",
        )
        .properties(width=150, height=150)
        .repeat(
            row=["duration", "views", "comments"],
            column=["comments", "views", "duration"],
        )
        .interactive()
    )
    st.altair_chart(chart)


def ScatterPlot_links():
    chart = (
        alt.Chart(df)
        .mark_point()
        .encode(
            x="duration",
            y="comments",
            color="published_month",
            href="url:N",
            tooltip=["event", "url:N"],
        )
        .interactive()
        .properties(width=650, height=500)
        .configure_legend(
            strokeColor="Xea4663",
            fillColor="#EEEEEE",
            padding=10,
            cornerRadius=10,
            orient="top-right",
        )
    )
    st.altair_chart(chart)


def HeatMap():
    chart = (
        alt.Chart(df)
        .mark_rect()
        .encode(
            x="published_year:O",
            y="published_day",
            color="languages",
            tooltip=["languages", "published_day"],
        )
        .interactive()
        .properties(width=650, height=500)
    )
    st.altair_chart(chart)


def BarChart_H():
    bar_data = df.sort_values(by="views", ascending=False)
    bar_data = bar_data.head(20)

    chart = (
        alt.Chart(bar_data)
        .mark_bar()
        .encode(x="views", y="event", href="url:N")
        .properties(width=650, height=500)
        .interactive()
    )

    st.altair_chart(chart)


def GroupBartChart():
    dff = df[(df["published_day"] == "Monday") | (df["published_day"] == "Tuesday")]
    toggle = st.checkbox("Toggle Horizontal")
    if toggle:
        chart = (
            alt.Chart(dff)
            .mark_bar()
            .encode(
                x="published_year:O",
                y=alt.Y("sum(views):Q", title="Sum of Views"),
                color="published_year:N",
                column="published_day",
            )
            .properties(width=650, height=500)
        )
    else:
        chart = (
            alt.Chart(dff)
            .mark_bar()
            .encode(
                y="published_year:O",
                x=alt.Y("sum(views):Q", title="Sum of Views"),
                color="published_year:N",
                column="published_day",
            )
            .properties(width=650, height=500)
        )

    st.altair_chart(chart)


def StackedBarChart():
    toggle = st.checkbox("Horizontal display")

    if toggle:
        chart = (
            alt.Chart(df)
            .mark_bar()
            .encode(
                y="published_year:O",
                x=alt.X("sum(views)"),
                color="published_day",
                tooltip=["sum(views)"],
            )
            .properties(width=650, height=500)
            .interactive()
        )
    else:
        chart = (
            alt.Chart(df)
            .mark_bar()
            .encode(
                x="published_year:O",
                y=alt.Y("sum(views)"),
                color="published_day",
                tooltip=["sum(views)"],
            )
            .properties(width=650, height=500)
            .interactive()
        )
    st.altair_chart(chart)


def Normalized_StackedBarChart():
    toggle = st.checkbox("toggle direction")
    if toggle:
        chart = (
            alt.Chart(df)
            .mark_bar()
            .encode(
                x=alt.X("mean(views)", stack="normalize"),
                y="published_year:O",
                color="published_day",
                tooltip=["mean(views)", "published_day"],
            )
            .properties(width=650, height=500)
            .interactive()
        )
    else:
        chart = (
            alt.Chart(df)
            .mark_bar()
            .encode(
                y=alt.Y("mean(views)", stack="normalize"),
                x="published_year:O",
                color="published_day",
                tooltip=["mean(views)", "published_day"],
            )
            .properties(width=650, height=500)
            .interactive()
        )
    st.altair_chart(chart)


def Normalized_SBarChart_text():
    text = (
        alt.Chart(df)
        .mark_text(dx=-10, color="white")
        .encode(
            x=alt.X("sum(num_speaker):Q", stack="normalize"),
            y="published_year:O",
            detail="published_day",
            text=alt.Text("sum(num_speaker):Q", format=".1f"),
        )
    )
    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X("sum(num_speaker):Q", stack="normalize"),
            y="published_year:O",
            color="published_day",
            tooltip=["sum(num_speaker):Q", "published_day"],
        )
        .properties(width=650, height=500)
        .interactive()
    )
    st.altair_chart(chart + text)
