import streamlit as st
import numpy as np
from PIL import Image
import io
import sys

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
        st.warning("Cannot display puzzle image. Please ensure 'misteri.png' is at the correct location.")
        return 

    st.subheader("Kode Referensi")
    reference_code = """
import numpy as np
from PIL import Image

# Pastikan path file gambar sudah benar
image_path = 'sample.jpg'
image = Image.open(image_path)
image_array = np.array(image)

# Ubah bentuk array menjadi daftar piksel (N, 3)
pixels = image_array.reshape(-1, 3)

# Hitung frekuensi setiap warna unik
unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)

# Temukan warna dengan frekuensi paling sedikit
rare_pixel = unique_colors[np.argmin(counts)]
print(f"Piksel anomali bernilai: {rare_pixel}")

# Temukan koordinat piksel tersebut
coords = np.argwhere(np.all(image_array == rare_pixel, axis=-1))
print(f"Koordinat: {coords[0]}")
"""
    st.code(reference_code, language='python')
    st.divider()

    st.subheader("Kanvas Kode Anda")
    st.markdown("Tulis dan jalankan kode Python Anda di sini untuk menganalisis gambar.")
    user_code_placeholder = """
# Tips: Anda bisa menggunakan kode referensi di atas sebagai permulaan.
# Pastikan path file gambar sudah benar dalam kode Anda.

from PIL import Image
import numpy as np

image_path = 'sample.jpg'
# Tulis sisa kode Anda di sini...

"""
    user_code = st.text_area("Kode Python:", value=user_code_placeholder, height=250)

    if st.button("Jalankan Kode"):
        if user_code:
            output_capture = io.StringIO()
            sys.stdout = output_capture
            try:
                exec(user_code, {'__name__': '__main__'})
            except Exception as e:
                st.error(f"Terjadi kesalahan saat menjalankan kode:\n{e}")
            finally:
                sys.stdout = sys.__stdout__ 
                output = output_capture.getvalue()
                st.subheader("Hasil Output:")
                if output:
                    st.code(output, language='text')
                else:
                    st.info("Kode berjalan tanpa menghasilkan output ke konsol.")
        else:
            st.warning("Kotak kode kosong. Silakan masukkan kode untuk dijalankan.")
    st.divider()

    st.subheader("Submit Puzzle Answer")
    st.info("""
    **Contoh Format Jawaban:**
    - Jika output kode Anda menemukan piksel anomali dengan nilai `[123 45 200]`.
    - Maka input yang harus dimasukkan adalah: `12345200`
    *(Semua spasi dan kurung siku dihilangkan)*.
    """)
    user_pixel_value = st.text_input("Nilai Piksel").replace(' ', '').replace('[','').replace(']','')

    if st.button("Kirim Jawaban Piksel"):
        correct_value = "12345200"
        if user_pixel_value == correct_value:
            st.session_state.step2_pixel_puzzle_solved = True
            st.success("Tepat! Kunci parsial telah didapatkan.")
        else:
            st.error("Nilai piksel salah. Coba periksa kembali representasi matriksnya.")
    st.divider()
    
    if st.session_state.get("step2_pixel_puzzle_solved", False):
        if st.button("Lanjut Membuka Poneglyph Kedua"):
            st.session_state.stage = 3
            st.rerun()
