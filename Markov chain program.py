from markov_chain import markovChainModel,predict
from scipy.sparse import load_npz,hstack
print("Loading data")
X_1_dev = load_npz("dev_questions.npz")
X_2_dev = load_npz("X_2_dev.npz")
Y_1_dev = load_npz("dev_articleTitles.npz")
Y_2_dev = load_npz("dev_answers.npz")
print("Data loaded; preprocessing to make compatible with Markov chains")
dataset_2 = hstack((X_2_dev,Y_2_dev)).toarray().tolist()
print("Preprocessing complete; training Markov models")
model_2 = markovChainModel(dataset_2,1)