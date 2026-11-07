# Checksums

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## Detecting that data changed

A checksum is a value calculated from data. The receiver can calculate it again and compare the result with the expected value. If they differ, the data is not identical.

Imagine downloading a photo archive. The publisher provides a SHA-256 digest. You calculate the digest of your downloaded file. A mismatch signals that the file differs from the expected bytes, perhaps because of corruption or an incomplete download.

A short network checksum mainly detects accidental errors. A cryptographic hash is designed to make particular collisions or deliberate substitution much harder. These have different strength guarantees.

The expected value must also come from a trusted source. An attacker who can replace both the file and an untrusted digest can make them agree. A digest by itself is not proof of who created a file, and it does not repair corrupted data.

**Check:** if two computed values differ, the files differ. Equal ordinary checksums do not mathematically guarantee that every byte is identical.

## Optional further reading

- [Additional explanation](https://algomaster.io/learn/system-design/checksums)

The lesson above is complete enough for this curriculum; external links are for deeper study.
