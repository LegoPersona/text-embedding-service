from fastapi import APIRouter
from .schemas import EmbeddingRequest, EmbeddingResponse
from .embedding_service import embed_text

router = APIRouter()

@router.post("/embed", response_model=EmbeddingResponse)
async def embed(payload: EmbeddingRequest):
    vector = await embed_text(payload.text)
    return EmbeddingResponse(embedding=vector)