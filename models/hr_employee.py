from odoo import fields, models, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    petty_cash_limit = fields.Float(string="Petty Cash Limit", default = 4000)
    approved_petty_cash_total = fields.Float(string="Cash In Hand", readonly = True)