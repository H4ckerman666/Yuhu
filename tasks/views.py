from rest_framework import viewsets
from tasks.models import Task
from tasks.serializers import TaskSerializer
from tasks.tasks import send_email_task
from drf_yasg.utils import swagger_auto_schema


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("-created_at")
    serializer_class = TaskSerializer

    @swagger_auto_schema(
        request_body=TaskSerializer,
        responses={201: TaskSerializer, 400: "Bad Request"},
    )
    def perform_create(self, serializer):

        task = serializer.save()
        print("MANDANDO EMAIL")
        send_email_task.delay(
            subject="Task Created",
            message=f"""
            Hey there! 
            Your task {task.title} has been created successfully
            Yuhu!!""",
            email=task.email,
        )

    def perform_update(self, serializer):
        task = serializer.save()
        send_email_task.delay(
            subject="Task Updated",
            message=f"""
            Hey there! 
            Your task {task.title} has been updated successfully
            Yuhu!!""",
            email=task.email,
        )
