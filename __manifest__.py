# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2017 Marlon Falcón Hernandez
#    (<http://www.falconsolutions.cl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Base CNP MFH',
    'version': '10.0.0.1.0',
    'author': "Falcón Solutions SpA",
    'maintainer': 'Falcon Solutions',
    'website': 'http://www.falconsolutions.cl',
    'license': 'AGPL-3',
    'category': 'Account',
    'summary': 'Invoice refund...',
    'depends': ['base','sale'],
    'description': """
Módulo Base
=============================================================================
- Se agregan campos

        """,
    'data': [
        'data/base_data.xml',
        'views/res_partner_view.xml',
        'views/product_template_view.xml',
    ],
    'installable': True,
}