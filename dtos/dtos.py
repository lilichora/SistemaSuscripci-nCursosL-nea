
from dataclasses import dataclass
from typing import Optional, List

# DTO for User
@dataclass
class UserDTO:
    id: Optional[int] = None
    first_name: str = ""
    last_name: str = ""
    email: str = ""
    user_type: str = ""  # 'admin', 'creator', 'consumer'

# DTO for Course
@dataclass
class CourseDTO:
    id: Optional[int] = None
    name: str = ""
    description: Optional[str] = None
    state: str = "en_construccion"  # 'en_construccion', 'activo', 'inactivo'
    creator_id: int = 0

# DTO for Subscription
@dataclass
class SubscriptionDTO:
    id: Optional[int] = None
    user_id: int = 0
    course_id: int = 0
    subscription_date: Optional[str] = None  # Use ISO format for date
