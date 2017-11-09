import pandas as pd
import numpy as np
import re
import profanity

custom_bad_words = []

with open("bad_words.txt") as f:
    custom_bad_words = f.readlines()

custom_bad_words = [x.strip() for x in custom_bad_words] 
print(custom_bad_words)

profanity.load_words(custom_bad_words)

regex_email = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
regex_phone = 
regex_url = r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)"

# get rid of those fucking carriage returns
def replace(x):
	if type(x) == str or type(x) == unicode:
		x = x.replace('\r', '')
	else:
		x = x[0].replace('\r', '')
	return x

csv_df = pd.read_csv('worst_answers_yuhang.csv')

csv_df["body"] = csv_df["body"].map(lambda x: x.replace('"', ''))
csv_df["body"] = csv_df["body"].map(lambda x: replace(x))

csv_df["disclaimer"] = csv_df["body"].map(lambda x: x.replace('"', ''))
csv_df["disclaimer"] = csv_df["body"].map(lambda x: replace(x))

email_in_answers = []
address_in_answers = []
url_in_answers = []
phone_number_in_answers = []
profanity_in_answers = []

for row in csv_df['body']:
	# check if email in body
	if not pd.isnull(row):
		result = 1 if re.search(regex_email, row) else 0
	else:
		result = 0
	email_in_answers.append(result)

	# check if phone number in body
	if not pd.isnull(row):
		result = 1 if re.search(regex_phone, row) else 0
	else:
		result = 0
	phone_number_in_answers.append(result)

	# check if url in body
	if not pd.isnull(row):
		result = 1 if re.search(regex_url, row) else 0
	else:
		result = 0
	url_in_answers.append(result)

	# # check if address in body
	# if not pd.isnull(row):
	# 	result = 1 if re.search(regex_email, row) else 0
	# else:
	# 	result = 0
	# email_in_answers.append(result)

	# check if body has profanity
	# if not pd.isnull(row):
	# 	result = 1 if profanity.contains_profanity(row) else 0
	# else:
	# 	result = 0
	# profanity_in_answers.append(result)

csv_df['email_in_answer'] = email_in_answers
csv_df['phone_number_in_answer'] = phone_number_in_answers
# csv_df['profanity_in_answer'] = profanity_in_answers
csv_df['url_in_answer'] = url_in_answers

csv_df.to_csv('worst_answers.csv')

