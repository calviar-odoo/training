# -*- coding:utf-8 -*-
from odoo import models,fields,api
class AccountMovePdf(models.Model):
    _inherit = 'account.move'
    pdf_invoice = fields.Binary(string = 'PDF', required = True, default=lambda self: self.pdf_generator()) # Llamamos a la función pdf_generator
    
    @api.model
    def pdf_generator(self):
        invoices = self.env['account.move'].search([('move_type', '=', 'out_invoice')])
        for invoice in invoices:
            self.pdf_invoice = self.env.ref('account.account_invoices_without_payment').report_action(self)
            
    def preview_invoice(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': self.get_portal_url(),
        }
            
    def action_invoice_print(self):
        """ Print the invoice and mark it as sent, so that we can see more
            easily the next step of the workflow
        """
        if any(not move.is_invoice(include_receipts=True) for move in self):
            raise UserError(_("Only invoices could be printed."))

        self.filtered(lambda inv: not inv.is_move_sent).write({'is_move_sent': True})
        if self.user_has_groups('account.group_account_invoice'):
            return self.env.ref('account.account_invoices').report_action(self)
        else:
            return self.env.ref('account.account_invoices_without_payment').report_action(self)