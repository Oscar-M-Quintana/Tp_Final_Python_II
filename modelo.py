# import sqlite3

from peewee import *


db = SqliteDatabase("nivel_avanzado.db")


class BaseModel(Model):
    """Clase que genera el uso del ORM."""

    class Meta:
        """Clase que genera el name_space database."""

        database = db


class Noticia(BaseModel):
    """Clase que genera la tabla Noticias."""
<<<<<<< HEAD
    
    # id = IntegerField(unique=True)
=======

>>>>>>> bf276896fbc6234720c45429d24b38567b7abafa
    titulo = CharField(unique=True)
    descripcion = TextField()


db.connect()
db.create_tables([Noticia])


class Abmc:
    """Clase para lograr el CRUD"""

    def __init__(
        self,
    ):
        pass

    def actualizar_treeview(self, mitreeview):
        """Metodo: limpieza de tabla."""

        records = mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)
        for fila in Noticia.select():
            print(fila)
            mitreeview.insert(
                "", 0, text=fila.id, values=(fila.titulo, fila.descripcion)
            )

    def cerrar_conexion(self):
        """Metodo para un print????"""

        print("cerrar_conexion")

    def alta(self, titulo, descripcion, mitreeview):
        """Metodo que genera el Alta."""

        noticia = Noticia()
        noticia.titulo = titulo.get()
        noticia.descripcion = descripcion.get()
        noticia.save()
        self.actualizar_treeview(mitreeview)

    def guarda(variables, popupGuardar, elobjeto):
        """Metodo para guardar."""

        popupGuardar.destroy()
        lista = []
        for variable in variables:
            lista.append(variable.get())
        noticia = Noticia()
        noticia.titulo = lista[0]
        noticia.descripcion = lista[1]
        noticia.save()
        elobjeto.mostrar()
<<<<<<< HEAD
=======

    def borrar(variables, popupEliminar, elobjeto):
        """Metodo para eliminar."""

        popupEliminar.destroy()
        lista = []
        for variable in variables:
            lista.append(variable.get())
>>>>>>> bf276896fbc6234720c45429d24b38567b7abafa

    def borrar(self, titulo, descripcion, mitreeview):
        """Metodo para eliminar."""

        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        
        borrar = Noticia.get(Noticia.titulo == titulo.get())
        borrar.delete_instance()
<<<<<<< HEAD
        
        self.actualizar_treeview(mitreeview)       

    def modificar(self, titulo, descripcion, mitreeview):
        """Metodo para modificar."""

        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        
        actualizar = Noticia.update(descripcion = descripcion.get()).where(
            Noticia.titulo == titulo.get())
        
        actualizar.execute()

        self.actualizar_treeview(mitreeview)
    
    def item_elegido(
        self,tabla, titulo, descripcion
    ):
        """Definimos el metodo item_elegido."""

        for selec in tabla.selection():
            item = tabla.item(selec)
            record = item["values"]
            titulo.set(record[0])
            descripcion.set(record[1])
            
=======

        elobjeto.mostrar()

    def modificar(self, titulo, descripcion, mitreeview):
        """Metodo para modificar."""

        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        con = self.conexion()

        cursor = con.cursor()
        sql = "UPDATE noticias SET (titulo, descripcion)=(?,?) WHERE id=?"
        datos = (titulo.get(), descripcion.get(), valor_id["text"])
        cursor.execute(sql, datos)
        con.commit()
        print(sql, datos)

        self.actualizar_treeview(mitreeview)
        ###

        popupModificar.destroy()
        lista = []
        for variable in variables:
            lista.append(variable.get())

        actualizar = Noticia.update(titulo=lista[1], descripcion=lista[2]).where(
            Noticia.id == lista[0]
        )
        actualizar.execute()

        elobjeto.mostrar()

>>>>>>> bf276896fbc6234720c45429d24b38567b7abafa

"""
    def baja(self, mitreeview):
        item_seleccionado=mitreeview.focus()
        valor_id=mitreeview.item(item_seleccionado)
        con=self.conexion()
        cursor=con.cursor()
        sql="DELETE FROM noticias WHERE id=?"
        datos=(valor_id["text"],)
        print(datos, sql)
        cursor.execute(sql, datos)
        con.commit()
        self.actualizar_treeview(mitreeview)

    def modificar(self, titulo, descripcion, mitreeview):
        item_seleccionado=mitreeview.focus()
        valor_id=mitreeview.item(item_seleccionado)
        con=self.conexion()

        cursor=con.cursor()
        sql="UPDATE noticias SET (titulo, descripcion)=(?,?) WHERE id=?"
        datos=(titulo.get(), descripcion.get(), valor_id["text"])
        cursor.execute(sql, datos)
        con.commit()
        print(sql, datos)

        self.actualizar_treeview(mitreeview)

"""
