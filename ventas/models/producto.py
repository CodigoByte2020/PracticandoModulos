from odoo import fields, models

class Producto(models.Model):

    _name = 'ventas.producto'

    name = fields.Char(string="Nombre")
    categoria = fields.Char(string="Categoria")
    precio = fields.Float(string="Precio")
    stock = fields.Integer(string="Stock")
