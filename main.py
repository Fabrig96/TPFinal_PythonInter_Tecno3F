import tkinter as tk
from cliente.vista import Frame,barra_menu

def main(): 
    ventana = tk.Tk()
    ventana.title('Gestor Farmacia')
    ventana.iconbitmap('img/farmacia_ico.ico')
    ventana.resizable(False,False)

    barra_menu(ventana)
    app = Frame(root=ventana)

    ventana.mainloop()
    
if __name__ == '__main__':
    main()
