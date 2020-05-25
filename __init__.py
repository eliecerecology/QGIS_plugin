# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PluginLoad
                                 A QGIS plugin
 plugin to load a layer
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-05-25
        copyright            : (C) 2020 by eliecer
        email                : eliecer
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PluginLoad class from file PluginLoad.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .loadlayer import PluginLoad
    return PluginLoad(iface)
