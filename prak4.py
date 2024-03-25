class Student:
    def __init__(self, nama, nim=None, nilai=None):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

    def set_nim(self, nim):
        self.nim = nim

    def set_nilai(self, nilai):
        self.nilai = nilai

    def print_data(self):
        print('Nama:', self.nama)
        print('NIM:', self.nim)
        print('Nilai:', self.nilai)

    @staticmethod
    def teman():
        teman1 = Student("Francisco", "064002300044", "90")
        teman2 = Student("Rombon", "064002300045", "85")
        teman3 = Student("Michael", "064002300046", "80")
        return [teman1, teman2, teman3]

print('--- Data Pribadi ---')
data_pribadi = Student("Faiz", "064002300043", "100")
data_pribadi.print_data()

teman_list = Student.teman()
no_teman = 1  
for teman in teman_list:
    print(f'\n--- Data Teman {no_teman} ---')
    teman.print_data()
    no_teman += 1 