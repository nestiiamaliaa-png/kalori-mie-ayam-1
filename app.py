import streamlit as st
import matplotlib.pyplot as plt

# CONFIG
st.set_page_config(
    page_title="Virtual Lab Mie Ayam",
    page_icon="🍜",
    layout="centered"
)

# TITLE
st.title("🍜 Virtual Lab Kalori Mie Ayam")
st.markdown("### Gunakan konsep integral untuk menghitung total kalori")

st.write("---")

# INPUT PORSI
porsi = st.number_input(
    "🍽️ Jumlah porsi mie ayam",
    min_value=1,
    max_value=10,
    value=1
)

# DATA KALORI
kalori_data = {
    "Sawi 🥬": 10,
    "Daun Bawang 🌿": 5,
    "Ceker 🍗": 150,
    "Bakso 🧆": 80,
    "Telur Rebus 🥚": 70,
    "Krupuk Pangsit 🟨": 120,
    "Bawang Goreng 🧅": 50,
    "Sambal 🌶️": 30,
    "Kecap 🍯": 40
}

st.write("---")
st.subheader("🧩 Pilih Komposisi Mie Ayam")

# INPUT SLIDER
komponen = {}
for item in kalori_data:
    komponen[item] = st.slider(f"{item}", 0, 5, 0)

# HITUNG KALORI
total_kalori = 0
detail_kalori = {}

for item, jumlah in komponen.items():
    kalori = jumlah * kalori_data[item] * porsi
    detail_kalori[item] = kalori
    total_kalori += kalori

st.write("---")

# OUTPUT
st.subheader("🔥 Total Kalori")
st.success(f"{total_kalori} kkal")

# KATEGORI
if total_kalori == 0:
    st.info("Belum ada komposisi dipilih 👀")
elif total_kalori < 300:
    st.success("Kalori Rendah 🟢")
elif total_kalori < 600:
    st.warning("Kalori Sedang 🟡")
else:
    st.error("Kalori Tinggi 🔴")

# GRAFIK
if total_kalori > 0:
    st.subheader("📊 Distribusi Kalori")

    fig, ax = plt.subplots()
    ax.pie(
        detail_kalori.values(),
        labels=detail_kalori.keys(),
        autopct='%1.1f%%'
    )
    ax.set_title("Kontribusi Kalori Tiap Komponen")

    st.pyplot(fig)

# PENJELASAN INTEGRAL
st.write("---")
st.subheader("📘 Konsep Integral")

st.markdown("""
Dalam aplikasi ini, total kalori dihitung menggunakan konsep integral:

K_total = Σ (kalori × porsi)

Artinya, setiap komponen makanan menyumbang sebagian kecil kalori, 
dan totalnya adalah hasil penjumlahan seluruh komponen tersebut.

👉 Ini adalah penerapan integral dalam kehidupan sehari-hari.
""")

# FOOTER
st.write("---")
st.caption("Dibuat untuk Virtual Lab Matematika 🍜✨")
