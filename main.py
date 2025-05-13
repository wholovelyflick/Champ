import customtkinter as ctk
import tkinter as tk

# Настройка темы
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class WASDApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("WASD Controller")
        self.root.geometry('600x600')
        self.root.overrideredirect(True)
        self.title_bar = ctk.CTkFrame(self.root, height=30, corner_radius=0)
        self.title_bar.pack(fill='x')
        close_btn = ctk.CTkButton(
            self.title_bar, 
            text="×", 
            width=30,
            command=self.root.destroy,
            fg_color="transparent",
            hover_color="#ff5555"
        )
        close_btn.pack(side='right', padx=5)
        self.title_label = ctk.CTkLabel(
            self.title_bar, 
            text="WASD Controller",
            anchor='w'
        )
        self.title_label.pack(side='left', padx=10, fill='x', expand=True)
        self.title_bar.bind("<ButtonPress-1>", self.start_move)
        self.title_bar.bind("<ButtonRelease-1>", self.stop_move)
        self.title_bar.bind("<B1-Motion>", self.on_move)
        self.title_label.bind("<ButtonPress-1>", self.start_move)
        self.title_label.bind("<ButtonRelease-1>", self.stop_move)
        self.title_label.bind("<B1-Motion>", self.on_move)
        self.create_wasd_ui()
        self.root.bind('<Escape>', lambda e: self.root.destroy())
    def start_move(self, event):
        self.x = event.x
        self.y = event.y
    def stop_move(self, event):
        self.x = None
        self.y = None
    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")
    def create_wasd_ui(self):
        """Создает интерфейс WASD контроллера"""
        self.control_frame = ctk.CTkFrame(
            self.root,
            corner_radius=15
        )
        self.control_frame.pack(expand=True, fill='both', padx=10, pady=10)
        btn_style = {
            'width': 120,
            'height': 120,
            'corner_radius': 12,
            'font': ('Arial', 20, 'bold'),
            'border_width': 2,
            'border_color': '#444',
            'fg_color': '#333',
            'hover_color': '#222'
        }
        self.key_w = ctk.CTkButton(
            self.control_frame,
            text="W",
            command=lambda: self.key_action('w', True),
            **btn_style
        )
        self.key_a = ctk.CTkButton(
            self.control_frame,
            text="A",
            command=lambda: self.key_action('a', True),
            **btn_style
        )
        self.key_s = ctk.CTkButton(
            self.control_frame,
            text="S",
            command=lambda: self.key_action('s', True),
            **btn_style
        )
        self.key_d = ctk.CTkButton(
            self.control_frame,
            text="D",
            command=lambda: self.key_action('d', True),
            **btn_style
        )
        self.key_w.grid(row=0, column=1, pady=5, padx=5)
        self.key_a.grid(row=1, column=0, pady=5, padx=5)
        self.key_s.grid(row=1, column=1, pady=5, padx=5)
        self.key_d.grid(row=1, column=2, pady=5, padx=5)
        
        self.root.bind('<KeyPress>', lambda e: self.key_action(e.keysym.lower(), True))
        self.root.bind('<KeyRelease>', lambda e: self.key_action(e.keysym.lower(), False))
    
    def key_action(self, key, pressed):
        """Обработка нажатий клавиш"""
        color = '#00aa77' if pressed else '#333'
        border = '#00ffaa' if pressed else '#444'
        
        if key == 'w': 
            self.key_w.configure(fg_color=color, border_color=border)
            if pressed: print("W pressed - движение вперед")
        elif key == 'a': 
            self.key_a.configure(fg_color=color, border_color=border)
            if pressed: print("A pressed - движение влево")
        elif key == 's': 
            self.key_s.configure(fg_color=color, border_color=border)
            if pressed: print("S pressed - движение назад")
        elif key == 'd': 
            self.key_d.configure(fg_color=color, border_color=border)
            if pressed: print("D pressed - движение вправо")
    
    def run(self):
        self.root.mainloop()

app = WASDApp()
app.run()