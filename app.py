import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import base64

st.set_page_config(layout="wide")
st.title("Canvas Background Test")

# --- Load the local test image ---
try:
    TEST_IMAGE_PATH = "test_image.png"
    pil_image = Image.open(TEST_IMAGE_PATH)
    with open(TEST_IMAGE_PATH, "rb") as f:
        img_bytes = f.read()
except FileNotFoundError:
    st.error("Could not find 'test_image.png'. Please make sure it's in the same folder as app.py.")
    st.stop()

# --- Display settings ---
width = st.slider("Canvas Width", 200, 1000, 700)
height = int(pil_image.height * (width / pil_image.width))
st.write(f"Canvas dimensions: {width}px x {height}px")

st.divider()

# --- METHOD 1: Using the `background_image` parameter ---
st.header("Method 1: The `background_image` Parameter")
st.info("This canvas uses the library's built-in background_image feature.")

st_canvas(
    background_image=pil_image,
    width=width,
    height=height,
    key="canvas_method_1"
)

st.divider()

# --- METHOD 2: Using the CSS background workaround ---
st.header("Method 2: The CSS Background Workaround")
st.info("This canvas uses a CSS background, bypassing the library feature.")

b64_string = base64.b64encode(img_bytes).decode()
st.markdown(f"""
<style>
.css-canvas-container {{
    background-image: url("data:image/png;base64,{b64_string}");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    border: 1px solid #eee;
}}
</style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="css-canvas-container">', unsafe_allow_html=True)
    st_canvas(
        background_color="rgba(0,0,0,0)",
        width=width,
        height=height,
        key="canvas_method_2"
    )
    st.markdown('</div>', unsafe_allow_html=True)
