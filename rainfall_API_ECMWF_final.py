#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 14:57:50 2018

@author: louwrenstimmer
"""
# Created on Tue 6 November 2018
# by Louwrens Timmer - 10668470
#!/usr/bin/env python

from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
 
def retrieve_cera20c_edmm():
    """
       A function to demonstrate how to iterate efficiently over all months."       
    """
    yearStart = 1991
    yearEnd = 2010
    monthStart = 1
    monthEnd = 12
    # edmm is arranged by years, so we iterate over the years
    for year in list(range(yearStart, yearEnd + 1)):
        requestMonthList = []
        for month in list(range(monthStart, monthEnd + 1)):
            requestMonthList.append('%04d-%02d-01' % (year, month))
        requestMonths = "/".join(requestMonthList)
        # a data request is submitted for the current year
        target = "cera20c_edmo_fc_%s_tp_python.nc" % (year)
        era20c_edmm_sfc_request(requestMonths, target)
 
def era20c_edmm_sfc_request(requestMonths, target):
    """     
        A CERA-20C request for analysis, sfc prcp data.
        Keywords and parameters can be changed below.
    """
    server.retrieve({
    "class": "ep",
    "dataset": "cera20c",
    "date": requestMonths,
#   "date": "20000101/20000201/20000301/20000401/20000501/20000601/20000701/20000801/20000901/20001001/20001101/20001201",
    "expver": "0001",
    "repres": "SH",
    "levtype": "sfc",
    "number": "0/1/2/3/4/5/6/7/8/9",
    "domain": "G",
    "resol": "AUTO",
    "param": "228.128",
    "stream": "edmo",
    "type": "fc",
#   N/W/S/E
    "area": "-26/27/-33/33",
    "grid": "0.125/0.125",  
    "target": target,
    "format": "netcdf",
#   "target": "cera20c_monthly_an_prcp_2000to2010.nc",
})
 
if __name__ == '__main__':
    retrieve_cera20c_edmm()