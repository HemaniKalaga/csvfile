from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

import csv
def insert_bank(request):
    with open('C:\\Users\\ASUS\\OneDrive\\Desktop\\django projects\\Hemani\\Scripts\\csvfile\\app\\bank.csv','r') as FO:
        IOD=csv.reader(FO)
        for i in IOD:
            bn=i[0].strip()
            BO=Bank(bname=bn)
            BO.save()
    return HttpResponse('Bank data is inserted')

def insert_branch(request):
    with open('C:\\Users\\ASUS\\OneDrive\\Desktop\\django projects\\Hemani\\Scripts\\csvfile\\app\\branch1.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            bn=i[0]
            BO=Bank.objects.filter(bname=bn)
            
            if BO:
                ifs=i[1]
                br=i[2]
                ad=i[3]
                co=i[4]
                ci=i[5]
                di=i[6]
                s=i[7]

                BRO=Branch(bname=BO,ifsc=ifs,branch=br,address=ad,contact=co,city=ci,district=di,state=s)
                BRO.save()
    return HttpResponse('Branch data is inserted')


