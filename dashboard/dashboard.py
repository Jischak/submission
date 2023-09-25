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


def berdasarkan_kondisi_musim_2011(df):
    df_bks_data = df
    df_bks_data_permusim_2011 = df_bks_data.loc[df_bks_data["dteday"] < "2012-01-01"]
    df_bks_data_permusim_2011 = df_bks_data_permusim_2011.groupby("season_cat")["cnt"].sum().reset_index()
    df_bks_data_permusim_2011.rename(columns={
                        "cnt": "count"
                        }, inplace=True)
    return df_bks_data_permusim_2011


def berdasarkan_kondisi_musim_2012(df):
    df_bks_data = df
    df_bks_data_permusim_2012 = df_bks_data.loc[df_bks_data["dteday"] > "2011-12-31"]
    df_bks_data_permusim_2012 = df_bks_data_permusim_2012.groupby("season_cat")["cnt"].sum().reset_index()
    df_bks_data_permusim_2012.rename(columns={
                        "cnt": "count"
                        }, inplace=True)
    return df_bks_data_permusim_2012


def cek_empty_value(nilai):
    temp_flag = np.any(nilai)

    if temp_flag == False:
        return 0
    else:
        return nilai


def rata_rata_jumlah_per_hari(df, bulan, tahun):

    df_bks_harian = df
    df_bks_harian = df_bks_data.resample(rule='D', on='dteday')['cnt'].sum().reset_index()

    # Mengubah weekday ke day
    df_bks_harian["day"] = df_bks_harian.dteday.apply(lambda x: x.strftime('%A'))
    day = pd.CategoricalDtype(['Sunday', 'Monday', 'Tuesday', 'Wednesday',
                           'Thursday', 'Friday', 'Saturday'], ordered=True)

    df_bks_harian["month"] = df_bks_harian.dteday.apply(lambda x: x.strftime('%B'))
    month = pd.CategoricalDtype(['January', 'February', 'March', 'April',
                           'May', 'June', 'July', 'August', 'September',
                           'October', 'November', 'December'], ordered=True)

    df_bks_harian["year"] = df_bks_harian.dteday.apply(lambda x: x.strftime('%Y'))
    year = pd.CategoricalDtype(['2011', '2012'])

    # Mengubah day ke tipe category
    df_bks_harian = df_bks_harian.astype({"day":day, "month":month, "year":year})

    #filter data jumlah penyewa sepeda untuk bulan Desember 2012
    if tahun == '2011':
        if bulan   == 'January':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2011-01-01") & (df_bks_harian["dteday"] < "2011-02-01") ]
        elif bulan == 'February':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2011-02-01") & (df_bks_harian["dteday"] < "2011-03-01") ]
        elif bulan == 'March':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2011-03-01") & (df_bks_harian["dteday"] < "2011-04-01") ]
        elif bulan == 'April':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2011-04-01") & (df_bks_harian["dteday"] < "2011-05-01") ]
        elif bulan == 'May':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2011-05-01") & (df_bks_harian["dteday"] < "2011-06-01") ]
        elif bulan == 'June':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2011-06-01") & (df_bks_harian["dteday"] < "2011-07-01") ]
        elif bulan == 'July':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2011-07-01") & (df_bks_harian["dteday"] < "2011-08-01") ]
        elif bulan == 'August':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2011-08-01") & (df_bks_harian["dteday"] < "2011-09-01") ]
        elif bulan == 'September':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2011-09-01") & (df_bks_harian["dteday"] < "2011-10-01") ]
        elif bulan == 'October':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2011-10-01") & (df_bks_harian["dteday"] < "2011-11-01") ]
        elif bulan == 'November':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2011-11-01") & (df_bks_harian["dteday"] < "2011-12-01") ]
        elif bulan == 'December':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2011-12-01") & (df_bks_harian["dteday"] < "2012-01-01") ]
    elif tahun == '2012':
        if bulan   == 'January':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2012-01-01") & (df_bks_harian["dteday"] < "2012-02-01") ]
        elif bulan == 'February':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2012-02-01") & (df_bks_harian["dteday"] < "2012-03-01") ]
        elif bulan == 'March':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2012-03-01") & (df_bks_harian["dteday"] < "2012-04-01") ]
        elif bulan == 'April':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2012-04-01") & (df_bks_harian["dteday"] < "2012-05-01") ]
        elif bulan == 'May':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2012-05-01") & (df_bks_harian["dteday"] < "2012-06-01") ]
        elif bulan == 'June':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2012-06-01") & (df_bks_harian["dteday"] < "2012-07-01") ]
        elif bulan == 'July':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2012-07-01") & (df_bks_harian["dteday"] < "2012-08-01") ]
        elif bulan == 'August':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2012-08-01") & (df_bks_harian["dteday"] < "2012-09-01") ]
        elif bulan == 'September':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2012-09-01") & (df_bks_harian["dteday"] < "2012-10-01") ]
        elif bulan == 'October':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2012-10-01") & (df_bks_harian["dteday"] < "2012-11-01") ]
        elif bulan == 'November':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2012-11-01") & (df_bks_harian["dteday"] < "2012-12-01") ]
        elif bulan == 'December':
            df_bks_harian = df_bks_harian.loc[ (df_bks_harian["dteday"] >= "2012-12-01") & (df_bks_harian["dteday"] <= "2012-12-31") ]

    df_bks_harian.rename(columns={
                            "cnt": "mean"
                            }, inplace=True)

    # Mengelompokkan data berdasarkan hari dan di rata-rata nilainya
    df_bks_harian_mean = df_bks_harian.groupby(["day"])["mean"].mean().reset_index()

    return df_bks_harian_mean


