from odoo import fields, models


class ComprobantePagoVenta(models.Model):
    _name = 'ventas.comprobante.pagoventa'
    _description = 'Comprobantes de pago de venta'

    name = fields.Char(string='Serie Comprobante')
    fecha_emision =  fields.Date(String='Fecha de emisión')
    fecha_vencimiento = fields.Date(string='Fecha de vencimiento')
    vendedor_id = fields.Many2one('ventas.vendedor',string='Vendedor')