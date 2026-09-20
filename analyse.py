"""Campaign performance analysis using sample (synthetic) data."""
import numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
channels = ["Google Search", "Meta", "TikTok", "YouTube", "LinkedIn"]
rows = []
for ch in channels:
    for month in pd.date_range("2025-01-01", periods=12, freq="MS"):
        spend = rng.uniform(3000, 15000)
        clicks = int(spend / rng.uniform(0.6, 3.0))
        conv = int(clicks * rng.uniform(0.01, 0.06))
        revenue = conv * rng.uniform(80, 220)
        rows.append([ch, month, spend, clicks, conv, revenue])
df = pd.DataFrame(rows, columns=["channel", "month", "spend", "clicks", "conversions", "revenue"])
df.to_csv("sample_campaign_data.csv", index=False)

s = df.groupby("channel")[["spend", "clicks", "conversions", "revenue"]].sum()
s["ROAS"] = s.revenue / s.spend
s["CPA"] = s.spend / s.conversions
s["CPC"] = s.spend / s.clicks
s = s.round(2).sort_values("ROAS", ascending=False)
print(s)
s.to_csv("channel_summary.csv")

ax = s["ROAS"].plot(kind="bar", color="#2b6cb0", figsize=(7, 4))
ax.set_title("ROAS by channel (sample data)"); ax.set_ylabel("ROAS")
plt.tight_layout(); plt.savefig("roas_by_channel.png", dpi=150)
print("Best channel:", s.index[0])
