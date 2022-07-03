"""
Aplikasi Deteksi Gempa Terkini
"""


def ekstrasi_data():
    """
    Info Gempa Mag:5.3, 03-Jul-22 06:49:13 WIB, Lok:1.05 LU, 126.12 BT (119 km Tenggara BITUNG-SULUT), Kedlmn:10 Km #BMKG
    :return:
    """
    hasil = dict()
    hasil['Mag'] = 5.3
    hasil['Tanggal'] = '03-Jul-22'
    hasil['Waktu'] = '06:49:13 WIB'
    hasil['Lok'] = {'LU':1.05,'BT':126.12,'Daerah': '119 km Tenggara BITUNG-SULUT'}
    hasil['Kedlmn'] = '10 Km'
    return hasil


def tampilan_data(result):
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Magnitudo   {result['Mag']}")
    print(f"Tanggal     {result['Tanggal']}")
    print(f"Waktu       {result['Waktu']}")
    print(f"Lokasi      LU={result['Lok']['LU']} BT={result['Lok']['BT']} Daerah={result['Lok']['Daerah']} ")
    print(f"Kedalaman   {result['Kedlmn']}")
    pass


if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstrasi_data()
    tampilan_data(result)


