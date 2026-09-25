print("{:.2f}".format(17.489))#17.49
print("{}{}".format("hello","world"))#helloworld
print("{0}{0}{0}{1}{1}".format("happy","birthday"))#happyhappyhappybirthdaybirthday
print("{fast}{last}".format(fast="happy",last="birthday"))#happybirthday
sentence="\t\n\t\nhiii welcome\t\n\n"
print(sentence.strip())#hiii welcome
print(sentence.lstrip())
sentence1="happy birthday"
print(sentence1.capitalize())#Happy birthday
print(sentence1.title())#Happy Birthday
sentence2 = 'to be or not to be that is the question'
print(sentence2.count("to"))#2
print(sentence2.count("to",12))#1
print(sentence2.index('be'))#3
print(sentence2.rindex('be'))#16
print('that'in sentence2)#true
print('That'in sentence2)#false
value='1\t2\t3\t4\t'
print(value.replace('\t',','))#1,2,3,4,
print(value.replace('\t','-->'))#1-->2-->3-->4-->
text='python is a fun language'
print(text.split())#['python', 'is', 'a', 'fun', 'language']