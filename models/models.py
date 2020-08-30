# -*- coding: utf-8 -*-
from ebaysdk.poller import orders
from odoo import models, fields, api


class drinks_menu(models.Model):
    _name = 'drink.drink'
    _description = 'drink_drink'

    name = fields.Char(string="name of drink")
    description = fields.Text(string="description of product")
    price = fields.Float(string="price")
    price_total = fields.Float(string='total', readonly=True)
    amount = fields.Float(string="amount")
    price_total = fields.Float(compute='_compute_amount', string='total', readonly=True, store=True)
    color = fields.Integer()

    @api.depends('price','amount')
    def _compute_amount(self):
        for order in self:
            order.price_total = order.amount * order.price


class order_menu(models.Model):
    _name = 'orders.orders'
    _description = 'orders_orders'
    _inherit = 'drink.drink'

    customer_name = fields.Many2one("res.partner", ondelet="set null", string="customer name",
                                    required=True)
    order_list = fields.Many2many("drink.drink", required=True, index=True,
                                  string="order")
    # total_price = fields.Float(string="Total price", compute='Total_price', store=True)
    #
    # @api.depends('price')
    # def Total_price(self):
    #     for r in self:
    #         total = 0.0
    #         for line in r.order_list:
    #             total += line.price
    #         r.total_price = total
