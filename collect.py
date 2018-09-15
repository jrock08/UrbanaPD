from sodapy import Socrata
client = Socrata('data.urbanaillinois.us',None)


codes_to_query = {'bike': ['6520', '6680', '8818', '8819'],
        'pedestrian': ['6674', '6710','6711','6712'],
        'car_failure_to_yield': ['6616', '6617', '6618', '6619', '6620', '6687'],
        'car_stop_sign': ['6605'],
        'car_stop_light': ['6606'],
        'car_mobile_phone': ['6635']}

years = ['%d'%(n) for n in range(2008,2018)]

queries = {}
for key in codes_to_query:
    queries[key] = {}
    for year in years:
        queries[key][year] = []

    for code in codes_to_query[key]:
        for year in years:
            queries[key][year].extend(client.get("x5m7-in2r", where="crime_code = '%s' and year_of_arrest = '%s'"%(code, year)))

def print_per_year(data):
    for year in years:
        print 'year: %s, num: %d'%(year, len(data[year]))

for key in queries:
    print key
    print_per_year(queries[key])

