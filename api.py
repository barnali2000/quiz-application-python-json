# Subject
import requests
import random

def menu():
  subject_code = input("""Select the subject
  1. Computers
  2. Mathematics
  3. General Knowledge
  """)

  if subject_code == "1":
    fetch_data(18)
  elif subject_code == "2":
    fetch_data(19)
  else:
    fetch_data(9)

def fetch_data(subject):
  # fetch data from the server
  url = "https://opentdb.com/api.php?amount=10&category={}&type=multiple".format(subject)
  data = requests.get(url)
  new_data = data.json()
  extract_questions(new_data)

def extract_questions(data):
  questions = []
  correct_options = []
  all_options = []

  for i in data['results']:
    questions.append(i['question'])
    correct_options.append(i['correct_answer'])
    single_option = []
    single_option.append(i['correct_answer'])
    single_option.extend(i['incorrect_answers'])
    random.shuffle(single_option)
    all_options.append(single_option)


  start_test(questions,correct_options,all_options)

def start_test(questions,correct_options,all_options):
  user_response = []
  # display all the questions with all options
  for i in range(len(questions)):
    print(i+1,". ",questions[i])
    for j in all_options[i]:
      print(j)
    # user input
    answer = input("Enter your answer")
    user_response.append(answer)
    print("-"*100)

  print_result(user_response,correct_options)

def print_result(user_response,correct_options):
  # result print - correct +3 incorrect -1
  # no. of correct answers incorrect answers
  result_dict = {'correct':0, 'incorrect':0}

  for i in range(len(user_response)):
    if user_response[i] == correct_options[i]:
      result_dict['correct'] = result_dict['correct'] + 1
    else:
      result_dict['incorrect'] = result_dict['incorrect'] + 1

  print(result_dict)
  print("No of correct answers",result_dict['correct'])
  print("No of incorrect answers",result_dict['incorrect'])
  score = 3 * result_dict['correct'] - result_dict['incorrect']
  print('Your final score is',score)




menu()