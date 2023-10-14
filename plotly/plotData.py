from loadData import *
import plotly.graph_objects as go
import plotly.express as px


def ShowData():
    st.write(df.head(10))
    dff = df.groupby("signup_method")["secs_elapsed"].sum().reset_index()
    st.write("After grouping w.r.t singup_method of secs_elapsed")
    st.write(dff.head(10))


def pieChart():
    dff = df.groupby("signup_method")["secs_elapsed"].sum().reset_index()
    label = dff["signup_method"]
    values = dff["secs_elapsed"]
    colors = ["maroon", "black", "orange"]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=label, values=values, hoverinfo="label+percent", textinfo="value"
            )
        ]
    )
    fig.update_traces(marker=dict(colors=colors))
    st.plotly_chart(fig)


def Donut_Chart():
    dff = df.groupby("device_type")["secs_elapsed"].sum().reset_index()
    label = dff["device_type"]
    values = dff["secs_elapsed"]
    # colors = ["maroon", "black", "orange"]

    fig = px.pie(
        dff,
        hole=0.2,
        values="secs_elapsed",
        names="device_type",
        color_discrete_sequence=px.colors.sequential.Cividis,
    )
    st.plotly_chart(fig)
