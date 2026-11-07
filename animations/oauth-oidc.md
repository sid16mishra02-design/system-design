# OAuth / OIDC: code, tokens, and audiences

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![OAuth / OIDC: code, tokens, and audiences](../assets/animations/oauth-oidc.gif)

</details>

## Read the same sequence without motion

1. The browser signs in at the provider; the client does not receive that password.
2. An authorization-code flow returns a code to the client redirect.
3. The client exchanges the code with the required checks, such as PKCE.
4. With OIDC, the client can receive an ID token; an access token targets an API.
5. The API validates the access token and enforces authorization.

[View all states as still images](../assets/animations/oauth-oidc-steps.png)

## Related lessons

- [OAuth 2.0 and OpenID Connect (OIDC)](../curriculum/10-security-and-location/02-oauth-20-and-openid-connect-oidc.md)
