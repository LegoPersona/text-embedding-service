from .model_loader import get_model

async def embed_texts(texts: list[str]):
    model = get_model()
    return model.encode(texts).tolist()