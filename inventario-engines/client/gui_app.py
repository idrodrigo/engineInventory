import tkinter as tk
from tkinter import ttk, messagebox
from model.engine_dao import crear_tabla, borrar_tabla, Engine, guardar, consultar, editar, eliminar

def barra_menu( root ):
    barra_menu = tk.Menu( root )
    root.config( menu = barra_menu, width=300, height=300)

    menu_inicio = tk.Menu( barra_menu, tearoff = 0)
    barra_menu.add_cascade( label = 'Inicio', menu = menu_inicio)

    menu_inicio.add_command( label = 'Nuevo Registro en Db', command = crear_tabla)
    menu_inicio.add_command( label = 'Eliminar Registro en Db', command= borrar_tabla)
    menu_inicio.add_command( label = 'Salir', command = root.quit)

    barra_menu.add_cascade( label = 'Consultas')
    barra_menu.add_cascade( label = 'Config')
    barra_menu.add_cascade( label = 'Ayuda')

class Frame( tk.Frame ):
    def __init__( self, root = None ):
        super().__init__( root, bg='gray' )
        self.root = root
        self.pack()
        self.config( width=500, height=500) 
        self.id_engine = None

        self.campos_registro()
        self.deshabilitar_campos()
        self.tabla_registros()

    def campos_registro( self ):
        #label
        self.label_marca = tk.Label( self, text = 'Marca: ')
        self.label_marca.config( font = ('Arial', 12, 'bold'), bg='gray', )
        self.label_marca.grid( row = 0, column = 0, padx= 10, pady=10 )

        self.label_tipo = tk.Label( self, text = 'Tipo: ')
        self.label_tipo.config( font = ('Arial', 12, 'bold'), bg='gray',  )
        self.label_tipo.grid( row = 1, column = 0, padx= 10, pady=10 )

        self.label_hp = tk.Label( self, text = 'HP: ')
        self.label_hp.config( font = ('Arial', 12, 'bold'), bg='gray',  )
        self.label_hp.grid( row = 2, column = 0, padx= 10, pady=10 )

        # Entry
        self.mi_marca = tk.StringVar()
        self.entry_marca = tk.Entry( self, textvariable = self.mi_marca )
        self.entry_marca.config( font = ('Arial', 12), width= 50 )
        self.entry_marca.grid( row = 0, column = 1, padx= 10, pady=10, columnspan=2 )

        self.mi_tipo = tk.StringVar()
        self.entry_tipo = tk.Entry( self, textvariable = self.mi_tipo )
        self.entry_tipo.config( font = ('Arial', 12), width= 50 )
        self.entry_tipo.grid( row = 1, column = 1, padx= 10, pady=10, columnspan=2 )

        self.mi_hp = tk.StringVar()
        self.entry_hp = tk.Entry( self, textvariable = self.mi_hp )
        self.entry_hp.config( font = ('Arial', 12), width= 50 )
        self.entry_hp.grid( row = 2, column = 1, padx= 10, pady=10, columnspan=2 )

        # Botones
        self.boton_nuevo = tk.Button( self, text = 'Nuevo', command=self.habilitar_campos )
        self.boton_nuevo.config( font = ('Arial', 12, 'bold'), bg='#158', fg='white', width= 20, cursor='hand2', activebackground='#157', activeforeground='white')
        self.boton_nuevo.grid( row = 4, column = 0, padx= 10, pady=10 )

        self.boton_guardar = tk.Button( self, text = 'Guardar', command=self.guardar_registro ) 
        self.boton_guardar.config( font = ('Arial', 12, 'bold'), bg='#158', fg='white', width= 20, cursor='hand2', activebackground='#157', activeforeground='white')
        self.boton_guardar.grid( row = 4, column = 1, padx= 10, pady=10 )

        self.boton_cancelar = tk.Button( self, text = 'Cancelar', command=self.deshabilitar_campos )
        self.boton_cancelar.config( font = ('Arial', 12, 'bold'), bg='#158', fg='white', width= 20, cursor='hand2', activebackground='#157', activeforeground='white')
        self.boton_cancelar.grid( row = 4, column = 2, padx= 10, pady=10 )

        self.boton_eliminar = tk.Button( self, text = 'Eliminar', command=self.eliminar_registro )  
        self.boton_eliminar.config( font = ('Arial', 12, 'bold'), bg='#900', fg='white', width= 20, cursor='hand2', activebackground='#157', activeforeground='white')
        self.boton_eliminar.grid( row = 6, column = 1, padx= 10, pady=10, columnspan=2 )

        self.boton_editar = tk.Button( self, text = 'Editar', command=self.editar_registro)
        self.boton_editar.config( font = ('Arial', 12, 'bold'), bg='#090', fg='white', width= 20, cursor='hand2', activebackground='#157', activeforeground='white')
        self.boton_editar.grid( row = 6, column = 0, padx= 10, pady=10, columnspan=2 )

    def habilitar_campos(self):
            self.mi_marca.set('')
            self.mi_tipo.set('')
            self.mi_hp.set('')
    
            self.entry_marca.config( state='normal' )
            self.entry_tipo.config( state='normal' )
            self.entry_hp.config( state='normal' )

            self.boton_guardar.config( state='normal' )
            self.boton_cancelar.config( state='normal' )

    def deshabilitar_campos(self):
            self.mi_marca.set('')
            self.mi_tipo.set('')
            self.mi_hp.set('')

            self.entry_marca.config( state='disabled' )
            self.entry_tipo.config( state='disabled' )
            self.entry_hp.config( state='disabled' )

            self.boton_guardar.config( state='disabled' )
            self.boton_cancelar.config( state='disabled' )
            self.boton_editar.config( state='disabled' )
            self.boton_eliminar.config( state='disabled' )

            self.id_engine = None

    def guardar_registro(self):
            engine = Engine(
                self.mi_marca.get(),
                self.mi_tipo.get(),  
                self.mi_hp.get()
            )

            if self.id_engine == None:
                guardar(engine)
            else:
                 editar(engine, self.id_engine)

            self.tabla_registros()

            self.deshabilitar_campos()

    def tabla_registros(self):
        self.lista_registros = consultar() 
        self.lista_registros.reverse()


        self.tabla = ttk.Treeview( self,
        columns = ('Marca', 'Tipo', 'HP'))    
        self.tabla.grid( row = 5, column = 0, columnspan=4, sticky='nse' )

        self.scrollbar = ttk.Scrollbar( self, orient='vertical', command=self.tabla.yview )
        self.scrollbar.grid( row = 5, column = 4, sticky='nse')
        self.tabla.configure( yscrollcommand=self.scrollbar.set )
         
        self.tabla.heading( '#0', text = 'ID' )
        self.tabla.heading( '#1', text = 'Marca' ) 
        self.tabla.heading( '#2', text = 'Tipo' )
        self.tabla.heading( '#3', text = 'HP' )


        for registro in self.lista_registros:
            self.tabla.insert( '', 0 , text = registro[0], values = (registro[1], registro[2], registro[3]) ) 
 
        self.tabla.bind('<<TreeviewSelect>>', self.on_selection)

    def on_selection(self, event):
        self.boton_editar.config( state='normal' )   
        self.boton_eliminar.config( state='normal' ) 

    def editar_registro(self):

        try:
            self.id_engine = self.tabla.item( self.tabla.selection() )['text']
            self.marca = self.tabla.item( self.tabla.selection() )['values'][0]
            self.tipo = self.tabla.item( self.tabla.selection() )['values'][1]
            self.hp = self.tabla.item( self.tabla.selection() )['values'][2]

            self.habilitar_campos()

            self.entry_marca.insert( 0, self.marca )
            self.entry_tipo.insert( 0, self.tipo )
            self.entry_hp.insert( 0, self.hp )
              
        except:
             messagebox.showwarning( 'Atención', 'Debe seleccionar un registro' )

    def eliminar_registro(self):
        try:
            self.id_engine = self.tabla.item( self.tabla.selection() )['text']

            eliminar(self.id_engine)

            self.tabla_registros()
            self.deshabilitar_campos()

        except:
             messagebox.showwarning( 'Atención', 'Debe seleccionar un registro' )