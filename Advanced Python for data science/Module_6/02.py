'''
Regular Expressions
Use re for text processing in NLP tasks.
'''
import re

text = "Contact: john.doe@example.com, jane.doe@example.com"
emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
print(emails)
'''
Breaking down the pattern:

[\w\.-]+: Matches the username part (before @)

\w: Word characters (letters, digits, underscore)
\.: Literal dot (escaped because . is a special regex character)
-: Hyphen character
+: One or more of the preceding characters


@: Literal @ symbol
[\w\.-]+: Matches the domain part (after @)

Same character class as username part



'''
# More robust pattern:
# More comprehensive email regex
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)