# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 21:00:22 2023

@author: Shriprada
"""

import streamlit as st
import spacy
from textblob import TextBlob
import en_core_web_sm
#rom gensim.summarization import summarize

#from sumy.parsers.plaintext import PlaintextParser
#from sumy.nlp.tokenizers import Tokenizer
#from sumy.summarizer.lex_rank import LexRankSummarizer

#def sumy_summarizer(doc):
  #  parser = PlaintextParser.from_string(doc, Tokenizer("english"))
   # lex_summarizer = LexRankSummarizer()
   # summary = lex_summarizer(parser.document,3)
   # summary_list = [str(sentence) for sentence in summary]
   # result = ' '.join(summary_list)
   # return result

def text_analyzer(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    tokens = [token.text for token in doc]
    allData = [('"Tokens":{},\n"Lemma":{}'.format(token.text,token.lemma_)) for token in doc]
    return allData



def entity_analyzer(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    tokens = [token.text for token in doc]
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    allDatas = ['"Tokens":{},\n"Entities":{}'.format(tokens,entities)]
    return allDatas
    
 

    

def main():
    
    st.title("HOTEL REVIEW - SENTIMENT ANALYSIS")
    st.subheader("Sentiment Analysis on the review")
    review = st.text_area("Enter the Review", "Type Here")
    
    if st.checkbox("Show Tokens and Lemma"):
        #st.subheader("Tokenize Your Text")
        #review = st.text_area("Enter the Review", "Type Here")
        if st.button("Analyze"):
            nlp_result = text_analyzer(review)
            st.json(nlp_result)
    
            
    if st.checkbox("Show Named Entities"):
         #st.subheader("Extract Entities From You Text")
         #review = st.text_area("Enter the Review", "Type Here")
         if st.button("Extract"):
             nlp_results = entity_analyzer(review)
             st.json(nlp_results)
             
             
    if st.checkbox("Show Sentiment Analysis"):
        #st.subheader("Sentiment of Your Text")
        #review = st.text_area("Enter the Review", "Type Here")
        if st.button("Sentiment"):
            blob = TextBlob(review)      
            if blob.sentiment.polarity > 0 :
                st.write('Positive')
            elif blob.sentiment.polarity == 0 :
                st.write("Neutral")
            else:
                st.write("negative")
                
            result_sentiment = blob.sentiment
            st.success(result_sentiment)
            
            
   # if st.checkbox("Show Text Summarization"):
    #     st.subheader("Summarize Your Text")
     #    review = st.text_area("Enter the Review", "Type Here")
      #   summary_options = st.selectbox("Choose Your Summarizer"("gensim", "sumy"))
         #if st.button("Summarize"):
             #if summary_options == 'gensim':
                # st.text("Using Gensim...")
                 #summary_result = summarize(review)
      #   summary_options == 'sumy'
      #   st.text("Using Sumy...")
      #   summary_result = sumy_summarizer(review)
             #else:
                 #st.warning("Using Default Summarizer")
                 #st.text("Using Gensim...")
                 #summary_result = summarize(review)
      #   st.success(summary_result)
      

            
if __name__ == '__main__':
    main()
            
        










