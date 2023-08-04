#!/usr/bin/env python3
#!/usr/bin/env python
"""Saves the model as a TorchScript."""

import glob
import os
import sys
from typing import List

import torch

from model import ModelArgs, Transformer

def main() -> None:
    model_args = ModelArgs(dim=512, n_layers=6, n_heads=8, vocab_size=32000)
    model = Transformer(model_args)
    torch.jit.save(torch.jit.script(model), "model.pt")


if __name__ == "__main__":
    main()
