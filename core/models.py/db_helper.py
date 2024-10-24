from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker as async_sessionmaker

class DataBaseHelper:
    def __init__(self, 
                 url,
                 echo=True, 
                 echo_pool=False, 
                 max_overflow=10,
                 pool_size=5):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            max_overflow=max_overflow,
            pool_size=pool_size
        )

        self.session_factory = async_sessionmaker(      #фабрика сессий!!!
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def dispose(self):
        await self.engine.dispose()

    async def session_getter(self):
        async with self.session_factory() as session:
            yield session
