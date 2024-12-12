import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

from modelo.consultasDAO import Productos,guardar_producto,listar_prod,listar_tipos,listar_proveedores,editar_producto,buscar_producto,eliminar_producto,reducir_stock,reponer_stock

productosVendidos = []
totalesProductos = []
class Frame(tk.Frame):  
    def __init__(self, root = None):    
        super().__init__(root,width=480,height=320)    
        self.root = root
         
        self.pack()    
        self.config(bg='lightblue')
        self.label_form()
        self.botones_principales(root)
        self.input_form()
        self.bloquear_campos()
        self.mostrar_tabla()
        self.id_producto = None
        self.encontrado = False

    def label_form(self):    
        self.label_nombre = tk.Label(self, text="Nombre: ",bg='lightblue')    
        self.label_nombre.config(font=('Arial',12,'bold'))    
        self.label_nombre.grid(row= 0, column=0,padx=10,pady=10)
        self.label_nombre = tk.Label(self, text="Tipo Producto: ",bg='lightblue')    
        self.label_nombre.config(font=('Arial',12,'bold'))    
        self.label_nombre.grid(row= 1, column=0,padx=10,pady=10)    
        self.label_nombre = tk.Label(self, text="Proveedor: ",bg='lightblue')    
        self.label_nombre.config(font=('Arial',12,'bold'))    
        self.label_nombre.grid(row= 2, column=0,padx=10,pady=10)
        self.label_nombre = tk.Label(self, text="Precio de venta: ",bg='lightblue')    
        self.label_nombre.config(font=('Arial',12,'bold'))    
        self.label_nombre.grid(row= 3, column=0,padx=10,pady=10)
        self.label_nombre = tk.Label(self, text="Cantidad: ",bg='lightblue')    
        self.label_nombre.config(font=('Arial',12,'bold'))    
        self.label_nombre.grid(row= 4, column=0,padx=10,pady=10)
        self.label_nombre = tk.Label(self, text="Buscar Producto: ",bg='lightblue')    
        self.label_nombre.config(font=('Arial',12,'bold'))    
        self.label_nombre.grid(row= 0, column=2,padx=1,pady=10)
    

    def input_form(self):
        self.nombre = tk.StringVar()    
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre)    
        self.entry_nombre.config(width=50)    
        self.entry_nombre.grid(row= 0, column=1,padx=10,pady=10)    
        
  
        x = listar_tipos()
        y = []
        for i in x:
            y.append(i[1])

        self.tipos = ['Selecione Uno'] + y
        self.entry_tipo = ttk.Combobox(self, state="readonly")
        self.entry_tipo['values'] = self.tipos
        self.entry_tipo.current(0)
        self.entry_tipo.config(width=25)    
        self.entry_tipo.bind("<<ComboboxSelected>>")    
        self.entry_tipo.grid(row= 1, column=1,padx=10,pady=10)
        
        x_ = listar_proveedores()
        y_ = []
        for i in x_:
            y_.append(i[1])

        self.proveedores = ['Selecione Uno'] + y_ 
        self.entry_proveedor = ttk.Combobox(self, state="readonly")
        self.entry_proveedor['values'] = self.proveedores
        self.entry_proveedor.current(0)
        self.entry_proveedor.config(width=25)    
        self.entry_proveedor.bind("<<ComboboxSelected>>")    
        self.entry_proveedor.grid(row= 2, column=1,padx=10,pady=10)

        self.precio = tk.StringVar()    
        self.entry_precio = tk.Entry(self, textvariable=self.precio)    
        self.entry_precio.config(width=50)    
        self.entry_precio.grid(row= 3, column=1,padx=10,pady=10)    

        self.cantidad = tk.StringVar()    
        self.entry_cantidad = tk.Entry(self, textvariable=self.cantidad)    
        self.entry_cantidad.config(width=50)    
        self.entry_cantidad.grid(row= 4, column=1,padx=10,pady=10)    

        self.buscar = tk.StringVar()    
        self.entry_buscar = tk.Entry(self, textvariable=self.buscar)    
        self.entry_buscar.config(width=50)    
        self.entry_buscar.grid(row= 0, column=3,padx=1,pady=10)    

    def botones_principales(self,root):    
        self.btn_alta = tk.Button(self, text='Nuevo', command= self.habilitar_campos)    
        self.btn_alta.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#20B2AA',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')    
        self.btn_alta.grid(row= 5, column=0,padx=10,pady=10)    
        
        self.btn_modi = tk.Button(self, text='Guardar', command= self.guardar_campos)    
        self.btn_modi.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#7B68EE',cursor='hand2',activebackground='#7594F5',activeforeground='#000000')    
        self.btn_modi.grid(row= 5, column=1,padx=10,pady=10)    
        
        self.btn_cance = tk.Button(self, text='Cancelar', command= self.bloquear_campos)    
        self.btn_cance.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')    
        self.btn_cance.grid(row= 5, column=2,padx=10,pady=10)

        self.btn_buscar = tk.Button(self, text='Buscar' ,command= self.buscar_registro)    
        self.btn_buscar.config(width= 10,font=('Arial', 12,'bold'),fg ='#000000' ,bg='#7FFF00',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')    
        self.btn_buscar.grid(row= 0, column=4,padx=10,pady=10)

        self.btn_venta = tk.Button(
                                self,
                                text='Venta',
                                command=lambda: abrir_ventas(self,root)  # Llama a abrir_ventas(root) cuando se presiona el botón
                                )
        self.btn_venta.config(
            width=15,
            font=('Arial', 12, 'bold'),
            fg='#000000',
            bg='#FFD700',
            cursor='hand2',
            activebackground='#F35B5B',
            activeforeground='#000000'
            )
        
        self.btn_venta.grid(row=2, column=4, padx=10, pady=10)

        self.btn_reponer = tk.Button(
                                self,
                                text='Reponer Stock',
                                command=lambda: abrir_reponer_stock(self,root)  # Llama a abrir_ventas(root) cuando se presiona el botón
                                )
        self.btn_reponer.config(
            width=15,
            font=('Arial', 12, 'bold'),
            fg='#000000',
            bg='#FFD700',
            cursor='hand2',
            activebackground='#F35B5B',
            activeforeground='#000000'
            )
        self.btn_reponer.grid(row=2, column=3, padx=10, pady=10)


    def habilitar_campos(self):    
        self.entry_nombre.config(state='normal')    
        self.entry_tipo.config(state='normal')    
        self.entry_proveedor.config(state='normal')   
        self.entry_precio.config(state='normal')   
        self.entry_cantidad.config(state='normal')   
        self.btn_modi.config(state='normal')    
        self.btn_cance.config(state='normal')    
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):    
        self.entry_nombre.config(state='disabled')    
        self.entry_tipo.config(state='disabled')    
        self.entry_proveedor.config(state='disabled')   
        self.entry_precio.config(state='disabled')    
        self.entry_cantidad.config(state='disabled')     
        self.btn_modi.config(state='disabled')    
        self.btn_cance.config(state='disabled')    
        self.btn_alta.config(state='normal')
        self.nombre.set('')
        self.precio.set('')
        self.cantidad.set('')
        self.entry_tipo.current(0)
        self.entry_proveedor.current(0)
       

    def mostrar_tabla(self):
      
        self.lista_p = listar_prod()
        self.lista_p.reverse()
        self.tabla = ttk.Treeview(self, columns=('Nombre','Tipo','Proveedor','Precio','Stock'))
        self.tabla.grid(row=6,column=0,columnspan=5, sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command= self.tabla.yview)
        self.scroll.grid(row=6,column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Tipo')
        self.tabla.heading('#3', text='Proveedor')
        self.tabla.heading('#4', text='Precio')
        self.tabla.heading('#5', text='Stock')


        for p in self.lista_p:
            self.tabla.insert('',0,text=p[0],
                              values=(p[1],p[2],p[3],p[4],p[5]))


        self.btn_editar = tk.Button(self, text='Editar', command=self.editar_registro)    
        self.btn_editar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#20B2AA',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')    
        self.btn_editar.grid(row= 7, column=0,padx=10,pady=10)    
        
        self.btn_delete = tk.Button(self, text='Eliminar', command=self.eliminar_regristro)    
        self.btn_delete.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')    
        self.btn_delete.grid(row= 7, column=1,padx=10,pady=10)  

    def guardar_campos(self):
        producto = Productos(
            self.nombre.get(),
            self.entry_tipo.current(),
            self.entry_proveedor.current(),
            self.entry_precio.get(),
            self.entry_cantidad.get()
        )
        if self.id_producto == None and self.encontrado == False:
            guardar_producto(producto)
        else :
            editar_producto(producto,int(self.id_producto))

        self.encontrado = False
        self.bloquear_campos()
        self.mostrar_tabla()


    def editar_registro(self):
        try:
            self.id_producto = self.tabla.item(self.tabla.selection())['text']

            self.nombre_prod = self.tabla.item(self.tabla.selection())['values'][0]
            self.tipo_prod = self.tabla.item(self.tabla.selection())['values'][1]
            self.proveedor_prod = self.tabla.item(self.tabla.selection())['values'][2]
            self.precio_prod = self.tabla.item(self.tabla.selection())['values'][3]
            self.cantidad_prod = self.tabla.item(self.tabla.selection())['values'][4]

            self.habilitar_campos()
            self.nombre.set(self.nombre_prod)
            self.entry_tipo.current(self.tipos.index(self.tipo_prod))
            self.entry_proveedor.current(self.proveedores.index(self.proveedor_prod))
            self.precio.set(self.precio_prod)
            self.cantidad.set(self.cantidad_prod)

        except:
            pass
    
   
    def buscar_registro(self):
        
        print(buscar_producto(self.entry_buscar.get()))
        try:
            
            busqueda = buscar_producto(self.entry_buscar.get())
            self.encontrado = True
            datos = busqueda[0]
            self.habilitar_campos()
            self.id_producto = datos[0]
            self.nombre.set(datos[1])
            self.entry_tipo.current(datos[2])
            self.entry_proveedor.current(datos[3])
            self.precio.set(datos[4])
            self.cantidad.set(datos[5])

            for item in self.tabla.get_children():  
                valores = self.tabla.item(item, "values")  
                if valores and valores[0] == datos[1]:  
                    self.tabla.selection_set(item)  
                    self.tabla.focus(item)  
                    self.tabla.see(item)  
                    break
        except:
            mostrar_error_busqueda()
    
    def eliminar_regristro(self):
        self.id_producto = self.tabla.item(self.tabla.selection())['text']

        respuesta = messagebox.askquestion("Atención", "¿Deseas continuar con la eliminación?")
        if respuesta == 'yes':
            eliminar_producto(int(self.id_producto))
        else:
            pass

        self.mostrar_tabla()

def barra_menu(root):  
    barra = tk.Menu(root)
    root.config(menu = barra, width = 300 , height = 300)
    menu_inicio = tk.Menu(barra, tearoff=0)
    menu_inicio2 = tk.Menu(barra, tearoff=0)
    menu_inicio3 = tk.Menu(barra, tearoff=0)
    menu_inicio4 = tk.Menu(barra, tearoff=0)

    barra.add_cascade(label='Inicio', menu = menu_inicio) 
    barra.add_cascade(label='Consultas', menu = menu_inicio2)  
    barra.add_cascade(label='Ayuda', menu = menu_inicio3) 
    barra.add_cascade(label='Acerca de', menu = menu_inicio4)  
   
   
    menu_inicio.add_command(label='Salir', command= root.destroy)

    menu_inicio2.add_command(label='Productos nuevos')  
    menu_inicio2.add_command(label='Proveedores')  
    menu_inicio2.add_command(label='Tipos de productos')

    menu_inicio3.add_command(
        label='Ayuda del sistema', 
        command=lambda: abrir_ayuda(root)  # Usar lambda para pasar root
    )


    menu_inicio4.add_command(
        label='Información de la farmacia'
    )  
    menu_inicio4.add_command(
        label='Autores y versión', 
        command=lambda: abrir_autores_y_version(root)  # Usar lambda para pasar root
    )






def abrir_ventas(Frame,root):
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Ventas")
    nueva_ventana.geometry("580x300")
    nueva_ventana.iconbitmap('img/farmacia_ico.ico')
    nueva_ventana.config(bg="#A3E4A3")

    frame = ttk.Frame(nueva_ventana)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    etiqueta_nombre = ttk.Label(frame, text="Nombre del producto:", style="Label.TLabel")
    etiqueta_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    nombre_var = tk.StringVar()
    entrada_nombre = ttk.Entry(frame, textvariable=nombre_var, width=50)
    entrada_nombre.grid(row=0, column=1, padx=10, pady=10)

    etiqueta_cantidad = ttk.Label(frame, text="Cantidad a vender:", style="Label.TLabel")
    etiqueta_cantidad.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    cantidad_var = tk.StringVar()
    entrada_cantidad = ttk.Entry(frame, textvariable=cantidad_var, width=50)
    entrada_cantidad.grid(row=1, column=1, padx=10, pady=10)


    boton_vender = ttk.Button(
        frame,
        text="Vender",
        style="Button.TButton",
        command=lambda: vender(nueva_ventana,Frame,nombre_var.get().strip(), cantidad_var.get())  # Eliminar espacios en blanco
    )
    boton_vender.grid(row=2, column=0, columnspan=1, pady=20)
   
    boton_generarFactura = ttk.Button(frame, text="Generar Factura", style="Button.TButton", command=lambda:generar_factura(root))
    boton_generarFactura.grid(row=2, column=1, columnspan=1, pady=20)

    boton_cerrar = ttk.Button(frame, text="Cerrar", style="Button.TButton", command=nueva_ventana.destroy)
    boton_cerrar.grid(row=3, column=0, columnspan=2, pady=40)

    style = ttk.Style()
    style.configure("Frame.TFrame", background="#A3E4A3")
    style.configure("Label.TLabel", background="#A3E4A3", font=("Arial", 12, "bold"))
    style.configure("Button.TButton", font=("Arial", 12, "bold"), foreground="#000000", background="#2874A6")
    style.map("Button.TButton", background=[("active", "#006400")])

def vender(nueva_ventana,Frame,nombre_producto, cantidad):
   
    print(f"DEBUG - Nombre del producto: '{nombre_producto}', Cantidad: {cantidad}")
    
    try:
        producto = buscar_producto(nombre_producto)  
        if producto:
            print(f"Producto encontrado: {producto}")
            productosVendidos.append({"nombre_producto": nombre_producto, "cantidad": cantidad})
            totalesProductos.append(producto)
            reducir_stock(nombre_producto,cantidad)
            mostrar_info()
            nueva_ventana.lift()
            Frame.mostrar_tabla()
        else:
            mostrar_error_busqueda()
            print("Producto no encontrado.")
            nueva_ventana.lift()
    except Exception as e:
        print(f"Error al buscar el producto: {e}")


def abrir_reponer_stock(Frame,root):
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Reposición de Stock")
    nueva_ventana.geometry("580x300")
    nueva_ventana.iconbitmap('img/farmacia_ico.ico')
    nueva_ventana.config(bg="#A3E4A3")

    frame = ttk.Frame(nueva_ventana)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    etiqueta_nombre = ttk.Label(frame, text="Nombre del producto:", style="Label.TLabel")
    etiqueta_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    nombre_var = tk.StringVar()
    entrada_nombre = ttk.Entry(frame, textvariable=nombre_var, width=50)
    entrada_nombre.grid(row=0, column=1, padx=10, pady=10)

    etiqueta_cantidad = ttk.Label(frame, text="Cantidad a reponer:", style="Label.TLabel")
    etiqueta_cantidad.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    cantidad_var = tk.StringVar()
    entrada_cantidad = ttk.Entry(frame, textvariable=cantidad_var, width=50)
    entrada_cantidad.grid(row=1, column=1, padx=10, pady=10)

   
    boton_vender = ttk.Button(
        frame,
        text="Reponer",
        style="Button.TButton",
        command=lambda: reponer(nueva_ventana,Frame,nombre_var.get().strip(), cantidad_var.get())  # Eliminar espacios en blanco
    )
    boton_vender.grid(row=2, column=0, columnspan=2, pady=20)

    boton_cerrar = ttk.Button(frame, text="Cerrar", style="Button.TButton", command=nueva_ventana.destroy)
    boton_cerrar.grid(row=3, column=0, columnspan=2, pady=40)

    style = ttk.Style()
    style.configure("Frame.TFrame", background="#A3E4A3")
    style.configure("Label.TLabel", background="#A3E4A3", font=("Arial", 12, "bold"))
    style.configure("Button.TButton", font=("Arial", 12, "bold"), foreground="#000000", background="#2874A6")
    style.map("Button.TButton", background=[("active", "#006400")])

def reponer(nueva_ventana,Frame,nombre_producto, cantidad):
    
    print(f"DEBUG - Nombre del producto: '{nombre_producto}', Cantidad: {cantidad}")
    
    try:
        producto = buscar_producto(nombre_producto)  
        if producto:
            print(f"Producto encontrado: {producto}")
            reponer_stock(nombre_producto,cantidad)
            mostrar_info()
            nueva_ventana.lift()
            Frame.mostrar_tabla()
        else:
            mostrar_error_busqueda()
            print("Producto no encontrado.")
            nueva_ventana.lift()
    except Exception as e:
        print(f"Error al buscar el producto: {e}")


def generar_factura(root):
    
    ventana_factura = tk.Toplevel(root)
    ventana_factura.title("Factura")
    ventana_factura.geometry("400x600")
    ventana_factura.config(bg="white")
    
    encabezado = tk.Label(ventana_factura, text="FARMACIA", font=("Arial", 14, "bold"), bg="white")
    encabezado.pack(pady=10)
    
    direccion = tk.Label(ventana_factura, text="Dirección: Sarmiento 2646", font=("Arial", 10), bg="white")
    direccion.pack()
    
    telefono = tk.Label(ventana_factura, text="Teléfono: (123) 441-7890", font=("Arial", 10), bg="white")
    telefono.pack(pady=5)
    
    separator = ttk.Separator(ventana_factura, orient="horizontal")
    separator.pack(fill="x", pady=5)

    ahora = datetime.now()

    fecha_hora_formateada = ahora.strftime("%d/%m/%Y %H:%M:%S")

    fecha_label = tk.Label(ventana_factura, text=fecha_hora_formateada, font=("Arial", 10), bg="white")
    fecha_label.pack(anchor="w", padx=10, pady=5)

    separator = ttk.Separator(ventana_factura, orient="horizontal")
    separator.pack(fill="x", pady=5)

    print(productosVendidos)

    factura_text = tk.Text(ventana_factura, font=("Courier New", 10), bg="white", relief="flat", height=20, wrap="none")
    factura_text.pack(fill="both", expand=True, padx=10, pady=5)
    
    total = 0
    index = 0
    totalCantidades = []
    for prod in productosVendidos:
        
        linea = f"Producto: {prod['nombre_producto']}, Cantidad: {prod['cantidad']}\n"
        totalCantidades.append(float(prod['cantidad']))
       
        factura_text.insert("end", linea)

    for sublist_totales in totalesProductos:
        for tupla in sublist_totales:
            if index < len(totalCantidades):  
                total += tupla[4] * totalCantidades[index]
                index += 1

    print(total)
    factura_text.insert("end", f"TOTAL: ${total:.2f}\n")
    factura_text.config(state="disabled")  

    cerrar_btn = ttk.Button(ventana_factura, text="Cerrar", command=ventana_factura.destroy)
    cerrar_btn.pack(pady=10)


def abrir_autores_y_version(root):
   
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Autores y Versión")
    nueva_ventana.geometry("300x200")
    
  
    etiqueta = ttk.Label(nueva_ventana, text="Autores:\nFabrizio Aguilar\n\nVersión: 1.0.0")
    etiqueta.pack(pady=20)

    
    boton_cerrar = ttk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy)
    boton_cerrar.pack()

