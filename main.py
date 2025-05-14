import customtkinter as ctk

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
ev3.speaker.beep()

# левый и правый моторы
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

color_sensor = ColorSensor(Port.S3) # датчик цвета

# Цвета
BLACK = 9
WHITE = 85
BASE_SPEED = 200 # скорость
GAIN = 1.8 # коэффицент
MAX_CORRECTION = 300 # ограничение коррекции

def move_on_line(space_click):
    while space_click:
        theshold = (BLACK + WHITE) / 2 # линия серого
        reflection_color = color_sensor.reflection()
        deviation = reflection_color - theshold # отклонение
        correction = deviation * GAIN # коррекция

        # условия для изменения маршрута
        if correction > MAX_CORRECTION:
            correction = MAX_CORRECTION
        elif correction < -MAX_CORRECTION:
            correction = -MAX_CORRECTION
        
        # запуск моторов
        left_motor.run(BASE_SPEED + correction)
        right_motor.run(BASE_SPEED - correction)

        wait(10) # задержка

class WASDApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("WASD Controller")
        self.root.geometry('500x500')
        self.root.overrideredirect(True)
        self.space_pressed = False
        self.title_bar = ctk.CTkFrame(self.root, height=30, corner_radius=0)
        self.title_bar.pack(fill='x')
        close_btn = ctk.CTkButton(self.title_bar, text="×", width=30,command=self.root.destroy,fg_color="transparent",hover_color="#ff5555")
        close_btn.pack(side='right', padx=5)
        
        self.title_label = ctk.CTkLabel(self.title_bar, text="WASD Controller",anchor='w')
        self.title_label.pack(side='left', padx=10, fill='x', expand=True)
        self.title_bar.bind("<ButtonPress-1>", self.start_move)
        self.title_bar.bind("<ButtonRelease-1>", self.stop_move)
        self.title_bar.bind("<B1-Motion>", self.on_move)
        self.main_frame = ctk.CTkFrame(self.root, corner_radius=15, fg_color="#2b2b2b")
        self.main_frame.pack(expand=True, fill='both', padx=10, pady=10)
        control_frame = ctk.CTkFrame(self.main_frame, corner_radius=15)
        control_frame.pack(expand=True, fill='both', padx=20, pady=10)
        btn_style = {
            'width': 80,
            'height': 80,
            'corner_radius': 12,
            'font': ('Arial', 18, 'bold'),
            'border_width': 2,
            'border_color': '#444',
            'fg_color': '#333',
            'hover_color': '#222'
        }
        control_frame.grid_columnconfigure(0, weight=1)
        control_frame.grid_columnconfigure(1, weight=1)
        control_frame.grid_columnconfigure(2, weight=1)
        control_frame.grid_rowconfigure(0, weight=1)
        control_frame.grid_rowconfigure(1, weight=1)
        control_frame.grid_rowconfigure(2, weight=1)

        self.key_w = ctk.CTkButton(control_frame, text="W", **btn_style)
        self.key_w.grid(row=0, column=1, pady=5)
        
        self.key_a = ctk.CTkButton(control_frame, text="A", **btn_style)
        self.key_a.grid(row=1, column=0, pady=5)
        
        self.key_s = ctk.CTkButton(control_frame, text="S", **btn_style)
        self.key_s.grid(row=1, column=1, pady=5)
        
        self.key_d = ctk.CTkButton(control_frame, text="D", **btn_style)
        self.key_d.grid(row=1, column=2, pady=5)
        
        self.key_space = ctk.CTkButton(control_frame,text="Пробел",width=180,height=60,corner_radius=12,font=('Arial', 14, 'bold'),border_width=2,border_color='#444',fg_color='#333',hover_color='#222')
        self.key_space.grid(row=2, column=0, columnspan=3, pady=10)
        self.root.bind('<KeyPress>', self.key_pressed)
        self.root.bind('<KeyRelease>', self.key_released)
        self.root.bind('<Escape>', lambda e: self.root.destroy())
    
    def start_move(self, event):
        self.x = event.x
        self.y = event.y
    
    def stop_move(self, event):
        self.x = None
        self.y = None
    
    def on_move(self, event):
        if hasattr(self, 'x') and self.x is not None:
            deltax = event.x - self.x
            deltay = event.y - self.y
            x = self.root.winfo_x() + deltax
            y = self.root.winfo_y() + deltay
            self.root.geometry(f"+{x}+{y}")
    
    def key_pressed(self, event):
        key = event.keysym.lower()
        
        if key == 'w':
            self.key_w.configure(fg_color='#00aa77', border_color='#00ffaa')
            # Ваш код для W здесь
            print("Код для W")
        
        elif key == 'a':
            self.key_a.configure(fg_color='#00aa77', border_color='#00ffaa')
            # Ваш код для A здесь
            print("Код для A")
        
        elif key == 's':
            self.key_s.configure(fg_color='#00aa77', border_color='#00ffaa')
            # Ваш код для S здесь
            print("Код для S")
        
        elif key == 'd':
            self.key_d.configure(fg_color='#00aa77', border_color='#00ffaa')
            # Ваш код для D здесь
            print("Код для D")
        
        elif key == 'space':
            self.space_pressed = not self.space_pressed
            color = '#00aa77' if self.space_pressed else '#333'
            border = '#00ffaa' if self.space_pressed else '#444'
            self.key_space.configure(fg_color=color, border_color=border)
            if self.space_pressed: 
                move_on_line(self.space_pressed)
    
    def key_released(self, event):
        key = event.keysym.lower()
        if key == 'w':
            self.key_w.configure(fg_color='#333', border_color='#444')
        
        elif key == 'a':
            self.key_a.configure(fg_color='#333', border_color='#444')
        
        elif key == 's':
            self.key_s.configure(fg_color='#333', border_color='#444')
        
        elif key == 'd':
            self.key_d.configure(fg_color='#333', border_color='#444')
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = WASDApp()
    app.run()