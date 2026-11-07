# Checksums

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

<!-- BEGIN INQUIRY -->
## Try solving this first

A backup job copies a 40 GB database snapshot across the network and reports success. During restore week, one flipped bit makes the archive unreadable. The file existed, the byte count matched, and transport completed. What evidence could have exposed corruption earlier, and why would that evidence still not prove the backup contains the correct business data?
<!-- END INQUIRY -->

## Detecting that data changed

A checksum is a value calculated from data. The receiver can calculate it again and compare the result with the expected value. If they differ, the data is not identical.

Imagine downloading a photo archive. The publisher provides a SHA-256 digest. You calculate the digest of your downloaded file. A mismatch signals that the file differs from the expected bytes, perhaps because of corruption or an incomplete download.

A short network checksum mainly detects accidental errors. A cryptographic hash is designed to make particular collisions or deliberate substitution much harder. These have different strength guarantees.

The expected value must also come from a trusted source. An attacker who can replace both the file and an untrusted digest can make them agree. A digest by itself is not proof of who created a file, and it does not repair corrupted data.

**Check:** if two computed values differ, the files differ. Equal ordinary checksums do not mathematically guarantee that every byte is identical.

## Where this comes into play

Integrity checks are useful for downloaded packages, uploaded files, stored objects, replication, and restored backups. Choose the mechanism for the threat: accidental corruption is different from malicious replacement.

## Worked example: a multi-part upload

Imagine a 1 GB archive uploaded in ten chunks. Each chunk can have its own verified digest so a damaged chunk can be retransmitted without repeating the entire upload. A full-file digest verifies the final assembled byte sequence. Per-chunk checks alone do not establish that the chunks were assembled in the correct order.

Store an expected digest with trustworthy metadata. A checksum that arrives through the same compromised channel as the replacement file may not establish authenticity; authenticated delivery or a verified digital signature addresses a different part of that problem.

## How to improve efficiency without losing the guarantee

Calculate a digest incrementally while streaming bytes rather than loading the whole file into memory. For large uploads, choose chunk sizes that balance retransmission cost, metadata overhead, and parallelism. Verify the final object after assembly when that matches the integrity requirement.

Use a cryptographic digest when resistance to deliberate tampering matters. Do not pick a weak checksum solely because it is faster, and do not treat any checksum as encryption. Verification detects disagreement; it cannot recover the original bytes on its own.

## How to verify improvement

Test one flipped byte, a missing chunk, reordered chunks, and an untrusted expected value. Record memory usage, verification time, and whether the chosen checks detect each relevant failure.

## Optional further reading

- [Additional explanation](https://algomaster.io/learn/system-design/checksums)

Optional references provide more detail; they are not required to follow this lesson.
