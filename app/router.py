from fastapi import APIRouter
from .schemas import EmbeddingRequest, EmbeddingResponse
from .embedding_service import embed_texts

router = APIRouter()

@router.post("/embed", response_model=EmbeddingResponse)
async def embed(payload: EmbeddingRequest):
    vectors = await embed_texts(payload.texts)
    return EmbeddingResponse(embeddings=vectors)