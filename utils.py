import streamlit as st
import pandas as pd
import markovify
import codecs

PONEGLYPH_1 = """
Ukiran batu ini penuh dengan pola berulang, kadang spiral, kadang patah-patah, seolah menggambarkan perjalanan waktu yang tidak pernah berhenti. Beberapa simbol seperti menirukan suara langkah raksasa yang bergema di hutan purba, meskipun artinya tidak pernah jelas bagi pembaca awam. Di sela barisan tanda yang seakan tidak berkaitan, tersisip frasa samar yang berbunyi **bangsa tubuh menjulang seperti menara** sebelum hilang lagi di antara coretan patah. Setelah itu ukiran kembali dipenuhi lingkaran tak beraturan, seakan menutup rahasia dengan tirai kabut. Tidak ada tanda arah jelas, hanya getaran samar dari batu ini yang membuat pembaca merasa seolah sedang diawasi.
"""
PONEGLYPH_2 = """
Barisan huruf kuno berlari dari satu sisi ke sisi lain, terkadang melengkung seperti ombak, terkadang tajam seperti pisau. Simbol-simbol itu tidak memiliki keteraturan, namun sesekali muncul potongan yang menyerupai alur cerita tak lengkap. Di tengah ukiran yang rusak, terlukis baris samar yang berbunyi **jalan tersembunyi menuju harta terbesar**, lalu segera ditutupi lagi dengan simbol silang yang menenggelamkan artinya. Coretan berikutnya hanya menyebutkan peristiwa badai dan cahaya bulan, tanpa petunjuk tambahan. Bagi pembaca yang ceroboh, batu ini hanyalah kumpulan cerita terputus. Namun bagi mereka yang teliti, sebuah petunjuk jelas terselip di antara kebisingan aksara.
"""
TEXT_CORPUS = "The final journey leads to the greatest treasure. Only the one true pirate king can claim the gold. The grand line holds the last secret. The one piece is found at the end of the grand line. A secret treasure waits for the king."

# CONFIG DATASET DISINI NANTI UNTUK KETIGA STEP | TUNGGU DATASET DI COMPLETE DULU
@st.cache_resource
def load_data_step1():
    """Memuat dataset untuk Step 1."""
    try:
        return pd.read_excel('assets/datasets/pulau_endgame.xlsx') # GANTI
    except FileNotFoundError:
        st.error("File 'pulau_endgame.xlsx' tidak ditemukan. Pastikan file berada di direktori yang benar.") # GANTI
        return pd.DataFrame()

@st.cache_resource
def load_data_keytostep3():
    """Memuat dataset untuk Key to Step 3."""
    try:
        return pd.read_excel('assets/datasets/pulau_endgame.xlsx') # GANTI
    except FileNotFoundError:
        st.error("File 'pulau_endgame.xlsx' tidak ditemukan. Pastikan file berada di direktori yang benar.") # GANTI
        return pd.DataFrame()

@st.cache_resource
def load_data_step3():
    """Memuat dataset untuk Step 3."""
    try:
        return pd.read_excel('assets/datasets/emoji.xlsx') # GANTI
    except FileNotFoundError:
        st.error("File 'emoji.xlsx' tidak ditemukan. Pastikan file berada di direktori yang benar.") # GANTI
        return pd.DataFrame()

@st.cache_resource
def load_markov_model():
    return markovify.Text(TEXT_CORPUS, state_size=2, well_formed=False)

# FUNGSI LAMA | DEPRECATED
def decode_rot13(text):
    return codecs.encode(text, 'rot_13')

# LOGIKA CORRECT ANSWER
def initialize_state():
    if 'stage' not in st.session_state:
        st.session_state.stage = 0
    keys_to_initialize = [
        'step1_guess_correct', 'step2_pixel_puzzle_solved',
        'step2_island_guess_correct', 'step3_final_puzzle_solved'
    ]
    for key in keys_to_initialize:
        if key not in st.session_state:
            st.session_state[key] = False

# FUNGSI RESET PROGRESS
def reset_progress():
    """Menghapus semua progres dan kembali ke awal."""
    keys_to_reset = list(st.session_state.keys())
    for key in keys_to_reset:
        del st.session_state[key]
