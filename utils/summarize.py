from .api import *
from bs4 import BeautifulSoup
from transformers import BartTokenizer, BartForConditionalGeneration





tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')



def chunks(text):
    for i in range(0,len(text),7000):
        txt = yield text[i:i + 7000]
    


    
    
    
def summarize(text):
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", truncation=True)
    summary_ids = model.generate(inputs, min_length=40, max_length = 150 ,length_penalty=2.0, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)






def summary(parsed_text):
    
    final_summary = ''
    for index,text in enumerate(chunks(parsed_text)):
        final_summary += summarize(text)
    
    final_summary=final_summary.replace('\'', "").split('. ')
    
    val = [point.strip() + '.' for point in final_summary if point]
    
    text = ["\n".join("*" + sub for sub in val)]
    
    return text[0]


