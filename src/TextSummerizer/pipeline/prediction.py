from TextSummerizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline
from transformers import AutoModelForSeq2SeqLM
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

    
    def predict(self,text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        single_input_encoding = tokenizer(text, return_tensors='pt', max_length=512, truncation=True, padding=True)
        model_path = self.config.model_path
        model_facebook = AutoModelForSeq2SeqLM.from_pretrained(model_path).to(device)
        with torch.no_grad():
            
            generated_ids_single = model_facebook.generate(single_input_encoding['input_ids'], max_length=500, num_beams=4, length_penalty=2.0, early_stopping=True)
            generated_summary_single = tokenizer.decode(generated_ids_single[0], skip_special_tokens=True)
        
        # gen_kwargs = {"length_penalty":0.8,"num_beams":8,"max_length":128}
        # pipe = pipeline("summarization",model= self.config.model_path,tokenizer=tokenizer)
        print("Dialogue:")
        print(text)
        print('\n Model Summary')
        print(generated_summary_single)
        return generated_summary_single