import numpy as np

class process:
    def __init__(self,inp_uni_array):
        self.inp_uni_array = inp_uni_array
        self.vector_len = len(self.inp_uni_array)

    def one_hot_encoding(self,inp_batch):
        self.inp_batch = inp_batch
        self.processed_array = []
        for tweet_sentence in self.inp_batch:
            sentence = []
            for word in tweet_sentence:
                idx = self.inp_uni_array.index(word)
                z = np.zeros(self.vector_len)
                z[idx] = 1
                sentence.append(z)
            self.processed_array.append(sentence)
        #avoid printing self.processed_array when inp_batch is large
        print(self.processed_array)
        return self.processed_array


    def discrete_value(self,inp_batch):
        self.inp_batch = inp_batch
        self.processed_array = []
        for tweet_sentence in self.inp_batch:
            sentence = []
            for word in tweet_sentence:
                idx = self.inp_uni_array.index(word)
                sentence.append(idx)
            self.processed_array.append(sentence)
        #avoid printing self.processed_array when inp_batch is large
        print(self.processed_array)
        return self.processed_array


if __name__ == '__main__':
    unique_array = ['a','b','c','d']
    """
        take input batch by iterating the input dataset  
    """
    inp_batch = [['a','a'],['b','b','d'],['d','c']]
    """class initialization"""
    prs = process(unique_array)
    print("One_Hot_Encoding")
    one_hot_encoded = prs.one_hot_encoding(inp_batch)
    print("discrete value encoding")
    discrete_value = prs.discrete_value(inp_batch)
    """
        Feed either one_hot_encoded input batch or 
        Feed discrete_value to the neural network 
    """