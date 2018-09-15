import math
import pandas
import seaborn as sns
import matplotlib.pyplot as plt

from sodapy import Socrata
client = Socrata('data.urbanaillinois.us',None)


codes_to_query = {'bike': ['6520', '6680', '8818', '8819'],
        'pedestrian': ['6674', '6710','6711','6712'],
        'car_failure_to_yield': ['6616', '6617', '6618', '6619', '6620', '6687'],
        'car_stop_sign': ['6605'],
        'car_stop_light': ['6606'],
        'car_mobile_phone': ['6635']}

years = ['%d'%(n) for n in range(2008,2018)]

all_data = []
for key in codes_to_query:
    for code in codes_to_query[key]:
        for year in years:
            X = client.get("x5m7-in2r", where="crime_code = '%s' and year_of_arrest = '%s'"%(code, year))
            for v in X:
                v['my_label'] = key
            all_data.extend(X)

dat = pandas.DataFrame(data=all_data)
dat['age_at_arrest'] = pandas.to_numeric(dat['age_at_arrest'])
V = []
for key in codes_to_query:
    print key
    sns.distplot(dat[dat['my_label'] == key]['age_at_arrest'], label=key)
    #dat[dat['my_label'] == key]['age_at_arrest'])
plt.legend()
plt.show()
#sns.distplot(V)
#sns.distplot(dat[dat['my_label']=='bike']['age_at_arrest'])

#fmt_data = {}
#fmt_data['age'] = range(100)
#def print_per_year(data, name):
#    counts = None
#    for year in years:
#        print 'year: %s, num: %d'%(year, len(data[year]))
#        counts = age_distribution(data[year], counts)
#    fmt_data[name] = counts
#
#def age_distribution(data, counts = None):
#    if counts is None:
#        counts = [0 for x in range(100)]
#    for d in data:
#        age = int(math.floor(float(d['age_at_arrest'])))
#        counts[age] += 1
#    return counts
#
#for key in queries:
#    print key
#    print_per_year(queries[key], key)
#
#V = pandas.DataFrame(data=fmt_data)


#years = ['%d'%(n) for n in range(2014, 2018)]
#months = ['%d'%(n+1) for n in range(12)]
#query_year_month = {}
#for key in codes_to_query:
#    query_year_month[key] = {}
#    for year in years:
#        query_year_month[key][year] = {}
#        for month in months:
#            query_year_month[key][year][month] = []
#
#    for code in codes_to_query[key]:
#        for year in years:
#            for month in months:
#                query_year_month[key][year][month].extend(client.get("x5m7-in2r", where="crime_code = '%s' and year_of_arrest = '%s' and month_of_arrest='%s'"%(code, year, month)))
#
#def print_per_year_month(data):
#    for year in years:
#        print 'year: %s'%(year)
#        month_dat = []
#        for month in months:
#            month_dat.append('%d'%(len(data[year][month])))
#        print ', '.join(month_dat)
#
#for key in query_year_month:
#    print key
#    print_per_year_month(query_year_month[key])



