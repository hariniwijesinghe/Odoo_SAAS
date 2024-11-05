# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class task_unique_id(models.Model):
#     _name = 'task_unique_id.task_unique_id'
#     _description = 'task_unique_id.task_unique_id'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'

    unique_id = fields.Char(string="Unique ID", readonly=True, copy=False, default=lambda self: self.env['ir.sequence'].next_by_code('project.task.unique') or '/')
