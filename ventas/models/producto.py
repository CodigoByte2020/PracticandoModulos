from odoo import fields, models

class Producto(models.Model):

    _name = 'ventas.producto'

    name = fields.Char(string="Nombre")
    precio = fields.Float(string="Precio")
    stock = fields.Integer(string="Stock")
    categoria = fields.Char(string="Categoria")
    disponible = fields.Boolean(string="Disponible")
