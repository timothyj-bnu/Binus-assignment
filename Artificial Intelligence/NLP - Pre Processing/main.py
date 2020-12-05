import nltk


def main():
    from nltk.tokenize import word_tokenize
    import re
    from nltk.probability import FreqDist
    from nltk.corpus import stopwords
    # source word: https://binusmaya.binus.ac.id/newStudent/#/class/info.COMP6639/017482/2010/LEC/13945
    text = '''This course provides students with the foundation of Artificial Intelligence, 
    understanding of representations and external constraints with the idea of improving students to think creatively. 
    By completing this course, students can explain many kinds of Artificial Intelligence algorithms, 
    and implement those algorithms to make an application. This course is prerequisite for Expert System, 
    Computer Vision and Artificial Neural Network course.'''
    # print(text)
    text_tokens = word_tokenize(text)
    # print(text_tokens)
    punctuation = re.compile(r'[-.?!,:;()|0-9]')
    post_punc_word = []
    for words in text_tokens:
        word = punctuation.sub("", words)
        if(len(word) > 0):
            post_punc_word.append(word)

    # print(post_punc_word)
    post_stop_word = []
    for word in post_punc_word:
        if word not in stopwords.words('english'):
            post_stop_word.append(word)

    post_lower_word = []
    for word in post_stop_word:
        post_lower_word.append(word.lower())


    final_array = lemmatization(post_lower_word)
    final_word = ''
    for word in final_array:
        final_word = final_word +' '+word
    visualization(final_word)


def lemmatization(array):
    from nltk.stem import wordnet
    from nltk.stem import WordNetLemmatizer

    lem = WordNetLemmatizer()
    post_lemmatization = []
    for w in array:
        post_lemmatization.append(lem.lemmatize(w))
    return posTag(post_lemmatization)


def posTag(array):
    tagged = nltk.pos_tag(array)
    return_arr = []
    for tag in tagged:
        if tag[1] == 'NN' or tag[1] == 'NNS' or tag[1] == 'NNP' or tag[1] == 'NNPS':
            return_arr.append(tag[0])
    return return_arr


def visualization(text):
    from PIL import Image
    import numpy as np
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    print(text)
    char_mask = np.array(Image.open('logo.png'))
    wordCloud = WordCloud().generate(text)

    plt.figure(figsize=(12,12))
    plt.imshow(wordCloud)

    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    main()

