# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import datetime

class IsEffectif(models.Model):
    _name='is.effectif'
    _order='name'
    name = fields.Char(u"Effectif", required=True)


class IsFormeJuridique(models.Model):
    _name='is.forme.juridique'
    _order='name'
    name = fields.Char(u"Forme juridique", required=True)

class IsSecteurActivite(models.Model):
    _name='is.secteur.activite'
    _order='name'
    name = fields.Char(u"Secteur d'activité", required=True)


class ResPartner(models.Model):
    _inherit = "res.partner"


    def _get_ca(self,year):
        cr=self._cr
        date_debut = str(year)+'-10-01'
        date_fin   = str(year+1)+'-10-01'
        for obj in self:
            ca = 0
            if obj.id:
                sql="""
                    SELECT type,sum(amount_untaxed)
                    FROM account_invoice
                    WHERE 
                        partner_id="""+str(obj.id)+""" and
                        date_invoice>='"""+date_debut+"""' and 
                        date_invoice<'"""+date_fin+"""' and
                        type in ('out_invoice','out_refund') and
                        state in ('open','paid')
                    GROUP BY type
                """
                cr.execute(sql)
                for row in cr.fetchall():
                    if row[0]=='out_refund':
                        ca = ca - row[1]
                    else:
                        ca = ca + row[1]
            return ca


    @api.depends('name')
    def _compute_is_ca(self):
        cr=self._cr
        now  = datetime.date.today()
        year = now.year
        if str(now)[-5:]<'10-01':
            year = year - 1
        for obj in self:
            obj.is_ca_n  = self._get_ca(year)
            obj.is_ca_n1 = self._get_ca(year-1)

    is_responsable_dossier_technique_id = fields.Many2one('res.users', u'Responsable du dossier technique')
    is_responsable_commercial_id        = fields.Many2one('res.users', u'Responsable commercial')
    is_courriel_entreprise              = fields.Char(u'Courriel entreprise')
    is_siret                            = fields.Char(u'SIRET')
    is_naf                              = fields.Char(u'NAF')
    is_effectif_id                      = fields.Many2one('is.effectif', u'Effectif')
    is_ca_entreprise                    = fields.Integer(u'CA Entreprise')
    is_forme_juridique_id               = fields.Many2one('is.forme.juridique', u'Forme juridique')
    is_secteur_activite_id              = fields.Many2one('is.secteur.activite', u"Secteur d'activité")
    is_ca_n                             = fields.Integer(u'CA année N'  , compute=_compute_is_ca, store=False, help=u"CA HT facturé du 1er octobre au 30 septembre")
    is_ca_n1                            = fields.Integer(u'CA année N-1', compute=_compute_is_ca, store=False, help=u"CA HT facturé du 1er octobre au 30 septembre")


#- CA ANNEE N-1 : Champ calculé :   CA facturé HT => onglet comptabilité (du 1er octobre au 30 septembre)
#- CA ANNEE N    : Champ calculé :   CA facturé HT => onglet comptabilité

