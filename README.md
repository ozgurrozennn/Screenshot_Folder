markdown# Ekran Görüntüsü Programı

Basit ve şık bir ekran görüntüsü alma uygulaması. Global klavye kısayolları ve modern şeffaf arayüz ile hızlı ekran görüntüsü almanızı sağlar.

## Özellikler

- Print Screen veya Ctrl+Shift+S ile hızlı ekran görüntüsü alma
- Modern şeffaf cam efektli arayüz
- Otomatik dosya adlandırma (tarih ve saat damgalı)
- Özelleştirilebilir kayıt konumu
- Kullanıcı dostu basit tasarım

## Kurulum

### Gereksinimler

Python 3.7 veya üzeri gereklidir.

### Bağımlılıkları Yükleme
```bash
pip install -r requirements.txt
```

Gerekli paketler:
- Pillow
- pyautogui
- keyboard

## Kullanım

Programı başlatmak için:
```bash
python ekran_kayit_basit.py
```

### Ekran Görüntüsü Alma

1. **Buton ile:** Programdaki "Ekran Görüntüsü Al" butonuna tıklayın
2. **Klavye ile:** Print Screen veya Ctrl+Shift+S tuşlarına basın

### Kayıt Konumunu Değiştirme

- Program açıldığında otomatik olarak klasör seçimi yapabilirsiniz
- "Seç" butonu ile istediğiniz zaman konumu değiştirebilirsiniz

## Dosya Adlandırma

Ekran görüntüleri otomatik olarak şu formatta adlandırılır:
```
screenshot_20231205_143025.png
```

Format: `screenshot_YYYYMMDD_HHMMSS.png`

## Klavye Kısayolları

| Kısayol | Fonksiyon |
|---------|-----------|
| Ctrl+Shift+S | Sessiz ekran görüntüsü al |

Not: Sessiz modda bildirim penceresi açılmaz, sadece durum çubuğunda bilgi gösterilir.

## Teknik Detaylar

- **Dil:** Python 3
- **GUI Framework:** Tkinter
- **Görüntü İşleme:** PIL (Pillow)
- **Ekran Yakalama:** pyautogui, ImageGrab
- **Global Hotkey:** keyboard

## Sorun Giderme

### Global hotkey çalışmıyor
Programı yönetici olarak çalıştırmayı deneyin (Windows).

### Import hatası
Tüm bağımlılıkların kurulu olduğundan emin olun:
```bash
pip install -r requirements.txt
