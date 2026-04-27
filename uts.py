import pandas as pd
import os
import psycopg2

nilai = os.getenv('DATA_NILAI', '85,90,78,92,88,95,80,100')
nilai_list = list(map(int, nilai.split(',')))

data = {'Nilai': nilai_list}
df = pd.DataFrame(data)

print('---Nilai Mahasiswa---')
print('Rata-rata nilai:', df['Nilai'].mean())
print('Nilai Terendah:', df['Nilai'].min())
print('Nilai tertinggi:', df['Nilai'].max())

# Simpan hasil ke file CSV
df.to_csv('hasil_nilai.csv', index=False)
print('Hasil nilai telah disimpan ke file hasil_nilai.csv')
print('Selesai')

# Simpan hasil ke database PostgreSQL
# Simpan hasil ke database PostgreSQL
try:
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'db'),
        database=os.getenv('DB_NAME', 'nilai_db'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASS', 'password'),
        port=os.getenv('DB_PORT', '5432')
    )

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nilai_mahasiswa (
            id SERIAL PRIMARY KEY,
            nilai INTEGER
        )
    """)

    # Menyimpan semua nilai ke database
    for nilai in nilai_list:
        cursor.execute(
            "INSERT INTO nilai_mahasiswa (nilai) VALUES (%s)",
            (nilai,)
        )

    conn.commit()

    print("Data berhasil disimpan ke PostgreSQL")

    cursor.close()
    conn.close()

except Exception as e:
    print("Terjadi error:", e)
