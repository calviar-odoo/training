# -*- coding:utf-8 -*-

from odoo import models,fields,api

class AccountMovePdf(models.Model):
    _name = 'account.move.pdf'
    _description = 'Account Model PDF'
    
    _inherit = 'account.move'
    
    pdf_invoice = fields.Binary(string='Factura en PDF')
    
    @api.model # model se utiliza para que tome lo que carga la pagina
    def _model_pdf_invoice(self):
        pdf = self.env['report'].sudo().get_pdf([invoice.id], 'account.report_invoice')
        
        