def value_hari_value_max(df):
    # ambil value hari yang rata-rata tinggi
    day_penyewaan_sepeda  = df["day"].loc[ df["mean"] == df["mean"].max() ]
    day_penyewaan_sepeda  = day_penyewaan_sepeda.values
    listToStr = ' '.join(day_penyewaan_sepeda)
    hari = konversi_day_ke_hari(listToStr)
    # ambil value max dari hari
    max_value_penyewaan_sepeda  = df["mean"].max()
    max_value_penyewaan_sepeda  = cek_empty_value(max_value_penyewaan_sepeda)
    return hari,max_value_penyewaan_sepeda 
    


#input dataset
df_bks_data = pd.read_csv("df_bks_data.csv")

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
tren_penyewaan_sepeda_df        = membuat_tren_penyewaan_sepeda(main_df)
penyewaan_sepeda_by_cuaca       = berdasarkan_kondisi_cuaca(main_df)
penyewaan_sepeda_by_musim_2011  = berdasarkan_kondisi_musim_2011(df_bks_data)
penyewaan_sepeda_by_musim_2012  = berdasarkan_kondisi_musim_2012(df_bks_data)



# Visualisasi Dasbor
st.header('Dasbor Penyewaan Sepeda :sparkles:')

st.divider() 

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

st.divider() 

#Berdasarkan kondisi cuaca
st.subheader('Jumlah Penyewa Sepeda berdasarkan Kondisi Cuaca 2011-2012')

st.text('Jumlah Penyewa Sepeda')

col7, col8, col9, col10 = st.columns(4)

with col7:
    weathersit_1  = penyewaan_sepeda_by_cuaca["count"].loc[ penyewaan_sepeda_by_cuaca["weathersit"] == 1 ]
    value_weathersit_1  = weathersit_1.values
    value_weathersit_1  = cek_empty_value(value_weathersit_1)
    st.metric(label="Kondisi Cuaca [1]", value=value_weathersit_1)

