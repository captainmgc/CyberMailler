# Cyber-Mailler

Güclü bir mail sunucu test aracı. E-posta sunucu yapılandırmalarını doğrulamak ve e-posta teslim yeteneklerini test etmek için tasarlanmıştır.

![Cyber-Mailler Logo](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWOaJq4YDvqsSE-XvTOb5vi10k72wjqhBCT_Vmd6HwqjpEzjVotfk3M2TOxzDi8IAT1yjfEyECVVlxkh0gfgCb8BonJhEBAmCxBg9lFA7M5BcSZk7XU9uMlI4tAaH2PMb7uB1F4gAm_HC8V5wkc8I5WnXSj9t50CJiO1fn-hq_Ib207FR7sjOGiRy9m7A/s320/logo-cybermailler.jpg)

## 🚀 Özellikler

- Birden fazla e-posta test servisi desteği
- Doğrudan SMTP sunucu testi
- MX kaydı doğrulaması
- API anahtarı gerektirmeyen kullanım
- Animasyonlu terminal arayüzü
- Çoklu iş parçacığı (multi-thread) ile servis kontrolü

## 📋 Gereksinimler

- Python 3.7 veya daha üstü
- Windows/Linux/MacOS

## 🔧 Kurulum

1. Depoyu klonlayın:
```bash
 git clone https://github.com/captainmgc/CyberMailler.git
```

2. Gerekli paketleri yükleyin:
```bash
 pip install -r requirements.txt
```

## 💻 Kullanım

Script'i çalıştırın:
```bash
 python cyber-mailler.py
```

Etkileşimli komut istemini takip edin:
1. Bir mail test servisi seçin
2. Alıcı e-posta adresini girin
3. Konu ve mesaj içeriğini sağlayın
4. Test sonuçlarını görüntüleyin

## 🛠️ Kullanılabilir Servisler

- **FormSubmit** - API anahtarı gerektirmeyen form-email dönüştürücü
- **Anonymous Email** - Basit web tabanlı form gönderimi
- **Web Form** - HTML form gönderimi tekniği
- **Direct SMTP** - Alıcının mail sunucusunu doğrudan test eder

## 📷 Ekran Görüntüleri

Aşağıdaki görseller, uygulamanın çalışma sürecini göstermektedir:

1. ![Ekran 1](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg2lfjHhVX_xBKXWLuW2PCeCqSVSOxkxc1R_gCyY5O85EsO_gQWlhIwjG65_6VQWeNW3aRC5Z3ybkg3lfR0lJV8KwoTuN6-7wVi2f_kuiGyly7kw7P4GMsq8r55xJYmDnLCvNuW-PsIZI5tF_qHarnrqbrKAkt-uoljbxZVMu-eWXHGDGDxrIYP-9SK_Jo/s16000/ekran1.png)

2. ![Ekran 2](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiM9SrBpQUKIuVGUZZfrhBOlQdQOTRuiujWYDMhO_9CNf3bUH-aZwuKImV0z2Tj0g-GDjya_r5-nYftMJpObZWqvFZefsdfdIfPeKM-po1TPOwSB-AHqIS1j85CUmYz5TRG3lj7KqL-PpxYIrPudYMdfVqcCMDTaqGDcDv8cHxhaixMmHFgmce_X-hHJX8/s16000/ekran2.png)

3. ![Ekran 3](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcdNi0mRifbmBuFwWB-A1iTKm8XXqN83uYVNz_NM6ivDu8cv_sBvc6QTPKF6fJKd5VLDw1ocM2ierA57ic7jiUUnHqg01LOyBAYrYsEh5leUZAobUa7QsLhGTTe5j72dywfk56u9zP0di6vH2zCrYuHgkDbcuTPQRU5RJ-XRUdQ10AeFK1GnxjltaaH7k/s16000/ekran3.png)

## ⚠️ Önemli Notlar

- Modern e-posta sistemleri güçlü spam önleme önlemlerine sahiptir.
- Test e-postaları spam klasörüne düşebilir veya tamamen engellenebilir.
- Bu araç yalnızca test amaçlı tasarlanmıştır.
- Bazı servisler ek yapılandırmalar gerektirebilir.

## 🔒 Güvenlik

Bu araç yalnızca yasal test amaçlı tasarlanmıştır. Lütfen e-posta sunucularını test etmeden önce uygun izinlere sahip olduğunuzdan emin olun.

## 📝 Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır. Detaylar için LICENSE dosyasına bakabilirsiniz.

## 🤝 Katkıda Bulunma

Geliştirmeler, hata bildirimleri ve yeni özellik talepleri memnuniyetle karşılanır!

## ⭐ Destek

Eğer bu aracı faydalı bulduysanız, GitHub deposuna ⭐ vererek destek olabilirsiniz!
