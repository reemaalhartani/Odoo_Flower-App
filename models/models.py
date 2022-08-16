# -*- coding: utf-8 -*-

from odoo import models, fields, api


class flower_app(models.Model):
     _name = 'flower_app.flower_app'

     CommonName = fields.Char(string='Common Name')
     ScientifiName = fields.Char(string='Scientific Name')
     SeasonStart = fields.Date(string="Start Of Season")
     SeasonEnd = fields.Date(string="End Of Season")
     WateringFreq = fields.Char(string='Watering Frequancy')
     WateringAmount = fields.Float(string='Watering Amount')


