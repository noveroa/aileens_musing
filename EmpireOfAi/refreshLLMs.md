# aileens_musing

## Cambridge, MA

![N|Solid](https://ca.slack-edge.com/T0495HV8H-U01AM69UW3E-ae635702c574-72)

###### 
> remember that i did machine learning and nlp... yeah, a while back now huh?  let's see if i can recall anything... 

######

* Large Language models (LLMs)
    * models that consume large data sets and use statistical probabilities to produce human like text responses.
    * [See more on history, transformers and the ilk](./generativeAi.md)
    * at LEAST two rival groups
        * Symbolic AI 
            * relies on explicit rules and symbols to represent knowledge and solve problems (ie ibm's ELIZA)
        * Connectionist AI
            * inspired by the brain, uses artificial neural networks to learn from data and recognize patterns (currently winning the race, ChatGPT - openai)
    | Type | Method | Use |  
    | ---- | ----- | ----- | 
    | Autoregressice LLMs | predict net word in a sentence based on previous words | text generation | 
    | Autoendcoding LLMs | focus on encoding and reconstructing text | Sentiment analysis, information retrieval | 
    | Hybrid LLMs | merge Autoregressive/Autoencoding | "versitile" |
    * Uses
        * Text generation - human-like text   : essays, stories, code snippets
        * Summarization - concise summary of a longer text : summarize news, research papers
        * Translation - translate text between languages
        * Question Answering - Given prompt, provide answer : trivia, explaining concepts
        * Sentiment Analyiss - Determine emotional tone of a text : analyze cutomer reviews
        * Text Completion - predict / complete unfinished sentencess, paragraphs : autocomplete
        * Conversational AI - chatbots/virtual assistants : customer support 
        * Code generation - generate / debug code 

    * Building LLMs
        * Data Curation 
            * more data (parameters/input) the better the training and model - **Large, Diverse, Clean**
            * unfortunately that also means more compute (power/energy/$$$) needed
            * currently (aug2025), Llama  / GPT-4 have 15 and 6.5 trillion token respectiveley, 
                * not the greatest sets ... common crawl, social media, ... no bueno
            * you need HIGH QUALITY data - trash in == trash out
            * **BE RESPONSIBLE**
                [text](https://miro.medium.com/v2/resize%3Afit%3A1400/format%3Awebp/0%2AYhCzJH4gzV0gzPSp)
            * **Clean** and structure your data
            * where to collect?
                * Publicly available datasets (common crawl (no!)), wikipedia
                * APIs - reddit, twitter, 
                * web scraping (ie via python's beuatiful soup)
        * Data Preprocessing 
            * Tranforming the data into a format the model can learn from
            * ---> [See more on history, transformers and the ilk](./generativeAi.md)
            * Tokenization
                * break text into smaller pieces (words / characters) allowing model to process and understand each part
                * character level, word level, or subword level
            * Embedding 
                * converts words, phrases, tokens into numerical vectors capturing semantic meaning of the texts - aid in model understnaind meaning and relationship between words
            * Attention
                * focusing on most important parts of a sentence, key sentiments
            * Transformer blocks
                * **CORE** 
                * self-attention layers
                    * process relationships between words in the input text
                * feedforward neural networks 
                    * perform additional computatoins to refine understanding of the text
                * multiple transformer blocks are stacked to improve model performance on complex tasks
            * Positional Encoding
                * transformers don't proces sequences in order - positional encoding helps model understand the order of words ina structure
            * Output Layers
                * Generated predictions based on input
        * LLM Traingin Loop
            * Data input and preparatoin
                * Data ingestion - collecti / load data sets
                * Data Cleaning - remove noise, handle missing data, redact sensitive information
                * Normalization - standadrdize the text, handle catagorical data, ensure data consistency
                * Chunking - split large texts into manageable chunks while preserving context
                * Tokenization - convert text chunks into tokens for model processing
                * Data Loadin - lod and shuffle data for optimized training - parallel loading as necessary
            * Loss Calculation
                * Calculate Loss - compare predictions to true labels using a loss functio (diff == 'loss' / 'error' value)
                * Performance Indicator - higher loss indicates poor accuracy; lower loss suggests better alignment with actual targets
            * Hyperparameter Tuning
                * Learning Rate 
                    * controls weight update size during training 
                    * too high can lead to instability
                    * too low slows down training
                * Batch Size
                    * number of samples per iteration 
                    * larger -> stabilizes training but requires more energy
                    * smaller -> introduces variability but less resource intensive
                    [text](https://miro.medium.com/v2/resize%3Afit%3A1400/format%3Awebp/0%2AXm8VY0KI_5Tds5bP)
            * Parallelization and Resource Management
                * data Parallelization
                    * split datasets across GPUs for faster processing
                * Model Paralleization 
                    * divide models across GPUs to handle large models
                * Gradient Checkpointing
                    * reduce memory usuage during training by selectively storing intermediate results
            * Iterations and Epochs
                * Iteratoins - process batches of data - updating weights each time
                * Epochs - complete passes through datasets, refining the model parameters with each pass
                * Monitoring - track metrics (loss/accuracy) with each epoch to guide adjeustments and avoiding overfitting
        * Evaluting LLMs
            * MMLU ( Massive Multitask Language Understanding)
                * Assess natural languge understanding and reasoning across subjects
            * GPQA ( General Purpose Question Answering)
                * Tests model's ability to handle diverse, complex questions across subjects
            * MATH 
                * Measures model's mathematical reasoning via multistep problems
            * Humaneval 
                * Evaulates coding proficiency - model's abilty to generate accurate, functoinal code
            *  [text](https://miro.medium.com/v2/resize%3Afit%3A1400/format%3Awebp/0%2AkfnZu52kFLGAu4FV)