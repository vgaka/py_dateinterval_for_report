#!/usr/bin/env python
# coding: utf-8

# # Class ToDay


import os
import datetime


class ToDay():
    def __setattr__(self, name, value):
        #print('set attribute', name)
        if name in ['beginlastmonth','beginnextmonth','date_time',
                    'beginthismonth','beginthisquarter','endlastmonth',
                    'endnextmonth','endthismonth','monthlist','now',
                    'today','beginnextcouplemonths','endnextcouplemonths']:
            return super().__setattr__(name, value)
        raise AttributeError('Unable to edit')
    def __getattribute__(self, name):
        if name in ('subtype'):
            raise AttributeError('Unable to view this object')
        return super().__getattribute__(name)
    
    def datetime(self, name):
        s = self.__getattribute__(name)
        return datetime.datetime(s.year, s.month, s.day, 0 ,0 ,0)

    def __init__(self):
        def last_day_of_month(any_day):
            next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
            return next_month - datetime.timedelta(days=next_month.day)
        def get_quarter(any_dt, locale='US'):
            if locale == 'JP':
                return int((any_dt.month -1 )/3)
        self.monthlist = [i for i in range(1,13)]
        self.now = datetime.datetime.now()
        self.today = datetime.datetime.today().date()
        self.beginthismonth = datetime.datetime(self.now.year,self.now.month,1).date()
        self.endthismonth = last_day_of_month(self.today)
        self.beginlastmonth = self.beginthismonth-datetime.timedelta(days=1)
        self.beginlastmonth = self.beginlastmonth.replace(day=1)
        self.endlastmonth = self.beginthismonth-datetime.timedelta(days=1)
        self.beginnextmonth = self.endthismonth+datetime.timedelta(days=1)
        endnextmonth = self.beginnextmonth+datetime.timedelta(weeks=6)
        self.endnextmonth = endnextmonth-datetime.timedelta(days= endnextmonth.day)
        beginnextcouplemonths = self.beginnextmonth+datetime.timedelta(days=45)
        self.beginnextcouplemonths = beginnextcouplemonths.replace(day=1)
        endnextcouplemonths = self.endnextmonth+datetime.timedelta(weeks=6)
        self.endnextcouplemonths = endnextcouplemonths-datetime.timedelta(days = endnextcouplemonths.day)
    def info(self):
        return self.__dict__
        # return f"today:= {self.today} lastmonth:= {self.beginlastmonth}:{self.endlastmonth} thismonth:= {self.beginthismonth}:{self.endthismonth}"
            
       
if __name__=='__main__':
    mydate = ToDay()
    print(mydate.info())
    print(mydate.date_time('endthismonth'))
