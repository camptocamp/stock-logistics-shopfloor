# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo.addons.component.core import Component


class ShopfloorSchemaAction(Component):
    _inherit = "shopfloor.schema.action"

    def package(self, with_packaging=False):
        res = super().package(with_packaging=with_packaging)
        res["package_type_id:package_type"] = self._schema_dict_of(
            self._simple_record(), required=False
        )
        return res
