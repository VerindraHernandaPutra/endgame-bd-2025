import streamlit as st
from utils import load_data_step1, PONEGLYPH_1, reset_progress
import time

def show_step_1():
    # DESKRIPSI PUZZLE
    st.header("Step 1: The First Poneglyph")
    st.markdown("Your adventure begins. Decipher the text below to determine your destination.")
    st.divider()

    st.info(PONEGLYPH_1)

    # DATASET
    islands_df = load_data_step1()
    if not islands_df.empty:
        st.subheader("Island Database Reference:")
        try:
            st.dataframe(islands_df[['Nama Pulau / Lokasi', 'Wilayah', 'Ras Penghuni', 'Iklim / Geografi', 'Ciri Kualitatif Utama']])
        except KeyError:
            st.warning("One or more columns missing from Excel file. Displaying raw data.")
            st.dataframe(islands_df)

    st.divider()

    # TEBAK PULAU
    st.subheader("Tebak nama pulau yang digambarkan oleh Poneglyph:")
    user_guess = st.text_input("Nama Pulau").lower()

    if st.button("Tebak"):
        if 'elbaph' in user_guess:
            st.success("Tepat! Frasa 'bangsa tubuh menjulang seperti menara' merujuk pada Elbaph, pulau para raksasa!")
            st.session_state.step1_guess_correct = True
        else:
            st.error("Tebakanmu salah. Kamu tersesat di lautan dan harus memulai dari awal!")
            time.sleep(2)
            reset_progress()
            st.rerun()

    if st.session_state.get("step1_guess_correct", False):
        if st.button("Lanjut ke Pulau Elbaph (Step 2)"):
            st.session_state.stage = 2
            st.rerun()
