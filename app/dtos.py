from typing import Optional
from pydantic import BaseModel

class UserDto(BaseModel):
    uid: Optional[str] = None
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    deactivated: Optional[bool] = None
    disabled: Optional[bool] = None

class PostDto(BaseModel):
    author: str
    has_media: bool
    content: str
    likes: int
    comments: list
    shares: int

class LocationDto(BaseModel):
    city: str
    country: str
    zip_code: int

class GroupChatDto(BaseModel):
    members: list