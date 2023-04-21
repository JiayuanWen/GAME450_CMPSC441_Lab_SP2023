
from sentence_transformers import SentenceTransformer, util 

if __name__ == '__main__':
    sentence1 = "The song played during the 2008 Beijing Olympic opening ceremony that was titled \"You and Me\" was performed by Chinese singer Liu Huan and British singer Sarah Brightman. The song was composed by Chen Qigang with lyrics by Lin Xi and was sung in both English and Mandarin Chinese. The duet was accompanied by a large choir of children and a group of drummers, and it was intended to symbolize the unity and cooperation between China and the rest of the world during the Olympic Games."
    sentence2 = "The song \"You and Me\" that was played during the 2008 Beijing Olympic opening ceremony was performed by Chinese singer Liu Huan and British singer Sarah Brightman. The song was composed by Chinese musician Chen Qigang and lyricist Lin Xi. The performance was one of the highlights of the opening ceremony and symbolized the unity and cooperation between China and the rest of the world."

    sentences = [sentence1, sentence2]
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    embedding_1 = model.encode(sentences[0], convert_to_tensor=True)
    embedding_2 = model.encode(sentences[1], convert_to_tensor=True)

    result = util.pytorch_cos_sim(embedding_1, embedding_2)
    print(result)
    # Sentence transformer gave a similarity score of 0.9725, meaning the sentence is 97.25% similar to each other.
    # 