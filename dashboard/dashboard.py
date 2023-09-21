import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import datetime


def membuat_tren_penyewaan_sepeda(df):
	df_bks_data = df
	df_bks_harian = df_bks_data.resample(rule='D', on='dteday').agg({"cnt": "sum"})
	df_bks_harian = df_bks_harian.reset_index()
	# Mengubah nama kolom dteday dan cnt pada dataset
	df_bks_harian.rename(columns={
    					"dteday": "date",
    					"cnt": "count"
						}, inplace=True)
	return df_bks_harian

def konversi_day_ke_hari(myday):
    if myday == 'Sunday':
        myday = 'Minggu'
    elif myday == 'Monday':
        myday = 'Senin'
    elif myday == 'Tuesday':
        myday = 'Selasa'
    elif myday == 'Wednesday':
        myday = 'Rabu'
    elif myday == 'Thursday':
        myday = 'Kamis'
    elif myday == 'Friday':
        myday = 'Jumaat'
    elif myday == 'Saturday':
        myday = 'Sabtu'
    return myday


def berdasarkan_kondisi_cuaca(df):
    df_bks_data = df
    df_bks_data_percuaca = df_bks_data.groupby("weathersit")["cnt"].sum().reset_index()
    df_bks_data_percuaca.rename(columns={
                        "cnt": "count"
                        }, inplace=True)
    return df_bks_data_percuaca


def berdasarkan_kondisi_musim(df):
    df_bks_data = df
    df_bks_data_permusim = df_bks_data.groupby("season_cat")["cnt"].sum().reset_index()
    df_bks_data_permusim.rename(columns={
                        "cnt": "count"
                        }, inplace=True)
    return df_bks_data_permusim


def cek_empty_value(nilai):
    temp_flag = np.any(nilai)

    if temp_flag == False:
        return 0
    else:
        return nilai


#input dataset
df_bks_data = pd.read_csv("dashboard/df_bks_data.csv")

#sorting dataset berdasarkan dteday
df_bks_data.sort_values(by="dteday", inplace=True)
df_bks_data.reset_index(inplace=True)

#konversi tipe dteday ke datetime 
df_bks_data["dteday"] = pd.to_datetime(df_bks_data["dteday"])



# membuat sidebar
min_date = df_bks_data["dteday"].min()
max_date = df_bks_data["dteday"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://img.freepik.com/premium-vector/sport-bike-logo-template_18099-3714.jpg")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = df_bks_data[(df_bks_data["dteday"] >= str(start_date)) & 
                (df_bks_data["dteday"] <= str(end_date))]



# Memanggil fungsi
tren_penyewaan_sepeda_df = membuat_tren_penyewaan_sepeda(main_df)
penyewaan_sepeda_by_cuaca = berdasarkan_kondisi_cuaca(main_df)
penyewaan_sepeda_by_musim = berdasarkan_kondisi_musim(main_df)


# Visualisasi Dasbor
st.header('Dasbor Penyewaan Sepeda :sparkles:')


#Tren Penyewaan Sepeda
st.subheader('Tren Penyewaan Sepeda')

st.text('Waktu Penyewaan Tertinggi')

col1, col2, col3 = st.columns(3)
 
with col1:
    max_date = tren_penyewaan_sepeda_df["date"].loc[ tren_penyewaan_sepeda_df["count"] == tren_penyewaan_sepeda_df["count"].max() ]
    date = max_date.apply(lambda x: x.strftime("%A"))
    date = date.values
    listToStr = ' '.join(date)
    hari = konversi_day_ke_hari(listToStr)
    st.metric("Hari", value=hari)
 
with col2:
    max_date = tren_penyewaan_sepeda_df["date"].loc[ tren_penyewaan_sepeda_df["count"] == tren_penyewaan_sepeda_df["count"].max() ]
    date = max_date.apply(lambda x: x.strftime("%Y-%m-%d"))
    date = date.values
    st.metric("Tanggal", value=date[0])

with col3:
    max_count = tren_penyewaan_sepeda_df["count"].max()
    st.metric("Jumlah Penyewaan Tertinggi", value=max_count)
 

st.text('Waktu Penyewaan Terendah')

col4, col5, col6 = st.columns(3)
 
with col4:
    min_date = tren_penyewaan_sepeda_df["date"].loc[ tren_penyewaan_sepeda_df["count"] == tren_penyewaan_sepeda_df["count"].min() ]
    date = min_date.apply(lambda x: x.strftime("%A"))
    date = date.values
    listToStr = ' '.join(date)
    hari = konversi_day_ke_hari(listToStr)
    st.metric("Hari", value=hari)
 
