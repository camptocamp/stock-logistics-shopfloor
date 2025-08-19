# Copyright 2025 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo.addons.component.core import Component


class DataDetailAction(Component):
    _inherit = "shopfloor.data.detail.action"

    @property
    def _packaging_detail_parser(self):
        res = super()._packaging_detail_parser
        res.append(
            ("is_being_measured", lambda rec, fname: bool(rec.measuring_device_id))
        )
        return res
