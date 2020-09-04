from odoo import fields, models

class Vendedor(models.Model):

    __name = 'ventas.vendedor'

    name = fields.Char(string = "Nombre")
    apellidos = fields.Char(string = "Apellidos")
    edad = fields.Integer(string = "Edad")
    direccion = fields.Char(string = "Direccion")