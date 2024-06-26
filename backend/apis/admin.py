from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.apis.deps import get_admin
from backend.crud.admin import (
    approve_company,
    approve_event,
    approve_institute,
    approve_post,
    approve_student,
    reject_company,
    reject_event,
    reject_institute,
    reject_post,
    reject_student,
)
from backend.exceptions.company import CompanyNotFound
from backend.exceptions.event import EventNotFound
from backend.exceptions.institute import InstituteNotFound
from backend.exceptions.post import PostNotFound
from backend.exceptions.student import StudentNotFound
from backend.models.admin import Admin
from backend.settings.db import get_db_sess

router = APIRouter()


@router.patch(
    "/approve-student/{student_id}",
    status_code=status.HTTP_200_OK,
)
def approve_student_application(
    student_id: UUID,
    db: Session = Depends(get_db_sess),
    admin: Admin = Depends(get_admin),
):
    try:
        approve_student(db, student_id)
    except StudentNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.delete(
    "/reject-student/{student_id}",
    status_code=status.HTTP_200_OK,
)
def reject_student_applicaiton(
    student_id: UUID,
    db: Session = Depends(get_db_sess),
    admin: Admin = Depends(get_admin),
):
    try:
        reject_student(db, student_id)
    except StudentNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.patch(
    "/approve-company/{company_id}",
    status_code=status.HTTP_200_OK,
)
def approve_company_application(
    company_id: UUID,
    db: Session = Depends(get_db_sess),
    admin: Admin = Depends(get_admin),
):
    try:
        approve_company(db, company_id)
    except CompanyNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.delete(
    "/reject-company/{company_id}",
    status_code=status.HTTP_200_OK,
)
def reject_company_application(
    company_id: UUID,
    db: Session = Depends(get_db_sess),
    admin: Admin = Depends(get_admin),
):
    try:
        reject_company(db, company_id)
    except CompanyNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.patch(
    "/approve-institute/{institute_id}",
    status_code=status.HTTP_200_OK,
)
def approve_institute_application(
    institute_id: UUID,
    db: Session = Depends(get_db_sess),
    admin: Admin = Depends(get_admin),
):
    try:
        approve_institute(db, institute_id)
    except InstituteNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.delete(
    "/reject-institute/{institute_id}",
    status_code=status.HTTP_200_OK,
)
def reject_institute_application(
    institute_id: UUID,
    db: Session = Depends(get_db_sess),
    admin: Admin = Depends(get_admin),
):
    try:
        reject_institute(db, institute_id)
    except InstituteNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.patch(
    "/approve-post/{post_id}",
    status_code=status.HTTP_200_OK,
)
def approve_post_request(
    post_id: UUID,
    db: Session = Depends(get_db_sess),
    admin: Admin = Depends(get_admin),
):
    try:
        approve_post(db, post_id)
    except PostNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.delete(
    "/reject-post/{post_id}",
    status_code=status.HTTP_200_OK,
)
def reject_post_request(
    post_id: UUID,
    db: Session = Depends(get_db_sess),
    admin: Admin = Depends(get_admin),
):
    try:
        reject_post(db, post_id)
    except PostNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.patch(
    "/approve-event/{event_id}",
    status_code=status.HTTP_200_OK,
)
def approve_event_request(
    event_id: UUID,
    db: Session = Depends(get_db_sess),
    admin: Admin = Depends(get_admin),
):
    try:
        approve_event(db, event_id)
    except EventNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.delete(
    "/reject-event/{event_id}",
    status_code=status.HTTP_200_OK,
)
def reject_event_request(
    event_id: UUID,
    db: Session = Depends(get_db_sess),
    admin: Admin = Depends(get_admin),
):
    try:
        reject_event(db, event_id)
    except EventNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
