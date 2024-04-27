from enum import StrEnum


class UserRole(StrEnum):
    STUDENT = "student"
    COMPANY = "company"
    INSTITUTE = "institute"


class SchoolType(StrEnum):
    SUNY_KOREA = "suny_korea"
    GEORGE_MASON = "george_mason"
    UTAH = "utah"
    GHENT = "ghent"


class EventType(StrEnum):
    IGC = "igc"
    CAREER = "career"
    SCHOOL = "school"


class LocationType(StrEnum):
    SEOUL = "seoul"
    INCHEON = "incheon"


class WorkType(StrEnum):
    ONLINE = "online"
    OFFLINE = "offline"
    HYBRID = "hybrid"


class EntityType(StrEnum):
    COMPANY = "company"
    INSTITUTE = "institute"
