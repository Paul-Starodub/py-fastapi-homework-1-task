from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from database import MovieModel


async def get_all_movies(db: AsyncSession):
    stmt = select(MovieModel)
    result: Result = await db.execute(stmt)
    return result.scalars().all()


async def get_movie_by_id(db: AsyncSession, movie_id: int):
    stmt = select(MovieModel).where(MovieModel.id == movie_id)
    result: Result = await db.execute(stmt)
    return result.scalar_one_or_none()
