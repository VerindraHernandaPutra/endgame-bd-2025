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
    try:
        return pd.read_excel('pulau_endgame.xlsx')
    except FileNotFoundError:
        st.error("File 'pulau_endgame.xlsx' not found. Please ensure the file exists in the root directory.")
        return pd.DataFrame()

@st.cache_resource
def load_markov_model():
    return markovify.Text(TEXT_CORPUS, state_size=2, well_formed=False)

def decode_rot13(text):
    return codecs.encode(text, 'rot_13')

def initialize_state():
    if 'stage' not in st.session_state:
        st.session_state.stage = 0
    keys_to_initialize = [
        'step1_guess_correct', 'step2_pixel_puzzle_solved',
        'step2_island_guess_correct'
    ]
    for key in keys_to_initialize:
        if key not in st.session_state:
            st.session_state[key] = False
    if 'step3_decoded_text' not in st.session_state:
        st.session_state.step3_decoded_text = None
    if 'step3_generated_phrase' not in st.session_state:
        st.session_state.step3_generated_phrase = None

def reset_progress():
    """Clears all progress and returns to the start screen."""
    keys_to_reset = [
        'stage', 'step1_guess_correct', 'step2_pixel_puzzle_solved',
        'step2_island_guess_correct', 'step3_decoded_text', 'step3_generated_phrase'
    ]
    for key in keys_to_reset:
        if key in st.session_state:
            del st.session_state[key]
    # Re-initialization will set stage back to 0 on the next rerun.
