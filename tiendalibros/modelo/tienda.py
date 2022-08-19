from datetime import datetime


class Transaccion:
    pass


class Libro:

    def __init__(self, isbn: str, titulo: str, precio_venta: float, precio_compra: float, cantidad_actual: int):
        self.isbn: str = isbn
        self.titulo: str = titulo
        self.precio_venta: float = precio_venta
        self.precio_compra: float = precio_compra
        self.cantidad_actual: int = cantidad_actual
        # TODO: Definición del atributo transacciones

    # TODO: Definición del método vender

    # TODO: Definición del método abastecer

    # TODO: Definición del método ejemplares_vendidos

    def __str__(self) -> str:
        return f"{self.titulo}\nISBN: {self.isbn}"


class TiendaDeLibros:

    def __init__(self):
        # TODO: Definición del atributo catalogo
        pass

    def registrar_libro(self, titulo: str, isbn: str, precio_venta: float, precio_compra: float, cantidad_actual: int):
        if self.buscar_libro_por_isbn(isbn) is None:
            libro: Libro = Libro(isbn, titulo, precio_venta, precio_compra, cantidad_actual)
            self.catalogo[isbn] = libro

    # TODO: Definición del método buscar_libro_por_isbn

    # TODO: Definición del método buscar_libro_por_titulo

    def eliminar_libro(self, isbn) -> bool:
        if isbn in self.catalogo.keys():
            del self.catalogo[isbn]
            return True
        else:
            return False

    def abastecer(self, isbn, cantidad) -> bool:
        libro = self.buscar_libro_por_isbn(isbn)
        if libro is not None:
            libro.abastecer(cantidad)
            return True
        else:
            return False

    def vender(self, isbn, cantidad):
        libro = self.buscar_libro_por_isbn(isbn)
        if libro is not None:
            return libro.vender(cantidad)
        else:
            return False

    def libro_mas_costoso(self):
        # TODO: Implementación del cuerpo del método libro_mas_costoso
        pass

    def libro_mas_economico(self):
        # TODO: Implementación del cuerpo del método libro_mas_economico
        pass

    def libro_mas_vendido(self):
        # TODO: Implementación del cuerpo del método libro_mas_vendido
        pass
