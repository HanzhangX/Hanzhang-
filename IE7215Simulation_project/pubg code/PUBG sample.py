# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:50:53 2020

@author: lenovo
"""

import SimFunctions
import SimRNG
import SimClasses
import pandas
import numpy as np
import matplotlib.pyplot as plt

ZSimRNG = SimRNG.InitializeRNSeed()
Queue1 = SimClasses.FIFOQueue()
Queue2 = SimClasses.FIFOQueue()
Queue4 = SimClasses.FIFOQueue()
Wait1 = SimClasses.DTStat()
Wait2 = SimClasses.DTStat()
Wait4 = SimClasses.DTStat()
Server = SimClasses.Resource()
Calendar = SimClasses.EventCalendar()

TheCTStats = []
TheDTStats = []
TheQueues = []
TheResource = []
ServerNumber= []

TheDTStats.append (Wait1)
TheQueues.append (Queue1)
TheDTStats.append (Wait2)
TheQueues.append (Queue2)
TheDTStats.append (Wait4)
TheQueues.append (Queue4)
TheResource.append (Server)

count = 0
servernumber = 0
MeanTBA = 1.0
MeanST = 18
Runlength =10*720.0
BattleNum = 99
AllWait1Mean = []
AllQueue1Mean = []
AllWait2Mean = []
AllQueue2Mean = []
AllWait4Mean = []
AllQueue4Mean = []
AllQueueNum = []
AllServerMean = []
AllServerMax = []

print ("Rep", "Average Wait1", "Average Number in Queue1","Average Wait2", "Average Number in Queue2","Average Wait3", "Average Number in Queue3", "Average Server Number", "Max Server Number")

def Arrival():
    
    if 0 < SimClasses.Clock < 720:
        MeanTBA = 3.23
    elif 720 < SimClasses.Clock < 2*720:
        MeanTBA = 6.195
    elif 2*720 < SimClasses.Clock < 3*720:
        MeanTBA = 8.954
    elif 3*720 < SimClasses.Clock < 4*720:
        MeanTBA = 6.717
    elif 4*720 < SimClasses.Clock < 5*720:
        MeanTBA = 5.225
    elif 5*720 < SimClasses.Clock < 6*720:
        MeanTBA = 3.358
    elif 6*720 < SimClasses.Clock < 7*720:
        MeanTBA = 11.07
    elif 7*720 < SimClasses.Clock < 8*720:
        MeanTBA = 11.07
    elif 8*720 < SimClasses.Clock < 9*720:
        MeanTBA = 3.733
    else:
        MeanTBA = 1.867
    
    interarrival = SimRNG.Expon(1/MeanTBA,1)
    SimFunctions.Schedule(Calendar, "Arrival", interarrival)
    Customer = SimClasses.Entity()
    global count 
    count = count + 1
    
    if SimRNG.Uniform(0.0, 1.0, 2) < 0.2:
        Queue1.Add(Customer)
        if Queue1.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
            Server.Seize(1)
            global servernumber
            servernumber = servernumber + 1
            ServerNumber.append(servernumber)
            global t
            t=[0]
            cp = Queue1.NumQueue()
            for i in range (0,cp,1):
                if i == cp-1:
                    ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win1")
                    DepartingCustomer = Queue1.Remove()
                    Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                elif i/cp < 0.1:
                    ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon1")
                    DepartingCustomer = Queue1.Remove()
                    Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                elif i/cp < 0.5:
                    ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half1")
                    DepartingCustomer = Queue1.Remove()
                    Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                else:
                    ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin1")
                    DepartingCustomer = Queue1.Remove()
                    Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    
    elif SimRNG.Uniform(0.0,1.0,2) < 0.6:
        Queue2.Add(Customer)
        if Queue2.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
            Server.Seize(1)
            #global servernumber
            servernumber = servernumber + 1
            ServerNumber.append(servernumber)
            #global t
            t=[0]
            cp = Queue2.NumQueue()
            for i in range (0,cp,1):
                if i == cp-1:
                    ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win2")
                    DepartingCustomer = Queue2.Remove()
                    Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                elif i/cp < 0.1:
                    ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon2")
                    DepartingCustomer = Queue2.Remove()
                    Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                elif i/cp < 0.5:
                    ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half2")
                    DepartingCustomer = Queue2.Remove()
                    Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                else:
                    ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin2")
                    DepartingCustomer = Queue2.Remove()
                    Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    
    else:
        Queue4.Add(Customer)
        if Queue4.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
            Server.Seize(1)
            #global servernumber
            servernumber = servernumber + 1
            ServerNumber.append(servernumber)
            #global t
            t=[0]
            cp = Queue4.NumQueue()
            for i in range (0,cp,1):
                if i == cp-1:
                    ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win4")
                    DepartingCustomer = Queue4.Remove()
                    Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                elif i/cp < 0.1:
                    ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon4")
                    DepartingCustomer = Queue4.Remove()
                    Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                elif i/cp < 0.5:
                    ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half4")
                    DepartingCustomer = Queue4.Remove()
                    Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                else:
                    ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin4")
                    DepartingCustomer = Queue4.Remove()
                    Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                
def ScheduleEOS (calendar, EventType, EventTime, TheObject):
    total = 0
    for ele in range (0, len(t)):
        total =total + t[ele]
    
    addedEvent = SimClasses.EventNotice()
    addedEvent.EventType = EventType
    addedEvent.EventTime = SimClasses.Clock + EventTime + total
    addedEvent.WhichObject = TheObject
    t.append (EventTime)
    calendar.Schedule(addedEvent)
    
def EndOfService():
    if SimRNG.Uniform(0.0,1.0,2)<0.7:    
        AgainOrNot()
    Server.Free(1)
    global servernumber
    servernumber = servernumber - 1
    ServerNumber.append(servernumber)
    
    
def ContinueService():
    if NextEvent.WhichObject == "DieSoon1" or "DieSoon2" or "DieSoon4":
        if SimRNG.Uniform(0.0,1.0,2)<0.6:
            AgainOrNot()
    elif NextEvent.WhichObject == "Half1" or "Half2" or "Half4":
        if SimRNG.Uniform(0.0,1.0,2)<0.6:
            AgainOrNot()
    else:
        if SimRNG.Uniform(0.0,1.0,2)<0.5:
            AgainOrNot()
    #pass


  
def AgainOrNot():
    #if customer choose to continue play, add a customer in a queue
    Customer = SimClasses.Entity()
    global count 
    count = count + 1
    
    if NextEvent.WhichObject == "Win1" or "AlmostWin1":
        
        if SimRNG.Uniform(0.0, 1.0, 2) < 0.5:
            Queue1.Add(Customer)
            if Queue1.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                global servernumber
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                global t
                t=[0]
                cp = Queue1.NumQueue()
                for i in range (0,cp,1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    
        elif SimRNG.Uniform(0.0,1.0,2) < 0.76:
            Queue2.Add(Customer)
            if Queue2.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue2.NumQueue()
                for i in range (0,cp,1):
                    if i == cp:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    
        else:
            Queue4.Add(Customer)
            if Queue4.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue4.NumQueue()
                for i in range (0,cp,1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                        
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
     
    elif NextEvent.WhichObject == "Win2" or "AlmostWin2":
        
        if SimRNG.Uniform(0.0, 1.0, 2) < 0.192:
            Queue1.Add(Customer)
            if Queue1.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue1.NumQueue()
                for i in range (0,cp,1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    
        elif SimRNG.Uniform(0.0,1.0,2) < 0.692:
            Queue2.Add(Customer)
            if Queue2.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue2.NumQueue()
                for i in range (0,Queue2.NumQueue(),1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    
        else:
            Queue4.Add(Customer)
            if Queue4.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue4.NumQueue()
                for i in range (0,cp,1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                        
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
 
                       
    elif NextEvent.WhichObject == "Win4" or "AlmostWin4":
        
        if SimRNG.Uniform(0.0, 1.0, 2) < 0.182:
            Queue1.Add(Customer)
            if Queue1.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue1.NumQueue()
                for i in range (0,cp,1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    
        elif SimRNG.Uniform(0.0,1.0,2) < 0.5:
            Queue2.Add(Customer)
            if Queue2.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue2.NumQueue()
                for i in range (0,cp,1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    
        else:
            Queue4.Add(Customer)
            if Queue4.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue4.NumQueue()
                for i in range (0,Queue4.NumQueue(),1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                        
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                        
                        
    elif NextEvent.WhichObject == "Half1":
        
        if SimRNG.Uniform(0.0, 1.0, 2) < 0.48:
            Queue1.Add(Customer)
            if Queue1.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue1.NumQueue()
                for i in range (0,Queue1.NumQueue(),1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    
        elif SimRNG.Uniform(0.0,1.0,2) < 0.75:
            Queue2.Add(Customer)
            if Queue2.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue2.NumQueue()
                for i in range (0,Queue2.NumQueue(),1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    
        else:
            Queue4.Add(Customer)
            if Queue4.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue4.NumQueue()
                for i in range (0,Queue4.NumQueue(),1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                        
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                        
                        
    elif NextEvent.WhichObject == "Half2":
        
        if SimRNG.Uniform(0.0, 1.0, 2) < 0.19:
            Queue1.Add(Customer)
            if Queue1.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue1.NumQueue()
                for i in range (0,Queue1.NumQueue(),1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    
        elif SimRNG.Uniform(0.0,1.0,2) < 0.67:
            Queue2.Add(Customer)
            if Queue2.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue2.NumQueue()
                for i in range (0,Queue2.NumQueue(),1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    
        else:
            Queue4.Add(Customer)
            if Queue4.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue4.NumQueue()
                for i in range (0,Queue4.NumQueue(),1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                        
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                        
                        
    elif NextEvent.WhichObject == "Half4":
        
        if SimRNG.Uniform(0.0, 1.0, 2) < 0.19:
            Queue1.Add(Customer)
            if Queue1.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue1.NumQueue()
                for i in range (0,Queue1.NumQueue(),1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    
        elif SimRNG.Uniform(0.0,1.0,2) < 0.52:
            Queue2.Add(Customer)
            if Queue2.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue2.NumQueue()
                for i in range (0,Queue2.NumQueue(),1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    
        else:
            Queue4.Add(Customer)
            if Queue4.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue4.NumQueue()
                for i in range (0,Queue4.NumQueue(),1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                        
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                        
                        
    elif NextEvent.WhichObject == "DieSoon1":
        
        if SimRNG.Uniform(0.0, 1.0, 2) < 0.47:
            Queue1.Add(Customer)
            if Queue1.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue1.NumQueue()
                for i in range (0,Queue1.NumQueue(),1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    
        elif SimRNG.Uniform(0.0,1.0,2) < 0.769:
            Queue2.Add(Customer)
            if Queue2.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue2.NumQueue()
                for i in range (0,Queue2.NumQueue(),1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    
        else:
            Queue4.Add(Customer)
            if Queue4.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue4.NumQueue()
                for i in range (0,Queue4.NumQueue(),1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                        
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                        
    elif NextEvent.WhichObject == "DieSoon2":
        
        if SimRNG.Uniform(0.0, 1.0, 2) < 0.158:
            Queue1.Add(Customer)
            if Queue1.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue1.NumQueue()
                for i in range (0,Queue1.NumQueue(),1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    
        elif SimRNG.Uniform(0.0,1.0,2) < 0.628:
            Queue2.Add(Customer)
            if Queue2.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue2.NumQueue()
                for i in range (0,Queue2.NumQueue(),1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    
        else:
            Queue4.Add(Customer)
            if Queue4.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue4.NumQueue()
                for i in range (0,Queue4.NumQueue(),1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                        
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                      
    elif NextEvent.WhichObject == "DieSoon4":
        
        if SimRNG.Uniform(0.0, 1.0, 2) < 0.193:
            Queue1.Add(Customer)
            if Queue1.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue1.NumQueue()
                for i in range (0,Queue1.NumQueue(),1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin1")
                        DepartingCustomer = Queue1.Remove()
                        Wait1.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    
        elif SimRNG.Uniform(0.0,1.0,2) < 0.53:
            Queue2.Add(Customer)
            if Queue2.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue2.NumQueue()
                for i in range (0,Queue2.NumQueue(),1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin2")
                        DepartingCustomer = Queue2.Remove()
                        Wait2.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    
        else:
            Queue4.Add(Customer)
            if Queue4.NumQueue()>BattleNum or SimClasses.Clock-Customer.CreateTime>60:
                Server.Seize(1)
                servernumber = servernumber + 1
                ServerNumber.append(servernumber)
                #global t
                t=[0]
                cp = Queue4.NumQueue()
                for i in range (0,Queue4.NumQueue(),1):
                    if i == cp-1:
                        ScheduleEOS (Calendar,"EndOfService", SimRNG.Expon(MeanST, 2), "Win4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
            
                    elif i/cp < 0.1:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "DieSoon4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                        
                    elif i/cp < 0.5:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "Half4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)
                    else:
                        ScheduleEOS (Calendar,"ContinueService", SimRNG.Expon(MeanST, 2), "AlmostWin4")
                        DepartingCustomer = Queue4.Remove()
                        Wait4.Record(SimClasses.Clock - DepartingCustomer.CreateTime)

for reps in range (0, 1, 1):
    SimFunctions.SimFunctionsInit(Calendar, TheQueues, TheCTStats,TheDTStats, TheResource)
    SimFunctions.Schedule(Calendar, "Arrival", SimRNG.Expon(MeanTBA, 1))
    SimFunctions.Schedule(Calendar,"EndSimulation",Runlength)
    
    NextEvent=Calendar.Remove()
    SimClasses.Clock = NextEvent.EventTime
    if NextEvent.EventType == "Arrival":
        Arrival()
    elif NextEvent.EventType == "ContinueService":
        ContinueService()
    elif NextEvent.EventType == "EndOfService":
        EndOfService()
    
    while NextEvent.EventType != "EndSimulation":
        NextEvent = Calendar.Remove()
        SimClasses.Clock = NextEvent.EventTime
        if NextEvent.EventType == "Arrival":
            Arrival()
        elif NextEvent.EventType == "ContinueService":
            ContinueService()
        elif NextEvent.EventType == "EndOfService":
            EndOfService()
            
    AllWait1Mean.append(Wait1.Mean())
    AllQueue1Mean.append(Queue1.Mean())
    AllWait2Mean.append(Wait2.Mean())
    AllQueue2Mean.append(Queue2.Mean())
    AllWait4Mean.append(Wait4.Mean())
    AllQueue4Mean.append(Queue4.Mean())
    AllServerMean.append(Server.Mean())
    AllServerMax.append(Server.MaxServer())
    print (reps+1, Wait1.Mean(), Queue1.Mean(),Wait2.Mean(), Queue2.Mean(),Wait4.Mean(), Queue4.Mean(), Server.Mean(), Server.MaxServer())

plt.plot(ServerNumber)
plt.show()
#active the following part to get the Excel output.

output = {"AllWait1mean": AllWait1Mean, "AllQueue1Mean": AllQueue1Mean, "AllWait2mean": AllWait2Mean, "AllQueue2Mean": AllQueue2Mean, "AllWait4mean": AllWait4Mean, "AllQueue4Mean": AllQueue4Mean, "AllServerMean": AllServerMean, "AllServerMax": AllServerMax}

output = pandas.DataFrame(output)
output.to_csv("PUBGSimple test.csv",sep=",")


AllWait1Mean = pandas.DataFrame(AllWait1Mean)
AllQueue1Mean = pandas.DataFrame(AllQueue1Mean)
AllWait2Mean = pandas.DataFrame(AllWait2Mean)
AllQueue2Mean = pandas.DataFrame(AllQueue2Mean)
AllWait4Mean = pandas.DataFrame(AllWait4Mean)
AllQueue4Mean = pandas.DataFrame(AllQueue4Mean)
AllServerMean = pandas.DataFrame(AllServerMean)
AllServerMax = pandas.DataFrame(AllServerMax)

print (AllWait1Mean.mean()[0])
print (AllWait1Mean.std())
print (AllQueue1Mean.mean())
print (AllQueue1Mean.std())
print (AllWait2Mean.mean()[0])
print (AllWait2Mean.std())
print (AllQueue2Mean.mean())
print (AllQueue2Mean.std())
print (AllWait4Mean.mean()[0])
print (AllWait4Mean.std())
print (AllQueue4Mean.mean())
print (AllQueue4Mean.std())
print (AllServerMean.mean())
print (AllServerMean.std())
print (AllServerMax.mean())
print (AllServerMax.std())

    
