import nltk


def chatbot(user_input):
  """
  Returns a response to the user's input.

  Args:
    user_input: The user's input.

  Returns:
    A response to the user's input.
  """

  # Tokenize the user's input.
  tokens = nltk.word_tokenize(user_input)

  # Remove stop words from the tokens.
  stop_words = nltk.corpus.stopwords.words('english')
  tokens = [token for token in tokens if token not in stop_words]

  # Match the tokens against a list of patterns.
  patterns = [
    ('hello', 'Hi there!'),
    ('how are you?', 'I am doing well, thank you for asking!'),
    ('what is your name?', 'My name is Bard.'),
  ]

  for pattern, response in patterns:
    if pattern in tokens:
      return response

  # If no pattern matches, return a default response.
  return 'I am not sure what you mean.'

def main():
  """
  Starts the chatbot.
  """

  while True:
    user_input = input('> ')
    response = chatbot(user_input)
    print(response)

if __name__ == '__main__':
  main()
