import pandas as pd
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
import datetime
from dateutil import parser, relativedelta
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

def collect_data():
	pass

def sanitize_data():
	pass

prefix = "/home/esthenos/prog/hacker_earth/synehack/"
data_collect = pd.read_csv(prefix+"correct_data/"+"customerdetails.csv")
#print data_collect.head()
credit_card_info = pd.read_csv(prefix+"correct_data/"+"creditcardinfo.csv")
#print credit_card_info.head()
customer_info = pd.read_csv(prefix+"correct_data/"+"customer.csv")
#print customer_info.head()
customer_info.drop("DATEOFBIRTH", axis=1, inplace=True)
customer_account = pd.read_csv(prefix+"correct_data/"+"customer_account.csv")
customer_account.columns = ['ID', 'ACCOUNTID']
#print customer_account
customer_info = pd.merge(customer_info, customer_account, on='ID')
#print customer_info.head()

customer_salary = pd.read_csv(prefix+"correct_data/"+"customersalary.csv")
customer_salary.columns = ['ID', 'SALARY']
#print customer_salary.head()
#print customer_salary.info()
customer_info = pd.merge(customer_info, customer_salary, on='ID')
#print customer_info.head()
#print customer_info.info()
#print customer_info.describe()
split_ratio = 0.20
train_data = customer_info[:int(len(customer_info)*(1-split_ratio))]
test_data = customer_info[int(len(customer_info)*(1-split_ratio)):]
print train_data
print test_data
card_transactions = pd.read_csv(prefix+"correct_data/"+"cardtransactions.csv")
card_transactions.columns = ['id',  'ID',  'amount',   'balance',  'transactionstatus',
  'transactiontype', 'whentime', 'merchantfirstname']
print card_transactions.info()
print card_transactions.head()
pd.merge(customer_info, card_transactions, on='ID')
print customer_info.info()
print customer_info.head()

