#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import streamlit as st
import numpy as np
import spacy



# ### Natural Language Processing | SpaCy
st.title('Simple SpaCy')
# messa funzione e decorazione
#@st.cache_data()
#def carica_lingua(lingua):
#    nlp = spacy.load(lingua)  # vs lg
#    # spacy_stopwords = spacy.lang.it.stop_words.STOP_WORDS # indagare qui
#    return nlp

lingua = 'it_core_news_md' 

#nlp = carica_lingua(lingua)


nlp = spacy.load(lingua)
spacy_stopwords = spacy.lang.it.stop_words.STOP_WORDS  # indagare qui


testo = st.text_input('Inserisci il testo')
if not testo:
    st.stop()

st.write('Il testo è:', testo)


doc = nlp(testo)

for i in range(len(doc)):
    token = doc[i]
    st.write(token.lemma_)
    st.write(token.is_stop)

