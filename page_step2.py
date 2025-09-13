import streamlit as st
from PIL import Image
import io
import sys
import time
from utils import reset_progress
import numpy as np

# --- Definisi Dialog Intro untuk Step 2 ---
@st.dialog("Pulau Kedua", width="large")
def intro_dialog_1():
    st.image("assets/images/page2_awal_part1.png", use_container_width=True)
    if st.button("Selidiki..."):
        st.session_state.step2_intro_slide = 2
        st.rerun()

@st.dialog("Ukiran Lain", width="large")
def intro_dialog_2():
    st.image("assets/images/page2_awal_part2.png", use_container_width=True)
    if st.button("Periksa Petunjuk..."):
        st.session_state.step2_intro_slide = 3
        st.rerun()

@st.dialog("Hint Puzzle 2", width="large")
def intro_dialog_3():
    st.image("assets/images/page2_awal_part3.png", use_container_width=True)
    if st.button("Mulai Pecahkan Puzzle Pixel"):
        st.session_state.step2_intro_slide = 0  # Selesaikan intro
        st.rerun()

# --- Definisi Dialog Outro untuk Step 2 ---
@st.dialog("Memasukkan Jawaban...", width="large")
def outro_dialog_1():
    st.image("assets/images/page2_akhir_part1.png", use_container_width=True)
    if st.button("Lihat Hasilnya..."):
        st.session_state.step2_outro_slide = 2
        st.rerun()

@st.dialog("Berhasil!", width="large")
def outro_dialog_2():
    st.image("assets/images/page2_akhir_part2.png", use_container_width=True)
    if st.button("Lanjutkan ke Stage 3"):
        st.session_state.step2_outro_slide = 0 # Selesaikan outro
        st.session_state.stage = 3             # Lanjut ke stage puzzle berikutnya
        st.rerun()

