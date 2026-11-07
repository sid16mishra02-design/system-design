# TLS and mTLS: protect connections, then authorize the operation

[← Animation index](README.md)

**Problem:** Protect data in transit and verify peers without confusing identity with record-level permission.

**Scenario:** A browser requests an order through a gateway and an internal orders service.

The full system map stays visible as the highlighted path and component states change. Every stage lasts one second and the sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![TLS and mTLS: protect connections, then authorize the operation](../assets/animations/tls-mtls.gif)

## Read the same sequence without motion

1. **Identify the external server.** The browser receives the gateway certificate during TLS setup. HTTPS is HTTP protected by TLS; a certificate helps authenticate the connection peer.
   Verify expected server name; Reject invalid or expired identity.
2. **Use local trust rules.** The browser validates the certificate with its trust configuration. This trust node is local configuration, not a required online CA call for every request.
   Trust chain and hostname matter; Do not bypass validation.
3. **Carry the request securely.** The protected browser connection carries the HTTP order request. TLS protects this hop; terminating it does not automatically protect another internal hop.
   Gateway sees decrypted request; Application identity still matters.
4. **Authenticate internal peers.** The gateway verifies the service; the service verifies the gateway certificate. mTLS authenticates both connection peers under their certificate rules.
   Use supported TLS configurations; Automate certificate renewal.
5. **Authorize the requested item.** The service evaluates the userâ€™s permission to read order 42. An authenticated gateway is not automatic permission for every end-user operation.
   Validate delegated user context; Enforce record-level ownership.
6. **Return the permitted result.** The allowed order response travels over the protected hops. Encryption and authorization solve different parts of the end-to-end problem.
   Protect each intended network hop; Reuse suitable established connections.
7. **Deny another userâ€™s order.** A valid connection requests an order outside the userâ€™s permissions. Valid certificates do not grant unlimited access.
   No forbidden record returned; Preserve authorization when optimizing.
8. **Fail a bad certificate.** A later invalid peer certificate prevents normal protected application traffic. Faster handshakes must not come from disabling verification.
   Monitor certificate expiry; Fix identity configuration safely.

**Design tradeoff:** Connection reuse can reduce handshake work, but verification and operation-level authorization must remain enforced.

[View all states as still images](../assets/animations/tls-mtls-steps.png)

## Related lessons

- [SSL, TLS, mTLS](../curriculum/10-security-and-location/01-ssl-tls-mtls.md)
- [HTTP/HTTPS](../curriculum/02-networking/06-httphttps.md)
