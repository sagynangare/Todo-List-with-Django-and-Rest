from django.views import generic
from django.views.generic.edit import CreateView
from .models import TodoTask, User
from .forms import TodoTaskForm
from django.urls import reverse_lazy ,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import redirect

#Rest framework
from rest_framework.response import Response
from .serializers import TodoTaskSerializer, RegisterSerializer, UserLoginSerializer
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView


#This class will provide all Tasks that are not deleted

class Dashboard(generic.ListView):
    serializer_class = TodoTaskSerializer
    template_name = 'mytask/index.html'

    def get_queryset(self):
        qs = TodoTask.objects.filter(is_deleted=False)
        return qs

#This class will Update Tasks
class AddToDoList(CreateView):
    form_class = TodoTaskForm
    model = TodoTask
    success_url = reverse_lazy('dashboard')
    template_name = 'mytask/addtodonew.html'

    def form_valid(self, form):
        #print("valid")
        todo_date=self.request.POST.get('new-todo-date')
        self.model = form.save(commit=False)
        self.model.membership_reminder_date=todo_date
        self.model.save()
        return super(AddToDoList, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form)
        )
    
#This class will Update Tasks
class UpdateToDoList(generic.UpdateView):
    form_class = TodoTaskForm
    model = TodoTask
    success_url = reverse_lazy('dashboard')
    template_name = 'mytask/updatetodolist.html'


    def form_valid(self, form):
        print("valid")
        todo_date=self.request.POST.get('update-todo-date')
        self.model = form.save(commit=False)
        self.model.membership_reminder_date=todo_date
        self.model.save()
        return super(UpdateToDoList, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form)
        )

#This will set is_deleted to True ( That means it is deleted )
class DeleteToDoList(generic.UpdateView):
    model = TodoTask
    fields = ['is_deleted']
    success_url = reverse_lazy('dashboard')
    template_name = 'mytask/deleteconfirmationtodolist.html'

    def form_valid(self, form):
        # This will make only deleted field to be changed when update modal form is submitted
        model = form.save(commit=False)
        model.is_deleted=True
        model.save()
        return HttpResponseRedirect(reverse('dashboard'))
    
# Rest Framework views
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UserLoginView(APIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)

def userlogout(request):
    logout(request)
    return redirect('dashboard')
# Get All Routes
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/register/',
        '/api/list',
        '/api/list/<todo_id>',
        '/api/login/',
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = "Hello buddy"
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)


class TodoListView(generics.ListCreateAPIView):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskSerializer

    def get_queryset(self):
        user = User.objects.get(id=1)
        todo = TodoTask.objects.filter(user=user) 
        return todo
    
class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoTaskSerializer

    def get_object(self):
        todo_id = self.kwargs['todo_id']
        user = User.objects.get(id=1)
        todo = TodoTask.objects.get(id=todo_id, user=user)

        return todo