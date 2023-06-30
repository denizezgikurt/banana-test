# This file runs during container build time to get model weights built into the container

# In this example: A Huggingface BERT model
from transformers import pipeline

def download_model():
    # do a dry run of loading the huggingface model, which will download weights
    pipeline('image-to-text', model='nlpconnect/vit-gpt2-image-captioning')

if __name__ == "__main__":
    download_model()