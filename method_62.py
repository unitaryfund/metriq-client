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
    """

    id: str("62")
    name: str("VQAA")
    full_name: str("Variational quantum adiabatic algorithm")
    description: str("the VQAA allows for a significant acceleration compared to the QAA with a linear adiabatic path, yet requires fewer parameters and measurements than the QAOA.")
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
