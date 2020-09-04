from odoo import fields, models

class Vendedor(models.Model):

    _name = 'ventas.vendedor' #Buena práctica se coloca nombre del módulo. nombre tabla

    name = fields.Char(string = "Nombre")
    apellidos = fields.Char(string = "Apellidos")
    edad = fields.Integer(string = "Edad")
    direccion = fields.Char(string = "Direccion")