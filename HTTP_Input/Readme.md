
curl -k "https://localhost:8088/services/collector" \
    -H "Authorization: Splunk CF179AE4-3C99-45F5-A7CC-3284AA91CF67" \
    -d '{"event": "Pony 1 has left the barn"}{"event": "Pony 2 has left the barn"}{"event": "Pony 3 has left the barn", "nested": {"key1": "value1"}}'