with col8:
    weathersit_2  = penyewaan_sepeda_by_cuaca["count"].loc[ penyewaan_sepeda_by_cuaca["weathersit"] == 2 ]
    value_weathersit_2  = weathersit_2.values
    value_weathersit_2  = cek_empty_value(value_weathersit_2)
    st.metric(label="Kondisi Cuaca [2]", value=value_weathersit_2)

with col9:
    weathersit_3  = penyewaan_sepeda_by_cuaca["count"].loc[ penyewaan_sepeda_by_cuaca["weathersit"] == 3 ]
    value_weathersit_3  = weathersit_3.values
    value_weathersit_3  = cek_empty_value(value_weathersit_3)
    st.metric(label="Kondisi Cuaca [3]", value=value_weathersit_3)

with col10:
    weathersit_4  = penyewaan_sepeda_by_cuaca["count"].loc[ penyewaan_sepeda_by_cuaca["weathersit"] == 4 ]
    value_weathersit_4  = weathersit_4.values
    value_weathersit_4  = cek_empty_value(value_weathersit_4)
    st.metric(label="Kondisi Cuaca [4]", value=value_weathersit_4)


# bar chart jumlah penyewaan sepeda berdasarkan kondisi cuaca
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=penyewaan_sepeda_by_cuaca, x="weathersit", y="count", color="peru")
sns.despine()
ticks_loc = ax.get_yticks().tolist()
ax.set_yticks(ax.get_yticks().tolist())
ax.set_yticklabels(['{:,.0f}'.format(x) for x in ticks_loc])
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

st.divider() 

#Berdasarkan kondisi musim
st.subheader('Jumlah Penyewa Sepeda berdasarkan Kondisi Musim')

#menampilkan jumlah penyewaan sepeda berdasarkan musim di tahun 2011-2012
tahunku = st.selectbox(
    label="Yuk cari tahu jumlah penyewaan sepeda per musim di tahun?",
    key = 1,
    options=('Pilih tahun',
             '2011', 
             '2012', 
             )
)

col11, col12, col13, col14 = st.columns(4)
col15, col16, col17, col18 = st.columns(4)

if tahunku == '2011':
    with col11:
        value_springer  = penyewaan_sepeda_by_musim_2011["count"].loc[ penyewaan_sepeda_by_musim_2011["season_cat"] == "springer" ]
        value_springer  = value_springer.values
        value_springer  = cek_empty_value(value_springer)
        st.metric(label="[Springer] Musim Semi", value=value_springer)
    with col12:
        value_summer    = penyewaan_sepeda_by_musim_2011["count"].loc[ penyewaan_sepeda_by_musim_2011["season_cat"] == "summer" ]
        value_summer    = value_summer.values
        value_summer    = cek_empty_value(value_summer)
        st.metric(label="[Summer] Musim Panas", value=value_summer)
    with col13:
        value_fall      = penyewaan_sepeda_by_musim_2011["count"].loc[ penyewaan_sepeda_by_musim_2011["season_cat"] == "fall" ]
        value_fall      = value_fall.values
        value_fall      = cek_empty_value(value_fall)
        st.metric(label="[Fall] Musim Gugur", value=value_fall)
    with col14:
        value_winter    = penyewaan_sepeda_by_musim_2011["count"].loc[ penyewaan_sepeda_by_musim_2011["season_cat"] == "winter" ]
        value_winter    = value_winter.values
        value_winter    = cek_empty_value(value_winter)
        st.metric(label="[Winter] Musim Dingin", value=value_winter)

    # bar chart jumlah penyewaan sepeda berdasarkan kondisi musim
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=penyewaan_sepeda_by_musim_2011, x="season_cat", y="count", color="peru")
    ax.set_title('Jumlah Penyewa Sepeda per Musim di Tahun 2011', loc='left', pad=30, fontsize=15, color='peru')
    ticks_loc = ax.get_yticks().tolist()
    ax.set_yticks(ax.get_yticks().tolist())
    ax.set_yticklabels(['{:,.0f}'.format(x) for x in ticks_loc])
    ax.set_xlabel('Musim', fontsize=15, color='blue')
    ax.set_ylabel('Jumlah Penyewa Sepeda', fontsize=15, color='blue')
    st.pyplot(fig) 

