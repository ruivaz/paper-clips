xml.sax.parse("allroutes.xml",
 EventHandler(
 buses_to_dicts(
 filter_on_field("route","22",
 filter_on_field("direction","North Bound",
 bus_locations())))
 ))
