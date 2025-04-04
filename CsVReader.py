
import re




def main():
    file_word_name = "Sort_the_words_by_frequency.text"
    file_letter_name = "sort_alpha.text"
    # Read the text
    file_path = r"Codes/Book Summaries.txt"
    file_content = read_file_content(file_path)
    # clean text
    clean_new_text = clean_text(file_content)
    # count words
    count_word = count_words(clean_new_text)
    # count letters
    count_letter = count_letters(clean_new_text)
    # sorted words
    sorted_words = sort_word_by_frequency(count_word)
    # sorted letters
    sorted_letters = sort_letters_alphabetically(count_letter)
    # write data
    write_data(file_word_name, sorted_words)
    write_data(file_letter_name, sorted_letters)






def read_file_content(file_path):
    """Get the file
        Read the file and its content
        Paremeters:
        file_path: text file 
        return:
        return the text as string
    """
    with open(file_path, "r") as f:
        read_file = f.read()
        return read_file


def clean_text(file_content):
    """Clear the text from punctuations and make the text lower case
    parameters:
    file_content: a text file
    return: return the new file without punctuations and lower case
    """
    clear_punctuations = re.sub(r'[^\w\s]','',file_content.lower())
    return clear_punctuations

def count_words(file_content):
    """Loop on each word of the text then calculate how much time it repeated in text
    Parameters:
    file_content : the file who has the text
    return: returns the dictionary who counts the words
    """
    count_word = {}
    split_words = file_content.split()
    for word in split_words:
        count_word[word] = count_word.get(word, 0) +1
    return count_word

def count_letters(file_content):
    """Loop on each letter of the text then calculate how much time it repeated in text
    Parameters:
    file_content : the file who has the text
    return: returns the dictionary who counts the Letters
    """
    count_letter = {}
    file_content = file_content.replace(" ","").replace("\n","")
    for letter in file_content:
        if letter.isalpha():
            count_letter[letter] = count_letter.get(letter, 0) + 1
    return count_letter

def sort_word_by_frequency(count_word):
    """Get the count_word dictinary (dict) and sort it with the most repeated word
    paremters:
    count_word: dictonary
    return: return the sorted dictionary
    """
    sorted_words = dict(sorted(count_word.items(), key= lambda words: (words[1],words[0]),reverse=True))
    return sorted_words

def sort_letters_alphabetically(count_alpha_letters):
    """Sort alpha letters"""
    sorted_alpha = dict(sorted(count_alpha_letters.items()))
    return sorted_alpha


def write_data(file_name,content_dict):
    """Get the file name and write the content on it"""
    with open(file_name,"w",newline="") as word_file:
        for key , value in content_dict.items():
            word_file.write(f"{key}: {value}\n")

if __name__ == "__main__":
    main()