# Extract Burmese NRC data from text using RegEx pattern

## Example Usage 1

```
from nrc_extractor import get_nrc_data

test_str = 'My National ID card number is 9/MAKANA(Naing)000333'

print(get_nrc_data(test_str))
```

This should print:

```
('9/MAKANA(Naing)000333', 'Mandalay')
```
## Example Usage 2

```
from nrc_extractor import get_nrc_data

test_str = 'မှတ်ပုံတင်အမှတ် ၉/မကန(နိုင်)၀၀၀၀၂၅'

print(get_nrc_data(test_str, state = True))

```

This should print:

```
('၉/မကန(နိုင်)၀၀၀၀၂၅', 'မန္တလေးတိုင်းဒေသကြီး')
```
*NOTE*  
Data used in the above examples are just sample data.

Future Work
- NRC validation
