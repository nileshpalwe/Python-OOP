# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 09:33:40 2021

@author: niles
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

class Job:
    def __init__(self,job_id,company,job_role,start_salary,high_salary):
        self.job_id = job_id
        self.company = company
        self.job_role = job_role
        self.start_salary = start_salary
        self.high_salary = high_salary
        
class Jobsportal:
    def __init__(self,portal_name,job_list):
        self.portal_name = portal_name
        self.job_list = job_list
        
    def get_bestjobbyrole(self,j_role):
        a=[]
        out =[]
        z = 0
        for i in self.job_list:
            if i.job_role.lower() ==j_role.lower():
                a.append(i)
        if len(a) != 0:
            for i in a:
                if(z<i.start_salary):
                    z = i.start_salary
                    for i in a:
                        if i.start_salary == z:
                            out.append(i)
                return out
                
    def jobswithsalary(self,salary):
        out_dic={}
        for i in self.job_list:
            if salary > i.start_salary and salary <= i.high_salary:
                out_dic [i.job_id] = i.company
                
        return out_dic
        

if __name__=="__main__":
    c=int(input("Number of entries: "))
    job_list=[]
    for i in range(c):
        job_id=int(input("Job ID : "))
        company=input("Company :" )
        job_role=input("Job Role : ")
        start_salary=int(input("Start Salary : "))
        high_salary=int(input("High Salary : "))
        job_list.append(Job(job_id,company,job_role,start_salary,high_salary))
    jp=Jobsportal("abc",job_list)
    job_r=input("Job role you are looking for : ")
    sal=int(input("Expected Salary : "))
    bj=jp.get_bestjobbyrole(job_r)
    if len(bj)==0:
        print("Job Not Found for the given role")
    else:
        for i in bj:
            print("\n Based on roles : ",i.job_id,i.company,i.high_salary)
    js=jp.jobswithsalary(sal)
    if len(js)==0:
        print("\n No matching jobs for the given salary")
    else:
        for x,y in js.items():
            print(x,y)
        
        
        
    