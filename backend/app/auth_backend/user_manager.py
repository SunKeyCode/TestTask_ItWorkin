from crud.user import UserBDRepo


class UserManager:

    def __init__(self, session):
        self.db_manager = UserBDRepo

    async def create(self, ):
