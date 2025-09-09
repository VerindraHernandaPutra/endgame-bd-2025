import streamlit as st
import markovify
from utils import load_markov_model, decode_rot13, reset_progress
import time

def show_step_3():
    st.header("Final: The Secret of Laugh Tale")
    st.markdown("Selamat datang di **Laugh Tale**! One Piece ada di sini, tapi terkunci di balik teka-teki terakhir!")
    st.divider()

    markov_model = load_markov_model()

    st.subheader("Langkah 1: Dekode Teks")
    st.markdown("Teks di bawah ini terenkripsi. Dekode untuk menemukan petunjuk!")
    encoded_text = "Gur oebja ebbfr fubjf bayl oernxvat tbyq, gubhtu gur jbeqf ner sver va gurfr qrnyf. Rirel jnl gur yvarf qbja, gurer vf bayl gubhtu pbairagvbaf. Gur jnl vf vaibyirq va gur nzbhag bs pbzznaqf, ohg gurer vf ab fcrpvny fbyhgvba. Vg nyjnlf frrzf yvxr gur yvar vf n ybg bs fbzrguvat arprffnel. Naq gurer vf na rknpg yvar gung fnlf: gurnger vf ba gur sebag qrngu zbhag. Gur erfg vf bayl bevtvany naq abguvat vf vagb fznyr."
    st.code(encoded_text, language='text')

    if st.button("Dekode Teks"):
        st.session_state.step3_decoded_text = decode_rot13(encoded_text)
        st.rerun()

    if st.session_state.get("step3_decoded_text"):
        st.subheader("Hasil Dekode Teks:")
        st.code(st.session_state.step3_decoded_text, language='text')
        st.divider()

        st.subheader("Langkah 2: Temukan Petunjuk dan Prediksi Kalimat")
        user_start_phrase = st.text_input("Masukkan frasa awal yang kamu temukan (1-2 kata)").strip()

        if st.button("Prediksi Kelanjutan Kalimat"):
             # Logic to generate sentence
             pass # Placeholder for brevity

        if st.session_state.get("step3_generated_phrase"):
            st.subheader("Hasil Prediksi Model:")
            st.code(st.session_state.step3_generated_phrase, language='text')
            st.divider()

            st.subheader("Langkah 3: Masukkan Frasa Kunci Final")
            user_phrase = st.text_input("Frasa kunci").strip()

            if st.button("Buka One Piece"):
                correct_phrase = "The one piece is found at the end of the grand line"
                if user_phrase.lower() == correct_phrase.lower():
                    st.balloons()
                    st.success("🎉 SELAMAT! Kamu telah menemukan One Piece! 🎉")
                else:
                    st.error("Frasa kunci salah. Harta karun menolakmu! Petualanganmu direset.")
                    time.sleep(2)
                    reset_progress()
                    st.rerun()
