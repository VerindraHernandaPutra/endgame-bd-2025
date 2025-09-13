import streamlit as st
import pandas as pd
import codecs

PONEGLYPH_1 = """
Ukiran batu ini penuh dengan pola berulang, kadang spiral, kadang patah-patah, seolah menggambarkan perjalanan waktu yang tidak pernah berhenti. Beberapa simbol seperti menirukan suara langkah raksasa yang bergema di hutan purba, meskipun artinya tidak pernah jelas bagi pembaca awam. Di sela barisan tanda yang seakan tidak berkaitan, tersisip frasa samar yang berbunyi **bangsa tubuh menjulang seperti menara** sebelum hilang lagi di antara coretan patah. Setelah itu ukiran kembali dipenuhi lingkaran tak beraturan, seakan menutup rahasia dengan tirai kabut. Tidak ada tanda arah jelas, hanya getaran samar dari batu ini yang membuat pembaca merasa seolah sedang diawasi.
"""
PONEGLYPH_2 = """
Barisan huruf kuno berlari dari satu sisi ke sisi lain, terkadang melengkung seperti ombak, terkadang tajam seperti pisau. Simbol-simbol itu tidak memiliki keteraturan, namun sesekali muncul potongan yang menyerupai alur cerita tak lengkap. Di tengah ukiran yang rusak, terlukis baris samar yang berbunyi **jalan tersembunyi menuju harta terbesar**, lalu segera ditutupi lagi dengan simbol silang yang menenggelamkan artinya. Coretan berikutnya hanya menyebutkan peristiwa badai dan cahaya bulan, tanpa petunjuk tambahan. Bagi pembaca yang ceroboh, batu ini hanyalah kumpulan cerita terputus. Namun bagi mereka yang teliti, sebuah petunjuk jelas terselip di antara kebisingan aksara.
"""

# --- Fungsi Pemuat Data ---
@st.cache_resource
def load_data_step1():
    """Memuat dataset untuk Step 1."""
    try:
        return pd.read_excel('assets/datasets/pulau_endgame.xlsx')
    except FileNotFoundError:
        st.error("File 'assets/datasets/pulau_endgame.xlsx' tidak ditemukan.")
        return pd.DataFrame()

@st.cache_resource
def load_data_keytostep3():
    """Memuat dataset untuk Key to Step 3."""
    try:
        return pd.read_excel('assets/datasets/pulau_endgame.xlsx')
    except FileNotFoundError:
        st.error("File 'assets/datasets/pulau_endgame.xlsx' tidak ditemukan.")
        return pd.DataFrame()

@st.cache_resource
def load_data_step3():
    """Memuat dataset untuk Step 3."""
    try:
        return pd.read_excel('assets/datasets/emoji.xlsx')
    except FileNotFoundError:
        st.error("File 'assets/datasets/emoji.xlsx' tidak ditemukan.")
        return pd.DataFrame()

# --- Manajemen State ---
def initialize_state():
    """Inisialisasi semua variabel state yang dibutuhkan dalam aplikasi."""
    if 'stage' not in st.session_state:
        st.session_state.stage = 0
        
    # Variabel state untuk storyboard
    story_states = {
        'intro_slide': 1,
        'step1_outro_slide': 0,
        'step2_intro_slide': 1,
        'step2_outro_slide': 0,
        'keytostep3_intro_slide': 1,
        'keytostep3_outro_slide': 0,
        'step3_intro_slide': 1,
        'step3_outro_slide': 0,
    }
    for key, value in story_states.items():
        if key not in st.session_state:
            st.session_state[key] = value

    # Variabel state untuk progres puzzle
    puzzle_states = [
        'step1_guess_correct', 'step2_pixel_puzzle_solved',
        'step2_island_guess_correct', 'step3_final_puzzle_solved'
    ]
    for key in puzzle_states:
        if key not in st.session_state:
            st.session_state[key] = False

def reset_progress():
    """Menghapus semua progres dan kembali ke halaman awal."""
    keys_to_reset = list(st.session_state.keys())
    for key in keys_to_reset:
        del st.session_state[key]
    st.session_state.stage = 0