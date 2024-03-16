from odoo import models, fields, api

class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = 'Yêu cầu mua hàng'

    Department_id = fields.Many2one('hr.department', string='Bộ phận')
    Request_id = fields.Many2one('res.users', string='Người tạo yêu cầu')
    Approver_id = fields.Many2one('res.users', string='Người phê duyệt')
    Date = fields.Date(string='Ngày tạo', default=fields.Date.today)
    Date_approve = fields.Date(string='Ngày phê duyệt')
    Request_line_ids = fields.One2many('purchase.request.line', 'request_id', string='Chi tiết yêu cầu mua hàng')
    Description = fields.Text(string='Mô tả')
    State = fields.Selection([('draft', 'Draft'), ('wait', 'Wait'), ('approved', 'Approved'), ('cancel', 'Cancel')],
                             string='Trạng thái', default='draft', readonly=True)
    Total_qty = fields.Float(string='Tổng số lượng', compute='_compute_total_qty', store=True)
    Total_amount = fields.Float(string='Tổng giá trị', compute='_compute_total_amount', store=True)

    @api.depends('Request_line_ids.qty')
    def _compute_total_qty(self):
        for request in self:
            request.Total_qty = sum(request.Request_line_ids.mapped('qty'))

    @api.depends('Request_line_ids.total')
    def _compute_total_amount(self):
        for request in self:
            request.Total_amount = sum(request.Request_line_ids.mapped('total'))
