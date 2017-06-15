# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class cnp_origen(models.Model):
    _description = "CNP Origen"
    _name = 'cnp.origen'
    name = fields.Char('Origen', translate=True)


class cnp_familia(models.Model):
    _description = "CNP Familia"
    _name = 'cnp.familia'
    name = fields.Char('Familia', translate=True)

class cnp_area(models.Model):
    _description = "CNP Area"
    _name = 'cnp.area'
    name = fields.Char('Area', translate=True)



class cnp_linea(models.Model):
    _description = "CNP Linea"
    _name = 'cnp.linea'
    name = fields.Char('Linea', translate=True)


class cnp_grupos(models.Model):
    _description = "CNP Grupos"
    _name = 'cnp.grupos'
    name = fields.Char('Grupos', translate=True)


class cnp_subgrupos(models.Model):
    _description = "CNP Sub Grupos"
    _name = 'cnp.subgrupos'
    name = fields.Char('Sub Grupos', translate=True)


class cnp_familiam(models.Model):
    _description = "CNP Familia"
    _name = 'cnp.familiam'
    name = fields.Char('Familia M', translate=True)


class cnp_categoria(models.Model):
    _description = "CNP Categoria"
    _name = 'cnp.categoria'
    name = fields.Char('Categoria de material', translate=True)


class cnp_formapago(models.Model):
    _description = "CNP Forma Pago"
    _name = 'cnp.formapago'
    name = fields.Char('Forma pago', translate=True)


class cnp_rubro(models.Model):
    _description = "CNP Rubro"
    _name = 'cnp.rubro'
    name = fields.Char('Rubro', translate=True)

class cnp_cliente(models.Model):
    _description = "CNP Tipo Cliente"
    _name = 'cnp.cliente'
    name = fields.Char('Tipo Cliente', translate=True)
