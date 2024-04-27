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
