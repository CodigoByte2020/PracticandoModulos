from odoo import fields, models


class Vendedor(models.Model):

    _name = 'ventas.vendedor' #Buena práctica se coloca nombre del módulo. nombre tabla

    name = fields.Char(string="Nombre", required=True,help='debes llenar este campo')
    apellidos = fields.Char(string = "Apellidos")
    edad = fields.Integer(string="Edad")
    direccion = fields.Char(string = "Direccion")