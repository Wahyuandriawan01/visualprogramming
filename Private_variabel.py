class data():
    _produk = 50 # private
 
    def __init__(self, nama_produk):
        self.nama = nama_produk
 
    def harga_produk(self,harga_Produk):
       hasil = self._produk * harga_Produk
       return hasil
 
Barang = data("Beras")
print(Barang.harga_produk(250000))
