import nltk

data = [(['Linux', 'is', 'the', 'best', 'OS'], ['OS','IR','IR','IR','IR']),
(['Ubuntu', 'is', 'my', 'favourite', 'OS'], ['OS','IR','IR','IR','IR']),
(['The', 'best', 'OS', 'is', 'Windows'], ['IR', 'IR', 'IR', 'IR', 'OS'])]
corpus = []
for (doc, tags) in data:
    doc_tag = []
    for word, tag in zip(doc,tags):
        doc_tag.append((word, tag))
    corpus.append(doc_tag)
# print(corpus)


def doc2features(doc, i):
    word = doc[i]
    
    # Features from current word
    features={
        'word.word': word,
    }
    # Features from previous word
    if i > 0:
        prevword = doc[i-1]
        features['word.prevword'] = prevword
    else:
        features['BOS'] = True # Special "Beginning of Sequence" tag
        
    # Features from next word
    if i < len(doc)-1:
        nextword = doc[i+1]
        features['word.nextword'] = nextword
    else:
        features['EOS'] = True # Special "End of Sequence" tag
    # print(features)
    return features
 
def extract_features(doc):
    return [doc2features([token for (token, tag) in doc], i) for i in range(len(doc))]
 
X = [extract_features(doc) for doc in corpus]
print(X)

def get_labels(doc):
    return [tag for (token,tag) in doc]
y = [get_labels(doc) for doc in corpus]
print(y)

# Train our model
import sklearn_crfsuite
crf = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    c1=0.1,
    c2=0.1,
    max_iterations=20,
    all_possible_transitions=False,
)
crf.fit(X, y)

# # Test our model on new data
test = [['CentOS', 'is', 'my', 'favourite', 'OS']]
X_test = [doc2features(test[0], i) for i in range (len(test[0]))]
print(X_test)
print(crf.predict_single(X_test))