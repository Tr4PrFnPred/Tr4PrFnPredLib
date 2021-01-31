from .PostProcess import PostProcess


class DeepGoPostProcess(PostProcess):

    def __init__(self, terms):
        self.terms = terms

    def postprocess(self, predictions, **kwargs):
        ids = kwargs["ids"]
        prot_ids = kwargs["prot_ids"]
        deep_preds = {}

        for i, j in enumerate(ids):
            prot_id = prot_ids[j]
            if prot_id not in deep_preds:
                deep_preds[prot_id] = {}
            for l in range(len(self.terms)):
                if predictions[i, l] >= 0.01:  # Filter out very low scores
                    if self.terms[l] not in deep_preds[prot_id]:
                        deep_preds[prot_id][self.terms[l]] = predictions[i, l]
                    else:
                        deep_preds[prot_id][self.terms[l]] = max(
                            deep_preds[prot_id][self.terms[l]], predictions[i, l])

        return deep_preds
