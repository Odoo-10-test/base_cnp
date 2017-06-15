#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError
from odoo.osv.expression import get_unaccent_wrapper


class res_partner(models.Model):
    _description = "Productos"
    _inherit = 'product.template'

    # Variables
    precio_minimo = fields.Integer("Precio Mínimo")
    precio_minimo_c = fields.Integer("Precio Mínimo Construcción")

    cnp_origen = fields.Many2one("cnp.origen",string="Origen")
    cnp_familia = fields.Many2one("cnp.familia",string="Familia")
    cnp_area = fields.Many2one("cnp.area",string="Área")
    cnp_linea = fields.Many2one("cnp.linea",string="Línea")
    cnp_grupos = fields.Many2one("cnp.grupos",string="Grupos")
    cnp_subgrupos = fields.Many2one("cnp.subgrupos",string="Sub Grupos")
    cnp_familiam = fields.Many2one("cnp.familiam",string="Familia Material")
    cnp_categoria = fields.Many2one("cnp.categoria",string="Categoria Material")



