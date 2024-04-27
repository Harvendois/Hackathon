from datetime import datetime
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from backend.exceptions.post import PostNotFound
from backend.models.post import Post
from backend.schemas.enums import EntityType, LocationType, WorkType
from backend.schemas.post import PostCreateIn, PostUpdateIn


def create_post(
    db: Session,
    request_data: PostCreateIn,
) -> Post:
    # create a post
    post = Post.create(
        **request_data.model_dump(),
    )
    db.add(post)
    db.commit()

    return post


def update_post(
    db: Session,
    request_data: PostUpdateIn,
) -> Post:
    # retrieve post from db
    statement = select(Post).where(Post.id == request_data.id)

    post: Post = db.execute(statement).scalars().one_or_none()

    if not post:
        raise PostNotFound(
            post_id=request_data.id,
        )

    # update post
    post.update(
        **request_data.model_dump(),
    )

    db.commit()
    db.refresh(post)

    return post


def get_post(
    db: Session,
    post_id: UUID,
) -> Post:
    # retrieve post from db
    statement = select(Post).where(Post.id == post_id)

    post: Post = db.execute(statement).scalars().one_or_none()

    if not post:
        raise PostNotFound(
            post_id=post_id,
        )

    return post


def get_posts(
    db: Session,
    location: LocationType | None,
    work_type: WorkType | None,
    entity_type: EntityType | None,
    company_id: UUID | None,
    institute_id: UUID | None,
    start_dt: datetime | None,
    end_dt: datetime | None,
    verified: bool,
    page: int,
    per_page: int,
) -> tuple[list[Post], int]:
    # retrieve posts from db
    statement = select(Post)

    if location:
        statement = statement.where(Post.location == location)
    if work_type:
        statement = statement.where(Post.type == work_type)
    if entity_type == EntityType.COMPANY:
        statement = statement.where(Post.company_id == company_id)
    elif entity_type == EntityType.INSTITUTE:
        statement = statement.where(Post.institute_id == institute_id)
    if start_dt:
        statement = statement.where(Post.start_dt >= start_dt)
    if end_dt:
        statement = statement.where(Post.end_dt <= end_dt)
    if verified:
        statement = statement.where(Post.verified == verified)
    # get total count
    total_count = (
        db.execute(select(func.count()).select_from(statement)).scalars().one()
    )

    # apply pagination
    statement = statement.offset((page - 1) * per_page).limit(per_page)

    # get paginated result
    result = db.execute(statement).all()

    return result, total_count
