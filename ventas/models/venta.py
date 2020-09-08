from odoo import api, fields, models
import time
import datetime

TERMINO_PAGO_SELECTION = [
    ('contado', 'Al contado'),
]


class ComprobantePagoVenta(models.Model):
    _name = 'ventas.comprobante.pagoventa'
    _description = 'Comprobantes de pago de venta'

    name = fields.Char(string='Serie Comprobante')
    tipo = fields.Selection([('boleta', 'Boleta'), ('factura','Factura')], string='Tipo')
    fecha_emision = fields.Date(string='Fecha de emisión', default=fields.Date.context_today)
    fecha_vencimiento = fields.Date(string ='Fecha de vencimiento', required=True)
    terminos_pago = fields.Selection([('contado', 'Al contado'), ('plazo', '15 días plazo')],
                                        string='términos pago')
    moneda = fields.Selection([('pen', 'Soles'), ('usd', 'Dólares'), ('eur', 'Euros')], string='Tipo de moneda')
    vendedor_id = fields.Many2one('ventas.vendedor', string='Vendedor')
    cliente_id = fields.Many2one('ventas.cliente', string='Cliente')
    state = fields.Selection(STATE.SELECTION)

    fecha_actual = time.strftime("%d%m%y") #timestamp, tiemlinex

    '''if fecha_vencimiento - (Date) fecha_actual > 0:
        estado = fields.Char(string='Pendiente', readonly=False)
    elif fecha_vencimiento - fecha_actual < 0:
        estado = fields.Char(string='Vencido', readonly=False)
    else:
        estado = fields.Char(string='HOY', editable=False)'''

    def dias_entre(d1, d2):
        d1 = datetime.strptime(d1, "%Y-%m-%d")
        d2 = datetime.strptime(d2, "%Y-%m-%d")
        return cantidad_dias((d2 - d1).days)

    lineas_ids = fields.One2many('ventas.venta_producto','venta_id', string='Venta') #???
    #Hacer un foreach para calcular el total las líneas

    @api.depends('line_ids')
    def _compute_precio_total(self):
        suma_total = 0
        for line in self.lineas_ids:
            suma_total += lineas_ids.precio_total


