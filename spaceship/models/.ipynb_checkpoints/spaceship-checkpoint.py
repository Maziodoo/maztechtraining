# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spaceship(models.Model) :
    
    _name = 'spaceship'
    _description = 'Spaceship Model to get to the moon'
    
    name = fields.Char(string='Rocket Name', required=True)
    description = fields.Text(string='Rocket description')