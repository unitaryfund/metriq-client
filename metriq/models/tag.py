from tea_client.models import TeaClientModel
from typing import Optional, List


class Tag(TeaClientModel):
    """Tag object.

    Attributes:
        name (str): Tag name.
        deletedDate (str): Date of submission.
        submissions (list): List of submissions for tag.
    """

    name: str
    deletedDate: Optional[str]
    submissions: Optional[str]
