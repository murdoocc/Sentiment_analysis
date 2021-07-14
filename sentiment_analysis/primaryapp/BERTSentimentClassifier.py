from torch import nn, optim
from transformers import BertModel
from transformers.models.bert.modeling_bert import BertModel,BertForMaskedLM
# TOKENIZACIÓN
PRE_TRAINED_MODEL_NAME = 'bert-base-cased'

# EL MODELO!
class BERTSentimentClassifier(nn.Module):
    def __init__(self, n_classes):
        super(BERTSentimentClassifier, self).__init__()
        self.bert = BertModel.from_pretrained(PRE_TRAINED_MODEL_NAME)
        self.drop = nn.Dropout(p=0.05)
        self.linear = nn.Linear(self.bert.config.hidden_size, n_classes)

    def forward(self, input_ids, attention_mask):
        _, cls_output = self.bert(
            input_ids = input_ids,
            attention_mask = attention_mask
        )
        drop_output = self.drop(cls_output)
        output = self.linear(drop_output)
        
        return output