from odoo import fields, models
import time


class ComprobantePagoVenta(models.Model):
    _name = 'ventas.comprobante.pagoventa'
    _description = 'Comprobantes de pago de venta'

    name = fields.Char(string='Serie Comprobante')
    tipo = fields.Selection([('boleta', 'Boleta'), ('factura','Factura')], string='Tipo')
    fecha_emision = fields.Date(string='Fecha de emisión')
    fecha_vencimiento = fields.Date(string ='Fecha de vencimiento', required=True)
    terminos_pago = fields.Selection([('contado', 'Al contado'), ('plazo', '15 días plazo')],
        string='términos pago')
    moneda = fields.Selection([('pen', 'Soles'), ('usd', 'Dólares'), ('eur', 'Euros')], string='Tipo de moneda')
    vendedor_id = fields.Many2one('ventas.vendedor', string='Vendedor')
    cliente_id = fields.Many2one('ventas.cliente', string='Cliente')

    fecha_actual = time.strftime("%d%m%y")

    if fecha_vencimiento - fecha_actual > 0:
        estado = fields.Char(string='Pendiente', editable=False)
    elif fecha_vencimiento - fecha_actual < 0:
        estado = fields.Char(string='Vencido', editable=False)
    else:
        estado = fields.Char(string='HOY', editable=False)

    lineas_ids = fields.One2many('ventas.venta_producto','venta_id', string='Venta') #???
    #Hacer un foreach para calcular el total las líneas

    @api.depends('precio_total')
    def _compute_precio_total(self):
    for total in lineas_ids:
        total.suma_total += lineas_ids.precio_total


