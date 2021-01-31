from .Tokenizer import Tokenizer

import numpy as np

import logging
logger = logging.getLogger(__name__)

AALETTER = [
    'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I',
    'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
AANUM = len(AALETTER)
AAINDEX = dict()
for i in range(len(AALETTER)):
    AAINDEX[AALETTER[i]] = i + 1


class DeepGoPlusTokenizer(Tokenizer):

    def tokenize(self, sequences):

        ids, data = DeepGoPlusTokenizer.get_data(sequences)
        onehot = DeepGoPlusTokenizer.to_onehot(data)
        
        return onehot

    @staticmethod
    def to_onehot(seq, start=0, maxlen=2000):
        onehot = np.zeros((maxlen, 21), dtype=np.int32)
        l = min(maxlen, len(seq))
        for i in range(start, start + l):
            onehot[i, AAINDEX.get(seq[i - start], 0)] = 1
        onehot[0:start, 0] = 1
        onehot[start + l:, 0] = 1
        return onehot

    @staticmethod
    def get_data(sequences, maxlen=2000):
        pred_seqs = []
        ids = []
        for i, seq in enumerate(sequences):
            if len(seq) > maxlen:
                st = 0
                while st < len(seq):
                    pred_seqs.append(seq[st: st + maxlen])
                    ids.append(i)
                    st += maxlen - 128
            else:
                pred_seqs.append(seq)
                ids.append(i)
        n = len(pred_seqs)
        data = np.zeros((n, maxlen, 21), dtype=np.float32)

        for i in range(n):
            seq = pred_seqs[i]
            data[i, :, :] = DeepGoPlusTokenizer.to_onehot(seq, maxlen=maxlen)
        return ids, data