import pandas as pd
import re
import numpy as np

regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
csv_df = pd.read_csv('worst_answers_backup.csv')

email_in_answers = []

for row in csv_df['body']:
	if not pd.isnull(row):
		# print(row)
		# print(re.search(regex, row))
		result = 1 if re.search(regex, row) else 0
	else:
		result = 0

	email_in_answers.append(result)

csv_df['email_in_answer'] = email_in_answers
csv_df.to_csv('worst_answers_backup.csv')