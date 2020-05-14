import transformers

MAX_LEN = 512
BERT_PATH = r"D:/My Workspace/IMDB/input/bert_base_uncased"
MODEL_PATH = r"D:/My Workspace/IMDB/model/model.bin"
TOKENIZER = transformers.BertTokenizer.from_pretrained(BERT_PATH, do_lower_case=True)
