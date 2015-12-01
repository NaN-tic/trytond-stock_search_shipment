# This file is part of the stock_search_shipment module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class StockSearchShipmentTestCase(ModuleTestCase):
    'Test Stock Search Shipment module'
    module = 'stock_search_shipment'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockSearchShipmentTestCase))
    return suite