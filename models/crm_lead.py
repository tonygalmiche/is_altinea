# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.addons.base.res.res_partner import FormatAddress


class IsMotifRefus(models.Model):
    _name='is.motif.refus'
    _order='name'
    name = fields.Char(u"Motif du refus", required=True)



class Lead(FormatAddress, models.Model):
    _inherit = "crm.lead"

    is_motif_refus_id = fields.Many2one('is.motif.refus', u'Motif du refus')
