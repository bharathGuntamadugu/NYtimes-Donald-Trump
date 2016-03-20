#!/usr/bin/env python
# coding=utf-8

import sys
import time

def reducer():
    resultSummary = dict()
    for line in sys.stdin:
        result=0
        data=line.strip().split('\t')
        date, url, para, positive, negative = data
        y,m,d = date.split("-")
        yearMonth = "{0}-{1}".format(y, m)
        pos=int(positive)
        neg=int(negative)
        result=(3*pos)-(7*neg)
        if (yearMonth in resultSummary.keys()):
            resultSummary[yearMonth] = resultSummary[yearMonth] + result 
        else:
            resultSummary[yearMonth] = result
    print (resultSummary)
        
reducer()
        
