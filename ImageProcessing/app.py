import streamlit as st
from PIL import Image
import PIL
import matplotlib.pyplot as plt
from PIL import ImageFilter, ImageEnhance


image = Image.open("../../data/birds.jpg")


fig = plt.figure()


def ploting():
    plt.imshow(image)
    plt.axis("off")
    st.pyplot(fig)


options = st.selectbox(
    "Select the processing option",
    [
        "Show Image",
        "rotate Image",
        "Create Thumbnail",
        "Crop Image",
        "Merging",
        "flipLR",
        "flip270",
        "Black and White",
        "Filter sharper",
        "Filter edge",
        "Contrast Image",
    ],
)


if options == "Show Image":
    image = Image.open("../../data/birds.jpg")
    ploting()

elif options == "rotate Image":
    image = image.rotate(180)
    ploting()

elif options == "create Thumbnails":
    size = 50, 50
    image.thumbnail(size, resample=PIL.Image.NEAREST)
    image.save("thumbnail.png")
    plt.grid("both")
    ploting()

elif options == "Crop Image":
    box = (50, 100, 200, 200)
    image = image.crop(box)
    ploting()

elif options == "Merging":
    position = (0, 300)
    logo = Image.open("../../data/icon.png")
    image.paste(logo, position, logo)
    ploting()

elif options == "flipLR":
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    ploting()

elif options == "flip270":
    image = image.transpose(Image.ROTATE_270)
    ploting()

elif options == "Black and White":
    image = image.convert("1")
    ploting()
elif options == "Filter sharper":
    image = image.filter(ImageFilter.SHARPEN)
    ploting()
elif options == "Filter edge":
    image = image.filter(ImageFilter.EDGE_ENHANCE)
    ploting()
elif options == "Contrast Image":
    image = ImageEnhance.Contrast(image).enhance(1.2)
    ploting()
