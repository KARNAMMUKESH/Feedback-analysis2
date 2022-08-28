import csv
import pandas as pd
import numpy as np

def write_to_csv_departments3(time,q1,q1s,q2,q2s,q3,q3s,q4,q4s,q5,q5s,q6,q6s,q7,q7s,q8,q8s):
                

    with open('dataset/database3.csv', 'r') as f:
        reader = csv.reader(f)
        for header in reader:
            break
    with open('dataset/database3.csv', "a", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        dict = {'Timestamp': time, 'q1': q1,'q1s': q1s, 'q2': q2, 'q2s' : q2s,
                'q3': q3, 'q3s' : q3s, 'q4': q4, 'q4s' : q4s,
                'q5': q5, 'q5s' : q5s, 'q6': q6, 'q6s': q6s,
                'q7': q7, 'q7s' : q7s,'q8': q8, 'q8s' : q8s}
        writer.writerow(dict)

def get_counts3():
    path = 'dataset/database.csv'
    df = pd.read_csv(path)
    index = df.index
    no_of_students = len(index)
    total_feedbacks = len(index)*8

    df1 = df.groupby('q1s').count()[['q1']]
    program_negative_count = df1['q1'][-1]
    program_neutral_count = df1['q1'][0]
    program_positive_count = df1['q1'][1]


    df1 = df.groupby('q2s').count()[['q2']]
    teaching_negative_count = df1['q2'][-1]
    teaching_neutral_count = df1['q2'][0]
    teaching_positive_count = df1['q2'][1]

    df1 = df.groupby('q3s').count()[['q3']]
    enjoy_negative_count = df1['q3'][-1]
    enjoy_neutral_count = df1['q3'][0]
    enjoy_positive_count = df1['q3'][1]

    df1 = df.groupby('q4s').count()[['q4']]
    presentation_negative_count = df1['q4'][-1]
    presentation_neutral_count = df1['q4'][0]
    presentation_positive_count = df1['q4'][1]

    df1 = df.groupby('q5s').count()[['q5']]
    job_negative_count = df1['q5'][-1]
    job_neutral_count = df1['q5'][0]
    job_positive_count = df1['q5'][1]

    df1 = df.groupby('q6s').count()[['q6']]
    clarity_negative_count = df1['q6'][-1]
    clarity_neutral_count = df1['q6'][0]
    clarity_positive_count = df1['q6'][1]

    df1 = df.groupby('q7s').count()[['q7']]
    recommend_negative_count = df1['q7'][-1]
    recommend_neutral_count = df1['q7'][0]
    recommend_positive_count = df1['q7'][1]

    df1 = df.groupby('q8s').count()[['q8']]
    question_negative_count = df1['q8'][-1]
    question_neutral_count = df1['q8'][0]
    question_positive_count = df1['q8'][1]

   
    total_positive_feedbacks = program_positive_count + teaching_positive_count + presentation_positive_count+ job_positive_count + clarity_positive_count + recommend_positive_count + question_positive_count + enjoy_positive_count
    total_neutral_feedbacks = program_neutral_count + teaching_neutral_count + presentation_neutral_count + job_neutral_count + clarity_neutral_count + recommend_neutral_count + question_neutral_count + enjoy_neutral_count
    total_negative_feedbacks = program_negative_count + teaching_negative_count + presentation_negative_count +job_negative_count + clarity_negative_count+ recommend_negative_count + question_negative_count + enjoy_negative_count

    li = [program_positive_count , teaching_positive_count , presentation_positive_count, job_positive_count , clarity_positive_count , recommend_positive_count , question_positive_count ,
    program_neutral_count , teaching_neutral_count , presentation_neutral_count , job_neutral_count , clarity_neutral_count , recommend_neutral_count , question_neutral_count 
    ,program_negative_count , teaching_negative_count , presentation_negative_count ,job_negative_count , clarity_negative_count, recommend_negative_count , question_negative_count , enjoy_positive_count , enjoy_neutral_count, enjoy_negative_count]
    return no_of_students,\
           int(round(total_positive_feedbacks / total_feedbacks * 100)),\
           int(round(total_negative_feedbacks / total_feedbacks * 100)),\
           int(round(total_neutral_feedbacks / total_feedbacks * 100)),\
            li

def get_tables3():
    df= pd.read_csv('dataset/database2.csv')
    df = df.tail(5)
    return [df.to_html(classes='data')]

def get_titles3():
    df = pd.read_csv('dataset/database2.csv')
    return df.columns.values