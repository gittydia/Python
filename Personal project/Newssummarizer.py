import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def summarize():

    if not nltk.data.find('tokenizers/punkt'):
        nltk.download('punkt')

    url = ulabel.get("1.0", "end").strip()

    article = Article(url)
    try:
        article.download()
    except Exception as e:
        print(f"An error occurred while downloading the article: {e}")

    article.download()
    article.parse()

    article.nlp()

    title.config(state="normal")
    author.config(state="normal")
    publication.config(state="normal")
    summary.config(state="normal")
    sentiment.config(state="normal")

    title.delete("1.0", "end")
    title.insert("1.0", article.title)


    author.delete("1.0", "end")
    author.insert("1.0",article.authors) # type: ignore

    publication.delete("1.0", "end")
    publication.insert("1.0", article.publish_date) # type: ignore

    summary.delete("1.0", "end")
    summary.insert("1.0", article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete("1.0", "end")
    sentiment.insert("1.0", f'Polarity: {analysis.polarity}, Sentiment: {"Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"}') # type: ignore
    

    title.config(state="disabled")
    author.config(state="disabled")
    publication.config(state="disabled")
    summary.config(state="disabled")
    sentiment.config(state="disabled")

    

    
# Create a GUI window
root = tk.Tk()
root.title("Summarizer")
root.geometry("1260x1000")

# Create a Title label
title_label = tk.Label(root, text="Title", font=("Helvetica", 15))
title_label.pack()

title = tk.Text(root, height=1, width=140)
title.config(state="disabled", bg = 'lightgrey')
title.pack()

#author

author_label = tk.Label(root, text="Author", font=("Helvetica", 15))
author_label.pack()

author = tk.Text(root, height=1, width=140)
author.config(state="disabled", bg = 'lightgrey')
author.pack()


#publication date
publication_label = tk.Label(root, text="Publication date", font=("Helvetica", 15))
publication_label.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state="disabled", bg = 'lightgrey')
publication.pack()


#summary
summary_label = tk.Label(root, text="Summary", font=("Helvetica", 15))
summary_label.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state="disabled", bg = 'lightgrey')
summary.pack()

sentiment_label = tk.Label(root, text="Sentiment Analysis", font=("Helvetica", 15))
sentiment_label.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state="disabled", bg = 'lightgrey')
sentiment.pack()


Url_label = tk.Label(root, text="URL", font=("Helvetica", 15))
Url_label.pack()

ulabel = tk.Text(root, height=1, width=140)
ulabel.pack()

btn = tk.Button(root, text="Summarize", font=("Helvetica", 15), command=summarize, )
btn.pack()



root.mainloop()

