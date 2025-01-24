import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score



data = pd.read_csv("data/Student Depression Dataset.csv")

# standardizing text
data.columns = data.columns.str.lower().str.replace(' ', '_')
data = data.rename(columns={'have_you_ever_had_suicidal_thoughts_?': 'suicidal_thoughts', 
                           'sleep_duration': 'sleep_duration_hours'})

str_columns = list(data.dtypes[data.dtypes == 'object'].index)

# changing text inside into lower and no space
for cat in str_columns:
    data[cat] = data[cat].str.lower()

# Drop missing value
data = data.dropna()


clean_data = data[['gender', 'age', 'academic_pressure', 'cgpa', 
                   'study_satisfaction', 'sleep_duration_hours', 'dietary_habits',  
                   'suicidal_thoughts', 'work/study_hours', 'financial_stress',
                   'family_history_of_mental_illness', 'depression']]


clean_data = clean_data[clean_data['sleep_duration_hours'] != 'others']
clean_data = clean_data[clean_data['dietary_habits'] != 'others']

# Simplify the value in sleep_duration_hours
clean_data.sleep_duration_hours = clean_data.sleep_duration_hours.map({'less than 5 hours': '<5',
                                                                       '5-6 hours': '5-6', 
                                                                       '7-8 hours': '7-8',
                                                                       'more than 8 hours': '>8'})



final_data = clean_data.drop('gender', axis=1)


df_full_train, df_test = train_test_split(final_data, test_size=0.2, random_state=12)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=12)


y_train = df_train.depression.values
y_val = df_val.depression.values
y_test = df_test.depression.values

del(df_train['depression'])
del(df_val['depression'])
del(df_test['depression'])


df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)


train_dict = df_train.to_dict(orient='records')
val_dict = df_val.to_dict(orient='records')
test_dict = df_test.to_dict(orient='records')


dv = DictVectorizer(sparse=False)
X_train = dv.fit_transform(train_dict)
X_val = dv.transform(val_dict)
X_test = dv.transform(test_dict)


lr = LogisticRegression(C=0.1, max_iter=100).fit(X_train, y_train)
y_pred = lr.predict(X_val)
print(f'Training accuracy {round(lr.score(X_train, y_train), 3)}')
print(classification_report(y_val, y_pred))



y_full_train = df_full_train.depression.values
del(df_full_train['depression'])
df_full_train = df_full_train.reset_index(drop=True)
full_train_dict = df_full_train.to_dict(orient='records')
X_full_train = dv.transform(full_train_dict)


lr = LogisticRegression(C=0.01, max_iter=300).fit(X_full_train, y_full_train)
y_pred = lr.predict(X_test)

print(f'Training accuracy {round(lr.score(X_full_train, y_full_train), 3)}')
print(f'AUC {round(roc_auc_score(y_test, y_pred), 3)}')
print(classification_report(y_test, y_pred))


# # Export the dv and model
# with open('../model/dv n model.bin', 'wb') as f_out:
#     pickle.dump((dv, lr), f_out)




