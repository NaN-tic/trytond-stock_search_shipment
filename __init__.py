# This file is part of the stock_search_shipment module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .shipment import *


def register():
    Pool.register(
        ShipmentIn,
        ShipmentInReturn,
        ShipmentOut,
        ShipmentOutReturn,
        ShipmentInternal,
        StockSearchShipmentStart,
        StockSearchShipmentStartFields,
        module='stock_search_shipment', type_='model')
    Pool.register(
        StockSearchShipment,
        module='stock_search_shipment', type_='wizard')
