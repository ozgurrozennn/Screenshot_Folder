import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageGrab
import pyautogui
from datetime import datetime
import os
import keyboard


class EkranGoruntsuProgrami:
    def __init__(self, root):
        self.root = root
        self.root.title("Ekran Görüntüsü Programı")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        self.root.attributes("-alpha", 0.95)
        self.root.configure(bg="#f0f0f0")

        self.kayit_yolu = None

        self.gui_olustur()

        self.root.after(100, self.ilk_klasor_sec)

    def gui_olustur(self):
        ana_frame = tk.Frame(self.root, bg='#f0f0f0')
        ana_frame.pack(fill='both', expand=True)

        baslik = tk.Label(ana_frame, text='Ekran Görüntüsü Programı',
                          font=('Arial', 18, 'bold'), bg="#f0f0f0", fg='#2c3e50')
        baslik.pack(pady=20)

        kisayol_label = tk.Label(ana_frame, text='CTRL + SHİFT + S tuşu ile hızlı ekran görüntüsü',
                                 font=('Arial', 9), fg='#7f8c8d', bg='#f0f0f0')
        kisayol_label.pack(pady=5)

        yol_frame = tk.Frame(ana_frame, bg="#f0f0f0")
        yol_frame.pack(pady=10, padx=20, fill='x')

        tk.Label(yol_frame, text='Kayıt Yolu:', font=('Arial', 10),
                 bg='#f0f0f0').pack(side='left')

        self.yol_label = tk.Label(yol_frame, text='Klasör Seçilmedi',
                                  font=('Arial', 9), fg='#555555',
                                  bg='#ffffff',
                                  relief='flat',
                                  width=35, anchor='w', padx=5,
                                  borderwidth=1, highlightthickness=1,
                                  highlightbackground='#cccccc')
        self.yol_label.pack(side='left', padx=5)

        yol_btn = tk.Button(yol_frame, text='Seç',
                            command=self.yol_sec,
                            bg='#3498db', fg='white',
                            font=('Arial', 9, 'bold'),
                            relief='flat', cursor='hand2')
        yol_btn.pack(side='left')

        tk.Frame(ana_frame, height=1, bg='#dddddd').pack(fill='x', pady=20)

        screenshot_frame = tk.Frame(ana_frame, bg="white", relief='flat', bd=0)
        screenshot_frame.pack(pady=10, padx=30, fill='x')

        tk.Label(screenshot_frame, text='Ekran Görüntüsü',
                 font=('Arial', 12, 'bold'), bg='white', fg='#2c3e50').pack(pady=10)

        tk.Button(screenshot_frame, text='Ekran Görüntüsü Al',
                  command=self.screenshot_al,
                  bg='#27ae60', fg='white',
                  font=('Arial', 11, 'bold'),
                  width=25, height=2, relief='flat',
                  cursor='hand2').pack(pady=10)

        self.durum_label = tk.Label(ana_frame, text='Hazır',
                                    font=('Arial', 10), fg='#7f8c8d', bg='#f0f0f0')
        self.durum_label.pack(pady=10)

        try:
            keyboard.add_hotkey('print screen', self.prtsc_basildi)
            keyboard.add_hotkey('ctrl+shift+s', self.prtsc_basildi)
            print('Global hotkeyler kaydedildi: Print Screen, Ctrl+Shift+S')
        except Exception as e:
            print(f'Hotkey kaydı hatası: {e}')
            self.root.bind('<Print>', self.prtsc_basildi)
            self.root.bind('<Control-Shift-S>', self.prtsc_basildi)

    def yol_sec(self):
        if self.kayit_yolu:
            yeni_yol = filedialog.askdirectory(initialdir=self.kayit_yolu)
        else:
            yeni_yol = filedialog.askdirectory()

        if yeni_yol:
            self.kayit_yolu = yeni_yol
            self.yol_label.config(text=self.kayit_yolu)

    def ilk_klasor_sec(self):
        self.yol_sec()
        if not self.kayit_yolu:
            messagebox.showinfo("Bilgi",
                                "Klasör seçmeden devam edebilirsiniz.\n'Seç' butonuyla klasör seçmeyi unutmayın!")

    def screenshot_al(self):
        if not self.kayit_yolu:
            messagebox.showwarning('Uyarı', 'Lütfen önce kayıt klasörü seçin!')
            return

        try:
            zaman = datetime.now().strftime('%Y%m%d_%H%M%S')
            dosya_adi = f'screenshot_{zaman}.png'
            dosya_yolu = os.path.join(self.kayit_yolu, dosya_adi)

            screenshot = ImageGrab.grab()
            screenshot.save(dosya_yolu)

            self.durum_label.config(text=f'Ekran görüntüsü kaydedildi: {dosya_adi}', fg='#27ae60')
            messagebox.showinfo('Başarılı', f'Ekran görüntüsü kaydedildi:\n{dosya_yolu}')

        except Exception as e:
            self.durum_label.config(text='Hata oluştu!', fg='#e74c3c')
            messagebox.showerror('Hata', f'Ekran görüntüsü alınırken hata:\n{str(e)}')

    def prtsc_basildi(self, event=None):
        if not self.kayit_yolu:
            return

        try:
            zaman = datetime.now().strftime("%Y%m%d_%H%M%S")
            dosya_adi = f"screenshot_{zaman}.png"
            dosya_yolu = os.path.join(self.kayit_yolu, dosya_adi)

            screenshot = ImageGrab.grab()
            screenshot.save(dosya_yolu)

            self.durum_label.config(text=f"Ekran görüntüsü: {dosya_adi}", fg="#27ae60")
            print(f"Print Screen: {dosya_yolu}")

        except Exception as e:
            self.durum_label.config(text="Hata oluştu!", fg="#e74c3c")
            print(f"Ekran görüntüsü hatası: {e}")

    def kapat(self):
        try:
            keyboard.unhook_all()
        except:
            pass
        self.root.destroy()


def main():
    root = tk.Tk()
    app = EkranGoruntsuProgrami(root)
    root.protocol("WM_DELETE_WINDOW", app.kapat)
    root.mainloop()


if __name__ == "__main__":
    main()