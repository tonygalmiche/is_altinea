# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    is_ref_client = fields.Char(related='order_line.is_ref_client', string="Ref Client")


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    is_ref_client = fields.Char(string="Ref Client")
