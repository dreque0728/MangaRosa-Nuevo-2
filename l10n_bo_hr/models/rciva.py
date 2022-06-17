from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Rciva(models.Model):
    _name = "rciva"
    _description = "rciva Form"

    employee = fields.Char(required=False, string='employee')
    period = fields.Char(required=False, string='period')
    balance = fields.Char(required=False, string='balance')
    value = fields.Char(required=False, string='value')
