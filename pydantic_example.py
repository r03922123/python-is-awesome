from pydantic import BaseModel, StrictInt


class User(BaseModel):
    name: str
    email: str
    account_id: StrictInt
    age: StrictInt


user = User(name="abc", email="abc@gamil.com", account_id=42, age=32)
print(user.model_dump())
print(user.model_dump_json())
