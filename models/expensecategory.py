from odoo import models,fields,api


class ExpenseCategory(models.Model):
    _name = "accounting.expense"
    # _rec_name = "expense_name"

    name= fields.Char(string="Name", tracking=True)
