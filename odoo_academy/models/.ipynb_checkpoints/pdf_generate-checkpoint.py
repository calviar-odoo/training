# -*- coding:utf-8 -*-

from odoo import models,fields,api

class SaleOrder(models.Model):
    _inherit = 'account.move'