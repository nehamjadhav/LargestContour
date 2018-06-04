from DetectContour import settings
from DetectContour.database.geoserver_interface import GeoserverInterface

__author__ = 'minjoon'

geoserver_interface = GeoserverInterface(settings.GEOSERVER_URL)
