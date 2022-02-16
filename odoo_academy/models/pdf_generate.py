# -*- coding:utf-8 -*-

from odoo import models,fields,api

class AccountMovePdf(models.Model):
    #_name = 'account.move.pdf'
    
    #_description = 'Account Model PDF'
    
    _inherit = 'account.move'
    
    #pdf_invoice = fields.Binary(string='Factura en PDF')
    pdf_invoice = fields.Binary(string = 'Factura en PDF', required = True, default=lambda self: self.pdf_generator()) # Llamamos a la función pdf_generator
    
    @api.model
    def pdf_generator(self):
        invoices = self.env['account.move'].search([('move_type', '=', 'out_invoice')])
        for invoice in invoices:
            self.pdf_invoice = self.env['Factura en PDF']