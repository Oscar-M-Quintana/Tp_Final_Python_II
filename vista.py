from tkinter import *
from tkinter import ttk

from modelo import *
from tktemas import temas


class Ventanita:
    """Clase que da inicio a la app."""

    def __init__(self, window):
        self.root = window
        self.root.geometry("525x445+800+150")
        self.tit = StringVar()
        self.des = StringVar()

        # ? no encuentro el uso de self.a
        self.a = IntVar()
        self.opcion = StringVar()
        self.frame1 = Frame(self.root)
        self.tree = ttk.Treeview(self.frame1)
        self.objeto_base = Abmc()
        # Frame
        self.root.title("Tarea Poo")
        self.frame1.config(width=1020, height=1020)
        self.frame1.grid(row=10, column=0, columnspan=4)

        # Etiquetas
        self.superior = Label(
            self.root, text="Ingrese sus datos", bg="orchid", fg="white", width=40
        )
        self.titulo = Label(self.root, text="Titulo")
        self.descripcion = Label(self.root, text="Descripcion")
        self.registros = Label(
            self.root, text="Mostrar registros existentes", bg="grey", width=40
        )
        self.temas = Label(
            self.root,
            text="Temas",
            bg="black",
            fg="red",
            height=1,
            width=40,
        )

        self.superior.grid(
            row=0, column=0, columnspan=4, padx=1, pady=1, sticky="w" + "e"
        )
        self.titulo.grid(row=1, column=0, sticky="w")
        self.descripcion.grid(row=2, column=0, sticky="w")
        self.registros.grid(
            row=3, column=0, columnspan=4, padx=1, pady=1, sticky="w" + "e"
        )
        self.temas.grid(
            column=0, row=20, columnspan=4, padx=1, pady=1, sticky="w" + "e"
        )

        # Entradas
        self.Ent1 = Entry(self.root, textvariable=self.tit)
        self.Ent1.grid(row=1, column=1)
        self.Ent2 = Entry(self.root, textvariable=self.des)
        self.Ent2.grid(row=2, column=1)

        # Frame Unidad 4
        self.frame_rojoizq = Frame(self.root, width="200", height="80", bg="red")
        self.frame_negro = Frame(self.root, width="80", height="80", bg="black")
        self.frame_rojoder = Frame(self.root, width="200", height="80", bg="red")

        self.frame_rojoizq.grid(column=0, row=21)
        self.frame_negro.grid(column=1, row=21)
        self.frame_rojoder.grid(column=2, row=21)

        # Botones
        self.boton_alta = Button(self.root, text="Alta", command=lambda: self.alta())
        self.boton_alta.grid(row=6, column=0)

        self.boton_editar = Button(
            self.root, text="Actualizar", command=lambda: self.modificar()
        )
        self.boton_editar.grid(row=6, column=1)

        self.boton_borrar = Button(
            self.root, text="Borrar", command=lambda: self.borrar()
        )
        self.boton_borrar.grid(row=6, column=2)

        self.boton_tema1 = Radiobutton(
            self.frame_negro,
            text="Tema 1",
            variable=self.opcion,
            value="01",
            fg="red",
            bg="black",
            command=lambda: temas.tema1(self, self.root),
        )
        self.boton_tema1.grid(column=2, row=21)

        self.boton_tema2 = Radiobutton(
            self.frame_negro,
            text="Tema 2",
            variable=self.opcion,
            value="02",
            fg="red",
            bg="black",
            command=lambda: temas.tema2(self, self.root),
        )
        self.boton_tema2.grid(column=2, row=22)

        self.boton_tema3 = Radiobutton(
            self.frame_negro,
            text="Tema 3",
            variable=self.opcion,
            value="03",
            fg="red",
            bg="black",
            command=lambda: temas.tema3(self, self.root),
        )
        self.boton_tema3.grid(column=2, row=23)

        # Tree
        self.tree["columns"] = ("col1", "col2")
        self.tree.column("#0", width=90, minwidth=50, anchor="w")
        self.tree.column("col1", width=200, minwidth=80)
        self.tree.column("col2", width=200, minwidth=80)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Título")
        self.tree.heading("col2", text="Descripción")
        self.tree.grid(row=0, column=0, columnspan=4)
        self.tree.bind(
            "<<TreeviewSelect>>",
            lambda event, a=self.tree, b=self.titulo, c=self.descripcion: self.objeto_base.item_elegido(
                a, b, c
            ),
        )

    def alta(self):
        """Metodo que define el alta"""

        self.objeto_base.alta(self.tit, self.des, self.tree)

    def borrar(
        self,
    ):
        """Metodo que define el borrar."""

        self.objeto_base.borrar(self.tit, self.des, self.tree)

    def modificar(
        self,
    ):
        """Metodo que define modificar."""

        self.objeto_base.modificar(self.tit, self.des, self.tree)

    def actualizar(
        self,
    ):
        """Metodo que define la actualización."""

        self.objeto_base.actualizar_treeview(self.tree)
