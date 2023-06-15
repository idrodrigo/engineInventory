import tkinter as tk
from client.gui_app import Frame, barra_menu

def main(): 
    root = tk.Tk()
    root.title('Inventario de Engines')
    root.iconbitmap('img/electric-motor.ico')
    root.resizable(0,0)
    # root.geometry('500x500')

    barra_menu( root )

    app = Frame( root = root)


    app.mainloop()

if __name__ == '__main__':
    main()