"""
Aplikasi Deteksi Gempa Terkini
"""
import gempaterkini

if __name__ == '__main__':
    print('Dashboard Monitoring')
    result = gempaterkini.ekstrasi_data()
    gempaterkini.tampilan_data(result)


