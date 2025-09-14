import streamlit as st
from utils import load_data_step1, PONEGLYPH_1, reset_progress
import time

# --- Definisi Dialog Intro untuk Step 1 ---
@st.dialog("Pulau Misterius", width="large")
def intro_dialog_1():
    st.image("assets/images/page1_awal_part1.png", use_container_width=True)
    if st.button("Periksa Lebih Dekat..."):
        st.session_state.intro_slide = 2
        st.rerun()

@st.dialog("Ukiran Kuno", width="large")
def intro_dialog_2():
    st.image("assets/images/page1_awal_part2.png", use_container_width=True)
    if st.button("Telusuri Petunjuk..."):
        st.session_state.intro_slide = 3
        st.rerun()

@st.dialog("Memulai Teka-Teki", width="large")
def intro_dialog_3():
    st.image("assets/images/page1_awal_part3.png", use_container_width=True)
    if st.button("Mulai Pecahkan Teka-Teki"):
        st.session_state.intro_slide = 0  # Selesaikan intro
        st.rerun()

# --- Definisi Dialog Outro untuk Step 1 ---
@st.dialog("Petunjuk Terungkap", width="large")
def outro_dialog_1():
    st.image("assets/images/page1_akhir_part1.png", use_container_width=True)
    if st.button("Lanjutkan... #1"):
        st.session_state.step1_outro_slide = 2
        st.rerun()

@st.dialog("Pulau Para Raksasa", width="large")
def outro_dialog_2():
    st.image("assets/images/page1_akhir_part2.png", use_container_width=True)
    if st.button("Lanjutkan... #2"):
        st.session_state.step1_outro_slide = 3
        st.rerun()

@st.dialog("Tantangan Berikutnya", width="large")
def outro_dialog_3():
    st.image("assets/images/page1_akhir_part3.png", use_container_width=True)
    if st.button("Lanjutkan... #3"):
        st.session_state.step1_outro_slide = 4
        st.rerun()

@st.dialog("Menuju Elbaf", width="large")
def outro_dialog_4():
    st.image("assets/images/page1_akhir_part4.png", use_container_width=True)
    if st.button("Berlayar ke Stage 2"):
        st.session_state.step1_outro_slide = 0 # Selesaikan outro
        st.session_state.stage = 2              # Lanjut ke stage puzzle berikutnya
        st.rerun()

# --- Fungsi Utama Halaman ---
def show_step_1():
    # Router internal untuk menampilkan dialog atau puzzle
    intro_slide = st.session_state.get("intro_slide", 1)
    outro_slide = st.session_state.get("step1_outro_slide", 0)

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
    elif outro_slide == 4:
        st.balloons()
        outro_dialog_4()
    else:
        # Tampilkan konten puzzle utama jika tidak ada dialog aktif
        st.header("Step 1: Pulau Tak Bernama & Batu Pertama")
        st.markdown("Perjalananmu telah dimulai. Pahami makna tulisan di bawah ini untuk mengetahui ke mana kau harus berlayar. Gunakan [kompas](https://docs.google.com/document/d/e/2PACX-1vRP-augeh1Uh_qxzJnWjfAWayMNJeMH-tnKsKbGiiuhhpGHQXqOOg3kMC9ryy4MeBpUKaB60euDnxBF/pub) ini sebagai penuntunmu agar tidak tersesat dalam perjalanan.", unsafe_allow_html=True)
        st.divider()

        st.info(PONEGLYPH_1)

        islands_df = load_data_step1()
        if not islands_df.empty:
            st.subheader("Nama-Nama Pulau:")
            try:
                st.dataframe(islands_df[['Nama Pulau / Lokasi', 'Wilayah', 'Ras Penghuni', 'Iklim / Geografi', 'Ciri Kualitatif Utama']])
            except KeyError:
                st.warning("One or more columns missing from Excel file. Displaying raw data.")
                st.dataframe(islands_df)
        st.divider()

        st.subheader("Tebak nama pulau yang digambarkan oleh Poneglyph:")
        user_guess = st.text_input("Nama Pulau").lower()

        if st.button("Tebak"):
            if 'elbaph' in user_guess.lower():
                st.session_state.step1_guess_correct = True
                st.session_state.step1_outro_slide = 1 # Memulai sekuens outro
                st.rerun()
            else:
                st.error("Tebakanmu salah. Kamu tersesat di lautan dan harus memulai dari awal!")
                time.sleep(2)
                reset_progress()
                st.rerun()
