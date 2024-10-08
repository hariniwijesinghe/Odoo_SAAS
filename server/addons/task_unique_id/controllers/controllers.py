# -*- coding: utf-8 -*-
# from odoo import http


# class TaskUniqueId(http.Controller):
#     @http.route('/task_unique_id/task_unique_id', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_unique_id/task_unique_id/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_unique_id.listing', {
#             'root': '/task_unique_id/task_unique_id',
#             'objects': http.request.env['task_unique_id.task_unique_id'].search([]),
#         })

#     @http.route('/task_unique_id/task_unique_id/objects/<model("task_unique_id.task_unique_id"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_unique_id.object', {
#             'object': obj
#         })

