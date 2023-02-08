# -*- coding: utf-8 -*-


from odoo import models, fields, api
from odoo.osv import expression


class RentalCustomerDriver(models.Model):
    _name = 'rental.customer.driver'
    _description = "Rental Customer Driver"

    name = fields.Char("Name", required=True)
    civil_id = fields.Char("Civil Id", required=True)
    vehicle_id = fields.Many2one('rental.customer.vehicle', string='Vehicle')

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        if name and operator in ('=', 'ilike', '=ilike', 'like', '=like'):
            args = args or []
            domain = ['|', ('name', operator, name), ('civil_id', operator, name)]
            attribute_ids = self._search(expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid)
            return models.lazy_name_get(self.browse(attribute_ids).with_user(name_get_uid))
        return super(RentalCustomerDriver, self)._name_search(name=name, args=args, operator=operator,
                                                              limit=limit, name_get_uid=name_get_uid)


class RentalCustomerVehicle(models.Model):
    _name = 'rental.customer.vehicle'
    _description = "Rental Customer Vehicle"

    name = fields.Char("Name", required=True)
    plate_no = fields.Char("Plate No", required=True)
