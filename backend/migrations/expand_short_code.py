"""Widen links.short_code to match the API's 20-character limit."""

import asyncio

from sqlalchemy import text

from app.database import engine


async def migrate() -> None:
    async with engine.begin() as connection:
        await connection.execute(
            text("ALTER TABLE links ALTER COLUMN short_code TYPE VARCHAR(20)")
        )
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(migrate())
