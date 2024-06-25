import streamlit as st
from load_file import load_file
from levenshtein_distance import levenshtein_distance

st.title("Word correction distance")
f_word = st.text_input("Enter a word: ")
vocabs = load_file("../data/vocab.txt")

if st.button("Submit"):
    # Compute levenshtein distance
    levenshtein_distance_dict = dict()
    for word in vocabs:
        levenshtein_distance_dict[word] = levenshtein_distance(word, f_word)

    # sort
    sorted_distances = dict(sorted(levenshtein_distance_dict.items(), key=lambda x: x[1]))
    correct_word = list(sorted_distances.keys())[0]
    st.write(correct_word)

    col1, col2 = st.columns(2)
    col1.write("Vocabulary")
    col1.write(vocabs)

    col2.write("Distance")
    col2.write(sorted_distances)

