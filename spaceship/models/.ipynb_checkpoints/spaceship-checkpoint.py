# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spaceship(models.Model) :
    
    _name = 'spaceship'
    _description = 'Spaceship Model to get to the moon'
    
    name = fields.Char(string='Rocket Name', required=True)
    description = fields.Text(string='Rocket description')
    dimensions = fields.Float(string='Ship Dimensions')
    ship_type = fields.Selection(string='Ship Type',
                             selection=[('small', 'Small'),
                                        ('medium', 'Medium'),
                                        ('large', 'Large')],
                             copy=False)
    count_passengers = fields.Integer(string='No. of passengers')
    active = fields.Boolean(string='Active', default=True)