# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    is_commentaire = fields.Text(string="Commentaire")


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def _prepare_invoice(self):
        vals = super(SaleOrder, self)._prepare_invoice()
        vals['project_title'] = self.project_title or ''
        return vals


    @api.multi
    def copy(self, default=None):
        order = super(SaleOrder, self).copy(default=default)
        order.message_follower_ids.unlink()
        order.user_id=self._uid
        return order
