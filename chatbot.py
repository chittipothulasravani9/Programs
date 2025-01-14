from nltk.chat.util import Chat,reflections
pairs=[
    [r'hi',['hie']],
    [r'hie',['hie there']],
    [r'how are you',['i am fine hoping you are good']],
    [r'what is your name',['Myname is chatbot']],
    [r'who is your boss',['my boss is sravani']],
    [r'who is invited you',['i am invited by sravani']],
    [r'are you mad',['nice joke']],
    [r'sorry',['machine can not have feeings its ok']],
    [r'what is python',['it is a programming language']],

]
chat=Chat(pairs,reflections)
chat.converse()
def quit1():
  print("hi iam chat bot ask me something")
  if __name__=="__main__":    quit1()
    
#>hi
#hie
#>how are you
#i am fine hoping you are good
#>what is your name
#Myname is chatbot
#>who is your boss
#my boss is sravani
#>who is your founder
#None
#>are you mad
#nice joke
#>sorry
#machine can not have feeings its ok
#>what is python
#it is a programming language