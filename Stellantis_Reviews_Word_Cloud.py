import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

df = pd.read_excel("data/REVIEWS of FCA.xlsx", sheet_name="Reviews")
stop_words = pd.read_excel("data/REVIEWS of FCA.xlsx", sheet_name="Stop Words")

# Convert reviews to a single string
text = ' '.join(df['REVIEWS'].astype(str))

# Convert stop words DataFrame to set
custom_stopwords = set(stop_words['Stop Words'])
custom_stopwords.update(STOPWORDS)

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=custom_stopwords).generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
