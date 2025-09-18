# Copyright 2023 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

# from odoo.osv import expression

# from odoo.addons.base_rest.components.service import to_int
from odoo.addons.component.core import Component

# from odoo.addons.shopfloor.utils import to_float


class Reception(Component):
    _inherit = "shopfloor.reception"

    def _set_destination_handle_extra_params(
        self, picking, selected_move_line, **kwargs
    ):
        if "height" in kwargs:
            height = kwargs.get("height")
            package = selected_move_line.result_package_id
            if height and package:
                # TODO validate height
                package.height = height
        return None
        # res = super()._set_destination_handle_extra_params(
        #     picking, selected_move_line, **kwargs
        # )


class ShopfloorReceptionValidator(Component):
    _inherit = "shopfloor.reception.validator"

    def set_destination(self):
        res = super().set_destination()
        res["height"] = {"type": "float", "required": False}
        res["height_uom"] = {"type": "string", "required": False}
        res["height_required"] = {"type": "boolean", "required": False}
        return res


class ShopfloorReceptionValidatorResponse(Component):
    _inherit = "shopfloor.reception.validator.response"

    # def _set_lot_confirm_action_next_states(self):
    #     res = super()._set_lot_confirm_action_next_states()
    #     res.update({"set_packaging_dimension"})
    #     return res

    # @property
    # def _schema_set_packaging_dimension(self):
    #     return {
    #         "picking": {"type": "dict", "schema": self.schemas.picking()},
    #         "selected_move_line": {
    #                "type": "dict",
    #                "schema": self.schemas.move_line()},
    #                "packaging": self._schema_packaging(),
    #     }

    # def _schema_packaging(self):
    #     return {
    #         "type": "dict",
    #         "schema": self.schemas_detail.packaging_detail(),
    #     }

    # def _set_packaging_dimension_next_states(self):
    #     return {"set_packaging_dimension", "set_quantity"}

    # def set_packaging_dimension(self):
    #     return self._response_schema(
    #         next_states=self._set_packaging_dimension_next_states()
    #     )
