import logging
from django.shortcuts import render, redirect
from .models import Todo, Category
logger = logging.getLogger(__name__)
# Create your views here.
def index(request): #the index view
    todos = Todo.objects.all() #querying all todos with the object manager
    categories = Category.objects.all() #getting all categories with object manager
    not_started = Todo.objects.filter(status="Not Started")
    in_progress = Todo.objects.filter(status="In Progress")
    completed = Todo.objects.filter(status="Completed")
    
    for todo in todos:
        todo.dueness_calculator()
        todo.save()
        logger.info(todo)
        logger.info(todo.dueness)
    
    if (request.method == "POST"): #checking if the request method is a POST
        if ("todoAdd" in request.POST): #checking if there is a request to add a todo
            title = request.POST["description"] #title
            todo_date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + todo_date + " " + category #content
            current_todo = Todo(title=title, content=content, due_date=todo_date, category=Category.objects.get(name=category))
            current_todo.save() #saving the todo
            return redirect("/") #reloading the page

        if ("todoUpdate" in request.POST):
            todo_update = request.POST["todoUpdate"] #making a post request for todoupdate
            logger.info("If post request works")
            logger.info(todo_update)
            not_started = Todo.objects.get(id=int(todo_update)) #we are querying the Todo class from models.py to get our status
            logger.info("to check if i am getting the status of Not Started")
            logger.info(not_started)
            if not_started.status == "Not Started":
                logger.info(not_started.status) #just checking if our todo is still on "not started"/checking if our code is working
                updated_status = Todo.objects.filter(status="In Progress")
                logger.info(updated_status) 
                not_started.status = updated_status
                not_started.save()
            elif not_started.status == "In Progress":
                final_status = Todo.objects.filter(status="Completed")
                not_started.status = final_status
                not_started.save()    
            return redirect("/") 

        if ("todoUpdate" in request.POST):
            todo_update2 = request.POST["todoUpdate"]
            completed = Todo.objects.get(id=int(todo_update2)) 
            logger.info("to check if i am getting the status of Completed")
            logger.info(completed)
            if completed.status == "Completed":
                logger.info(completed.status) 
                updated_status = Todo.objects.filter(status="In Progress") 
                completed.status = updated_status
                completed.save()
            elif completed.status == "In Progress":
                final_status2 = Todo.objects.filter(status="Not Started")
                completed.status = final_status2
                completed.save()    
            return redirect("/") 

        
        if ("todoDelete" in request.POST): #checking if there is a request to delete a todo
            todo_id = request.POST["todoDelete"]
            current_todo = Todo.objects.get(id=int(todo_id)) # getting todo id
            current_todo.delete() # deleting todo
            return redirect("/") # reloading the page

    return render(request, "index.html", {"todos": todos, "categories":categories, "Not_Started": not_started, "In_Progress": in_progress, "Completed": completed})