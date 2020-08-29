# -*- coding: utf-8 -*-

from odoo import models, fields, api


class drinks_menu(models.Model):
    _name = 'drink.drink'
    _description = 'drink_drink'

    name = fields.Char(string="name of drink")
    description = fields.Text(string="description of product")
    price = fields.Float(string="price")
    color = fields.Integer()


class List_menu(models.Model):
    _name = 'list.list'
    _description = 'list_list'
    _inherit = 'drink.drink'

    name_drinks = fields.Many2one("drink.drink", ondelete="cascade", required=True, index=True,
                                  string="name of drink")
    name = fields.Char(related="name_drinks.name", string="name of drink")
    amount = fields.Float(string="amount", required=True)
    total_price = fields.Float(string="Total price", store=True, compute='_total_price')
    Price = fields.Float(related="name_drinks.price", string="price")

    @api.depends('Price', 'amount')
    def _total_price(self):
        for r in self:
            r.total_price = r.Price * r.amount


class order_menu(models.Model):
    _name = 'orders.orders'
    _description = 'orders_orders'
    _inherit = 'list.list'

    customer_name = fields.Char(string="customer name", required=True)
    order_list = fields.Many2many("list.list", 'name_drink', required=True, index=True,
                                  string="order")
    order_price = fields.Float(string="order price", store=True, compute='_total_total_price')

    @api.depends('total_price')
    def _total_total_price(self):
        x = 0
        for r in self.order_list:
            x = x + r.total_price
            print(x)


