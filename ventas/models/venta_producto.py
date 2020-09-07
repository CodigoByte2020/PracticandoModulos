from odoo import api, fields, models


class Venta_Producto(models.Model):

    _name = 'ventas.venta_producto'

    venta_id = fields.Many2one('ventas.comprobante.pagoventa', required=True, string='Venta ID')
    producto_id = fields.Many2one('ventas.producto', required=True, string='Producto ID')
    cantidad = fields.Float(string='Cantidad')
    #precio = fields.Float(compute='_compute_precio', store=True, string='Precio x unidad' )
    #precio_total = fields.Float(compute='_compute_precio_total', string='Precio total')
    precio = fields.Float(string='Precio x unidad')
    precio_total = fields.Float(string='Precio total')

    #Al cambiar al menos un parámetro se ejecuta la función compute
    #Las variables que tienen compute odoo los hace ineditables
    #store para que lo guarde en base de datos
    #@api.depends('producto_id')
    #def _compute_precio(self):
        #for reg in self:
            #reg.precio = reg.producto_id.precio

    # El campo que queremos que cambie su valor cuando se dispare esta función
    @api.onchange('producto_id')
    def _onchange_producto_id (self):
        self.precio = self.producto_id.precio

    #@api.depends('precio', 'cantidad')
    #def _compute_precio_total(self):
        #for reg in self:
            #reg.precio_total = reg.precio * reg.cantidad

    @api.onchange('precio', 'cantidad')
    def _onchange_precio_cantidad(self):
        self.precio_total = self.precio * self.cantidad

    #El dependes no persiste en BD y el onchanged si
    #El depends hace no editable el campo
    #Ambos se ejecutan cuando cambia al menos un valor de sus parámetros