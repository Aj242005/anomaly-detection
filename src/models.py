import torch
import torch.nn as nn
from transformers import ViTFeatureExtractor, ViTForImageClassification


class AnomalyDetector(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.feature_extractor = ViTFeatureExtractor.from_pretrained("google/vit-base-patch16-224")
        self.vit = ViTForImageClassification.from_pretrained(
            "google/vit-base-patch16-224",
            num_labels=config.MODEL_SETTINGS['num_classes'],
            ignore_mismatched_sizes=True
        )

    def forward(self, pixel_values):
        outputs = self.vit(pixel_values)
        return outputs.logits
