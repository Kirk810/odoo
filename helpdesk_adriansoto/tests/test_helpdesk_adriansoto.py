from odoo.tests.common import TransactionCase

class TestHelpdeskAdrianSoto(TransactionCase):
    def setUp(self):
        super(TestHelpdeskAdrianSoto, self).setUp()

        self.tcket = self.env["helpdesk.ticket"].create({
            'name': 'Test ticket'
        })
        self.user_id = self.ref('base.user_admin')
        
    def test_01_ticket(self):
        self.assertEqual(self.ticket.name, "Test ticket")
        
    def test_02_ticket(self):
        self.assertEqual(self.ticket.user_id, self.env['res.user'])
        self.ticket.user_id = self.user_id
        self.assertEqual(self.ticket.user_id, self.user_id)
        
    def test_03_ticket(self):
        self.assertFalse(self.ticket.name == "Test ticket")
        