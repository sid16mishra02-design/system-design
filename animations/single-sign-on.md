# SSO: reuse provider login, keep application sessions explicit

[← Animation index](README.md)

**Problem:** Reuse one identity-provider login across applications without assuming one universal session or logout.

**Scenario:** An employee opens payroll and email, then logs out of payroll.

The full system map stays visible as the highlighted path and component states change. Every stage lasts one second and the sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![SSO: reuse provider login, keep application sessions explicit](../assets/animations/single-sign-on.gif)

## Read the same sequence without motion

1. **Open the first application.** Payroll redirects the browser to the trusted identity provider. An application relies on an agreed identity protocol, not another appâ€™s password store.
   App access rules remain local; Validate redirect handling.
2. **Authenticate once.** The employee signs in at the provider and receives a provider session. The provider session is separate from application sessions.
   The provider authenticates U; No payroll password copy needed.
3. **Establish payroll access.** Payroll validates the result and creates its own session. Authenticated identity still needs payroll permission.
   Use stable subject identifiers; Signed-in does not mean admin.
4. **Open another application.** Email redirects through the same provider. The provider can recognize its existing session instead of demanding a new password.
   Provider session reuse is policy-based; Extra authentication may be required.
5. **Create a second app session.** Email validates its result and establishes an independent session. One sign-in can produce multiple independent application sessions.
   Each app controls its own session; Their expiration times may differ.
6. **Log out of payroll only.** Payroll invalidates its session after the employee selects logout. Local logout is not universal logout unless that policy is implemented.
   Provider session can remain active; Email session can remain active.
7. **Email still works.** The browser accesses email using its still-valid email session. This follows independent session boundaries, not a failure of SSO.
   Provider may still be signed in; Payroll may sign in again on reopening.
8. **Design global revocation.** Organization-wide sign-out needs explicit provider and application-session rules. Disabling an account does not inherently end every already-established application session immediately.
   Define revocation propagation; Balance reuse and revocation delay.

**Design tradeoff:** Central sign-in improves reuse, but application permissions, session lifetimes, and global revocation still need coordination.

[View all states as still images](../assets/animations/single-sign-on-steps.png)

## Related lessons

- [Single Sign-On (SSO)](../curriculum/10-security-and-location/03-single-sign-on-sso.md)
