#!/usr/bin/env python
# This file is part of the stock_search_shipment module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.tests.test_tryton import test_view, test_depends
import trytond.tests.test_tryton
import unittest


class StockSearchShipmentTestCase(unittest.TestCase):
    'Test Stock Search Shipment module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('stock_search_shipment')

    def test0005views(self):
        'Test views'
        test_view('stock_search_shipment')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockSearchShipmentTestCase))
    return suite
