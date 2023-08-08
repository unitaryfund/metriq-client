from typing import List

from tea_client.http import HttpClient
from tea_client.handler import handler

from metriq.config import config
from metriq.models import (
    Submission,
    SubmissionCreateRequest,
    SubmissionUpdateRequest,
    Tag,
    Task,
    TaskCreateRequest,
    TaskUpdateRequest,
    Method,
    MethodCreateRequest,
    MethodUpdateRequest,
    Result,
    ResultCreateRequest,
    Platform,
    PlatformCreateRequest,
    PlatformUpdateRequest,
)


class MetriqClient:
    """Metriq client."""

    def __init__(self, token=None, url="https://metriq.info"):
        url = url or config.server_url
        self.http = HttpClient(
            url=f"{url}/api/",
            token=token or "",
            authorization_method=HttpClient.Authorization.token,
        )

    @handler
    def metriq_hello(self):
        print(self.http.url)
        return self.http.get("/")

    @handler
    def submission_get(self, submission_id: str) -> Submission:
        """Return a submission by it's ID.

        Args:
            submission_id (str): ID of the submission.

        Returns:
            Submission: Submission object.
        """
        response = self.http.get(f"/submission/{submission_id}/")
        print(response["message"])
        return Submission(**response["data"])

    @handler
    def submission_delete(self, submission_id: str):
        """Delete a submission.

        Args:
            submission_id (str): ID of the submission.
        """
        return self.http.delete(f"/submission/{submission_id}/")

    @handler
    def submission_add(self, submission: SubmissionCreateRequest) -> Submission:
        """Add a submission.

        Args:
            submission (SubmissionCreateRequest): Submission create request.

        Returns:
            Submission: Created submission.
        """
        response = self.http.post("/submission/", data=submission)
        print(response["message"])
        return Submission(**response["data"])

    @handler
    def submission_add_method(self, submission_id: str, method_id: str) -> Submission:
        """Add a method to a submission.

        Args:
            submission_id: ID of submission
            method_id: ID of method

        Returns:
            Submission: Created submission with method.
        """
        response = self.http.post(f"/submission/{submission_id}/method/{method_id}", data=None)
        print(response["message"])
        return Submission(**response["data"])

    @handler
    def submission_add_task(self, submission_id: str, task_id: str) -> Submission:
        """Add a task to a submission.

        Args:
            submission_id: ID of submission
            task_id: ID of task

        Returns:
            Submission: Created submission with task.
        """
        response = self.http.post(f"/submission/{submission_id}/task/{task_id}", data=None)
        print(response["message"])
        return Submission(**response["data"])

    @handler
    def submission_add_tag(self, submission_id: str, tag_name: str) -> Submission:
        """Add a tag to a submission.

        Args:
            submission_id: ID of submission
            tag_name: ID of tag

        Returns:
            Submission: Created submission with tag.
        """
        response = self.http.post(f"/submission/{submission_id}/tag/{tag_name}", data=None)
        print(response["message"])
        return Submission(**response["data"])

    @handler
    def submission_update(self, submission_id: str, submission: SubmissionUpdateRequest) -> Submission:
        """Update a submission.

        Args:
            submission_id (str): ID of the submission.
            submission (SubmissionUpdateRequest): Submission update request.

        Returns:
            Submission: Updated submission.
        """
        return Submission(**self.http.patch(f"/submission/{submission_id}/", data=submission))

    @handler
    def submission_upvote(self, submission_id: str):
        """Up-vote a submission.

        Args:
            submission_id (str): Primary key of submission to upvote

        Returns:
            Submission: Returned submission.
        """
        response = self.http.post(f"/submission/{submission_id}/upvote")
        print(response["message"])
        return Submission(**response["data"])

    @handler
    def submission_get_by_trending(self, page: int = 0) -> List[Submission]:
        """Return a list of trending submissions.

        Args:
            page (int): Desired page.

        Returns:
            List[Submission]: List of submission objects.
        """
        response = self.http.get(f"/submission/trending/{page}/")
        print(response["message"])
        return [
            Submission(**r)
            for r in response["data"]
        ]

    @handler
    def submission_get_by_popular(self, page: int = 0) -> List[Submission]:
        """Return a list of popular submissions.

        Args:
            page (int): Desired page.

        Returns:
            List[Submission]: List of submission objects.
        """
        response = self.http.get(f"/submission/popular/{page}/")
        print(response["message"])
        return [
            Submission(**r)
            for r in response["data"]
        ]

    @handler
    def submission_get_by_latest(self, page: int = 0) -> List[Submission]:
        """Return a list of latest submissions.

        Args:
            page (int): Desired page.

        Returns:
            List[Submission]: List of submission objects.
        """
        response = self.http.get(f"/submission/latest/{page}/")
        print(response["message"])
        return [
            Submission(**r)
            for r in response["data"]
        ]

    @handler
    def submission_get_by_trending_tag(self, tag: str, page: int = 0) -> List[Submission]:
        """Return a list of trending submissions by tag.

        Args:
            tag (str): Tag to search by.
            page (int): Desired page.

        Returns:
            List[Submission]: List of submission objects.
        """
        response = self.http.get(f"/submission/{tag}/trending/{page}/")
        print(response["message"])
        return [
            Submission(**r)
            for r in response["data"]
        ]

    @handler
    def submission_get_by_popular_tag(self, tag: str, page: int = 0) -> List[Submission]:
        """Return a list of popular submissions by tag.

        Args:
            tag (str): Tag to search by.
            page (int): Desired page.

        Returns:
            List[Submission]: List of submission objects.
        """
        response = self.http.get(f"/submission/{tag}/popular/{page}/")
        print(response["message"])
        return [
            Submission(**r)
            for r in response["data"]
        ]

    @handler
    def submission_get_by_latest_tag(self, tag: str, page: int = 0) -> List[Submission]:
        """Return a list of latest submissions by tag.

        Args:
            tag (str): Tag to search by.
            page (int): Desired page.

        Returns:
            List[Submission]: List of submission objects.
        """
        response = self.http.get(f"/submission/{tag}/latest/{page}/")
        print(response["message"])
        return [
            Submission(**r)
            for r in response["data"]
        ]

    @handler
    def tag_get(self) -> List[Tag]:
        """Return a List of Tag objects.

        Returns:
            List: List of Tag objects.
        """
        response = self.http.get(f"/tag/")
        print(response["message"])
        return [
            Tag(**r)
            for r in response["data"]
        ]

    @handler
    def tag_names_get(self) -> List[Tag]:
        """Return a List of names of Tag objects.

        Returns:
            List: List of names of Tag objects.
        """
        response = self.http.get(f"/tag/names/")
        print(response["message"])
        return [
            Tag(**r)
            for r in response["data"]
        ]

    @handler
    def task_add(self, task: TaskCreateRequest) -> Task:
        """Add a task.

        Args:
            task (TaskCreateRequest): Task create request.

        Returns:
            Task: Created task.
        """
        response = self.http.post("/task/", data=task)
        print(response["message"])
        return Task(**response["data"])

    @handler
    def task_delete(self, task_id: str):
        """Delete a task.

        Args:
            task_id (str): ID of the task.
        """
        return self.http.delete(f"/task/{task_id}/")

    @handler
    def task_update(self, task_id: str, task: TaskUpdateRequest) -> Task:
        """Update a task.

        Args:
            task_id (str): ID of the task.
            task (TaskUpdateRequest): Task update request.

        Returns:
            Task: Updated task.
        """
        return Task(**self.http.patch(f"/task/{task_id}/", data=task))

    @handler
    def task_get(self, task_id: str) -> Task:
        """Return a task by it's ID.

        Args:
            task_id (str): ID of the task.

        Returns:
            Task: Task object.
        """
        response = self.http.get(f"/task/{task_id}/")
        print(response["message"])
        return Task(**response["data"])

    @handler
    def task_get_submission_count(self) -> List[Task]:
        """Return a list of submission counts per Task.

        Returns:
            List: List of submission counts by Task object.
        """
        response = self.http.get(f"/task/submissionCount/")
        print(response["message"])
        return [
            Task(**r)
            for r in response["data"]
        ]

    @handler
    def task_get_names(self) -> List[Task]:
        """Return a list of Task names.

        Returns:
            List: List of names of each Task object.
        """
        response = self.http.get(f"/task/names/")
        print(response["message"])
        return [
            Task(**r)
            for r in response["data"]
        ]

    @handler
    def method_add(self, method: MethodCreateRequest) -> Method:
        """Add a method.

        Args:
            method (MethodCreateRequest): Method create request.

        Returns:
            Method: Created method.
        """
        response = self.http.post("/method/", data=method)
        print(response["message"])
        return Method(**response["data"])

    @handler
    def method_delete(self, method_id: str):
        """Delete a method.

        Args:
            method_id (str): ID of the method.
        """
        return self.http.delete(f"/method/{method_id}/")

    @handler
    def method_update(self, method_id: str, method: MethodUpdateRequest) -> Method:
        """Update a method.

        Args:
            method_id (str): ID of the method.
            method (MethodUpdateRequest): Method update request.

        Returns:
            Method: Updated method.
        """
        return Method(**self.http.patch(f"/method/{method_id}/", data=method))

    @handler
    def method_get(self, method_id: str) -> Method:
        """Return a method by it's ID.

        Args:
            method_id (str): ID of the method.

        Returns:
            Method: Method object.
        """
        return Method(**(self.http.get(f"/method/{method_id}/")['data']))

    @handler
    def method_get_submission_count(self) -> List[Method]:
        """Return method submission count.

        Returns:
            List: List of Method objects.
        """
        response = self.http.get(f"/method/submissionCount/")
        print(response["message"])
        return [
            Method(**r)
            for r in response["data"]
        ]

    @handler
    def method_get_names(self) -> List[Method]:
        """Return method names.

        Returns:
            List: List of Method objects.
        """
        response = self.http.get(f"/method/names/")
        print(response["message"])
        return [
            Method(**r)
            for r in response["data"]
        ]

    @handler
    def platform_update(self, platform_id: str, platform: PlatformUpdateRequest) -> Platform:
        """Update an Platform.

        Args:
            platform_id (str): ID of the platform.
            platform (platformUpdateRequest): platform update request.

        Returns:
            Platform: Updated platform.
        """
        return Platform(**self.http.patch(f"/platform/{platform_id}/", data=platform))

    @handler
    def platform_add(self, platform: PlatformCreateRequest) -> Platform:
        """Add an platform.

        Args:
            platform (PlatformCreateRequest): Platform create request.

        Returns:
            Platform: Created platform.
        """
        response = self.http.post("/platform/", data=platform)
        return Platform(**response["data"])

    @handler
    def platform_get(self) -> List[Platform]:
        """Return a List of Platform objects.

        Returns:
            List: List of Platform objects.
        """
        response = self.http.get(f"/platform/")
        return [
            Platform(**r)
            for r in response["data"]
        ]
    
    @handler
    def platform_get_names(self)->List[Platform]:
          """Return platform names.

        Returns:
            List: List of Platform objects.
        """
        response = self.http.get("/platform/names")
        print(response["message"])
        return [
            Platform(**r)
            for r in response["data"]
        ]

    @handler
    def result_metric_names(self) -> List[Result]:
        response = self.http.get(f"/result/metricNames/")
        print(response["message"])
        return [
            Result(**r)
            for r in response["data"]
        ]

    @handler
    def result_get(self, result_id: str) -> Method:
        """Return a result by it's ID.

        Args:
            result_id (str): ID of the result.

        Returns:
            Method: Method object.
        """
        return Result(**(self.http.get(f"/result/{result_id}/")['data']))

    @handler
    def result_add(self, result: ResultCreateRequest, submission_id: str) -> Result:
        """Add a result to a submission.

        Args:
            result (ResultCreateRequest): Result create request.

        Returns:
            Result: Created result.
        """
        response = self.http.post(f"/submission/{submission_id}/result", data=result)
        print(response["message"])
        return Result(**response["data"])
