from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from datetime import datetime

class KpssSayacApp(App):
    def build(self):
        # KPSS 2026 Genel Kültür - Genel Yetenek Tarihi: 26 Temmuz 2026 Saat 10:15
        self.sinav_tarihi = datetime.strptime("2026-07-26 10:15:00", "%Y-%m-%d %H:%M:%S")
        
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        layout.add_widget(Label(text="KPSS'YE KALAN SÜRE", font_size='28sp', bold=True))
        
        self.label_sure = Label(text="", font_size='36sp', bold=True)
        layout.add_widget(self.label_sure)
        
        Clock.schedule_interval(self.guncelle, 1.0)
        return layout

    def guncelle(self, dt):
        kalan_sure = self.sinav_tarihi - datetime.now()
        if kalan_sure.total_seconds() <= 0:
            self.label_sure.text = "Sınav Zamanı Geldi!\nBaşarılar Annem!"
        else:
            toplam_saniye = int(kalan_sure.total_seconds())
            gun = toplam_saniye // 86400
            saat = (toplam_saniye % 86400) // 3600
            dakika = (toplam_saniye % 3600) // 60
            saniye = toplam_saniye % 60
            
            self.label_sure.text = f"{gun} Gün\n{saat} Saat\n{dakika} Dakika\n{saniye} Saniye"

if __name__ == '__main__':
    KpssSayacApp().run()
