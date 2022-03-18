class Keluarga:
	def __init__(self, inputBapak, inputIbu, inputKakak):
		self.bapak = inputBapak
		self.Ibu = inputIbu
		self.Kakak = inputKakak
		
Keluarga1 = Keluarga("Wahyu Andriawan", "Nur1", "Pertama")
Keluarga2 = Keluarga("Wahyu", "Nur2", "Kedua") 
print(Keluarga1.bapak)
print(Keluarga2.bapak)