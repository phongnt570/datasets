from typing import Dict, List

from ..features import ClassLabel, Features, Value
from .base import TaskTemplate


class TextClassification(TaskTemplate):
    task = "text_classification"
    input_schema = Features({"text": Value("string")})
    label_schema = Features({"label": ClassLabel})

    def __init__(
        self,
        labels: List[str],
        text_column: str = "text",
        label_column: str = "label",
    ):
        assert sorted(set(labels)) == sorted(labels), "Labels must be unique"
        self.ordered_labels = sorted(labels)
        self.label_schema["label"] = ClassLabel(names=self.ordered_labels)
        self.text_column = text_column
        self.label_column = label_column
        self.label2id = {label: idx for idx, label in enumerate(self.ordered_labels)}

    @property
    def column_mapping(self) -> Dict[str, str]:
        return {
            self.text_column: "text",
            self.label_column: "label",
        }

    @classmethod
    def from_dict(cls, template_dict: dict) -> "TextClassification":
        return cls(
            text_column=template_dict["text_column"],
            label_column=template_dict["answer_column"],
            labels=template_dict["labels"],
        )

    def label_mapping(self, id2label: Dict[int, str]) -> Dict[int, int]:
        return {idx: self.label2id[label] for label, idx in self.label2id.items()}
