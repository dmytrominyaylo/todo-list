from django.urls import path
from task.views import (index,
                        TagListView,
                        TagCreateView,
                        TagUpdateView,
                        TagDeleteView,
                        TaskCreateView,
                        TaskUpdateView,
                        TaskDeleteView,
                        change_task_status,
                        )

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/change-status/", change_task_status, name="task-change"),
]

app_name = "task"
