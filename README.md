# Machine Learning
![purwadhika](./storage/Logo.png)
#

# Heart-Machine-Learning-Project 
Dataset yang digunakan adalah heart.csv

### Problem
Ingin mengetahui apakah seseorang tersebut menderita penyakit jantung dilihat dari usia, jenis kelamin, dan tekanan darah pasien

#
### Goals
Dapat memprediksi seseorang tersebut menderita penyakit jantung apa tidak dilihat dari usia, jenis kelamin, tekanan darah, kolestrol, gula darah, dan beberapa variabel lainnya

#
### Data Visualization
**Dataset**
![dataset](./storage/Dataset.png)

**Describe Data**
![describe_data](./storage/Heart.png)

**Jumlah penderita penyakit jantung pada dataset**
![jumlah_penderita](./storage/jumlah_penderita.png)

**Jumlah penderita berdasarkan gender**
![gender](./storage/jumlah_gender.png)

**Jumlah penderita pada dataset berdasarkan usia**
![usia](./storage/jumlah_usia.png)

**Penderita dilihat dari usia dan tekanan darah**
![usia><tekanan_darah](./storage/usia_tekanandarah.png)

**Penderita dilihat dari usia dan denyut nadi**
![usia><nadi](./storage/usia_nadi.png)

**Korelasi Variabel**
![korelasi](./storage/korelasi_variabel.png)

#
### Evaluation Metrics
**Menggunakan RandomForestClassifier**
![EM](./storage/Evaluation_metrics.png)

#
### Kesimpulan dan Saran
**Kesimpulan**
- Lebih dari 50% dari data, menderita penyakit jantung
- Jenis kelamin laki-laki lebih berisiko terkena penyakit jantung
- Usia lebih tua juga lebih rentan terkena penyakit jantung
- Pasien dengan tekanan darah tinggi, belum tentu memiliki penyakit jantung
- Pasien dengan denyut nadi yang tinggi kemungkinan memiliki penyakit jantung
- Digunakan model randomforest karena memiliki score balance accuracy tertinggi

**Saran**
- Kemungkinan dapat menambah beberapa feature lainnya, dikarenakan penyakit jantung tidak akurat jika dilihat dari features-features yang ada
- Kemungkinan dapat menambahkan feature genetik, uji stress, penyakit sistemik lainnya, merokok, konsumsi alkohol, BMI
- Untuk pemeriksaan menggunakan machine ini kemungkinan diperlukan alat lain, karena adanya pemeriksaan tekanan darah, kolestrol, ekg, dan lain-lain

#
### Dashboard
#### Home
![home](./storage/home.png)

#### Prediksi
![prediksi](./storage/prediksi.png)

#### Hasil
![hasil](./storage/hasil.png)
*saya stuck dibagian dashboard hasil, tidak bisa mengimport ke python. bolak-balik nyoba joblib dan pickle tetap error saat import model*

#### Data Visualization
![Data](./storage/data_vis.png)
