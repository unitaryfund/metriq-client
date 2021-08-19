from urllib import parse
from typing import Dict, List, Optional


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
    Methods,
    MethodCreateRequest,
    MethodUpdateRequest,
    Result,
    Paper,
    Papers,
    Repository,
    Conference,
    Conferences,
    Proceeding,
    Proceedings,
    Dataset,
    DatasetCreateRequest,
    DatasetUpdateRequest,
    Datasets,
    Metric,
    MetricCreateRequest,
    MetricUpdateRequest,
    EvaluationTable,
    EvaluationTables,
    EvaluationTableCreateRequest,
    EvaluationTableUpdateRequest,
)


class MetriqClient:
    """Metriq client."""

    def __init__(self, token=None, url=None):
        url = url or config.server_url
        self.http = HttpClient(
            url=f"{url}/api/",
            token=token or "",
            authorization_method=HttpClient.Authorization.token,
        )

    @handler
    def hello(self):
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
    def submission_trending_list(self, page: int = 0) -> List[Submission]:
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
    def submission_popular_list(self, page: int = 0) -> List[Submission]:
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
    def submission_latest_list(self, page: int = 0) -> List[Submission]:
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
    def submission_trending_by_tag_list(self, tag: str, page: int = 0) -> List[Submission]:
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
    def submission_popular_by_tag_list(self, tag: str, page: int = 0) -> List[Submission]:
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
    def submission_latest_by_tag_list(self, tag: str, page: int = 0) -> List[Submission]:
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
    def task_submission_count_get(self) -> List[Task]:
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
    def task_names_get(self) -> List[Task]:
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
    def result_metric_names(self) -> List[Result]:
        response = self.http.get(f"/result/metricNames/")
        print(response["message"])
        return [
            Result(**r)
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
    def method_get(self, method_id) -> Method:
        """Return a method by it's ID.

        Args:
            method_id (str): ID of the method.

        Returns:
            Method: Method object.
        """
        return Method(**self.http.get(f"/method/{method_id}/"))

    @handler
    def method_submission_count_get(self) -> List[Method]:
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
    def method_names_get(self) -> List[Method]:
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

    @staticmethod
    def __params(page: int, items_per_page: int, **kwargs) -> Dict[str, str]:
        params = {key: str(value) for key, value in kwargs.items()}
        params.update(
            {"items_per_page": str(items_per_page), "page": str(page)}
        )
        return params

    @staticmethod
    def __parse(url: str) -> int:
        """Return page number."""
        p = parse.urlparse(url)
        if p.query == "":
            return 1
        else:
            q = parse.parse_qs(p.query)
            return q["page"][0]

    @classmethod
    def __page(cls, result, page_model):
        next_page = result["next"]
        if next_page is not None:
            next_page = cls.__parse(next_page)
        previous_page = result["previous"]
        if previous_page is not None:
            previous_page = cls.__parse(previous_page)
        return page_model(
            count=result["count"],
            next_page=next_page,
            previous_page=previous_page,
            results=result["results"],
        )

    # @staticmethod
    # def __create_result(data: dict) -> Result:
    #     return Result(**data)
    #
    # @staticmethod
    # def __create_result_sync_data(data: dict) -> dict:
    #     return data

    @handler
    def paper_list(
        self, q: Optional[str] = None, page: int = 1, items_per_page: int = 50
    ) -> Papers:
        """Return a paginated list of papers.

        Args:
            q (str): Filter papers by querying the paper title and abstract.
            page (int): Desired page.
            items_per_page (int): Desired number of items per page.
                Default: 50.

        Returns:
            Papers: Papers object.
        """
        params = self.__params(page, items_per_page)
        timeout = None
        if q is not None:
            params["q"] = q
            timeout = 60
        return self.__page(
            self.http.get("/papers/", params=params, timeout=timeout), Papers
        )

    @handler
    def paper_get(self, paper_id: str) -> Paper:
        """Return a paper by it's ID.

        Args:
            paper_id (str): ID of the paper.

        Returns:
            Paper: Paper object.
        """
        return Paper(**self.http.get(f"/papers/{paper_id}/"))

    @handler
    def paper_repository_list(self, paper_id: str) -> List[Repository]:
        """Return a list of paper implementations.

        Args:
            paper_id (str): ID of the paper.

        Returns:
            List[Repository]: List of repository objects.
        """
        return [
            Repository(**r)
            for r in self.http.get(f"/papers/{paper_id}/repositories/")
        ]

    # @handler
    # def paper_task_list(self, paper_id: str) -> List[Task]:
    #     """Return a list of tasks mentioned in the paper.
    #
    #     Args:
    #         paper_id (str): ID of the paper.
    #
    #     Returns:
    #         List[Task]: List of task objects.
    #     """
    #     return [Task(**t) for t in self.http.get(f"/papers/{paper_id}/tasks/")]

    @handler
    def paper_method_list(self, paper_id: str) -> List[Method]:
        """Return a list of methods mentioned in the paper.

        Args:
            paper_id (str): ID of the paper.

        Returns:
            List[Method]: List of method objects.
        """
        return [
            Method(**t) for t in self.http.get(f"/papers/{paper_id}/methods/")
        ]

    # @handler
    # def paper_result_list(self, paper_id: str) -> List[Result]:
    #     """Return a list of evaluation results for the paper.
    #
    #     Args:
    #         paper_id (str): ID of the paper.
    #
    #     Returns:
    #         List[Result]: List of result objects.
    #     """
    #     return [
    #         self.__create_result(result)
    #         for result in self.http.get(f"/papers/{paper_id}/results/")
    #     ]

    @handler
    def conference_list(
        self, page: int = 1, items_per_page: int = 50
    ) -> Conferences:
        """Return a paginated list of conferences.

        Args:
            page (int): Desired page.
            items_per_page (int): Desired number of items per page.
                Default: 50.

        Returns:
            Conferences: Conferences object.
        """
        return self.__page(
            self.http.get(
                "/conferences/", params=self.__params(page, items_per_page)
            ),
            Conferences,
        )

    @handler
    def conference_get(self, conference_id: str) -> Conference:
        """Return a conference by it's ID.

        Args:
            conference_id (str): ID of the conference.

        Returns:
            Conference: Conference object.
        """
        return Conference(**self.http.get(f"/conferences/{conference_id}/"))

    @handler
    def proceeding_list(
        self, conference_id: str, page: int = 1, items_per_page: int = 50
    ) -> Proceedings:
        """Return a paginated list of conference proceedings.

        Args:
            conference_id (str): ID of the conference.
            page (int): Desired page.
            items_per_page (int): Desired number of items per page.
                Default: 50.

        Returns:
            Proceedings: Proceedings object.
        """
        return self.__page(
            self.http.get(
                f"/conferences/{conference_id}/proceedings/",
                params=self.__params(page, items_per_page),
            ),
            Proceedings,
        )

    @handler
    def proceeding_get(
        self, conference_id: str, proceeding_id: str
    ) -> Proceeding:
        """Return a conference proceeding by it's ID.

        Args:
            conference_id (str): ID of the conference.
            proceeding_id (str): ID of the proceeding.

        Returns:
            Proceeding: Proceeding object.
        """
        return Proceeding(
            **self.http.get(
                f"/conferences/{conference_id}/proceedings/{proceeding_id}/"
            )
        )

    @handler
    def proceeding_paper_list(
        self, conference_id: str, proceeding_id: str
    ) -> List[Paper]:
        """Return a list of papers published in a confernce proceeding.

        Args:
            conference_id (str): ID of the conference.
            proceeding_id (str): ID of the proceding.

        Returns:
            List[Paper]: List of paper objects.
        """
        return [
            Paper(**p)
            for p in self.http.get(
                f"/conferences/{conference_id}/proceedings/{proceeding_id}"
                f"/papers/"
            )
        ]

    # @handler
    # def area_list(
    #     self, q: Optional[str] = None, page: int = 1, items_per_page: int = 50
    # ) -> Areas:
    #     """Return a paginated list of areas.
    #
    #     Args:
    #         q (str): Filter areas by querying the area name.
    #         page (int): Desired page.
    #         items_per_page (int): Desired number of items per page.
    #             Default: 50.
    #
    #     Returns:
    #         Areas: Areas object.
    #     """
    #     params = self.__params(page, items_per_page)
    #     timeout = None
    #     if q is not None:
    #         params["q"] = q
    #         timeout = 60
    #     return self.__page(
    #         self.http.get("/areas/", params=params, timeout=timeout), Areas
    #     )
    #
    # @handler
    # def area_get(self, area_id: str) -> Area:
    #     """Return an area by it's ID.
    #
    #     Args:
    #         area_id (str): ID of the area.
    #
    #     Returns:
    #         Area: Area object.
    #     """
    #     return Area(**self.http.get(f"/areas/{area_id}/"))
    #
    # @handler
    # def area_task_list(
    #     self, area_id: str, page: int = 1, items_per_page: int = 50
    # ) -> Tasks:
    #     """Return a paginated list of tasks in an area.
    #
    #     Args:
    #         area_id (str): ID of the area.
    #         page (int): Desired page.
    #         items_per_page (int): Desired number of items per page.
    #             Default: 50.
    #
    #     Returns:
    #         Tasks: Tasks object.
    #     """
    #     return self.__page(
    #         self.http.get(
    #             f"/areas/{area_id}/tasks/",
    #             params=self.__params(page, items_per_page),
    #         ),
    #         Tasks,
    #     )
    #
    # @handler
    # def task_list(
    #     self, q: Optional[str] = None, page: int = 1, items_per_page: int = 50
    # ) -> Tasks:
    #     """Return a paginated list of tasks.
    #
    #     Args:
    #         q (str): Filter tasks by querying the task name.
    #         page (int): Desired page.
    #         items_per_page (int): Desired number of items per page.
    #             Default: 50.
    #
    #     Returns:
    #         Tasks: Tasks object.
    #     """
    #     params = self.__params(page, items_per_page)
    #     timeout = None
    #     if q is not None:
    #         params["q"] = q
    #         timeout = 60
    #     return self.__page(
    #         self.http.get("/tasks/", params=params, timeout=timeout), Tasks
    #     )
    #
    # @handler
    # def task_get(self, task_id: str) -> Task:
    #     """Return a task by it's ID.
    #
    #     Args:
    #         task_id (str): ID of the task.
    #
    #     Returns:
    #         Task: Task object.
    #     """
    #     return Task(**self.http.get(f"/tasks/{task_id}/"))
    #
    # @handler
    # def task_add(self, task: TaskCreateRequest) -> Task:
    #     """Add a task.
    #
    #     Args:
    #        task (TaskCreateRequest): Task create request.
    #
    #     Returns:
    #         Task: Created task.
    #     """
    #     return Task(**self.http.post("/tasks/", data=task))
    #
    # @handler
    # def task_update(self, task_id: str, task: TaskUpdateRequest) -> Task:
    #     """Update a task.
    #
    #     Args:
    #         task_id (str): ID of the task.
    #         task (TaskUpdateRequest): Task update request.
    #
    #     Returns:
    #         Task: Updated task.
    #     """
    #     return Task(**self.http.patch(f"/tasks/{task_id}/", data=task))
    #
    # @handler
    # def task_delete(self, task_id: str):
    #     """Delete a task.
    #
    #     Args:
    #         task_id (str): ID of the task.
    #     """
    #     self.http.delete(f"/tasks/{task_id}/")
    #
    # @handler
    # def task_paper_list(
    #     self, task_id: str, page: int = 1, items_per_page: int = 50
    # ) -> Papers:
    #     """Return a paginated list of papers for a selected task.
    #
    #     Args:
    #         task_id (str): ID of the task.
    #         page (int): Desired page.
    #         items_per_page (int): Desired number of items per page.
    #             Default: 50.
    #
    #     Returns:
    #         Papers: Papers object.
    #     """
    #     return self.__page(
    #         self.http.get(
    #             f"/tasks/{task_id}/papers/",
    #             params=self.__params(page, items_per_page),
    #         ),
    #         Papers,
    #     )
    #
    # @handler
    # def task_evaluation_list(self, task_id: str) -> List[EvaluationTable]:
    #     """Return a list of evaluation tables for a selected task.
    #
    #     Args:
    #         task_id (str): ID of the task.
    #
    #     Returns:
    #         List[EvaluationTable]: List of short evaluation table objects.
    #     """
    #     return [
    #         EvaluationTable(**sp)
    #         for sp in self.http.get(f"/tasks/{task_id}/evaluations/")
    #     ]

    @handler
    def dataset_list(
        self, q: Optional[str] = None, page: int = 1, items_per_page: int = 50
    ) -> Datasets:
        """Return a paginated list of datasets.

        Args:
            q (str): Filter datasets by querying the dataset name.
            page (int): Desired page.
            items_per_page (int): Desired number of items per page.
                Default: 50.

        Returns:
            Datasets: Datasets object.
        """
        params = self.__params(page, items_per_page)
        timeout = None
        if q is not None:
            params["q"] = q
            timeout = 60
        return self.__page(
            self.http.get("/datasets/", params=params, timeout=timeout),
            Datasets,
        )

    @handler
    def dataset_get(self, dataset_id: str) -> Dataset:
        """Return a dastaset by it's ID.

        Args:
            dataset_id (str): ID of the dataset.

        Returns:
            Dataset: Dataset object.
        """
        return Dataset(**self.http.get(f"/datasets/{dataset_id}/"))

    @handler
    def dataset_add(self, dataset: DatasetCreateRequest) -> Dataset:
        """Add a dataset.

        Args:
           dataset (DatasetCreateRequest): Dataset create request.

        Returns:
            Dataset: Created dataset.
        """
        return Dataset(**self.http.post("/datasets/", data=dataset))

    @handler
    def dataset_update(
        self, dataset_id: str, dataset: DatasetUpdateRequest
    ) -> Dataset:
        """Update a dataset.

        Args:
            dataset_id (str): ID of the dataset.
            dataset (DatasetUpdateRequest): Dataset update request.

        Returns:
            Dataset: Updated dataset.
        """
        return Dataset(
            **self.http.patch(f"/datasets/{dataset_id}/", data=dataset)
        )

    @handler
    def dataset_delete(self, dataset_id: str):
        """Delete a dataset.

        Args:
            dataset_id (str): ID of the dataset.
        """
        self.http.delete(f"/datasets/{dataset_id}/")

    @handler
    def dataset_evaluation_list(
        self, dataset_id: str
    ) -> List[EvaluationTable]:
        """Return a list of evaluation tables for a selected dataset.

        Args:
            dataset_id (str): ID of the dasaset.

        Returns:
            List[EvaluationTable]: List of short evaluation table objects.
        """
        return [
            EvaluationTable(**sp)
            for sp in self.http.get(f"/datasets/{dataset_id}/evaluations/")
        ]

    @handler
    def method_list(self, page: int = 1, items_per_page: int = 50) -> Methods:
        """Return a paginated list of methods.

        Args:
            page (int): Desired page.
            items_per_page (int): Desired number of items per page.
                Default: 50.

        Returns:
            Methods: Methods object.
        """
        return self.__page(
            self.http.get(
                "/methods/", params=self.__params(page, items_per_page)
            ),
            Methods,
        )

    @handler
    def evaluation_list(
        self, page: int = 1, items_per_page: int = 50
    ) -> EvaluationTables:
        """Return a paginated list of evaluation tables.

        Args:
            page (int): Desired page.
            items_per_page (int): Desired number of items per page.
                Default: 50.

        Returns:
            EvaluationTables: Evaluation table page object.
        """
        return self.__page(
            self.http.get(
                "/evaluations/", params=self.__params(page, items_per_page)
            ),
            EvaluationTables,
        )

    @handler
    def evaluation_get(self, evaluation_id: str) -> EvaluationTable:
        """Return a evaluation table by it's ID.

        Args:
            evaluation_id (str): ID of the evaluation table.

        Returns:
            EvaluationTable: Evaluation table object.
        """
        return EvaluationTable(
            **self.http.get(f"/evaluations/{evaluation_id}/")
        )

    @handler
    def evaluation_create(
        self, evaluation: EvaluationTableCreateRequest
    ) -> EvaluationTable:
        """Create an evaluation table.

        Args:
            evaluation (EvaluationTableCreateRequest): Evaluation table create
                request object.

        Returns:
            EvaluationTable: The new created evaluation table.
        """
        return EvaluationTable(
            **self.http.post("/evaluations/", data=evaluation)
        )

    @handler
    def evaluation_update(
        self, evaluation_id: str, evaluation: EvaluationTableUpdateRequest
    ) -> EvaluationTable:
        """Update an evaluation table.

        Args:
            evaluation_id (str): ID of the evaluation table.
            evaluation (EvaluationTableUpdateRequest): Evaluation table update
                request object.

        Returns:
            EvaluationTable: The updated evaluation table.
        """
        return EvaluationTable(
            **self.http.patch(
                f"/evaluations/{evaluation_id}/", data=evaluation
            )
        )

    @handler
    def evaluation_delete(self, evaluation_id: str):
        """Delete an evaluation table.

        Args:
            evaluation_id (str): ID of the evaluation table.
        """
        self.http.delete(f"/evaluations/{evaluation_id}/")

    @handler
    def evaluation_metric_list(self, evaluation_id: str) -> List[Metric]:
        """List all metrics used in the evaluation table.

        Args:
            evaluation_id (str): ID of the evaluation table.

        Returns:
            List[Metric]: All metrics used in the evaluation table.
        """
        return [
            Metric(**m)
            for m in self.http.get(f"/evaluations/{evaluation_id}/metrics/")
        ]

    @handler
    def evaluation_metric_get(
        self, evaluation_id: str, metric_id: str
    ) -> Metric:
        """Get a metrics used in the evaluation table.

        Args:
            evaluation_id (str): ID of the evaluation table.
            metric_id (str): ID of the metric.

        Returns:
            Metric: Requested metric.
        """
        return Metric(
            **self.http.get(
                f"/evaluations/{evaluation_id}/metrics/{metric_id}/"
            )
        )

    @handler
    def evaluation_metric_add(
        self, evaluation_id: str, metric: MetricCreateRequest
    ) -> Metric:
        """Add a metrics to the evaluation table.

        Args:
            evaluation_id (str): ID of the evaluation table.
            metric (MetricCreateRequest): Metric create request.

        Returns:
            Metric: Created metric.
        """
        return Metric(
            **self.http.post(
                f"/evaluations/{evaluation_id}/metrics/", data=metric
            )
        )

    @handler
    def evaluation_metric_update(
        self, evaluation_id: str, metric_id: str, metric: MetricUpdateRequest
    ) -> Metric:
        """Update a metrics in the evaluation table.

        Args:
            evaluation_id (str): ID of the evaluation table.
            metric_id (str): ID of the metric.
            metric (MetricCreateRequest): Metric update request.

        Returns:
            Metric: Updated metric.
        """
        return Metric(
            **self.http.patch(
                f"/evaluations/{evaluation_id}/metrics/{metric_id}/",
                data=metric,
            )
        )

    @handler
    def evaluation_metric_delete(self, evaluation_id: str, metric_id: str):
        """Delete a metrics from the evaluation table.

        Args:
            evaluation_id (str): ID of the evaluation table.
            metric_id (str): ID of the metric.
        """
        self.http.delete(f"/evaluations/{evaluation_id}/metrics/{metric_id}/")

    # @handler
    # def evaluation_result_list(self, evaluation_id: str) -> List[Result]:
    #     """List all results from the evaluation table.
    #
    #     Args:
    #         evaluation_id (str): ID of the evaluation table.
    #
    #     Returns:
    #         List[Result]: All results from the evaluation table.
    #     """
    #     return [
    #         self.__create_result(result)
    #         for result in self.http.get(
    #             f"/evaluations/{evaluation_id}/results/"
    #         )
    #     ]

    # @handler
    # def evaluation_result_get(
    #     self, evaluation_id: str, result_id: str
    # ) -> Result:
    #     """Get a result from the evaluation table.
    #
    #     Args:
    #         evaluation_id (str): ID of the evaluation table.
    #         result_id (str): ID of the result.
    #
    #     Returns:
    #         Result: Requested result.
    #     """
    #     return self.__create_result(
    #         self.http.get(f"/evaluations/{evaluation_id}/results/{result_id}/")
    #     )
    #
    # @handler
    # def evaluation_result_add(
    #     self, evaluation_id: str, result: ResultCreateRequest
    # ) -> Result:
    #     """Add a result to the evaluation table.
    #
    #     Args:
    #         evaluation_id (str): ID of the evaluation table.
    #         result (ResultCreateRequest): Result create request.
    #
    #     Returns:
    #         Result: Created result.
    #     """
    #     return self.__create_result(
    #         self.http.post(
    #             f"/evaluations/{evaluation_id}/results/", data=result
    #         )
    #     )
    #
    # @handler
    # def evaluation_result_update(
    #     self, evaluation_id: str, result_id: str, result: ResultUpdateRequest
    # ) -> Result:
    #     """Update a result in the evaluation table.
    #
    #     Args:
    #         evaluation_id (str): ID of the evaluation table.
    #         result_id (str): ID of the result.
    #         result (ResultUpdateRequest): Result update request.
    #
    #     Returns:
    #         Result: Updated result.
    #     """
    #     return self.__create_result(
    #         self.http.patch(
    #             f"/evaluations/{evaluation_id}/results/{result_id}/",
    #             data=result,
    #         )
    #     )
    #
    # @handler
    # def evaluation_result_delete(self, evaluation_id: str, result_id: str):
    #     """Delete a result from the evaluation table.
    #
    #     Args:
    #         evaluation_id (str): ID of the evaluation table.
    #         result_id (str): ID of the result.
    #     """
    #     self.http.delete(f"/evaluations/{evaluation_id}/results/{result_id}/")
    #
    # @handler
    # def evaluation_synchronize(
    #     self, evaluation: EvaluationTableSyncRequest
    # ) -> EvaluationTableSyncResponse:
    #     d = self.http.post("/rpc/evaluation-synchronize/", data=evaluation)
    #     d["results"] = [
    #         self.__create_result_sync_data(result) for result in d["results"]
    #     ]
    #     return EvaluationTableSyncResponse(**d)