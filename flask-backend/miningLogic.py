from keybert import KeyBERT
from transformers import DistilBertTokenizer, DistilBertModel, pipeline


doc = """
I am Thirsty
      """
kw_model = KeyBERT()
keywords = kw_model.extract_keywords(doc)

extracted_words = kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 1), stop_words=None)

doc_arr = doc.replace('\n', '').split(' ')

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


for i in range(0,len(extracted_words)):
    for j in range(0,len(doc_arr)):
        if(extracted_words[i][0].lower() == doc_arr[j].lower()):
            doc_arr[j] = '[MASK]'

masked_statement = listToString(doc_arr)


# tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
# model = DistilBertModel.from_pretrained("distilbert-base-uncased")
text = "[MASK] me by any text you'd like."
# encoded_input = tokenizer(text, return_tensors='pt')
# output = model(**encoded_input).logits

unmasker = pipeline('fill-mask', model='distilbert-base-uncased')
result = unmasker(masked_statement)
print(result)

# todos: 
# limit to 3 mask 
# and limit to 3 mask value