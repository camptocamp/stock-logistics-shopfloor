# Copyright 2025 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo.addons.component.core import Component


class ShopfloorSchemaDetailAction(Component):
    _inherit = "shopfloor.schema.detail.action"

    def packaging_detail(self):
        res = super().packaging_detail()
        res.update(
            {
                "is_being_measured": {
                    "type": "boolean",
                    "nullable": False,
                    "required": True,
                }
            }
        )
        return res
