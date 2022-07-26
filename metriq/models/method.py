from telnetlib import theNULL
from typing import List, Optional
from xml.dom.expatbuilder import theDOMImplementation

from tea_client.models import TeaClientModel

from metriq.models.page import Page


class Method(TeaClientModel):
    """Method object.

    Attributes:
        id (str): Method ID.
        name (str): Method short name.
        full_name (str): Method full name.
        description (str): Method description.
        paper (str, optional): ID of the paper that describes the method.
        submissionCount (str): Number of submissions with the method.
        resultCount (str): Number of results with the method.
        upVoteTotal (str): Number of upvotes given to the method.
        createdAt (str): Date of method creation.
        updatedAt (str): Method update date.
    """

    id: str
    name: str
    fullName: str
    description: str
    submissionCount: str
    upVoteTotal: str
    resultCount: str
    createdAt: str
    updatedAt: str
    paper: Optional[str]



class Methods(Page):
    """Object representing a paginated page of methods.

    Attributes:
        count (int): Number of elements matching the query.
        next_page (int, optional): Number of the next page.
        previous_page (int, optional): Number of the previous page.
        results (List[Method]): List of methods on this page.
    """

    results: List[Method]
    