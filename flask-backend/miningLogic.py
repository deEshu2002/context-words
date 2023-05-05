from pydoc import doc
from keybert import KeyBERT
from functools import reduce
import re
import string
from transformers import AutoModelForMaskedLM, AutoTokenizer
import torch

model_checkpoint = "distilbert-base-uncased"

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += (ele + " ")
    return str1

def transform_input_to_mask_words(input):
    kw_model = KeyBERT()
    keyword = kw_model.extract_keywords(input)
    extracted_words = kw_model.extract_keywords(input, keyphrase_ngram_range=(1, 1), stop_words=None)
    input_arr = input.replace('\n', '').split(' ')

    output_arr =[]
    for i in range(0,3):
        for j in range(0,len(input_arr)):
            if(extracted_words[i][0].lower() == input_arr[j].lower()):
                initial_word = input_arr[j]
                input_arr[j] = '[MASK]'
                output_arr.append(listToString(input_arr))
                input_arr[j] = initial_word
    return output_arr

def format_keywords(keywords_array):
    special_chars = string.punctuation
    output = {}
    for i in keywords_array:
        for j in i:
            bools = list(map(lambda char: char in special_chars, j ))
            if not any(bools):
                output[j] = j
    return output


def get_words(input):
    masked_sentences =  transform_input_to_mask_words(input)
    model = AutoModelForMaskedLM.from_pretrained(model_checkpoint)
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
    keyword_array_2D = []
    for sentence in masked_sentences:
        inputs = tokenizer(sentence, return_tensors='pt' )
        token_logits = model(**inputs).logits
        mask_token_index = torch.where(inputs["input_ids"] == tokenizer.mask_token_id)[1]
        mask_token_logits = token_logits[0, mask_token_index, :]
        top_3_tokens = torch.topk(mask_token_logits, 4, dim=1).indices[0].tolist()
        keyword_array = []
        for token in range(1,len(top_3_tokens)):
            keyword_array.append(tokenizer.decode(top_3_tokens[token]))
        keyword_array_2D.append(keyword_array)
    formatted_words = format_keywords(keyword_array_2D)
    return formatted_words


# print(get_words('Paris is the capital of France'))
