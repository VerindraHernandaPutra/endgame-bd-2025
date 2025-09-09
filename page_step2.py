import streamlit as st
from PIL import Image
import io
import sys
import time
from utils import reset_progress
import numpy as np # Ensure numpy import for exec scope

def show_step_2():
    st.header("Step 2: The Elbaph Trial - Pixel Puzzle")
    st.markdown("You have arrived at Pulau Elbaph. To unlock the Poneglyph Kedua, you must first solve this technical puzzle.")
    st.divider()

    st.subheader("Teka-Teki Pixel Puzzle")
    st.markdown("Analyze the image below. Your task is to write Python code to find the anomalous pixel value.")

    try:
        image_path = 'sample.jpg'
        image = Image.open(image_path)
        st.image(image, caption="Poneglyph Terkunci", width=300)
    except FileNotFoundError:
        st.error(f"Image file not found at path: {image_path}")
        st.warning("Cannot display puzzle image. Please ensure the image file is in the correct directory.")
        return

    st.subheader("Kode Referensi")
    reference_code = """
import numpy as np
from PIL import Image

image_path = 'sample.jpg'
image = Image.open(image_path)
image_array = np.array(image)
pixels = image_array.reshape(-1, 3)
unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)
rare_pixel = unique_colors[np.argmin(counts)]
print(f"Piksel anomali bernilai: {rare_pixel}")
coords = np.argwhere(np.all(image_array == rare_pixel, axis=-1))
print(f"Koordinat: {coords[0]}")
"""
    st.code(reference_code, language='python')
    st.divider()

    st.subheader("Kanvas Kode Anda")
    user_code_placeholder = """from PIL import Image
import numpy as np

image_path = 'sample.jpg'
# Tulis sisa kode Anda di sini...
# image = Image.open(image_path)
# print("Hello World")
"""
    user_code = st.text_area("Kode Python:", value=user_code_placeholder, height=250)

    # --- Code Execution Logic ---
    if st.button("Jalankan Kode"):
        if user_code:
            output_capture = io.StringIO()
            sys.stdout = output_capture
            try:
                # Prepare global scope for exec to work with libraries like PIL, numpy
                exec_globals = {
                    "Image": Image,
                    "np": np,
                    "__name__": "__main__"
                }
                exec(user_code, exec_globals)
            except FileNotFoundError:
                 st.error(f"File not found. Pastikan path file ('{image_path}') sudah benar di dalam kode Anda.")
            except Exception as e:
                st.error(f"Terjadi kesalahan saat menjalankan kode:\n{type(e).__name__}: {e}")
            finally:
                sys.stdout = sys.__stdout__  # Restore standard output
                output = output_capture.getvalue()
                st.subheader("Hasil Output:")
                if output:
                    st.code(output, language='text')
                else:
                    st.info("Kode berjalan tanpa menghasilkan output ke konsol.")
        else:
            st.warning("Kotak kode kosong. Silakan masukkan kode untuk dijalankan.")

    st.divider()

    # --- Answer Submission Section ---
    st.subheader("Submit Puzzle Answer")
    st.info("""
    **Contoh Format Jawaban:**
    - Jika output kode Anda menemukan piksel anomali dengan nilai `[123 45 200]`.
    - Maka input yang harus dimasukkan adalah: `12345200`
    """)
    user_pixel_value = st.text_input("Nilai Piksel").replace(' ', '').replace('[','').replace(']','')

    if st.button("Kirim Jawaban Piksel"):
        correct_value = "12345200"
        if user_pixel_value == correct_value:
            st.session_state.step2_pixel_puzzle_solved = True
            st.success("Tepat! Kunci parsial telah didapatkan.")
        else:
            st.error("Nilai piksel salah. Teka-teki menolakmu! Kembali ke awal.")
            time.sleep(2)
            reset_progress()
            st.rerun()

    st.divider()
    if st.session_state.get("step2_pixel_puzzle_solved", False):
        if st.button("Lanjut Membuka Poneglyph Kedua"):
            st.session_state.stage = 3
            st.rerun()