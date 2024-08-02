import tkinter as tk
from tkinter import scrolledtext
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import string

# Load the CSV file into a DataFrame
file_path = 'train.csv'
# Update with your file path
df = pd.read_csv(file_path)

# Preprocess the data for chatbot
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    tokens = [token for token in word_tokenize(text.lower()) if token not in string.punctuation]
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    return tokens

df['processed_question'] = df['Question'].apply(preprocess_text)
df['processed_answer'] = df['Answer'].apply(preprocess_text)

# Define function to calculate similarity
def calculate_similarity(tokens1, tokens2):
    return 1 - nltk.jaccard_distance(set(tokens1), set(tokens2))

# Define function to generate responses
def generate_response(user_input):
    user_input_tokens = preprocess_text(user_input)
    max_sim = -1
    best_response = ""
    for idx, row in df.iterrows():
        question_tokens = row['processed_question']
        sim = calculate_similarity(user_input_tokens, question_tokens)
        if sim > max_sim:
            max_sim = sim
            best_response = row['Answer']
    return best_response if max_sim > 0 else "I'm sorry, I couldn't understand that."

# Define function to summarize answer
def summarize_answer(answer):
    sentences = nltk.sent_tokenize(answer)
    summary_sentences = sentences[:2]  # Keep the first 2 sentences as summary
    summarized_text = ' '.join(summary_sentences)
    return summarized_text

# Tkinter app
def send_message(option=None):
    if option is not None:
        user_input = option
    else:
        user_input = entry.get()
    response = generate_response(user_input)
    summarized_response = summarize_answer(response)
    chat_history.insert(tk.END, f"You: {user_input}\nChatbot: {summarized_response}\n\n")
    chat_history.see(tk.END)
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Panda Interface")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

chat_history = scrolledtext.ScrolledText(frame, width=70, height=20, wrap=tk.WORD, font=("Arial", 12))
chat_history.pack()

options_frame = tk.Frame(frame)
options_frame.pack()

options = ["Heart Disease", "Common cold", "Fever"]  # Define your suggested input options
for option in options:
    button = tk.Button(options_frame, text=option, width=10, font=("Arial", 12), command=lambda option=option: send_message(option))
    button.pack(side=tk.LEFT, padx=5, pady=5)

entry = tk.Entry(frame, width=70, font=("Arial", 12))
entry.pack(pady=10)

send_button = tk.Button(frame, text="Send", width=10, font=("Arial", 12), command=send_message)
send_button.pack()

root.mainloop()
