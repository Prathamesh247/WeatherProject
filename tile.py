from pyowm import OWM
from pyowm.tiles.enums import MapLayerEnum
from pyowm.utils.geo import Point
from pyowm.commons.tile import Tile

api_key = "56b68c7a673ba0a55a2035d3d7c0a2eb"

owm = OWM(api_key)

layer_name = MapLayerEnum.WIND

tm = owm.tile_manager(layer_name)

tile = tm.get_tile(3, 2, 2)

tile.persist('C:/Users/Admin/Desktop/APSIT/Programs/WeatherProject/file2.png')

geopoint = Point(5, 2)
X_tile, Y_tile = Tile.tile_coords_for_point(geopoint, 6)