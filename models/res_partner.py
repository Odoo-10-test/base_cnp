#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError
from odoo.osv.expression import get_unaccent_wrapper


class res_partner(models.Model):
    _description = "Partner registered turns"
    _inherit = 'res.partner'

    # Variables
    forma_pago = fields.Many2one("cnp.formapago",string="Forma de Pago")
    credito = fields.Integer("Línea de Crédito")
    rubro = fields.Many2one("cnp.rubro", string="Rubro")
    cliente = fields.Many2one("cnp.cliente", string="Tipo Cliente")


