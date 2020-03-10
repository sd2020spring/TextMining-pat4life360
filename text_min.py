import bs4 as bs
import urllib.request
import operator

#Add URLs to the list
biglist=['https://worldsoccertalk.com/2013/10/02/transcript-of-sir-alex-fergusons-interview-on-the-charlie-rose-show/','https://www.dailymail.co.uk/sport/football/article-6517697/FULL-TRANSCRIPT-Ole-Gunnar-Solskjaers-quotes-Manchester-United-manager.html','https://www.mirror.co.uk/sport/football/news/full-transcript-freddie-ljungbergs-first-20989866','https://www.dailymail.co.uk/sport/football/article-7212929/FULL-TRANSCRIPT-Frank-Lampard-promises-blood-young-talent-interview-Chelsea-boss.html','https://www.dailymail.co.uk/sport/football/article-7711367/FULL-TRANSCRIPT-Jose-Mourinhos-press-conference-Tottenham-manager.html','https://www.express.co.uk/sport/football/1207137/Jose-Mourinho-first-interview-transcript-Tottenham-Mauricio-Pochettino','https://www.theguardian.com/football/2008/oct/03/newcastleunited.premierleague','https://www.football365.com/news/fascinating-rafa-benitez-interview-the-full-transcript','https://www.liverpoolfc.com/news/first-team/195447-jrgen-klopp-exclusive-first-lfc-interview']
#Define the list where all the text will be entered
all_words=[]

#Function to pull the text from the source code
def get_words():
   """Code to parse and get word from the html transcript
   """
   for url in biglist:
       soup=bs.BeautifulSoup(urllib.request.urlopen(url),'lxml')
       for script in soup(["script", "style"]):
           script.extract()
       for paragraph in soup.find_all('p'):
           all_words.append(paragraph.text)
   return all_words


interview_notes=get_words()

#
def listToString():
    """Split the list text into a string
    """
    str1 = " "
    return (str1.join(interview_notes))




interview_string=listToString()
#Make all the text lowercase
lower_interview_string=interview_string.lower()

#Make a dictionary of the word frequencies, by first splitting the string
counts = dict()
words = lower_interview_string.split()

for word in words:
	 if word in counts:
	      counts[word] += 1
	 else:
	      counts[word] = 1

sorted_count = sorted(counts.items(), key=operator.itemgetter(1),reverse=True)


print(sorted_count)


#Code for bar chart of word distribution, can be commented out or not
plt.bar(range(len(sorted_count)), [val[1] for val in sorted_count], align='center')
plt.xticks(range(len(sorted_count))), [val[0] for val in sorted_count]
plt.xticks(rotation=70)
plt.ylim((0, 300))
plt.title("Spread of word frequencies in interview form highest to smallest")
plt.show()
