# Retrieval Debugging Guide

Use this order when a grounded answer is weak:

1. Did ingestion keep the relevant text?
2. Was the right chunk created?
3. Did metadata filtering exclude the right source?
4. Did ranking surface the wrong evidence?
5. Did synthesis overstate the support?

If you skip directly to prompt changes, you usually hide the real failure source.