elif tahunku == '2012':
    with col15:
        value_springer  = penyewaan_sepeda_by_musim_2012["count"].loc[ penyewaan_sepeda_by_musim_2012["season_cat"] == "springer" ]
        value_springer  = value_springer.values
        value_springer  = cek_empty_value(value_springer)
        st.metric(label="[Springer] Musim Semi", value=value_springer)
    with col16:
        value_summer    = penyewaan_sepeda_by_musim_2012["count"].loc[ penyewaan_sepeda_by_musim_2012["season_cat"] == "summer" ]
        value_summer    = value_summer.values
        value_summer    = cek_empty_value(value_summer)
        st.metric(label="[Summer] Musim Panas", value=value_summer)
    with col17:
        value_fall      = penyewaan_sepeda_by_musim_2012["count"].loc[ penyewaan_sepeda_by_musim_2012["season_cat"] == "fall" ]
        value_fall      = value_fall.values
        value_fall      = cek_empty_value(value_fall)
        st.metric(label="[Fall] Musim Gugur", value=value_fall)
    with col18:
        value_winter    = penyewaan_sepeda_by_musim_2012["count"].loc[ penyewaan_sepeda_by_musim_2012["season_cat"] == "winter" ]
        value_winter    = value_winter.values
        value_winter    = cek_empty_value(value_winter)
        st.metric(label="[Winter] Musim Dingin", value=value_winter)

    # bar chart jumlah penyewaan sepeda berdasarkan kondisi musim
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=penyewaan_sepeda_by_musim_2012, x="season_cat", y="count", color="peru")
    ax.set_title('Jumlah Penyewa Sepeda per Musim di Tahun 2012', loc='left', pad=30, fontsize=15, color='peru')
    ticks_loc = ax.get_yticks().tolist()
    ax.set_yticks(ax.get_yticks().tolist())
    ax.set_yticklabels(['{:,.0f}'.format(x) for x in ticks_loc])
    ax.set_xlabel('Musim', fontsize=15, color='blue')
    ax.set_ylabel('Jumlah Penyewa Sepeda', fontsize=15, color='blue')
    st.pyplot(fig)


st.divider() 

#Rata-rata jumlah penyewa sepeda per minggu di tahun 2011-2012
st.subheader('Rata-rata Jumlah Penyewa Sepeda per hari di tahun 2011-2012')

nilai_tahun = st.selectbox(
    label="Cari tahu rata-rata jumlah penyewaan sepeda di tahun?",
    key = 2,
    options=('Pilih tahun',
             '2011', 
             '2012', 
             )
)

# inisialisasi variabel
bulan = ''
tahun = nilai_tahun
dataku = []

button_id1 = (i for i in range (1,100))
button_id2 = (i for i in range (200, 300))


