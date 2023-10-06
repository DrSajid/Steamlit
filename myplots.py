import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from mydata import *


def bar_chart():
  fig = plt.figure(figsize=(12,5))
  plt.xticks(rotation=70)
  bar_data = df.sort_values(by='views', ascending=False)
  bar_data = bar_data.head(20)
  plt.ticklabel_format(style="plain")
  plt.bar(bar_data['event'], bar_data['views'])
  plt.xlabel("Event")
  plt.ylabel("Views")
  plt.title("Events & View plot")
  st.pyplot(fig)

def horizontal_bar():
  fig = plt.figure(figsize=(12,5))
  plt.xticks(rotation=70)
  bar_data = df.sort_values(by='views', ascending=False)
  bar_data = bar_data.head(20)
  plt.ticklabel_format(style="plain")
  plt.barh(bar_data['event'], bar_data['views'])
  plt.ylabel("Event")
  plt.xlabel("Views")
  plt.title("Events & View plot")
  st.pyplot(fig)

def visualize_scatter():
  fig = plt.figure(figsize=[10,8])
  plt.scatter(
    x = df["comments"],
    y=df["views"],
    marker='*',
    s=df['comments']/20,
    c=df['languages'],
  )
  plt.xlabel("comments")
  plt.ylabel('Views')
  st.pyplot(fig)

def histogram():
  fig = plt.figure(figsize=[10,8])
  plt.hist(df["languages"], color='y', bins=50)
  plt.xlabel("Languages")
  plt.ylabel("counts")
  st.pyplot(fig)

def pie_chart():
  explode = (.1,0,0,0,0,0,0)
  days_data = (
    df.groupby("published_day")["views"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
  )
  fig = plt.figure(figsize=[10,8])
  plt.pie(
    days_data['views'],
    labels=days_data['published_day'],
    shadow=True,
    explode=explode,
    autopct="%1.1f%%"
  )
  plt.xlabel("Languages")
  plt.ylabel("counts")
  st.pyplot(fig)

def two_subplots():
  fig = plt.figure(figsize=[15,10])
  plt.subplot(1,2,1)
  bar_data = df.sort_values(by='views', ascending=False)
  bar_data = bar_data.head(20)
  plt.barh(bar_data['event'], bar_data['views'])
  
  plt.subplot(1,2,2)
  plt.scatter(
  x = df["comments"],
  y=df["views"],
  marker='*',
  s=df['comments']/20,
  c=df['languages'],
  )

  st.pyplot(fig)

def Four_subplots():
  fig = plt.figure(figsize=[15,10])
  plt.subplot(2,2,1)
  days_data = (
    df.groupby("published_day")["views"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
  )
  plt.pie(
    days_data['views'],
    labels=days_data['published_day'],
    shadow=True,
    explode=(.1,0,0,0,0,0,0),
    autopct="%1.1f%%"
  )

  plt.subplot(2,2,2)
  month_data = (
    df.groupby("published_month")["views"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
  )
  plt.pie(
    month_data['views'],
    labels=month_data['published_month'],
    shadow=True,
    explode=(.1,0,0,0,0,0,0,0,0,0,0,0),
    autopct="%1.1f%%"
  )

  plt.subplot(2,2,3)
  bar_data = df.sort_values(by='views', ascending=False)
  bar_data = bar_data.head(20)
  plt.xticks(rotation=70)
  plt.ticklabel_format(style="plain")
  plt.bar(bar_data['event'], bar_data['views'])

  plt.subplot(2,2,4)
  views = df.groupby("published_year")["views"].sum().reset_index()
  plt.plot(views["published_year"], views["views"])

  st.pyplot(fig)

def Four_Axes():
  fig, ax = plt.subplots(2,2,figsize=[15,10])
  # plt.subplot(2,2,1)
  days_data = (
    df.groupby("published_day")["views"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
  )
  ax[0,0].pie(
    days_data['views'],
    labels=days_data['published_day'],
    shadow=True,
    explode=(.1,0,0,0,0,0,0),
    autopct="%1.1f%%"
  )

  # # plt.subplot(2,2,2)
  month_data = (
    df.groupby("published_month")["views"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
  )
  ax[0,1].pie(
    month_data['views'],
    labels=month_data['published_month'],
    shadow=True,
    explode=(.1,0,0,0,0,0,0,0,0,0,0,0),
    autopct="%1.1f%%"
  )

  # plt.subplot(2,2,3)
  bar_data = df.sort_values(by='views', ascending=False)
  bar_data = bar_data.head(20)
  ax[1,0].ticklabel_format(style="plain")
  ax[1,0].bar(bar_data['event'], bar_data['views'])

  # plt.subplot(2,2,4)
  views = df.groupby("published_year")["views"].sum().reset_index()
  ax[1,1].plot(views["published_year"], views["views"])

  st.pyplot(fig)