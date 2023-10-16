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
