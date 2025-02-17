from odoo import models, fields, api, _

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Ticket'
    _inherits = {'project.task': 'task_id'}
    
    task_id = fields.Many2one(
        comodel_name='project.task',
        string='Task',        
        auto_join=True, index=True, ondelete="cascade", required=True        
    )
    sale_id = fields.Many2one(
        comodel_name='sale.order',
        string='Sale Order',
        help='Related Sale Order'
    )
    action_corrective = fields.Html(
        string='Corrective Action',
        help='Descrive corrective actions to do'
    )
    action_preventive = fields.Html(
        string='Preventive Action',
        help='Descrive preventive actions to do'
    )

    def action_recurring_subtask(self):
        self.ensure_one()
        return self.task_id.action_recurring_subtask()