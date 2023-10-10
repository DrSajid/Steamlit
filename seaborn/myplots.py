import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

from dataload import *

sns.set_palette("deep")
sns.set_style("darkgrid")


def show_data():
    st.write(df.head(10))


def count_plot():
    fig = plt.figure(figsize=(8, 6))
    plt.title("Prefix Countplot")
    plt.xticks(rotation=60, fontsize=12)
    sns.countplot(x="teacher_prefix", hue="project_is_approved", data=df)
    st.pyplot(fig)


def violin_strip():
    plot = st.selectbox("Please Select the Plot", ["Violen plot", "Strip plot"])

    ca = df[df["school_state"] == "CA"]
    fig = plt.figure(figsize=(8, 6))
    if plot == "Violen plot":
        sns.violinplot(
            x="teacher_prefix",
            y="teacher_number_of_previously_posted_projects",
            data=ca,
        )
        plt.title("Violen plot")
    elif plot == "Strip plot":
        hue_order = [
            "Saturday",
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
        ]
        sns.stripplot(
            x="teacher_prefix",
            y="teacher_number_of_previously_posted_projects",
            data=ca,
            hue="day",
            hue_order=hue_order,
            dodge=True,
            palette="Set2",
        )
        plt.title("Violen plot")
    st.pyplot(fig)


def barplot():
    dff = (
        df.groupby("school_state")["teacher_number_of_previously_posted_projects"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .head(15)
    )
    fig = plt.figure(figsize=(8, 6))

    orientation = st.selectbox(
        "Please select the plot", ["data", "Vertical", "Horizontal"]
    )

    if orientation == "data":
        st.write(dff)
    elif orientation == "Vertical":
        sns.barplot(
            x="school_state", y="teacher_number_of_previously_posted_projects", data=dff
        )
        st.pyplot(fig)
    elif orientation == "Horizontal":
        sns.barplot(
            y="school_state", x="teacher_number_of_previously_posted_projects", data=dff
        )
        st.pyplot(fig)


def linePlot():
    dff = (
        df.groupby("project_submitted_date")[
            "teacher_number_of_previously_posted_projects"
        ]
        .sum()
        .reset_index()
    )
    dff["project_submitted_date"] = pd.to_datetime(dff["project_submitted_date"])
    fig = plt.figure(figsize=(12, 6))
    sns.lineplot(
        x="project_submitted_date",
        y="teacher_number_of_previously_posted_projects",
        data=dff,
        color="r",
    )
    st.pyplot(fig)


def Subplots():
    dff = (
        df.groupby("school_state")["teacher_number_of_previously_posted_projects"]
        .sum()
        .sort_values(ascending=True)
        .reset_index()
        .head(15)
    )
    fig = plt.figure(figsize=(15, 8))
    plt.subplot(1, 2, 1)
    sns.barplot(
        x="school_state", y="teacher_number_of_previously_posted_projects", data=dff
    )

    plt.subplot(1, 2, 2)
    sns.countplot(x="teacher_prefix", hue="project_is_approved", data=df)
    st.pyplot(fig)


def FigureAxes():
    dff = (
        df.groupby("school_state")["teacher_number_of_previously_posted_projects"]
        .sum()
        .sort_values(ascending=True)
        .reset_index()
        .head(15)
    )
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 8))

    sns.barplot(
        x="school_state",
        y="teacher_number_of_previously_posted_projects",
        data=dff,
        ax=ax[0],
    )

    sns.countplot(x="teacher_prefix", hue="project_is_approved", data=df, ax=ax[1])
    st.pyplot(fig)
