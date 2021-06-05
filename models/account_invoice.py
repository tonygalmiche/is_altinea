# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.model
    def create(self, vals):
        invoice = super(AccountInvoice, self).create(vals)
        invoice.message_follower_ids.unlink()
        #invoice.user_id=self._uid
        print(invoice)
        return invoice

