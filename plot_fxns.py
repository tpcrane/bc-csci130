import matplotlib.pyplot as plt

#word = 'brontosaurus and tyrannosaurus and aptosaurus'
def count_occur(word):
    d = dict()
    for char in word:
            d[char] = d.get(char,0) + 1  #the zero is what is returned if char is not in d
    return(d)        #counting


def plot_bar(d, title):
    plt.bar(list(d.keys()), d.values())
    plt.ylabel('Counts')
    plt.title(title) 
    plt.show()  #bar


#data = [4,5,8,3,6,5,6,7,6,9,1,4,5,6,7,6,5,6,6,7]

# We can set the number of bins with the *bins* keyword argument. 

def plot_hist(data):
    plt.hist(data,bins=7)
    
    plt.ylabel('Counts')
    plt.title('Frequency of letters') 

    plt.show()  #hist

