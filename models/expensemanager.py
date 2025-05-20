from odoo import models,fields,api



class ExpenseCategory(models.Model):
    _name = "accounting.manager"

    date = fields.Date( string="Date", tracking=True)
    name = fields.Selection([
       ("Academic Support", "Academic Support"),
       ("Institutional Support", "Institutional Support"),
       ("Operation and Maintenance of Plant", "Operation and Maintenance of Plant"),
       ("Public Service", "Public Service"),
       ("Research", "Research"),
       ("Student Services", "Student Services"),
       ("Transportation", "Transportation"),

   ],  string ="Expense Category")
