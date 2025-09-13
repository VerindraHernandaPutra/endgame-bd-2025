import streamlit as st
from utils import load_data_step3, reset_progress
import time

# --- Definisi Dialog Intro ---
@st.dialog("Pulau Terakhir", width="large")
def intro_dialog_1():
    st.image("assets/images/page3_awal_part1.png", use_container_width=True)
    if st.button("Hampir Sampai..."):
        st.session_state.step3_intro_slide = 2
        st.rerun()

@st.dialog("Poneglyph Final", width="large")
def intro_dialog_2():
    st.image("assets/images/page3_awal_part2.png", use_container_width=True)
    if st.button("Lihat Petunjuknya..."):
        st.session_state.step3_intro_slide = 3
        st.rerun()

@st.dialog("Memulai Teka-Teki Terakhir", width="large")
def intro_dialog_3():
    st.image("assets/images/page3_awal_part3.png", use_container_width=True)
    if st.button("Pecahkan Teka-Teki Terakhir"):
        st.session_state.step3_intro_slide = 0  # Selesaikan intro
        st.rerun()

# --- Definisi Dialog Outro ---
@st.dialog("Tebakan Benar!", width="large")
def outro_dialog_1():
    st.image("assets/images/page3_akhir_part1.png", use_container_width=True)
    if st.button("Lanjutkan..."):
        st.session_state.step3_outro_slide = 2
        st.rerun()

@st.dialog("One Piece!", width="large")
def outro_dialog_2():
    st.image("assets/images/page3_akhir_part2.png", use_container_width=True)
    if st.button("Lanjutkan..."):
        st.session_state.step3_outro_slide = 3
        st.rerun()

@st.dialog("Raja Bajak Laut", width="large")
def outro_dialog_3():
    st.image("assets/images/page3_akhir_part3.png", use_container_width=True)
    if st.button("Buka Matamu..."):
        st.session_state.step3_outro_slide = 0 # Selesaikan outro
        st.session_state.stage = 5              # Lanjut ke halaman kemenangan
        st.rerun()

# --- Fungsi Utama Halaman ---
def show_step_3():
    # Page Guard
    if not st.session_state.get("step2_island_guess_correct", False):
        st.error("Anda harus menyelesaikan teka-teki sebelumnya terlebih dahulu.")
        return

    # Router internal
    intro_slide = st.session_state.get("step3_intro_slide", 1)
    outro_slide = st.session_state.get("step3_outro_slide", 0)

    if intro_slide == 1:
        intro_dialog_1()
    elif intro_slide == 2:
        intro_dialog_2()
    elif intro_slide == 3:
        intro_dialog_3()
    elif outro_slide == 1:
        outro_dialog_1()
    elif outro_slide == 2:
        outro_dialog_2()
    elif outro_slide == 3:
        outro_dialog_3()
    else:
        # --- Konten Puzzle Utama ---
        st.header("Final: Teka-Teki Poneglyph Terakhir")
        st.markdown("Selamat datang di **Laugh Tale**! Untuk menemukan One Piece, Anda harus menerjemahkan pesan terakhir yang terukir di sini. Sebelum melangkah lebih jauh, bacalah [arahan](https://docs.google.com/document/d/e/2PACX-1vR-C5PEw7-63IG2qe0tuljWuPdRxv04puZBbKBhoXz_a7L8lFokXIpeazSmfQ9nowma_nycFAGgN_gY/pub) yang akan menuntunmu memecahkan teka-teki terakhir ini.")
        st.divider()

        # --- Deskripsi Puzzle & Petunjuk Pengerjaan BARU ---
        st.subheader("Petunjuk Pengerjaan")
        st.info("""
        Tugas Anda adalah menemukan frasa kunci rahasia yang tersembunyi dalam catatan kuno. Ikuti langkah-langkah berikut:

        1.  **Cari Anomali:** Periksa dataset di bawah. Temukan satu emoji yang unik (anomali) dari masing-masing `Label`.
        2.  **Urutkan Emoji:** Setelah 5 emoji terkumpul, susun dalam urutan berikut: **Joy > Sadness > Anger > Fear > Neutral**.
        3.  **Terjemahkan Emoji:** Gunakan kamus emoji resmi di [Link Ini](https://www.youtube.com/watch?v=xvFZjo5PgG0&list=RDxvFZjo5PgG0&start_radio=1) untuk menerjemahkan setiap emoji dalam urutan yang benar ke dalam bahasa Inggris.
        4.  **Susun Jawaban:** Gabungkan hasil terjemahan kata per kata (dipisahkan spasi) dan masukkan sebagai jawaban akhir.
        """)
        st.divider()

        # DATASET
        st.subheader("Catatan Kuno")
        placeholder_df = load_data_step3()
        if not placeholder_df.empty:
            st.dataframe(placeholder_df)
        st.divider()

        # CONTOH JAWABAN (TETAP ADA)
        st.subheader("Contoh Cara Menjawab (Ini Bukan Jawaban Sebenarnya)")
        st.markdown("Bayangkan Anda telah menemukan dan menyusun emoji berikut:")
        col1, col2, col3 = st.columns(3)
        col1.markdown("<h2 style='text-align: center;'>🍊</h2>", unsafe_allow_html=True)
        col2.markdown("<h2 style='text-align: center;'>🚬</h2>", unsafe_allow_html=True)
        col3.markdown("<h2 style='text-align: center;'>🤥</h2>", unsafe_allow_html=True)
        st.warning(
        "Setelah emoji tersusun, terjemahkan menjadi kata-kata (misal: **'tangerine cigarette lying face'**). Frasa inilah yang dimasukkan sebagai jawaban."
        )
        st.divider()
        
        # INPUT JAWABAN
        st.subheader("Kunci Final One Piece")
        st.markdown("**Masukkan frasa rahasia yang sudah Anda pecahkan:**")
        user_answer = st.text_input("Frasa Kunci Rahasia").lower()

        if st.button("Tebak"):
            CORRECT_PHRASE = "smiling face with hearts money-mouth face hot face confused face weary cat"
            if user_answer.strip() == CORRECT_PHRASE:
                st.session_state.step3_final_puzzle_solved = True
                st.session_state.step3_outro_slide = 1
                st.rerun()
            else:
                st.error("Frasa yang Anda masukkan salah! Poneglyph mereset dirinya dan Anda terlempar kembali ke awal.")
                time.sleep(3)
                reset_progress()
                st.rerun()