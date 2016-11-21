# -*- coding: utf-8 -*-
"""
/***************************************************************************
OpenLayers Plugin
A QGIS plugin

                             -------------------
begin                : 2009-11-30
copyright            : (C) 2009 by Pirmin Kalberer, Sourcepole
email                : pka at sourcepole.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4.QtCore import QSettings
from weblayer import WebLayer3857


class OlBairesMapsLayer(WebLayer3857):

    emitsLoadEnd = True

    def __init__(self, name, html):
        WebLayer3857.__init__(self, groupName="Baires Maps", groupIcon="google_icon.png",
                              name=name, html=html)

    #def html_url(self):
    #    url = WebLayer3857.html_url(self)
    #    #apiKey = QSettings().value("Plugin-OpenLayers/googleMapsApiKey")
    #    #if apiKey != None and bool(apiKey.strip()):
    #    #    url += "?key=%s" % apiKey
    #    return url

class OlBairesLayer(OlBairesMapsLayer):

    def __init__(self):
        OlBairesMapsLayer.__init__(self, name="Baires Map", html="baires.html")
