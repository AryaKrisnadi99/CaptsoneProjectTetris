import pandas as pd
import altair as alt
import streamlit as st

st.set_page_config(
    page_title = "Analisa Tingkat Penganguran Terbuka di Jawa Barat",
    layout = "wide"
)

st.title("Analisa Tingkat Penganguran Terbuka di Jawa Barat")
st.header("Berapa Jumlah Penganguran di Indonesia ?")

st.markdown('''<div style='text-align: left; margin-top:-10px'> 
Pada bulan Agustus 2022 tercatat jumlah penganguran di Indonesia mencapai 8,42 Juta orang.
Jawa Barat menempati peringkat pertama dengan jumlah penganguran sebesar 8,31%, 
Kepulauan Riau berada di posisi kedua dengan jumlah penganguran sebesar 8,23%, 
Banten diurutan ketiga dengan jumlah penganguran sebesar 8,09%, 
DKI Jakarta di posisi keempat dengan jumlah penganguran sebesar 7,18% 
dan Maluku diposisi kelima dengan jumlah penganguran sebesar 6,88.<br><br>''', unsafe_allow_html=True)

st.write("Untuk persebaran Tingkat Penganguran Terbuka(TPT) di Jawa Barat dapat di lihat pada grafik di bawah ini : ")

#Untuk melakukan agragasi data
df_umur = pd.read_csv('umur.csv', sep=";")
df_jenis_kelamin = pd.read_csv('jenis_kelamin.csv', sep=";")
df_pendidikan = pd.read_csv('jenjang_pendidikan.csv', sep=";")
df_loker = pd.read_csv('loker.csv', sep=";")

df_merged = pd.merge(df_umur, df_pendidikan, on=['tahun','nama_provinsi', 'kode_provinsi'])
df_merged = pd.merge(df_merged, df_jenis_kelamin, on=['tahun','nama_provinsi', 'kode_provinsi'])
df_merged = pd.merge(df_merged, df_loker, on=['tahun','nama_provinsi', 'kode_provinsi'])


# Pilih Grafik Penganguran
grafik_penganguran = st.selectbox(
    "Silahkan Pilih Grafik Jenis Tingkat Pengangguran Terbuka (TPT)",
    ['Pilih','Umur','Jenis Kelamin','Jenjang Pendidikan']
)
if grafik_penganguran == 'Pilih':
    grafik_penganguran
    
elif grafik_penganguran == 'Umur':

# Membuat grafik menggunakan Altair
    chart1 = alt.Chart(df_merged).mark_line().encode(
        alt.X('tahun', title='Tahun',axis=alt.Axis(format='d',tickCount=5,labelAngle=0)),
        alt.Y('penganguran_x', title='Jumlah Penganguran', aggregate='sum'),
        color='umur'    
    ).properties(
        width=800,
        height=400
    )
    st.subheader('Grafik Jumlah Penganguran Berdasarkan Umur')
    st.altair_chart(chart1, use_container_width=True)

    st.write("Pada grafik TPT berdasarkan umur di atas dapat terdapat beberapa hal yang dapat dilihat yaitu: ",'\n'
             "1. Rentang umur umur 20-24 memiliki jumlah penganguran terbanyak pada tahun 2018-2022.", '\n'
             '''2. Pada tahun 2020 hingga 2022 hanya rentang 15-19 tahun yang mengalami kenaikan angka penganguran sedangkan rentan umur 
             lainnya mengalami penurunan atau stabil.''')
    
elif grafik_penganguran == 'Jenis Kelamin':
    
    chart2 = alt.Chart(df_merged).mark_line().encode(
        alt.X('tahun', title='Tahun',axis=alt.Axis(format='d',tickCount=5,labelAngle=0)),
        alt.Y('penganguran', title='Jumlah Penganguran', aggregate='sum'),
        color='jenis_kelamin'
    ).properties( 
        width=600,
        height=400
    )
    
    st.subheader('Grafik Jumlah Penganguran Berdasarkan Jenis Kelamin')
    st.altair_chart(chart2, use_container_width=True)

    st.write("Pada grafik TPT berdasarkan Jenis Kelamin di atas dapat terdapat beberapa hal yang dapat dilihat yaitu: ",'\n'
             "1. Jenis kelamin LAKI - LAKI memiliki jumlah penganguran terbanyak.",'\n'
             "2. Setelah tahun 2020 jumlah penganguran mengalami penurunan")

else:

    chart3 = alt.Chart(df_merged).mark_line().encode(
        alt.X('tahun', title='Tahun',axis=alt.Axis(format='d',tickCount=5,labelAngle=0)),
        alt.Y('penganguran_y', title='Jumlah Penganguran', aggregate='sum'),
        color='pendidikan'
    ).properties( 
        width=300,
        height=400
    )

    st.subheader('Grafik Jumlah Penganguran Berdasarkan Jenjang Pendidikan')
    st.altair_chart(chart3, use_container_width=True)

    st.write("Pada grafik TPT berdasarkan Jenjang Pendidikan di atas dapat terdapat beberapa hal yang dapat dilihat yaitu: ",'\n'
             '''1. Jenjang Pendidikan SD mengami kenaikan jumlah penganguran terbanyak pada tahun 2020 dibandingkan jenjang
              pendidikan yang lain.''', '\n'
             '''2. Setelah tahun 2020 jumlah penganguran mengalami penurunan.''')

st.markdown('\n')
st.markdown("Kemudian bagaimana dengan lowongan kerja yang dibuka pada tahun 2018 - 2020 di Jawa Barat ?")


chart4 = alt.Chart(df_loker).mark_bar().encode(
    alt.X('tahun', title='Tahun',axis=alt.Axis(format='d',tickCount=5,labelAngle=0)),
    alt.Y('lowongan', title='Jumlah Lowongan', aggregate='sum')
).properties( 
    width=580,
    height=400
)

