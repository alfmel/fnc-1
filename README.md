# My version of FNC-1 corpus

This is my version of the FNC-1 training corpus. It simply splits the `train_bodies.csv` file into individual files named by the `Body ID`. I figure others may find this useful, so I decided to contribute.

The split article bodies showed there are only 1,683 unique article bodies. The `article_frequencies.py` script iterates through the `train_stances` file, extracts the unique Body IDs and returns the use frequency of each article body. This helped me verify the integrity of the corpus.

## Stance Detection dataset for FNC-1

For details of the task, see [FakeNewsChallenge.org](http://fakenewschallenge.org)


The data provided is `(headline, body, stance)` instances, where `stance` is one of `{unrelated, discuss, agree, disagree}`. The dataset is provided as two CSVs:


### `train_bodies.csv`

This file contains the body text of articles (the `articleBody` column) with corresponding IDs (`Body ID`)

### `train_stances.csv`

This file contains the labeled stances (the `Stance` column) for pairs of article headlines (`Headline`) and article bodies (`Body ID`, referring to entries in `train_bodies.csv`).

### Distribution of the data

The distribution of `Stance` classes in `train_stances.csv` is as follows:

|   rows |   unrelated |   discuss |     agree |   disagree |
|-------:|------------:|----------:|----------:|-----------:|
|  49972 |    0.73131  |  0.17828  | 0.0736012 |  0.0168094 |

Credits:

- Edward Misback
- Craig Pfeifer
