import pandas as pd
import numpy as np
import re
import Algorithmia

# setup algorithmia for profanity
client = Algorithmia.client('simePH15/LlJOCVpgEbzCo89mHV1')
algo = client.algo('nlp/ProfanityDetection/1.0.0')

# regexes to find attributes
regex_email = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
regex_phone = r"""(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)"""
regex_url = r"""(http://www.|https://www.|http://|https://|www.)+[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?"""

# to get rid of those fucking carriage returns
def replace(x):
	if type(x) == str or type(x) == unicode:
		x = x.replace('\r', '')
	else:
		x = x[0].replace('\r', '')
	return x

# READ IN THE CSV
csv_df = pd.read_csv('best_answers_yuhang.csv')

# remove the carriage returns
csv_df["body"] = csv_df["body"].map(lambda x: x.replace('"', ''))
csv_df["body"] = csv_df["body"].map(lambda x: replace(x))
csv_df["disclaimer"] = csv_df["body"].map(lambda x: x.replace('"', ''))
csv_df["disclaimer"] = csv_df["body"].map(lambda x: replace(x))

# lists to convert into pandas columns
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
	# so far this doesn't work well, need to multithread requests and too many false positives
	# try:
	# 	if not pd.isnull(row):
	# 		algo_result = algo.pipe(row)
	# 		print algo_result
	# 		result = 1 if algo_result else 0
	# 	else:
	# 		result = 0
	# 	profanity_in_answers.append(result)
	# except:
	# 	print("Exception in Algorithmia code: " + row)
	# 	profanity_in_answers.append(0)

csv_df['email_in_answer'] = email_in_answers
csv_df['phone_number_in_answer'] = phone_number_in_answers
# csv_df['profanity_in_answer'] = profanity_in_answers
csv_df['url_in_answer'] = url_in_answers

csv_df.to_csv('best_answers.csv')

