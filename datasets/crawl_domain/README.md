---
annotations_creators:
- expert-generated
language_creators:
- crowdsourced
- expert-generated
- found
languages:
- en
licenses:
- mit
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- extended|other-Common-Crawl
- original
task_categories:
- other
task_ids:
- other-other-text-to-speech
- other-other-web-search
---

# Dataset Card for Common Crawl Domain Names
## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://github.com/google-research-datasets/common-crawl-domain-names
- **Repository:** https://github.com/google-research-datasets/common-crawl-domain-names
- **Paper:** https://arxiv.org/pdf/2011.03138
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

Corpus of domain names scraped from Common Crawl and manually annotated to add word boundaries (e.g. "commoncrawl" to "common crawl").

Breaking [domain names](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL) such as "openresearch" into component words "open" and "research" is important for applications such as Text-to-Speech synthesis and web search.  [Common Crawl](https://commoncrawl.org/)  is an open repository of web crawl data that can be accessed and analyzed by anyone. Specifically, we scraped the plaintext (WET) extracts for domain names from URLs that contained diverse letter casing (e.g. "OpenBSD"). Although in the previous example, segmentation is trivial using letter casing, this was not always the case (e.g. "NASA"), so we had to manually annotate the data.

### Supported Tasks and Leaderboards

- Text-to-Speech synthesis
- Web search

### Languages

en: English

## Dataset Structure

### Data Instances

Each sample is an example of space separated segments of a domain name. The examples are stored in their original letter casing, but harder and more interesting examples can be generated by lowercasing the input first.

For example:

```
Open B S D
NASA
ASAP Workouts
```

### Data Fields

- `example`: a `string` feature: space separated segments of a domain name. 

### Data Splits

| split | size  | trivial | avg_input_length | avg_segments |
|-------|-------|---------|------------------|--------------|
| train | 17572 | 13718   | 12.63            | 2.65         |
| eval  | 1953  | 1536    | 12.77            | 2.67         |
| test  | 2170  | 1714    | 12.63            | 2.66         |

## Dataset Creation

### Curation Rationale

The dataset was curated by scraping the plaintext (WET) extracts for domain names from URLs that contained diverse letter casing (e.g. "OpenBSD"). Although in the previous example, segmentation is trivial using letter casing, this was not always the case (e.g. "NASA"), so the curators of the dataset had to manually annotate the data.

### Source Data

#### Initial Data Collection and Normalization

Corpus of domain names scraped from Common Crawl and manually annotated to add word boundaries

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

The annotators are the curators of this dataset

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

The curators of this dataset are [Jae Hun Ro](https://github.com/JaeHunRo) and [mwurts4google](https://github.com/mwurts4google), who are the contributors of the official Github repository for this dataset. Since the account handles of other curators are unknown currently, the authors of the paper linked to this dataset is mentioned here as curators, [Hao Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang%2C+H), [Jae Ro](https://arxiv.org/search/cs?searchtype=author&query=Ro%2C+J), and [Richard Sproat](https://arxiv.org/search/cs?searchtype=author&query=Sproat%2C+R).

### Licensing Information

[MIT License](https://github.com/google-research-datasets/common-crawl-domain-names/blob/master/LICENSE)

### Citation Information

```
@inproceedings{zrs2020urlsegmentation,
  title={Semi-supervised URL Segmentation with Recurrent Neural Networks Pre-trained on Knowledge Graph Entities},
  author={Hao Zhang and Jae Ro and Richard William Sproat},
  booktitle={The 28th International Conference on Computational Linguistics (COLING 2020)},
  year={2020}
}
```


### Contributions

Thanks to [@Karthik-Bhaskar](https://github.com/Karthik-Bhaskar) for adding this dataset.