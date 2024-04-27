from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.crud.post import create_post, get_post, update_post
from backend.exceptions.post import PostNotFound
from backend.schemas.base import PaginationOut
from backend.schemas.post import (
    PostCreateIn,
    PostFilterIn,
    PostIDOut,
    PostOut,
    PostUpdateIn,
)
from backend.settings.db import get_db_sess

router = APIRouter()


@router.post(
    "/posts{post_id}",
    response_model=PostIDOut,
    status_code=status.HTTP_201_CREATED,
)
def create_a_post(
    request_data: PostCreateIn,
    db: Session = Depends(get_db_sess),
):
    post = create_post(db, request_data)
    return PostIDOut(
        post_id=post.id,
    )


@router.patch(
    "/posts{post_id}",
    response_model=PostIDOut,
    status_code=status.HTTP_200_OK,
)
def update_a_post(
    post_id: UUID,
    request_data: PostUpdateIn,
    db: Session = Depends(get_db_sess),
):
    try:
        update_post(db, request_data)
    except PostNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.get(
    "/posts/{post_id}",
    response_model=PostIDOut,
    status_code=status.HTTP_200_OK,
)
def get_a_post(
    post_id: UUID,
    db: Session = Depends(get_db_sess),
):
    try:
        post = get_post(db, post_id)
    except PostNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
    return PostOut(
        **post.model_dump(),
    )


@router.get(
    "/posts",
    response_model=PaginationOut,
    status_code=status.HTTP_200_OK,
)
def get_posts(
    request_data: PostFilterIn,
    db: Session = Depends(get_db_sess),
):
    posts, count = get_posts(db, **request_data.model_dump())
    return PaginationOut(
        total=count,
        page=request_data.page,
        per_page=request_data.per_page,
        items=posts,
    )