# Fungsi menampilkan button
def fungsiku(df, tahun):
    col19, col20, col21, col22, col23, col24= st.columns(6)
    col25, col26, col27, col28, col29, col30= st.columns(6)
    if tahun == '2011':
        with col19:
            if st.button("January", key=next(button_id1)):
                bulan = 'January'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col20:
            if st.button("February", key=next(button_id1)):
                bulan = 'February'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col21:
            if st.button("March", key=next(button_id1)):
                bulan = 'March'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col22:
            if st.button("April", key=next(button_id1)):
                bulan = 'April'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col23:
            if st.button("May", key=next(button_id1)):
                bulan = 'May'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col24:
            if st.button("June", key=next(button_id1)):
                bulan = 'June'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col25:
            if st.button("July", key=next(button_id1)):
                bulan = 'July'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col26:
            if st.button("August", key=next(button_id1)):
                bulan = 'August'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col27:
            if st.button("September", key=next(button_id1)):
                bulan = 'September'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col28:
            if st.button("October", key=next(button_id1)):
                bulan = 'October'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col29:
            if st.button("November", key=next(button_id1)):
                bulan = 'November'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col30:
            if st.button("December", key=next(button_id1)):
                bulan = 'December'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
    elif tahun == '2012':
        with col19:
            if st.button("January", key=next(button_id2)):
                bulan = 'January'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col20:
            if st.button("February", key=next(button_id2)):
                bulan = 'February'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col21:
            if st.button("March", key=next(button_id2)):
                bulan = 'March'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col22:
            if st.button("April", key=next(button_id2)):
                bulan = 'April'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col23:
            if st.button("May", key=next(button_id2)):
                bulan = 'May'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col24:
            if st.button("June", key=next(button_id2)):
                bulan = 'June'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col25:
            if st.button("July", key=next(button_id2)):
                bulan = 'July'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col26:
            if st.button("August", key=next(button_id2)):
                bulan = 'August'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col27:
            if st.button("September", key=next(button_id2)):
                bulan = 'September'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col28:
            if st.button("October", key=next(button_id2)):
                bulan = 'October'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col29:
            if st.button("November", key=next(button_id2)):
                bulan = 'November'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]
        with col30:
            if st.button("December", key=next(button_id2)):
                bulan = 'December'
                rata_rata_penyewaan_sepeda = rata_rata_jumlah_per_hari(df, bulan, tahun)
                return [rata_rata_penyewaan_sepeda, bulan, tahun]


# Membuat visualisasi rata-rata jumlah penyewa sepeda per hari
def membuat_visualisasiku(df, bulan, tahun):
    #visualisasi rata-rata jumlah penyewa sepeda per hari
    fig, ax = plt.subplots(figsize=(10,5))
    sns.barplot(data=df, x="day", y="mean", color="peru")
    ax.set_title(f'Rata-rata Jumlah Penyewa Sepeda per hari di bulan {bulan} (tahun {tahun})', loc='left', pad=30, fontsize=15, color='orange')
    ticks_loc = ax.get_yticks().tolist()
    ax.set_yticks(ax.get_yticks().tolist())
    ax.set_yticklabels(['{:,.0f}'.format(x) for x in ticks_loc])
    ax.set_xlabel('Hari', fontsize=15, color='blue')
    ax.set_ylabel('Jumlah Penyewa Sepeda', fontsize=15, color='blue')
    st.pyplot(fig)


# Proses menampilkan visualisasi rata-rata jumlah penyewa sepeda per hari 
if nilai_tahun is "Pilih tahun":
    st.text("Silahkan Pilih Tahun")
elif nilai_tahun is "2011":
    dataku = fungsiku(df_bks_data,tahun)
    if dataku is not None:
        membuat_visualisasiku(dataku[0], dataku[1], dataku[2])
        nilai_hari,nilai_max = value_hari_value_max(dataku[0])
        st.text("Pada Bulan {} {} Rata-rata Jumlah Penyewa Sepeda Tertinggi terdapat di hari {} dengan jumlah rata-rata {}".format(dataku[1], dataku[2], nilai_hari, nilai_max))
    else:
        st.text("Silahkan Pilih Bulan")
elif nilai_tahun is "2012":
    dataku = fungsiku(df_bks_data,tahun)
    if dataku is not None:
        membuat_visualisasiku(dataku[0], dataku[1], dataku[2])
        nilai_hari,nilai_max = value_hari_value_max(dataku[0])
        st.text(f"Pada Bulan {dataku[1]} {dataku[2]} Rata-rata Jumlah Penyewa Sepeda Tertinggi terdapat di hari {nilai_hari} dengan jumlah rata-rata {nilai_max}")
    else:
        st.text("Silahkan Pilih Bulan")