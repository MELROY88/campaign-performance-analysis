# Campaign Performance Analysis

Which ad channel gives the best return? This project answers that with Python.

**Metrics:** ROAS, CPA, CPC by channel.
**Data:** sample (synthetic) data. No real company data.

## Run it

```
pip install pandas numpy matplotlib
python analyse.py
```

Outputs: `channel_summary.csv`, `sample_campaign_data.csv` and `roas_by_channel.png`.

## Example result

In the sample data, Google Search has the best ROAS (about 4.3) and TikTok the lowest (about 2.4).

## Next steps

- Use real (anonymised) data
- Add a budget-shift recommendation
