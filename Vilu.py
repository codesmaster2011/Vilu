import tkinter as tk
from tkinter import filedialog
import webbrowser
import time
import os  # Lisää tämä rivi

class ViluApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vilu")
        self.root.geometry("800x600")
        self.root.configure(bg='turquoise')  # Aseta taustaväri turkoosiksi

        # Luo Google Chrome -painike kotinäyttöön
        self.chrome_button_main = tk.Button(self.root, text="Google Chrome", command=self.open_chrome)
        self.chrome_button_main.place(x=50, y=50)

        # Luo Google Maps -painike kotinäyttöön
        self.maps_button_main = tk.Button(self.root, text="Google Maps", command=self.open_maps)
        self.maps_button_main.place(x=200, y=50)

        # Luo Spotify-painike kotinäyttöön
        self.spotify_button_main = tk.Button(self.root, text="Spotify", command=self.open_spotify)
        self.spotify_button_main.place(x=350, y=50)

        # Luo tehtäväpalkki tummansinisellä värillä
        self.taskbar = tk.Frame(self.root, bg='darkblue', height=80)
        self.taskbar.pack(side='bottom', fill='x')

        # Luo kellon etiketti
        self.time_label = tk.Label(self.taskbar, bg='darkblue', fg='white', font=('Arial', 12))
        self.time_label.pack(side='right', padx=10)

        # Luo vihreä neliö-painike tehtäväpalkkiin
        self.square_button = tk.Button(self.taskbar, text="☐", bg='green', fg='white', font=('Arial', 20), command=self.open_square_window)
        self.square_button.pack(side='left', padx=10, pady=10)

        # Luo Google Chrome -painike tehtäväpalkkiin
        self.chrome_button_taskbar = tk.Button(self.taskbar, text="Google Chrome", command=self.open_chrome)
        self.chrome_button_taskbar.pack(side='left', padx=10, pady=10)

        # Luo Google Maps -painike tehtäväpalkkiin
        self.maps_button_taskbar = tk.Button(self.taskbar, text="Google Maps", command=self.open_maps)
        self.maps_button_taskbar.pack(side='left', padx=10, pady=10)

        # Luo Tiedostot-painike tehtäväpalkkiin
        self.files_button_taskbar = tk.Button(self.taskbar, text="Tiedostot", command=self.open_files)
        self.files_button_taskbar.pack(side='left', padx=10, pady=10)

        # Luo Paint-painike tehtäväpalkkiin
        self.paint_button_taskbar = tk.Button(self.taskbar, text="Paint", command=self.open_paint)
        self.paint_button_taskbar.pack(side='left', padx=10, pady=10)

        # Luo hakukenttä tehtäväpalkkiin
        self.search_entry = tk.Entry(self.taskbar, font=('Arial', 12))
        self.search_entry.pack(side='left', padx=10, pady=10)
        self.search_button = tk.Button(self.taskbar, text="Hae", command=self.search_app)
        self.search_button.pack(side='left', padx=10, pady=10)

        # Käynnistä kellon päivitys
        self.update_time()

    def open_chrome(self):
        # Avaa www.google.com -sivusto
        webbrowser.open("http://www.google.com")

    def open_maps(self):
        # Avaa Google Maps -sivusto
        webbrowser.open("http://maps.google.com")

    def open_files(self):
        # Avaa tiedostovalitsin
        filedialog.askopenfilename()

    def open_spotify(self):
        # Avaa Spotify-verkkosivusto
        webbrowser.open("http://www.spotify.com")

    def open_paint(self):
        # Avaa Paint-sovellus suoraan
        os.system("mspaint")

    def open_square_window(self):
        # Luo uusi ikkuna vihreän neliön klikkauksesta
        square_window = tk.Toplevel(self.root)
        square_window.title("Menu")
        square_window.geometry("400x300")
        square_window.configure(bg='darkblue')  # Aseta taustaväri tummansiniseksi
        
        # Luo painikkeet uuteen ikkunaan
        chrome_button = tk.Button(square_window, text="Google Chrome", command=self.open_chrome)
        chrome_button.pack(pady=10)
        
        maps_button = tk.Button(square_window, text="Google Maps", command=self.open_maps)
        maps_button.pack(pady=10)
        
        files_button = tk.Button(square_window, text="Tiedostot", command=self.open_files)
        files_button.pack(pady=10)
        
        paint_button = tk.Button(square_window, text="Paint", command=self.open_paint)
        paint_button.pack(pady=10)

        # Lisää Spotify-painike menu-ikkunaan
        spotify_button = tk.Button(square_window, text="Spotify", command=self.open_spotify)
        spotify_button.pack(pady=10)

    def search_app(self):
        query = self.search_entry.get().lower()
        if 'chrome' in query:
            self.open_chrome()
        elif 'maps' in query:
            self.open_maps()
        elif 'tiedostot' in query or 'files' in query:
            self.open_files()
        elif 'spotify' in query:
            self.open_spotify()
        elif 'paint' in query:
            self.open_paint()
        else:
            print("Sovellusta ei löytynyt.")

    def update_time(self):
        current_time = time.strftime('%H:%M:%S')
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)  # Päivitä joka sekunti

if __name__ == '__main__':
    root = tk.Tk()
    app = ViluApp(root)
    root.mainloop()
