class Grader:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

    def tentukan_grade(self):
        if 80.00 <= self.nilai <= 100:
            return 'A'
        elif 77.00 <= self.nilai <= 79.99:
            return 'A-'
        elif 74.00 <= self.nilai <= 76.99:
            return 'B+'
        elif 68.00 <= self.nilai <= 73.99:
            return 'B'
        elif 65.00 <= self.nilai <= 67.99:
            return 'B-'
        elif 62.00 <= self.nilai <= 64.99:
        	return 'C+'
        elif 56.00 <= self.nilai <= 61.99:
        	return 'C'
        elif 45.00 <= self.nilai <= 55.99:
        	return 'D'
        elif 0 <= self.nilai < 44.99:
        	return 'E'
        else:
            return 'Nilai tidak valid'

def main():
    nama = input("Nama: ")
    nim = int(input("Nim: "))
    nilai = float(input("Masukkan nilai: "))
    grade = Grader(nama, nim, nilai)
    print('\n--- DATA PRAKTIKAN PBO 2024 ---')
    print(f"Nama: {grade.nama}\nNim: {grade.nim}\nGrade: {grade.tentukan_grade()}")

if __name__ == "__main__":
    main()