def abrir_ayuda(root):
    
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Ayuda")
    nueva_ventana.geometry("500x700")
    
    
    texto = tk.Text(nueva_ventana, wrap="word", font=("Arial", 11), bg="white", fg="black")
    texto.pack(fill="both", expand=True, padx=10, pady=10)

    contenido = """
    Ayuda del Sistema - Gestor Farmacéutico
    1. Alta de Producto
    Para agregar un nuevo producto, haga clic en el botón "Nuevo". Luego, complete los campos requeridos y pulse "Guardar" para registrar el producto.
    Si desea cancelar el proceso de alta, haga clic en "Cancelar" y los cambios no se guardarán.

    2. Modificación de Producto
    Si desea modificar un producto, seleccione el registro correspondiente en la tabla de productos y haga clic en "Editar".
    Luego, podrá modificar los campos necesarios y guardar los cambios.

    3. Eliminación de Producto
    Para eliminar un producto, seleccione el registro en la tabla y haga clic en "Eliminar".
    Esta acción eliminará el producto seleccionado de manera permanente.

    4. Búsqueda de Producto
    Para localizar un producto específico, utilice el campo de búsqueda ingresando el nombre del producto y haga clic en "Buscar".
    El sistema posicionará automáticamente el registro correspondiente, y los campos se habilitarán para que pueda editar o eliminar el producto según sea necesario.

    5. Venta de Producto
    Haga clic en el botón "Venta" para ingresar el nombre del producto y la cantidad que desea vender.
    Presione "Vender" para realizar la venta.
    Puede seguir realizando ventas dentro de la misma ventana. Una vez finalizadas las ventas, puede generar una factura mediante el botón correspondiente.
    Cada venta se verá reflejada en el registro automáticamente.

    6. Reposición de Stock
    Para reponer el stock de un producto, haga clic en el botón "Reponer Stock".
    Ingrese el nombre del producto y la cantidad a reponer, luego pulse "Reponer".
    El stock se actualizará automáticamente en el registro correspondiente.
    """
    texto.insert("1.0", contenido)  
    texto.config(state="disabled")

    boton_cerrar = ttk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy)
    boton_cerrar.pack(pady=10)


def mostrar_info():
    messagebox.showinfo("Información", "Operación completada exitosamente.")


def mostrar_error_busqueda():
    messagebox.showerror("Error", "Producto no encontrado")