from odoo import fields, models, api


class PettyCashRequests(models.Model):
    _name = "petty.cash.requests"

    employee_name = fields.Many2one("hr.employee",
                                    string="Requester Name",
                                    default=lambda self: self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1)
                                    )
    request_date = fields.Datetime(string="Request Date", default=fields.Datetime.now)
    request_amount = fields.Float(string="Request Amount")
    project_id = fields.Many2one("project.project", string="Project")
    description = fields.Text(string="Description")
    cash_in_hand = fields.Float(string="Cash in Hand", readonly = True)
    petty_cash_limit = fields.Float(string="Petty Cash Limit", readonly = True)
    remining_petty_cash_balance = fields.Float(string="Remaining Petty Cash Balance")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('dep_approval', 'Pending Department Approval'),
        ('acc_approval', 'Pending Chief Accountant Approval'),
        ('hq_approval', 'Pending HQ Approval'),
        ('approved', 'Approved'),
        ('released', 'Released'),
        ('cancelled', 'Cancelled'),
    ], string="Status", default="draft", tracking=True)

    def action_submit(self):
        self.state = 'dep_approval'

    def action_dep_approve(self):
        self.state = 'acc_approval'

    def action_acc_approve(self):
        self.state = 'hq_approval'

    def action_hq_approve(self):
        self.state = 'approved'

    def action_approve(self):
        self.state = 'approved'

    def action_release(self):
        self.state = 'released'

    def action_cancel(self):
        self.state = 'cancelled'