with col5:
    max_date = tren_penyewaan_sepeda_df["date"].loc[ tren_penyewaan_sepeda_df["count"] == tren_penyewaan_sepeda_df["count"].min() ]
    date = max_date.apply(lambda x: x.strftime("%Y-%m-%d"))
    date = date.values
    st.metric("Tanggal", value=date[0])

with col6:
    max_count = tren_penyewaan_sepeda_df["count"].min()
    st.metric("Jumlah Penyewaan Terendah", value=max_count)

# line chart tren penyewaan sepeda
fig, ax = plt.subplots(figsize=(15, 7))
ax.plot(tren_penyewaan_sepeda_df["date"], tren_penyewaan_sepeda_df["count"], color='peru', marker='o', linewidth=2)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15, labelrotation = 90)
st.pyplot(fig)


#Berdasarkan kondisi cuaca
st.subheader('Jumlah Penyewa Sepeda berdasarkan Kondisi Cuaca 2011-2012')

# bar chart jumlah penyewaan sepeda berdasarkan kondisi cuaca
fig, ax = plt.subplots(figsize=(15, 7))
sns.barplot(data=penyewaan_sepeda_by_cuaca, x="weathersit", y="count", color="peru")
sns.despine()
ax.set_xlabel('Kondisi Cuaca', fontsize=15, color='blue')
ax.set_ylabel('Jumlah Penyewa Sepeda', fontsize=15, color='blue')
st.pyplot(fig)

#menampilkan info kondisi cuaca
cuacaku = st.selectbox(
    label="Apa kondisi cuaca dengan jumlah penyewa sepeda tertinggi?",
    options=('[1] Cerah, Sedikit awan,Sebagian berawan,Sebagian berawan', 
             '[2] Kabut + Mendung, Kabut + Awan pecah, Kabut + Sedikit awan, Kabut', 
             '[3] Salju Ringan, Hujan Ringan + Badai Petir + Awan berserakan, Hujan Ringan + Awan berserakan',
             '[4] Hujan Lebat + Hujan Es + Badai Petir + Kabut, Salju + Kabut')
)


#Berdasarkan kondisi musim
st.subheader('Jumlah Penyewa Sepeda berdasarkan Kondisi Musim')

# bar chart jumlah penyewaan sepeda berdasarkan kondisi musim
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=penyewaan_sepeda_by_musim, x="season_cat", y="count", color="peru")
ax.set_title('Jumlah Penyewa Sepeda per Musim di Tahun 2012', loc='left', pad=30, fontsize=15, color='orange')
ax.set_xlabel('Musim', fontsize=15, color='blue')
ax.set_ylabel('Jumlah Penyewa Sepeda', fontsize=15, color='blue')
st.pyplot(fig)


#menampilkan jumlah tertinggi dan terendah penyewaan sepeda berdasarkan kondisi musim
musimku = st.selectbox(
    label="Yuk cari tahu jumlah penyewaan sepeda berdasarkan musim-nya?",
    options=('Pilih Musim',
             '[Springer] Musim Semi', 
             '[Summer] Musim Panas', 
             '[Fall] Musim Gugur',
             '[Winter] Musim Dingin')
)

if '[Springer] Musim Semi' in musimku:
    value_springer  = penyewaan_sepeda_by_musim["count"].loc[ penyewaan_sepeda_by_musim["season_cat"] == "springer" ]
    value_springer  = value_springer.values
    value_springer  = cek_empty_value(value_springer)
    st.metric(label="Jumlah Penyewa Sepeda di Musim Semi", value=value_springer)
elif '[Summer] Musim Panas' in musimku:
    value_summer    = penyewaan_sepeda_by_musim["count"].loc[ penyewaan_sepeda_by_musim["season_cat"] == "summer" ]
    value_summer    = value_summer.values
    value_summer    = cek_empty_value(value_summer)
    st.metric(label="Jumlah Penyewa Sepeda di Musim Panas", value=value_summer)
elif '[Fall] Musim Gugur' in musimku:
    value_fall      = penyewaan_sepeda_by_musim["count"].loc[ penyewaan_sepeda_by_musim["season_cat"] == "fall" ]
    value_fall      = value_fall.values
    value_fall      = cek_empty_value(value_fall)
    st.metric(label="Jumlah Penyewa Sepeda di Musim Gugur", value=value_fall)
elif '[Winter] Musim Dingin' in musimku:
    value_winter    = penyewaan_sepeda_by_musim["count"].loc[ penyewaan_sepeda_by_musim["season_cat"] == "winter" ]
    value_winter    = value_winter.values
    value_winter    = cek_empty_value(value_winter)
    st.metric(label="Jumlah Penyewa Sepeda di Musim Dingin", value=value_winter)
