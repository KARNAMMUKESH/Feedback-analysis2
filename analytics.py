import csv
import pandas as pd
import numpy as np

def write_to_csv_departments(time,program,programscore,teaching,teachingscore,enjoy,enjoyscore,presentation,presentationscore,
                 job,jobscore,clarity,clarityscore,recommend,recommendscore,questions,questionscore,goal,goalscore,choice,choicescore,aware,awarescore,part,partscore):

    with open('dataset/database.csv', 'r') as f:
        reader = csv.reader(f)
        for header in reader:
            break
    with open('dataset/database.csv', "a", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        dict = {'Timestamp': time, 'q1': program,'q1s': programscore, 'q2': teaching, 'q2s' : teachingscore,
                'q3': enjoy, 'q3s' : enjoyscore, 'q4': presentation, 'q4s' : presentationscore,
                'q5': job, 'q5s' : jobscore, 'q6': clarity, 'q6s': clarityscore,
                'q7': recommend, 'q7s' : recommendscore,'q8': questions, 'q8s' : questionscore, 'q9': goal, 'q9s' : goalscore,
                'q10': choice, 'q10s' : choicescore, 'q11': aware, 'q11s' : awarescore,
                'q12': part, 'q12s' : partscore,}
        writer.writerow(dict)

def get_counts():
    path = 'dataset/database.csv'
    df = pd.read_csv(path)
    index = df.index
    no_of_students = len(index)
    total_feedbacks = len(index)*12

    df1 = df.groupby('programscore').count()[['program']]
    program_negative_count = df1['program'][-1]
    program_neutral_count = df1['program'][0]
    program_positive_count = df1['program'][1]


    df1 = df.groupby('teachingscore').count()[['teaching']]
    teaching_negative_count = df1['teaching'][-1]
    teaching_neutral_count = df1['teaching'][0]
    teaching_positive_count = df1['teaching'][1]

    df1 = df.groupby('enjoyscore').count()[['enjoy']]
    enjoy_negative_count = df1['enjoy'][-1]
    enjoy_neutral_count = df1['enjoy'][0]
    enjoy_positive_count = df1['enjoy'][1]

    df1 = df.groupby('presentationscore').count()[['presentation']]
    presentation_negative_count = df1['presentation'][-1]
    presentation_neutral_count = df1['presentation'][0]
    presentation_positive_count = df1['presentation'][1]

    df1 = df.groupby('jobscore').count()[['job']]
    job_negative_count = df1['job'][-1]
    job_neutral_count = df1['job'][0]
    job_positive_count = df1['job'][1]

    df1 = df.groupby('clarityscore').count()[['clarity']]
    clarity_negative_count = df1['clarity'][-1]
    clarity_neutral_count = df1['clarity'][0]
    clarity_positive_count = df1['clarity'][1]

    df1 = df.groupby('recommendscore').count()[['recommend']]
    recommend_negative_count = df1['recommend'][-1]
    recommend_neutral_count = df1['recommend'][0]
    recommend_positive_count = df1['recommend'][1]

    df1 = df.groupby('questionsscore').count()[['question']]
    question_negative_count = df1['question'][-1]
    question_neutral_count = df1['question'][0]
    question_positive_count = df1['question'][1]

    df1 = df.groupby('goalscore').count()[['goal']]
    goal_negative_count = df1['goal'][-1]
    goal_neutral_count = df1['goal'][0]
    goal_positive_count = df1['goal'][1]

    df1 = df.groupby('choicescore').count()[['choice']]
    choice_negative_count = df1['choice'][-1]
    choice_neutral_count = df1['choice'][0]
    choice_positive_count = df1['choice'][1]

    df1 = df.groupby('awarescore').count()[['aware']]
    aware_negative_count = df1['aware'][-1]
    aware_neutral_count = df1['aware'][0]
    aware_positive_count = df1['aware'][1]

    df1 = df.groupby('partscore').count()[['part']]
    part_negative_count = df1['part'][-1]
    part_neutral_count = df1['part'][0]
    part_positive_count = df1['part'][1]


    total_positive_feedbacks = program_positive_count + teaching_positive_count + presentation_positive_count+ job_positive_count + clarity_positive_count + recommend_positive_count + question_positive_count + goal_positive_count + choice_positive_count + aware_positive_count + part_positive_count + enjoy_positive_count
    total_neutral_feedbacks = program_neutral_count + teaching_neutral_count + presentation_neutral_count + job_neutral_count + clarity_neutral_count + recommend_neutral_count + question_neutral_count + goal_neutral_count + choice_neutral_count + aware_neutral_count + part_neutral_count + enjoy_neutral_count
    total_negative_feedbacks = program_negative_count + teaching_negative_count + presentation_negative_count +job_negative_count + clarity_negative_count+ recommend_negative_count + question_negative_count + goal_negative_count + choice_negative_count + aware_negative_count + part_negative_count + enjoy_negative_count

    li = [program_positive_count + teaching_positive_count + presentation_positive_count+ job_positive_count + clarity_positive_count + recommend_positive_count + question_positive_count + goal_positive_count + choice_positive_count + aware_positive_count + part_positive_count,
    program_neutral_count + teaching_neutral_count + presentation_neutral_count + job_neutral_count + clarity_neutral_count + recommend_neutral_count + question_neutral_count + goal_neutral_count + choice_neutral_count + aware_neutral_count + part_neutral_count
    ,program_negative_count + teaching_negative_count + presentation_negative_count +job_negative_count + clarity_negative_count+ recommend_negative_count + question_negative_count + goal_negative_count + choice_negative_count + aware_negative_count + part_negative_count + enjoy_positive_count + enjoy_neutral_count+ enjoy_negative_count]
    return no_of_students,\
           int(round(total_positive_feedbacks / total_feedbacks * 100)),\
           int(round(total_negative_feedbacks / total_feedbacks * 100)),\
           int(round(total_neutral_feedbacks / total_feedbacks * 100)),\
            li

def get_tables():
    df= pd.read_csv('dataset/database.csv')
    df = df.tail(5)
    return [df.to_html(classes='data')]

def get_titles():
    df = pd.read_csv('dataset/database.csv')
    return df.columns.values