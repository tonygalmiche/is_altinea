# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools, SUPERUSER_ID
from odoo.addons.base.res.res_partner import FormatAddress


class IsMotifRefus(models.Model):
    _name='is.motif.refus'
    _order='name'
    name = fields.Char(u"Motif du refus", required=True)


class Lead(FormatAddress, models.Model):
    _inherit = "crm.lead"

    is_motif_refus_id = fields.Many2one('is.motif.refus', u'Motif du refus')

    is_courriel_entreprise = fields.Char(u'Courriel entreprise')
    is_forme_juridique_id  = fields.Many2one('is.forme.juridique', u'Forme juridique')
    is_secteur_activite_id = fields.Many2one('is.secteur.activite', u"Secteur d'activité")
    is_siret               = fields.Char(u'SIRET')
    is_naf                 = fields.Char(u'NAF')
    is_effectif_id         = fields.Many2one('is.effectif', u'Effectif')
    is_website             = fields.Char(u'Site Web')
    is_ca_entreprise       = fields.Integer(u'CA Entreprise')


    @api.multi
    def _lead_create_contact(self, name, is_company, parent_id=False):
        """ extract data from lead to create a partner
            :param name : furtur name of the partner
            :param is_company : True if the partner is a company
            :param parent_id : id of the parent partner (False if no parent)
            :returns res.partner record
        """
        email_split = tools.email_split(self.email_from)
        values = {
            'name': name,
            'user_id': self.env.context.get('default_user_id') or self.user_id.id,
            'comment': self.description,
            'team_id': self.team_id.id,
            'parent_id': parent_id,
            'phone': self.phone,
            'mobile': self.mobile,
            'email': email_split[0] if email_split else False,
            'fax': self.fax,
            'title': self.title.id,
            'function': self.function,
            'street': self.street,
            'street2': self.street2,
            'zip': self.zip,
            'city': self.city,
            'country_id': self.country_id.id,
            'state_id': self.state_id.id,
            'is_company': is_company,
            'type': 'contact',

            'is_courriel_entreprise': self.is_courriel_entreprise,
            'is_forme_juridique_id': self.is_forme_juridique_id.id,
            'is_secteur_activite_id': self.is_secteur_activite_id.id,
            'is_siret': self.is_siret,
            'is_naf': self.is_naf,
            'is_effectif_id': self.is_effectif_id.id,
            'is_ca_entreprise': self.is_ca_entreprise,
            'website': self.is_website,
        }
        return self.env['res.partner'].create(values)





















