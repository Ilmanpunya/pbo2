#ilman nafis al-fariq
#R4
#210511144

class Youtube:
    def __init__(self, chanel, kategori):
        self.chanel = chanel
        self.kategori = kategori
    def streamer(self):
        print(self.chanel, "sedang membuat konten")
class Artis:
    def __init__(self,chanel, nama):
        self.chanel = chanel
        self.nama = nama
    def tampil(self):
        print(self.nama, "sedang tampil di Tv")
class YoutubeArtis(Youtube, Artis):
    def __init__(self, chanel, kategori, nama):
        Youtube.__init__(self,chanel,kategori)
        Artis.__init__(self, chanel, nama)
    def streaming(self):
        print("youtube",self.chanel, "sedang reaction", self.kategori)

yt_artis = YoutubeArtis("S.P.J", "MPL", "EKO")
yt_artis.streamer()
yt_artis.tampil()
yt_artis.streaming()