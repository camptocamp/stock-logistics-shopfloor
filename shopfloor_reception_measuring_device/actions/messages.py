# Copyright 2025 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import _
from odoo.addons.component.core import Component

class MessageAction(Component):
    _inherit = "shopfloor.message.action"

    def no_measuring_device_found(self):
        return {
            "message_type": "error",
            "body": _("No measuring device found"),
        }

    def measuring_device_already_in_use(self, device):
        return {
            "message_type": "error",
            "body": _("Measuring device %s already in use", device.name),
        }

    def measuring_device_selected(self, device, packaging):
        return {
            "message_type": "success",
            "body": _(
                (
                    "The device %s has been reserved, "
                    "you can now measure packaging %s"
                ),
                device.name, packaging.name,
            ),
        }

    def no_measuring_device_to_release(self, packaging):
        return {
            "message_type": "warning",
            "body": _(
                "No measuring device to release from packaing %s", packaging.name
            ),
        }

    def measuring_device_released(self, packaging, device):
        return {
            "message_type": "success",
            "body": _(
                "The device has %s has been released from packaging %s",
                device.name, packaging.name,
            ),
        }
