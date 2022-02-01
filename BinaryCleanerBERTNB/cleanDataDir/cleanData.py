import pandas as pd
import numpy as np
import csv 
import sys
import string
import nltk 
import re 
import time
import warnings

def main():
    proj_name = "audacity"
    filtered = "Unfiltered"
    smoteConfig = "SMOTE"
    inputFile = filtered + "/" + "UNCLEAN_" + smoteConfig + "/" + proj_name + "uncleanSMOTE.csv"
    print(inputFile)
    data_test1 = pd.read_csv(inputFile)
    #del data_test1["Named"]
    print(data_test1.head())
    data_test1 = clean_data(data_test1, proj_name)
    data_test1.to_csv("cleaned_" + proj_name + "_" + filtered + "_" + smoteConfig + ".csv", index=False)

def clean_data(data_test1, proj_name):
    
    if not sys.warnoptions:
        warnings.simplefilter("ignore")

    def cleanHtml(sentence):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, ' ', str(sentence))
        return cleantext

    def cleanPunc(sentence): #function to clean the word of any punctuation or special characters
        cleaned = re.sub(r'[?|!|\'|"|#]',r'',sentence)
        cleaned = re.sub(r'[\[|\]|<|>|@|.|,|~|)|(|\|/|`|\d|:|-|*|ø|%|+]',r' ',cleaned)
        cleaned = cleaned.strip()
        cleaned = cleaned.replace("\n"," ")
        cleaned = cleaned.replace("-"," ")
        cleaned = cleaned.replace(r'[(...)|.|,|-|<|>|)|~|(|\|/]', '')
        cleaned = re.sub(r'^x ', r'', cleaned)
        return cleaned

    def removeExtraSpaces(sentence):
        sentence = ' '.join(sentence.split())
        return sentence

    def keepAlpha(sentence):
        alpha_sent = ""
        for word in sentence.split():
            alpha_word = re.sub('[^a-z A-Z]+', ' ', word)
            alpha_sent += alpha_word
            alpha_sent += " "
        alpha_sent = alpha_sent.strip()
        return alpha_sent
    
    """def give_emoji_free_text(sentence):
        allchars = [str for str in sentence]
        emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
        clean_text = ' '.join([str for str in sentence.split() if not any(i in str for i in emoji_list)])

        return clean_text"""
    
    def remove_template(sentence):
        if proj_name == "guava":
            cleaned = sentence.replace("moe sync this code has been reviewed and submitted internally feel free to discuss on the pr and we can submit follow up changes as necessarycommits", "")
            cleaned = cleaned.replace("moe sync this code has been reviewed and submitted internally feel free to discuss onthe pr and we can submit follow up changes as necessarycommits", "")
            cleaned = cleaned.replace("this code has been reviewed and submitted internally feel free to discuss on the pr and we can submit follow up changes as necessarycommits", "")
            cleaned = cleaned.replace("this code has been reviewed and submitted internally feel free to discuss onthe pr and we can submit follow up changes as necessarycommits", "")
            cleaned = re.sub(r'^ ', r'', cleaned)
            return cleaned
        return sentence 

    data_test1['corpus'] = data_test1['corpus'].str.lower()
    data_test1['corpus'] = data_test1['corpus'].apply(cleanHtml)
    data_test1['corpus'] = data_test1['corpus'].apply(cleanPunc)
    #data_test1['corpus'] = data_test1['corpus'].apply(give_emoji_free_text)
    data_test1['corpus'] = data_test1['corpus'].apply(removeExtraSpaces)
    if proj_name == "guava":
        data_test1['corpus'] = data_test1['corpus'].apply(remove_template)
    #data_test1['corpus'] = data_test1['corpus'].apply(keepAlpha)
    
    return data_test1

if __name__ == '__main__':
    main()