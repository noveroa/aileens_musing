"""
Data Preprocessing

Raw data often contains noise, irrelevant information, and inconsistencies.
Preprocessing ensures that the data is clean and standardized, improving the model’s understanding and performance.

Common Preprocessing Tasks
    Removing Stop Words
        Stop words (e.g., “the,” “is”) don’t add much value to the model and can be removed.
        Tokenization
    Break text into smaller units like words or sentences.
    Lowercasing
        Convert all text to lowercase for uniformity.
    Handling Special Characters
        Remove symbols, numbers, or unwanted characters that don’t contribute to the task.

Libraries for Preprocessing
    nltk: Natural Language Toolkit for tokenization, stop word removal, etc.
    spaCy: Advanced NLP processing.
    pandas: Data manipulation for handling text in large datasets.
Key Notes
    Efficiency: Preprocessing makes the data simpler for the model to process.
    Flexibility: You can customize the steps based on your specific task.
    Tools: NLTK is great for beginners; spaCy is better for more advanced tasks.
    Press enter or click to view image in full size

"""
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required NLTK data
# # he 'punkt' tokenizer is a pre-trained model used for sentence tokenization, which means it helps in splitting a given text into individual sentences.
nltk.download('punkt_tab') 
# # 
nltk.download('stopwords')

# Sample text
text = "My name is Abdul Rauf jatoi"

# Step 1: Tokenize text into words
tokens = word_tokenize(text)

# Step 2: Convert to lowercase and remove non-alphanumeric tokens
tokens = [word.lower() for word in tokens if word.isalnum()]

# Step 3: Remove stop words
filtered_tokens = [word for word in tokens if word not in stopwords.words('english')]

# Display the preprocessed tokens
print(filtered_tokens)
