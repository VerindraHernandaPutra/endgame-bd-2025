import streamlit as st
import time

def show_final_page():
    """
    Menampilkan halaman kemenangan setelah pemain menemukan One Piece.
    """

    # 1. Memicu animasi perayaan secara otomatis
    st.balloons()

    # 2. Judul utama halaman
    st.title("🎉 SELAMAT, PETUALANG! 🎉")
    st.markdown("---")

    # 3. Pesan kemenangan yang epik
    st.header("Anda Telah Menemukan Harta Karun Legendaris...")
    st.header("ONE PIECE!")
    
    st.info("Jerih payahmu terbayar sudah! Namamu akan terukir dalam sejarah sebagai Raja Bajak Laut yang baru!", icon="👑")
    
    # 4. Menampilkan "Harta Karun" (bisa berupa gambar atau teks)
    # Anda bisa mengganti link gambar di bawah ini dengan gambar Anda sendiri.
    # Cukup unggah gambar ke folder yang sama dengan script dan ganti linknya.
    st.image(
        "https://i.pinimg.com/originals/e0/e0/0a/e0e00a8a7a3b3a3d5f1b1b1b1b1b1b1b.gif", # Ganti dengan URL gambar harta karun atau path file lokal
        caption="Harta karun terbesar kini menjadi milikmu!",
        use_column_width=True
    )

    st.markdown("---")

    # 5. Memberi pesan tambahan dan tombol untuk bermain lagi
    st.subheader("Perjalananmu mungkin telah berakhir, tapi legendamu akan abadi.")

    if st.button("Mulai Petualangan Baru 🗺️"):
        # Logika untuk mereset permainan
        # Pastikan Anda punya fungsi reset_progress() dari file utils.py
        # Jika file digabung, pastikan fungsi ini tersedia.
        
        # Contoh pemanggilan fungsi reset
        # reset_progress() 
        
        st.toast("Memulai kembali perjalanan...")
        time.sleep(2)
        st.session_state.stage = 0 # Kembali ke halaman awal
        st.rerun()

# --- Cara menggunakan fungsi ini di file utama Anda ---
#
# Di file app.py utama, Anda akan memiliki logika seperti ini:
#
# elif current_stage == 4:
#     # Logika untuk teka-teki terakhir (page_step3)
#     # Jika jawaban benar, ubah stage ke 5
#     if user_answer.strip() == CORRECT_PHRASE:
#         st.session_state.stage = 5
#         st.rerun()
#
# elif current_stage == 5:
#     show_final_page() # Panggil halaman kemenangan ini
#