# --- Fungsi Utama Halaman ---
def show_step_2():
    # Router internal untuk menampilkan dialog atau puzzle
    intro_slide = st.session_state.get("step2_intro_slide", 1)
    outro_slide = st.session_state.get("step2_outro_slide", 0)

    if intro_slide == 1:
        intro_dialog_1()
    elif intro_slide == 2:
        intro_dialog_2()
    elif intro_slide == 3:
        intro_dialog_3()
    elif outro_slide == 1:
        outro_dialog_1()
    elif outro_slide == 2:
        st.balloons()
        outro_dialog_2()
    else:
        # --- Konten Puzzle Utama ---
        st.header("Step 2: The Elbaf Trial - Pixel Puzzle")
        st.markdown("Selamat datang di Pulau Elbaf. Poneglyph Kedua terkunci di sini, dan untuk membukanya, kamu harus melewati sebuah teka teki pixel puzzle. Di tahap ini, sebuah [arahan](https://docs.google.com/document/d/e/2PACX-1vR24X3fUZw0t2TJvKv7VbX1c1wa-qx_LhgI2M9G00rcpP2-4MAEzSKl50Y0jAHCa5a22fzW4KcwH4AW/pub) telah dipersiapkan untuk menuntunmu menyelesaikan teka-teki mosaik ini.", unsafe_allow_html=True)
        st.divider()

        st.subheader("Teka-Teki Pixel Puzzle")
        try:
            image_path = 'misteri.png'
            image = Image.open(image_path)
            st.image(image, caption="Poneglyph Terkunci [misteri.png]", width=1080)
            st.info("Elbaf tidak seperti yang kamu bayangkan. Bukan hanya besar—ia mengintimidasi. Burung-burung setinggi manusia, akar pohon sebesar kapal. Tapi kamu tidak di sini untuk kekaguman. Kamu mencari **Poneglyph Kedua**. Di kaki air terjun batu, kamu menemukannya. Namun berbeda dari yang pertama, batu ini tampak rusak… sebagian ukiran hancur. Tapi di permukaannya, terukir pola aneh—mosaik pixel? “Ini bukan hanya batu kuno. Ini semacam… kode.” ")
        except FileNotFoundError:
            st.error(f"File gambar '{image_path}' tidak ditemukan.")
            return
        st.divider()

        # PETUNJUK PENGERJAAN | BISA DI GANTI DENGAN DOCS LINK KLO MAU
        st.subheader("Petunjuk Pengerjaan")
        st.markdown("""
        Tulis kode Python pada kanvas di bawah untuk menemukan piksel anomali. Ikuti langkah-langkah berikut:

        **1. Konversi Gambar ke Array NumPy:**
        * **Tugas:** Ubah objek gambar PIL (dimuat dengan `Image.open()`) menjadi array NumPy.
        * **Dokumentasi:** [Pillow Image to NumPy Array Conversion](https://numpy.org/doc/stable/reference/generated/numpy.array.html)

        **2. Ubah Bentuk Array (Reshape):**
        * **Tugas:** Ubah bentuk array dari format 3D `(height, width, channels)` menjadi format 2D `(total_pixels, channels)`. Gunakan `-1` agar NumPy menghitung jumlah total piksel secara otomatis.
        * **Dokumentasi:** [numpy.reshape()](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)

        **3. Hitung Frekuensi Unik:**
        * **Tugas:** Temukan semua warna unik dan hitung frekuensinya. Gunakan parameter `axis=0` untuk membandingkan piksel (baris) secara keseluruhan, bukan nilai individual.
        * **Dokumentasi:** [numpy.unique()](https://numpy.org/doc/stable/reference/generated/numpy.unique.html) (Perhatikan parameter `return_counts=True` and `axis=0`).

        **4. Temukan Indeks Paling Langka:**
        * **Tugas:** Cari indeks dari nilai frekuensi terendah. Piksel langka adalah piksel dengan jumlah kemunculan paling sedikit.
        * **Dokumentasi:** [numpy.argmin()](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html)

        **5. Ambil Nilai Piksel:**
        * **Tugas:** Gunakan indeks dari langkah 4 untuk mengambil nilai RGB dari daftar warna unik yang Anda buat di langkah 3.
        """)
        st.divider()

        st.subheader("Kanvas Kode Anda")
        user_code = st.text_area("Kode Python:", placeholder="Tulis kode analisis Anda di sini...", height=250)
        if st.button("Jalankan Kode"):
            if user_code:
                output_capture = io.StringIO()
                sys.stdout = output_capture
                try:
                    exec_globals = {"Image": Image, "np": np, "__name__": "__main__"}
                    exec(user_code, exec_globals)
                except Exception as e:
                    st.error(f"Terjadi kesalahan saat menjalankan kode:\n{type(e).__name__}: {e}")
                finally:
                    sys.stdout = sys.__stdout__
                    output = output_capture.getvalue()
                    st.subheader("Hasil Output:")
                    if output:
                        st.code(output, language='text')
                    else:
                        st.info("Kode berjalan tanpa menghasilkan output ke konsol.")
        st.divider()
        
        # PETUNJUK TAMBAHAN
        with st.expander("Butuh petunjuk? Masukkan kode unik di sini"):
            st.write("Dapatkan bantuan dari langit dengan mendapatkan kode unik dari asisten Big Data untuk membuka petunjuk.")
            hint_code = st.text_input("Masukkan Kode Unik", type="password")
            if st.button("Buka Petunjuk"):
                CORRECT_HINT_CODE = "admin123"
                if hint_code == CORRECT_HINT_CODE:
                    st.success("Kode Benar! Berikut adalah kode solusi untuk referensi.")
                    solution_code = """
import numpy as np
from PIL import Image

image_path = 'misteri.png'
image = Image.open(image_path)

# 1. Konversi gambar PIL ke NumPy array
image_array = np.array(image)

# 2. Ubah bentuk array
pixels = image_array.reshape(-1, 3)

# 3. Hitung frekuensi setiap warna unik
unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)

# 4. Temukan indeks dari warna yang paling langka
rare_pixel_index = np.argmin(counts)

# 5. Ambil nilai piksel langka
rare_pixel = unique_colors[rare_pixel_index]

print(f"Piksel anomali bernilai: {rare_pixel}")
"""
                    st.code(solution_code, language='python')
                else:
                    st.error("Kode unik salah.")

        st.divider()

        st.subheader("Submit Puzzle Answer")
        st.info("""
        **Contoh Format Jawaban:**
        - Jika output kode Anda menemukan piksel anomali dengan nilai `[111 22 333]`.
        - Maka input yang harus dimasukkan adalah: `11122333`
        """)
        user_pixel_value = st.text_input("Nilai Piksel").replace(' ', '').replace('[','').replace(']','')

        if st.button("Kirim Jawaban Piksel"):
            correct_value = "12345200"
            if user_pixel_value == correct_value:
                st.session_state.step2_pixel_puzzle_solved = True
                st.session_state.step2_outro_slide = 1 # Memulai sekuens outro
                st.rerun()
            else:
                st.error("Nilai piksel salah. Teka-teki menolakmu! Kembali ke awal.")
                time.sleep(2)
                reset_progress()
                st.rerun()