import streamlit as st
import pandas as pd
import markovify
import codecs

# --- Constants and Game Data ---

PONEGLYPH_1 = """
"Ukiran batu ini penuh dengan pola berulang, kadang spiral, kadang patah-patah, seolah menggambarkan perjalanan waktu yang tidak pernah berhenti. Beberapa simbol seperti menirukan suara langkah raksasa yang bergema di hutan purba, meskipun artinya tidak pernah jelas bagi pembaca awam. Di sela barisan tanda yang seakan tidak berkaitan, tersisip frasa samar yang berbunyi **bangsa tubuh menjulang seperti menara** sebelum hilang lagi di antara coretan patah. Setelah itu ukiran kembali dipenuhi lingkaran tak beraturan, seakan menutup rahasia dengan tirai kabut. Tidak ada tanda arah jelas, hanya getaran samar dari batu ini yang membuat pembaca merasa seolah sedang diawasi."
"""
PONEGLYPH_2 = """
"Barisan huruf kuno berlari dari satu sisi ke sisi lain, terkadang melengkung seperti ombak, terkadang tajam seperti pisau. Simbol-simbol itu tidak memiliki keteraturan, namun sesekali muncul potongan yang menyerupai alur cerita tak lengkap. Di tengah ukiran yang rusak, terlukis baris samar yang berbunyi **jalan tersembunyi menuju harta terbesar**, lalu segera ditutupi lagi dengan simbol silang yang menenggelamkan artinya. Coretan berikutnya hanya menyebutkan peristiwa badai dan cahaya bulan, tanpa petunjuk tambahan. Bagi pembaca yang ceroboh, batu ini hanyalah kumpulan cerita terputus. Namun bagi mereka yang teliti, sebuah petunjuk jelas terselip di antara kebisingan aksara."
"""

TEXT_CORPUS = "The final journey leads to the greatest treasure. Only the one true pirate king can claim the gold. The grand line holds the last secret. The one piece is found at the end of the grand line. A secret treasure waits for the king."

# --- Helper Functions ---

@st.cache_resource
def load_excel_data():
    """Loads island data from an Excel file."""
    try:
        # Note: 'pulau_endgame.xlsx' must be in the root directory or update path.
        return pd.read_excel('pulau_endgame.xlsx')
    except FileNotFoundError:
        st.error("File 'pulau_endgame.xlsx' not found. Please ensure the file exists in the root directory.")
        return pd.DataFrame()

@st.cache_resource
def load_markov_model():
    """Creates and loads the Markov Chain model."""
    return markovify.Text(TEXT_CORPUS, state_size=2, well_formed=False)

def decode_rot13(text):
    """Decodes text using ROT13 cipher."""
    return codecs.encode(text, 'rot_13')

def initialize_state():
    """Initializes session state variables if they don't exist."""
    if 'stage' not in st.session_state:
        st.session_state.stage = 0 # 0: Welcome, 1: Step 1, 2: Step 2, 3: Step 3

    # State variables for Step 1 progress
    if 'step1_guess_correct' not in st.session_state:
        st.session_state.step1_guess_correct = False

    # State variables for Step 2 progress
    if 'step2_pixel_puzzle_solved' not in st.session_state:
        st.session_state.step2_pixel_puzzle_solved = False
    if 'step2_island_guess_correct' not in st.session_state:
        st.session_state.step2_island_guess_correct = False

    # State variables for Step 3 progress
    if 'step3_decoded_text' not in st.session_state:
        st.session_state.step3_decoded_text = None
    if 'step3_generated_phrase' not in st.session_state:
        st.session_state.step3_generated_phrase = None