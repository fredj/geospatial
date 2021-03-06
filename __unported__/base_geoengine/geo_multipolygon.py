# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Nicolas Bessi
#    Copyright 2011-2012 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from __future__ import absolute_import
from osv import fields
from . import geo_field

class GeoMultiPolygon(geo_field.Geom):
    """New type of column in the  ORM for POSTGIS geometry MultiPolygon type"""
    _type = 'geo_multi_polygon'
    def __init__(self, string, dim=2, srid=900913 , gist_index=True, **args):
        res = super(GeoMultiPolygon, self).__init__(string, "MULTIPOLYGON",
                                                    dim=dim, srid=srid, gist_index=gist_index, **args)
        return res

fields.geo_multi_polygon = GeoMultiPolygon
