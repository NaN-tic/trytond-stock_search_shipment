# This file is part of the stock_search_shipment module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields, ModelView
from trytond.pool import Pool, PoolMeta
from trytond.wizard import Button, StateAction, StateView, Wizard
from trytond.pyson import PYSONEncoder
from trytond.transaction import Transaction

__all__ = ['ShipmentIn', 'ShipmentInReturn',
    'ShipmentOut', 'ShipmentOutReturn', 'ShipmentInternal',
    'StockSearchShipmentStart', 'StockSearchShipmentStartFields',
    'StockSearchShipment']

__metaclass__ = PoolMeta


class ShipmentIn():
    __name__ = 'stock.shipment.in'

    @classmethod
    def search_rec_name(cls, name, clause):
        return ['OR',
            ('code',) + tuple(clause[1:]),
            ('reference',) + tuple(clause[1:]),
            ]


class ShipmentInReturn():
    __name__ = 'stock.shipment.in.return'

    @classmethod
    def search_rec_name(cls, name, clause):
        return ['OR',
            ('code',) + tuple(clause[1:]),
            ('reference',) + tuple(clause[1:]),
            ]


class ShipmentOut():
    __name__ = 'stock.shipment.out'

    @classmethod
    def search_rec_name(cls, name, clause):
        return ['OR',
            ('code',) + tuple(clause[1:]),
            ('reference',) + tuple(clause[1:]),
            ]


class ShipmentOutReturn():
    __name__ = 'stock.shipment.out.return'

    @classmethod
    def search_rec_name(cls, name, clause):
        return ['OR',
            ('code',) + tuple(clause[1:]),
            ('reference',) + tuple(clause[1:]),
            ]


class ShipmentInternal():
    __name__ = 'stock.shipment.internal'

    @classmethod
    def search_rec_name(cls, name, clause):
        return ['OR',
            ('code',) + tuple(clause[1:]),
            ('reference',) + tuple(clause[1:]),
            ]


class StockSearchShipmentStart(ModelView):
    'Stock Search Shipment Start'
    __name__ = 'stock.search.shipment.start'
    shipments = fields.One2Many('stock.search.shipment.start.field', 'search',
        'Shipments')


class StockSearchShipmentStartFields(ModelView):
    'Stock Search Shipment Start'
    __name__ = 'stock.search.shipment.start.field'
    search = fields.Many2One('stock.search.shipment.start', 'Search')
    name = fields.Char('Code', required=True,
        help='The code of the stock shipment you are looking for.')


class StockSearchShipment(Wizard):
    'Stock Search Shipment'
    __name__ = 'stock.search.shipment'
    start = StateView('stock.search.shipment.start',
        'stock_search_shipment.stock_search_shipment_start_form_view', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Search', 'open_', 'tryton-ok', True),
            ])
    open_ = StateAction('stock.act_shipment_out_form')

    def do_open_(self, action):
        pool = Pool()
        context = Transaction().context
        Shipment = pool.get(context['active_model'])
        ActWindow = pool.get('ir.action.act_window')
        View = pool.get('ir.ui.view')
        ActWindowView = pool.get('ir.action.act_window.view')

        action_window, = ActWindow.search([
                ('res_model', '=', context['active_model']),
                ('domain', '=', None),
                ], limit=1)
        codes = [s.name for s in self.start.shipments]
        shipments = [s.id for s in Shipment.search([
                    ('code', 'in', codes),
                    ])]
        if shipments:
            action['pyson_domain'] = PYSONEncoder().encode([
                    ('id', 'in', shipments),
                    ])
            if context['active_model'] != 'stock.shipment.out':
                action['res_model'] = context['active_model']
                action['name'] = action_window.action.name
                action['rec_name'] = action['name']
                action['views'] = [(v.id, v.type)
                    for v in View.search([
                            ('model', '=', context['active_model']),
                            ], order=[('type', 'DESC')]) if v.type]
                action['act_window_views'] = [v.id
                    for v in ActWindowView.search([
                            ('act_window', '=', action_window),
                            ])]
            del action['act_window_domains']
            action['domains'] = []
            self.start.shipments = None
        return action, {}
