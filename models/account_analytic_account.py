# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    is_payment_term_id = fields.Many2one('account.payment.term', 'Conditions de Paiement Client')

    @api.multi
    def _prepare_invoice(self):
        for obj in self:
            res=super(AccountAnalyticAccount, self)._prepare_invoice()
            if obj.is_payment_term_id.id:
                res['payment_term_id']=obj.is_payment_term_id.id
            return res


