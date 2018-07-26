import pygeoip
gi=pygeoip.GeoIP('GeoLiteCity.dat')

target=raw_input("Please enter a target Ip:")

def trace(target):

	record=gi.record_by_addr(target)
	city=record['city']
	region=record['region_code']
	country=record['country_name']
	country_code=record['country_code']
	lon=record['longitude']
	lat=record['latitude']
	print '[*] Target:'+ target +' Geo-located.'
	print '[+]'+str(city)+'.'+str(region)+'.'+str(country)+'('+str(country_code)+')'
	print '[+] Latitude:'+str(lat)+'.Longitude:'+str(lon)

trace(target)


