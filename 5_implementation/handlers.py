
class ModelHandler:
    def __init__(self, model_path: str = "./sarcasm_model.pkl"):
        import joblib

        self.model = joblib.load(model_path)

    def predict(self, headline: str):
        return self.model.predict([headline.lower()])[0]

class DatasetHandler:

    def __init__(self, dataset_path: str = "./test_data.json"): # only play with the test data the model hasn't seen before
        import json
        from random import randint

        dataset_fp = open(dataset_path, "r")
        self.dataset = json.load(dataset_fp)
        self.randint = randint

    def get_random_entry(self) -> tuple[int, str]:
        # get a random entry
        entry = self.dataset[self.randint(0, len(self.dataset)-1)]
        
        # return the entry as a tuple of (is_sarcastic, headline)
        return (entry['is_sarcastic'], entry['headline'])