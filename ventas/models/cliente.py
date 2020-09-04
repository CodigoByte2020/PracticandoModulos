from odoo import fields, models


class Cliente(models.Model):

    _name = 'ventas.cliente'

    name = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos")
    edad = fields.Integer(string="Edad")
    celular = fields.Integer(string="Celular",help="Ingrese un número de 9 digitos")

