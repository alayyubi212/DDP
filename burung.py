from Animal import *

class burung (Animal) :
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self. jenis = jenis
        self. bunyi = bunyi

    def cetak_burung (self):
        super ().cetak ()
        print("jenis \t\t\t\t\t: ",self. jenis,
        "\nbunyi \t\t\t\t\t : " ,self. bunyi)

perkutuk = burung ("perkutuk", "jagung", "alam terbuka", "bertelur", "jalak jawa", "perkutuk")
perkutuk.cetak_burung()

beo = burung ("beo", "buah", "alam terbuka", "bertelur", "jawa", "ckukukur")
beo.cetak_burung ()

