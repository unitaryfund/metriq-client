from lib2to3.pgen2.token import OP
from tea_client.models import TeaClientModel
from typing import Optional, List

class User(TeaClientModel):
    """
    id (str): User ID.
    name(str): User name.
    fullName(str): User Full name.
    userName(str): Username.
    email(str): User Email.
    passwordHash(str): User password.
    affiliation(str): User affiliation.
    createdDate(str): Date of creation.
    modifiedDate(str): Date of modification.
    userToken(str): User API token.
    tokenCreationDate: Date of token creation.


    """

    id:Optional[str]
    name:Optional[str]
    fullName:Optional[str]
    userName:Optional[str]
    email:Optional[str]
    passwordHash:Optional[str]
    affiliation:Optional[str]
    createdDate:Optional[str]
    modifiedDate:Optional[str]
    userToken:Optional[str]
    tokenCreationDate:Optional[str]
