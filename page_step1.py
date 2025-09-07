import streamlit as st
from utils import load_excel_data, PONEGLYPH_1

def show_step_1():
    st.header("Step 1: The First Poneglyph")
    st.markdown("Your adventure begins. Decipher the text below to determine your destination.")
    st.divider()

    # JUDUL
    st.info(PONEGLYPH_1)

    # LOAD DATASET
    islands_df = load_excel_data()
    if not islands_df.empty:
        st.subheader("Island Database Reference:")
        try:
            st.dataframe(islands_df[['Nama Pulau / Lokasi', 'Wilayah', 'Ras Penghuni', 'Iklim / Geografi', 'Ciri Kualitatif Utama']]) # JIKA MAU EDIT HEADER PER-KOLOM, UBAH SINI AE
        except KeyError:
            st.warning("One or more columns missing from Excel file. Displaying raw data.")
            st.dataframe(islands_df)

    st.divider()

    # PERTANYAAAN DAN INPUT KOLOM
    st.subheader("Tebak nama pulau yang digambarkan oleh Poneglyph:")
    user_guess = st.text_input("Nama Pulau").lower()

    if st.button("Tebak"):
        if 'elbaph' in user_guess:
            st.success("Tepat! Frasa 'bangsa tubuh menjulang seperti menara' merujuk pada Elbaph, pulau para raksasa!")
            st.session_state.step1_guess_correct = True
        else:
            st.error("Tebakanmu salah. Kamu mendarat di pulau palsu.")
            st.session_state.step1_guess_correct = False

    # DIRECT KE STEP 2
    if st.session_state.step1_guess_correct:
        if st.button("Lanjut ke Pulau Elbaph (Step 2)"):
            st.session_state.stage = 2
            st.rerun()