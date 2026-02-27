from .model_loader import get_model

async def embed_text(text: str):
    model = get_model()
    return model.encode(text).tolist()