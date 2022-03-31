from django.shortcuts import redirect, render
i=0
qnos=[1,2,3,4,5,6,7,8,9,10]
ques=[
    'The entity integrity rule states that:',
    'A transitive dependency is which of the following?',
    'The part of machine level instruction, which tells the central processor what has to be done, is',
    'What is the term used for describing the judgmental or commonsense part of problem solving?',
    'An AI technique that allows computers to understand associations and relationships between objects and events is called:',
    'What difference does the 5th generation computer have from other generation computers?',
    'Which of the following TCP/IP protocol is used for transferring electronic mail messages from one machine to another?',
    'The part of machine level instruction, which tells the central processor what has to be done, is',
    'The section of the CPU that selects, interprets and sees to the execution of program instructions',
    'The DBMS acts as an interface between what two components of an enterprise-class database system?'

]
answer=[
    'no primary key attribute may be null.',
    'A functional dependency between two or more nonkey attributes.',
    'Operation code',
    'Heuristic',
    'pattern matching',
    'Technological advancement',
    'SMTP',
    'Operation code',
    'Control unit',
    'Database application and the database'
]
options=[
    ['no primary key attribute may be null.','no primary key can be composite.','no primary key may be unique.','no primary key may be equal to a value in a foreign key.'],
    ['A functional dependency between two or more key attributes.','A functional dependency between two or more nonkey attributes.','A relation that is in first normal form.','A relation that is in second normal form.'],
    ['Operation code','Address','Locator','Flip-Flop'],
    ['Heuristic','Critical','Value based','Analytical'],
    ['heuristic processing','cognitive science','relative symbolism','pattern matching'],
    ['Technological advancement','Scientific code','Object Oriented Programming','All of the above'],
    ['FTP','SNMP','SMTP','RPC'],
    ['Operation code','Address','Locator','Flip-Flop'],
    ['Memory','Register unit','Control unit','ALU'],
    ['Database application and the database','Data and the database','The user and the database application','Database application and SQL']
]
useranswer=[]

def Take_Test(request):
   global i,useranswer
   i=0
   useranswer=[]
   return render(request,'Quiz/show-question.html',{'ques':ques[i],'option1':options[i][0],'option2':options[i][1],
    'option3':options[i][2],'option4':options[i][3],'qno':i+1,'totalques':10})
 
def ShowQues(request):
    global i,useranswer
    
    useranswer.append(request.GET.get('choice'))

    if i==9:
        return redirect('quiz-details')
    i+=1
    return render(request,'Quiz/show-question.html',{'ques':ques[i],'option1':options[i][0],'option2':options[i][1],
    'option3':options[i][2],'option4':options[i][3],'qno':i+1,'totalques':10})


def Show_details(request):
    return render(request,'Quiz/details.html',{'zip_data':zip(qnos,ques,useranswer,answer)})