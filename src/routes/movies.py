from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
import crud
from database import get_db
from schemas.movies import MovieDetailResponseSchema, MovieListResponseSchema


router = APIRouter()


@router.get("/movies/", response_model=list[MovieListResponseSchema])
async def get_movies(db: Annotated[AsyncSession, Depends(get_db)]):
    movies = await crud.get_all_movies(db)
    if not movies:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No movies found.")
    return movies


@router.get("/movies/{movie_id}/", response_model=MovieDetailResponseSchema)
async def get_movie_by_id(movie_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    movie = await crud.get_movie_by_id(db=db, movie_id=movie_id)
    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie with the given ID was not found.")
    return movie