col1, col2 = st.columns([1,2])

with col1:
    st.subheader('Grafik Jumlah Lowongan per Tahun')
    st.altair_chart(chart4, use_container_width=False)

with col2: 
    st.markdown('''<div style='text-align: left; margin-left:177px;'>  <br><br><br><br>
            Berdasarkan grafik jumlah lowongan terbuka pada tahun 2018 - 2020 di 
               Jawa Barat terdapat kenaikan yang singnifikan untuk lowongan kerja terbuka pada taun 
               2021 dan 2022. Namun jumlah lowongan terbuka sangatlah jauh jika dibandingkan dengan
               jumlah TPT.''', unsafe_allow_html=True)
    st.write('''<div style='text-align: left; margin-left:177px;'><br>
            Sebagai perbandingan jumlah lowongan terbuka dan jumlah TPT berdasarkan Umur pada tahun 2022.
            Jumlah lowongan sebanyak 169.005 sedangkan jumlah penganguran sebesar 2.125.606 sehingga''',
            '''<br> jumlah penganguran adalah 12.5x dari jumlah lowongan kerja.''',unsafe_allow_html=True)

st.write("---")
st.header("Langkah Apa Saja yang Sudah Dilakukan Pemerintah Dalam Mengurangi Angka TPT")

st.markdown('''<div style='text-align: left; margin-bottom:5px'>
            Pemerintah telah mengupayakan berbagai hal dalam menurunkan angka penganguran seperti : ''', unsafe_allow_html=True)
st.write("1. Membuat progaram Kartu Prakerja")
st.markdown('''<div style='text-align: left; margin-left:28px; margin-top:-13px;margin-bottom:-25px'>
            Berdasarkan hasil survei pada 2000 responden yang mengikuti program Kartu Prakerja pada gelombang 1-11, 
            jumlah penganguran turun 16.5% menjadi 39.85%, yang bekerja naik 3.2% menjadi 34.6%, dan yang
            berwisausaha naik 13% menjadi 25,6%. Hal ini berarti terdapat perubahan yang signifikan bagi responden yang telah mengikuti program 
            Kartu Prakerja''', unsafe_allow_html=True)

st.markdown('''<div style='text-align: left; margin-left:28px;'>''', unsafe_allow_html=True)

st.write('''2. Membuat program Merdeka Belajar-Kampus Merdeka (MBKM)''')
st.markdown('''<div style='text-align: left; margin-left:28px; margin-top:-13px'>
            Berdasarkan hasil survei menujukkan bahwa mahasiswa yang mengikuti 
            program MBKM memiliki waktu yang tunggu untuk mendapatkan pekerjaan 
            lebih singkat dibandingkand dengan yang tidak mengikuti.''', unsafe_allow_html=True)

st.write("---")
st.header("Saran")
st.markdown('''<div style='text-align: left; margin-top:-10px'> 
            Berdasarkan hasil analisa di atas berikut saran saya terhadapat pemerintah dalam menurunkan angka penganguran : '''
            ,unsafe_allow_html=True)

st.write('''1. Meningkatakan jumlah lapangan kerja, terutama di provinsi yang memiliki anga pengaguran yang tinggi seperti Jawa Barat''',
         '\n''''2. Terus menjalan program Kartu Pra Kerja dan Kampus Merdeka serta meningkatkan kualitas dari program tersebut 
         karena sudah terbukti dalam mengurangi angka TPT''')

st.write("---")
st.header("Referensi")
st.markdown("""
<style>
    .hyperlink {
        text-align: left;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hyperlink">1. Open Data Jabar (<a href="https://opendata.jabarprov.go.id/id/dataset?q=penganguran&suggestion=on&region=1">Dataset</a>)</div>',unsafe_allow_html=True)
st.markdown('''
<div class="hyperlink">
    2. KumparanNews. (2022).
    <em>Kemendikbudristek Pastikan Sarjana Tidak Menganggur Lewat Kampus Merdeka. </em>
    <a href="https://kumparan.com/kumparannews/kemendikbudristek-pastikan-sarjana-tidak-menganggur-lewat-kampus-merdeka-1zVxz7HsRlN/full">
         Link Referensi
    </a>
</div>''',unsafe_allow_html=True)
st.markdown('''
<div class="hyperlink">
    3. Kompas.com. (2021).
    <em>Program Kartu Prakerja Berhasil Tekan Pengangguran?. </em>
    <a href="https://money.kompas.com/read/2021/10/25/103900826/program-kartu-prakerja-berhasil-tekan-pengangguran-">
         Link Referensi
    </a>
</div>''',unsafe_allow_html=True)
st.markdown('''
<div class="hyperlink">
    4. CNN Indonesia. (2023).
    <em>Pengangguran RI Tembus 8,42 Juta Orang di 2022. </em>
    <a href="https://www.cnnindonesia.com/ekonomi/20230219133919-92-914985/pengangguran-ri-tembus-842-juta-orang-di-2022">
         Link Referensi
    </a>
</div>''',unsafe_allow_html=True)
with st.sidebar:
    st.title("Analisa Tingkat Penganguran Terbuka di Jawa Barat")
    st.subheader("TETRIS CAPSTONE PROJECT")

    st.markdown("""
    <style>
        .sidebar-text {
            text-align: left;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-text"> I Gede Arya Krisnadi</div>',unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text"> Email : aryakrisnadi96@gmail.com</div>',unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text"><a href="https://www.linkedin.com/in/i-gede-arya-krisnadi-886b741a2/">Linkedin</a></div>',unsafe_allow_html=True)
    