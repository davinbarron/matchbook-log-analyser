# Anomaly Findings

## 1. Dominant Single IP Address

IP `162.13.194.49` made 136,992 requests. The next highest IP (`81.88.167.22`) made 11,495 requests. This volume from a single client is abnormal and could indicate some sort of automated scripts or even a bot rather than a human user.

## 2. Activity Profile of the Dominant IP

The breakdown of HTTP methods for `162.13.194.49` is:

- POST: 70,261 (51.3%)
- DELETE: 66,605 (48.6%)
- PUT: 126 (0.092%)

There is nearly an equal split between POST and DELETE on the offers endpoints. This suggests that the client is rapidly submitting and cancelling offers in quick succession. This would warrant further investigation.

## 3. Geographic Traffic Concentration

Great Britain (`gb`) accounts for 143,262 requests, far exceeding all other countries. This is likely driven almost entirely by the single dominant IP `162.13.194.49`.

## 4. Login Failure Rate

Of 79 total login attempts, 7 returned a 400-series status code. While not alarming in isolation, combined with the high request volume from a single IP it may be worth confirming whether any of those failed logins are associated with `162.13.194.49`.
