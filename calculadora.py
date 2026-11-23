import tkinter as tk
from pathlib import Path

class calculator:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title('Calculadora')
        self.ventana.geometry('400x500+200+50')
        self.ventana.resizable(False, False)
        self.ventana.config(bg='gray20')
        try:
            PATH = Path(__file__).resolve().parent
            filePath = PATH / 'calc.ico'
            self.ventana.iconbitmap(filePath)
        except Exception:
            pass 

        self.pantalla = tk.Entry(
            self.ventana, 
            readonlybackground='seagreen3',
            bg='seagreen3', 
            font=('Arial', 32, 'bold'), 
            justify='right',
            state='readonly'
        )

        self.pantalla.place(
            relx=0.05, 
            rely=0.05, 
            relwidth=0.9, 
            relheight= 0.15
        )

        self.crearInterfaz()

    def crearBotones(self, x, y, text, bg='gray67'):
        '''Creates a button, only x, y, text needed'''
        button = tk.Button(
            self.ventana, 
            bg=bg, 
            text=text, 
            font=('Arial', 28, 'bold'), 
            cursor='hand2',
            command=lambda t=text: self.press(t)
            )
        button.place(relx=x, rely=y, relheight=0.15, relwidth=0.17)
        return button

    def limpiar(self):
        '''Clean the screen, probably gonna add a C button in the future'''
        self.pantalla.config(state='normal')
        self.pantalla.delete(0, tk.END)
        self.pantalla.config(state='readonly')

    def press(self, valor):
        if valor == '=':
            try:
                self.pantalla.config(state='normal')
                expr = self.pantalla.get().replace('x', '*')
                result = eval(expr)
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, str(result))
                self.pantalla.config(state='readonly')
            except Exception:
                self.pantalla.config(state='normal')
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, 'ERROR')
                self.pantalla.after(500, self.limpiar)
                self.pantalla.config(state='readonly')
        else:
            self.pantalla.config(state='normal')
            self.pantalla.insert(tk.END, str(valor))
            self.pantalla.config(state='readonly')

    def crearInterfaz(self):
        self.crearBotones(0.05, 0.26, 7)
        self.crearBotones(0.285, 0.26, 8)
        self.crearBotones(0.518, 0.26, 9)
        self.crearBotones(0.748, 0.26, '/','yellow3')
        
        self.crearBotones(0.05, 0.44, 4)
        self.crearBotones(0.285, 0.44, 5)
        self.crearBotones(0.518, 0.44, 6)
        self.crearBotones(0.748, 0.44, 'x','yellow3')

        self.crearBotones(0.05, 0.62, 1)
        self.crearBotones(0.285, 0.62, 2)
        self.crearBotones(0.518, 0.62, 3)
        self.crearBotones(0.748, 0.62, '-','yellow3')

        self.crearBotones(0.05, 0.80, 0)
        self.crearBotones(0.285, 0.80, '.')
        self.crearBotones(0.518, 0.80, '=','red2')
        self.crearBotones(0.748, 0.80, '+','yellow3')



if __name__ == '__main__':
    ventanaApp = tk.Tk()

    app = calculator(ventanaApp)

    ventanaApp.mainloop()