# HBase design: `metrics` table

## Purpose
Store one row per check result (a time series per monitor).

## Access patterns
1. Latest N measurements of a monitor.
2. Measurements of a monitor within a time range.

## Row key
`<monitor_id>#<reversed_timestamp>`

- `reversed_timestamp = 9999999999999 - epoch_milliseconds` (13 digits, fixed width)
- Why monitor_id first: ...
- Why a reversed timestamp: ...
- Why a separator: ...

## Column family
One family named `m` (short name: it is repeated in every stored cell).

| Qualifier | Content |
|---|---|
| status | up / down |
| latency_ms | response time in milliseconds |
| http_code | HTTP status code |
| ssl_days | days before the SSL certificate expires |
| error | error message, if any |

## Retention
TTL: 90 days. VERSIONS: 1.

## Example
Monitor `m42`, measurement at 1792364536260 ms
-> row key `m42#8207635463739`
