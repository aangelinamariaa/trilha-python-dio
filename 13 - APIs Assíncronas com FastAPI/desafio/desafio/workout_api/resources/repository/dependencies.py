from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

DatabaseDepency = Annotated[AsyncSession, Depends(get_session)]