from collections import Counter
import re
import glob

class Token:
    #Test files to store the results
    file1 = "task1.txt"
    file2 = "task2.txt"
    
    #Function to tokenize the given dataset
    def text_transform():
        filenames = glob.glob('dataset/cranfieldDocs/cranfield*')
        n=[]
        outputlist = []
        for f in filenames:
            string = open(f, 'r').read()
            clear = re.compile('<.*?>')
            cleartext = re.sub(clear, '', string)
            matches = re.findall('\w+', cleartext)
            outputlist.append(matches)
            newlist = [item for sublist in outputlist for item in sublist]

            x = len(matches)
            n.append(x)
            unique_count = len(set(newlist))
        top_fifty = Counter(newlist).most_common(50)
        collection_count = sum(n)
        print("Task 1")
        print("a) Total number of words in the collection:",collection_count)
        print("b) Vocabulary size:",unique_count)
        print("c) Top 50 words and their frequencies:",top_fifty, "\n\n")
        return top_fifty, collection_count, unique_count, newlist
    
    #Function to remove the stopwords fron the tokenized dataset
    def remove_stopwords(newlist):
        stop_words = open('dataset/common_words.txt', 'r').read()
        stop_list = stop_words.splitlines()
        remove_stopword = []
        #use set to iterate over
        #check with list if loop

        for word in newlist:
            if word not in stop_list: 
                remove_stopword.append(word)
            else:
                pass
        new_collection_count = len(remove_stopword)
        new_unique_count = len(set(remove_stopword))
        new_top_fifty = Counter(remove_stopword).most_common(50)
        print("Task 2")
        print("a) Total number of words in the collection:",new_collection_count)
        print("b) Vocabulary size:",new_unique_count)
        print("c) Top 50 words and their frequencies:",new_top_fifty)
        return new_top_fifty, new_collection_count, new_unique_count

    #Function to write the final answer to the text documents
    def write_file(filename, collection_count, unique_count, top_fifty):
        text_file = open(filename, "w")
        text_file.write("a) Total number of words in the collection: %s\n" % collection_count)
        text_file.write("b) Vocabulary size: %s\n" % unique_count)
        text_file.write("c) Top 50 words and their frequencies: %s\n\n "% top_fifty)
        text_file.close()
    
    top_fifty, collection_count, unique_count, newlist= text_transform()
    new_top_fifty, new_collection_count,new_unique_count = remove_stopwords(newlist)
    
    write_file(file1, collection_count, unique_count,top_fifty)
    
    write_file(file2,new_collection_count,new_unique_count, new_top_fifty)
    

def main():
    c= Token()

if __name__ == "__main__":
    main()