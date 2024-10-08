from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'

    unique_id = fields.Char(string='Unique Task ID', required=True, copy=False, readonly=True, index=True)

    def create(self, vals):
        if 'unique_id' not in vals:
            vals['unique_id'] = self.env['ir.sequence'].next_by_code('task.sequence') or '/'
        return super(ProjectTask, self).create(vals)
