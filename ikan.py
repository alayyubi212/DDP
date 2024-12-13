from Animal import *

class ikan (Animal) :
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self. jenis = jenis
        self. bunyi = warna

    def cetak_ikan (self):
        super ().cetak()
        print("jenis \t\t\t\t\t: ",self. jenis,
        "\nwarna \t\t\t\t\t : " ,self. warna)

muajair = ikan("mujair", "pelet", "air", "bertelur", "mujair red", "merah")
muajair.cetak_ikan()

nila = ikan("nila", "pelet", "air", "bertelur", "bangkok", "merah")
nila.cetak_ikan()
