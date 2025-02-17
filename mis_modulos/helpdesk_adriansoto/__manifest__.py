# Copyright 2025 ODOO
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk Adrian Soto",
    "version": "18.0.1.0",
    "author": "ODOO, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": [
        "base",
        "mail",
    ],
    "data": [
        "data/delete_tag_cron.xml",
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "report/helpdesk_ticket_report_templates.xml",
        "views/helpdesk_menu.xml",
        "wizards/create_ticket_view.xml",
        "views/helpdesk_tag_view.xml",
        "views/helpdesk_view.xml",
    ],
}