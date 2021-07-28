'''
© 2021 AnD CGI This work is licensed under a
Creative Commons Attribution-ShareAlike 4.0 International License.

Get Row Column Position Of Current Date

This Is Way To Get The Row Column Postion Of Current(Any) Date From
The 7 x 6 Matrix Type Calender That Python Uses.
'''
import calendar
import datetime 
import numpy as np
import re
thisDay = datetime.datetime.now()
dDay = thisDay.day
dYear = thisDay.year

cal = calendar.TextCalendar(calendar.SUNDAY)
iCal = cal.formatmonth(thisDay.year, thisDay.month)

getSpanYear = re.search((r'\b{}\b').format(dYear), iCal)
mkLstYr = list(getSpanYear.span())
d = mkLstYr[1]+1
iCal = iCal[d:]

getSpanDt = re.search((r'\b{}\b').format(dDay), iCal)
mkLstDt = list(getSpanDt.span())
rw = mkLstDt[0]//21
clm = mkLstDt[0]%21
clm = int(clm/3)+1
print(iCal)
print(rw)
print(clm)
