from huggingface_hub import HfApi

api = HfApi()
api.upload_file(
    path_or_fileobj="ResnetModel.pth",
    path_in_repo="ResnetModel.pth",
    repo_id="guriko/resnet50",
    repo_type="model",
)