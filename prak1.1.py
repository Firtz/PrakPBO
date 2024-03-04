class Kalkulator:
    def __init__(self):
        self.numb1 = 0
        self.numb2 = 0

    def input_angka(self):
        self.numb1 = float(input('Masukan angka Pertama: '))
        self.numb2 = float(input('Masukan angka kedua: '))

    def tambah(self):
        return self.numb1 + self.numb2

    def tampilkan_hasil(self, hasil):
        print(f'Hasil penjumlahan: {hasil}')


def main():
    print('=======Kalkulator Penjumlahan=======\n')
    kalkulator = Kalkulator()  
    kalkulator.input_angka()  
    hasil = kalkulator.tambah()  
    kalkulator.tampilkan_hasil(hasil)  


if __name__ == "__main__":
    main()
