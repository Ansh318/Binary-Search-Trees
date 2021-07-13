#Name: aragarwal@wisc.edu
#Hours: 16

import os, json, csv
from zipfile import ZipFile, ZIP_DEFLATED
from io import TextIOWrapper
import pandas as pd
import tree

class ZippedCSVReader:
    
    def __init__(self,file_name):
        self.file_name = file_name
        self.paths = list()
        with ZipFile(self.file_name) as zf:
            for file in zf.namelist():
                self.paths.append(file) 
                          
    def __str__(self):
            return self.paths   
    
    def __repr__(self):
        return f"ZippedCSVReader({self.file_name})"
    
    def load_json(self,json_file = None):
    
        if json_file == None:
            raise ArgumentError("1 argument needed")
        else:
            with ZipFile(self.file_name) as zf:
                with zf.open(json_file,'r') as f:
                    return json.load(f)
        
            
    def rows(self, file = None):
        self.dict_list = list()
        if file == None:
            with ZipFile(self.file_name) as zf:
                paths = zf.namelist()
                paths.sort()
                for file in paths:
                    with zf.open(file, 'r') as infile:
                        reader = list(csv.reader(TextIOWrapper(infile, 'utf-8')))
                        header = reader[0]
                        csv_data = reader[1:]
                        for i in csv_data:
                            self.json_dict = dict()
                            for index in range(len(i)):
                                self.json_dict[header[index]] = i[index]
                            self.dict_list.append(self.json_dict)
                return self.dict_list
                            
        else:
            if file in self.paths:
                with ZipFile(self.file_name) as zf:
                    with zf.open(file, 'r') as infile:
                            reader = list(csv.reader(TextIOWrapper(infile, 'utf-8')))
                            header = reader[0]
                            csv_data = reader[1:]
                            for i in csv_data:
                                self.json_dict = dict()
                                for index in range(len(i)):
                                    self.json_dict[header[index]] = i[index]
                                self.dict_list.append(self.json_dict)
                            return self.dict_list
            else:
                raise Exception("File not in directory")
                    
class Loan:
    def __init__(self, amount, purpose, race, income, decision):
        self.amount = amount
        self.purpose = purpose
        self.race = race
        self.income = income
        self.decision = decision

    def __repr__(self):
        return f"Loan({self.amount}, {repr(self.purpose)}, {repr(self.race)}, {self.income}, {repr(self.decision)})"


    def __getitem__(self, lookup):
        param_ls = ["amount", "purpose", "race", "income", "decision"]  
        
        if type(lookup) == str:
            lookup = lookup.strip().lower()
            
            
        if lookup in param_ls:
            if lookup == "amount":
                return self.amount
            if lookup == "purpose":
                return self.purpose
            if lookup ==  "race":
                return self.race
            if lookup == "income":
                return self.income
            if lookup == "decision":
                return self.decision
            
        else:
            
            if lookup == self.amount:
                return 1
            elif lookup == self.purpose.strip().lower():
                return 1
            elif lookup ==  self.race.strip().lower():
                return 1
            elif lookup == self.income:
                return 1
            elif lookup == self.decision.strip().lower():
                return 1
            else:
                return 0
            
            
class Bank: 
    def __init__(self, name,reader):
        self.name = name
        self.reader = reader
        self.data_ls = list()
        self.data_ls2 = list()
    
    def loans(self):
            if self.name == None:
                for app_ in self.reader.rows(None):
                    if app_['action_taken'] == 1:
                        if app_['loan_amount_000s'] == "":
                            app_['loan_amount_000s'] = 0
                        if app_['applicant_income_000s'] == "":
                            app_['applicant_income_000s'] = 0
                        data = Loan(int(app_['loan_amount_000s']),app_['loan_purpose_name'],app_['applicant_race_name_1'],int(app_['applicant_income_000s']),'approve')
                        self.data_ls.append(data)
                    else:
                        if app_['loan_amount_000s'] == "":
                            app_['loan_amount_000s'] = 0
                        if app_['applicant_income_000s'] == "":
                            app_['applicant_income_000s'] = 0
                        data = Loan(int(app_['loan_amount_000s']),app_['loan_purpose_name'],app_['applicant_race_name_1'],int(app_['applicant_income_000s']),'deny')
                        self.data_ls.append(data)
                return self.data_ls


            else:
                for app_ in self.reader.rows(None):
                    if app_['agency_abbr'] == self.name:
                        self.data_ls.append(app_)
                for data in self.data_ls:
                    if int(data['action_taken']) == 1:
                        data = Loan(data['loan_amount_000s'],data['loan_purpose_name'],data['applicant_race_name_1'],data['applicant_income_000s'],'approve')
                        self.data_ls2.append(data)
                    else:
                        data = Loan(data['loan_amount_000s'],data['loan_purpose_name'],data['applicant_race_name_1'],data['applicant_income_000s'],'deny')
                        self.data_ls2.append(data)
                return self.data_ls2
               
        
def get_bank_names(reader):
    bank_names = list()
    for name in reader.rows(None):
        bank_name = name['agency_abbr']
        if bank_name not in bank_names:
            bank_names.append(bank_name)
        else:
            continue
    bank_names.sort()
    return bank_names

class SimplePredictor:
    
    def __init__(self):
        
        self.approved = 0
        self.denied = 0 
        
    def predict(self,loan):
    
        if loan['Refinancing'] == 1:
            self.approved += 1
            return True
        else:
            self.denied += 1
            return False
            
    def get_approved(self):
        return self.approved
        
    def get_denied(self):
        return self.denied

class DTree(SimplePredictor):
    
    def __init__(self, nodes):
        SimplePredictor.__init__(self)
        self.approved = 0
        self.denied = 0
        self.root = nodes
        
    def dump(self, node=None, indent=0):
        if node == None:
            node = self.root
            
        if node["field"] == "class":
            line = "class=" + str(node["threshold"])   
        else:
            line = node["field"] + " <= " + str(node["threshold"])
            
        print("  "*indent + line)
        
        if node['left']:
            self.dump(node['left'], indent + 1)
            
        if node['right']:
            self.dump(node['right'], indent + 1)
        
                   
    def __node_count_helper(self, node):       
        count =  1
        if (node is None):
            return 0
        else:
            count += self.__node_count_helper(node["left"])
            count += self.__node_count_helper(node["right"])
            return count

           
    def node_count(self):
        node = self.root
        return self.__node_count_helper(node)     

    def predict(self,loan,node=None):
        if node == None:
            node = self.root

        if node['field'] == 'class' and node['threshold'] == 1:
                self.approved += 1
                return True
        elif node['field'] == 'class' and node['threshold'] != 1:
                self.denied += 1
                return False

        else:
            
            if loan[node['field']] >= node['threshold']:
                return self.predict(loan, node['right'])
            else:
                return self.predict(loan, node['left'])


        def get_approved(self):
            return self.approved

        def get_denied(self):
            return self.denied    
    
    

def bias_test(bank, predictor, race_override):
    count = 0
    for loan in bank.loans():
        predicted_loan = predictor.predict(loan)
        override_loan = Loan(loan['amount'],loan['purpose'],race_override,loan['income'],loan['decision'])
        override_loan_pred = predictor.predict(override_loan)
        if predicted_loan != override_loan_pred:
            count += 1
    bias_percent = count/len(bank.loans())
    return bias_percent