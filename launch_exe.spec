# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import collect_all

datas = []
binaries = []
hiddenimports = []

transformers_deps = {
    "Pillow": "Pillow",
    "accelerate": "accelerate>=0.7.1",
    "black": "black~=22.0",
    "codecarbon": "codecarbon==1.2.0",
    "cookiecutter": "cookiecutter==1.7.3",
    "dataclasses": "dataclasses",
    "datasets": "datasets",
    "deepspeed": "deepspeed>=0.6.4",
    "fairscale": "fairscale>0.3",
    "faiss-cpu": "faiss-cpu",
    "fastapi": "fastapi",
    "filelock": "filelock",
    "flake8": "flake8>=3.8.3",
    "flax": "flax>=0.3.5",
    "ftfy": "ftfy",
    "fugashi": "fugashi>=1.0",
    "GitPython": "GitPython<3.1.19",
    "hf-doc-builder": "hf-doc-builder>=0.3.0",
    "huggingface-hub": "huggingface-hub>=0.1.0,<1.0",
    "importlib_metadata": "importlib_metadata",
    "ipadic": "ipadic>=1.0.0,<2.0",
    "isort": "isort>=5.5.4",
    "jax": "jax>=0.2.8,!=0.3.2,<=0.3.6",
    "jaxlib": "jaxlib>=0.1.65,<=0.3.6",
    "jieba": "jieba",
    "nltk": "nltk",
    "numpy": "numpy>=1.17",
    "onnxconverter-common": "onnxconverter-common",
    "onnxruntime-tools": "onnxruntime-tools>=1.4.2",
    "onnxruntime": "onnxruntime>=1.4.0",
    "optuna": "optuna",
    "optax": "optax>=0.0.8",
    "packaging": "packaging>=20.0",
    "parameterized": "parameterized",
    "phonemizer": "phonemizer",
    "protobuf": "protobuf",
    "psutil": "psutil",
    "pyyaml": "pyyaml>=5.1",
    "pydantic": "pydantic",
    "pytest": "pytest",
    "pytest-timeout": "pytest-timeout",
    "pytest-xdist": "pytest-xdist",
    "python": "python>=3.7.0",
    "ray[tune]": "ray[tune]",
    "regex": "regex!=2019.12.17",
    "requests": "requests",
    "rjieba": "rjieba",
    "rouge-score": "rouge-score",
    "sacrebleu": "sacrebleu>=1.4.12,<2.0.0",
    "sacremoses": "sacremoses",
    "sagemaker": "sagemaker>=2.31.0",
    "scikit-learn": "scikit-learn",
    "sentencepiece": "sentencepiece>=0.1.91,!=0.1.92",
    "sigopt": "sigopt",
    "librosa": "librosa",
    "starlette": "starlette",
    "tensorflow-cpu": "tensorflow-cpu>=2.3",
    "tensorflow": "tensorflow>=2.3",
    "tf2onnx": "tf2onnx",
    "timeout-decorator": "timeout-decorator",
    "timm": "timm",
    "tokenizers": "tokenizers>=0.11.1,!=0.11.3,<0.13",
    "torch": "torch>=1.0",
    "torchaudio": "torchaudio",
    "pyctcdecode": "pyctcdecode>=0.3.0",
    "tqdm": "tqdm>=4.27",
    "unidic": "unidic>=1.0.2",
    "unidic_lite": "unidic_lite>=1.0.7",
    "uvicorn": "uvicorn",
}

for dep in transformers_deps:
    tmp_ret = collect_all(dep)
    datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]

deps = ['gradio', 'basicsr', 'clip', 'open_clip', 'skimage', 'jsonmerge', 'cleanfid',
    'resize_right', 'tqdm', 'wandb', 'einops', 'timm', 'blendmodes',
    'accelerate', 'fairscale', 'fonts', 'font-roboto', 'font_roboto', 'gfpgan', 'invisible-watermark',
    'omegaconf', 'piexif', 'requests', 'Pillow', 'pytorch_lightning',
    'realesrgan', 'transformers', 'torchdiffeq', 'kornia', 'lark', 'inflection', 'GitPython',
    'torchsde', 'safetensors', 'regex', 'gdown']

for dep in deps:
    tmp_ret = collect_all(dep)
    datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]

block_cipher = None


a = Analysis(
    ['launch_exe.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='launch_exe',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='launch_exe',
)
