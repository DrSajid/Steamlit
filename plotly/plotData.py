from loadData import *
import plotly.graph_objects as go
import plotly.express as px
import plotly.subplots as make_subplots


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


def Scatter_Plot():
    fig = px.scatter(
        df,
        x="age",
        y="secs_elapsed",
        color="month_name_account_created",
        size="secs_elapsed",
        hover_data=["day_account_created"],
        width=900,
        height=600,
        color_discrete_sequence=px.colors.sequential.Agsunset,
        category_orders={
            "month_name_account_created": [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December",
            ]
        },
    )
    st.plotly_chart(fig)


def Scatter_with_Columans():
    fig = px.scatter(
        df,
        x="age",
        y="secs_elapsed",
        color="month_name_account_created",
        size="secs_elapsed",
        hover_data=["day_account_created"],
        facet_col="signup_method",
        width=900,
        height=600,
        color_discrete_sequence=px.colors.sequential.Agsunset,
        category_orders={
            "month_name_account_created": [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December",
            ]
        },
    )
    st.plotly_chart(fig)


def LinePlot():
    dff = df.groupby("dayofyear_account_created")["user_id"].count().reset_index()
    dff.columns = ["Day of Year", "Number of Accounts"]
    fig = px.line(dff, x="Day of Year", y="Number of Accounts", width=700)
    st.plotly_chart(fig)


def Bar_plot():
    dff = df.groupby("device_type")["secs_elapsed"].sum().reset_index()
    fig = px.bar(
        dff,
        x="device_type",
        y="secs_elapsed",
        title="Seconds vs device type",
        color="device_type",
        width=1000,
        height=700,
        color_discrete_sequence=px.colors.qualitative.G10,
    )
    st.plotly_chart(fig)


def Stack_Barchar():
    dff = (
        df.groupby(["device_type", "signup_method"])["secs_elapsed"].sum().reset_index()
    )
    fig = px.bar(
        dff,
        x="device_type",
        y="secs_elapsed",
        title="Secs vs device type",
        color="signup_method",
        color_discrete_sequence=px.colors.qualitative.D3,
        width=900,
        height=700,
    )
    st.plotly_chart(fig)


def Animate():
    fig = px.scatter(
        df,
        x="age",
        y="secs_elapsed",
        color="signup_method",
        animation_frame="month_name_account_created",
        size_max=40,
        size="secs_elapsed",
        hover_data=["day_account_created"],
        width=900,
        height=600,
        color_discrete_sequence=px.colors.sequential.Agsunset,
        category_orders={
            "month_name_account_created": [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December",
            ]
        },
    )
    st.plotly_chart(fig)


def Subplots():
    dff = df.groupby("signup_method")["secs_elapsed"].sum().reset_index()
    fig = make_subplots.make_subplots(rows=1, cols=2)
    fig.add_trace(
        go.Bar(
            x=dff["signup_method"],
            y=df["secs_elapsed"],
            marker=dict(color="SkyBlue"),
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Bar(
            x=dff["signup_method"],
            y=df["secs_elapsed"],
            marker=dict(color="red"),
        ),
        row=1,
        col=2,
    )
    st.plotly_chart(fig)
