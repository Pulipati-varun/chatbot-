from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Chatbot',read_only=False,
                logic_adapters=[
                    {
                        
                        'import_path':'chatterbot.logic.BestMatch',
                        'default_response':'Sorry, I dont know what means',
                        'maximum_similarity_threshold':0.90
                    
                    
                    }])

list_to_train = [

        "hi",
        "hi, there", 
        "What's your name?",
        "I'm just a chatbot",
        "Tell about Anurag university, AU, what is anurag university, Anurag, Anurag university",
        "Anurag University is established as a Private State University through Ordinance No- 1/2020 dated: 20/05/2020 as per the Telangana State Private Universities Act No 11 of 2018 Anurag University run by Gayatri educational and cultural trust began offering undergraduate programs since 1998 from Lalitha Degree & PG college and CVSR college of Engineering,It was officially named as Anurag University in 2020 The Anurag Group of Institutions (AGI) is one of the first few integrated campuses of South India established in 2002 offering programs in Engineering & Technology Pharmacy and Business Management Anurag University is a private university located in Hyderabad Telangana Our primary focus is to provide a high-quality graduate postgraduate and doctoral education in engineering pharmacy and management fields"

]


list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

def index(request):
    return render(request,'bot/index.html')

def specific(request):
    list1 = [1,2,3,4]
    return HttpResponse("list1")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)
    