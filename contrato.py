from datetime import datetime
from typing import Tuple   
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, Field
from enum import Enum

class produto_enum(str, Enum):
    produto1 = "ZapFlow com ChatGPT"
    produto2 = "ZapFlow com Llama"
    produto3 = "ZapFlow com Gemini"


class Venda(BaseModel):
    email: EmailStr
    data_hora: datetime
    valor_venda: PositiveFloat
    quantidade_produto: PositiveInt
    produto: produto_enum
