def main():
    book_path="books/frankenstein.txt"
    file_contents=read_file(book_path)
    wordCount = count_words(file_contents)
    print(f"This book has {wordCount} words!~")
    letter_count=count_each_letter(file_contents)
    letter_count=sort_letter_count(letter_count)
    for i in range(0,len(letter_count)):
        print(f"{letter_count[i]["letter"]} was used {letter_count[i]["count"]} time(s)!!!")
        

def count_words(str):
    words=str.split()
    return len(words)

def read_file(path):
    with open(path) as f:
        return f.read()

def count_each_letter(str):
    str=str.lower()
    letter_count={}
    for c in str:
        if not c.isalpha():
            continue
        try:
            letter_count[c]+=1
        except Exception as e:
            letter_count[c]=1
    return letter_count

def sort_on(dict):
    return dict["count"]

def sort_letter_count(letter_counts):
    letters_list=[]
    for l in letter_counts:
        letters_list.append({"letter":l, "count":letter_counts[l]})
    letters_list.sort(reverse=True,key=sort_on)
    return letters_list

def count_each_word(str):
    wordCount={}
    words = str.split()
    for word in words:
        if (wordCount[word]==None):
            wordCount[word]=1
        else:
            wordCount[word]+=1
    return wordCount

main()
