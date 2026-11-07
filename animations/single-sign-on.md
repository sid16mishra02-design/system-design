# SSO: reuse provider login, keep application sessions explicit

[← Animation index](README.md)

**Problem:** Reuse one identity-provider login across applications without assuming one universal session or logout.

**Scenario:** An employee opens payroll and email, then logs out of payroll.

The full system map stays visible as the highlighted path and component states change. Every stage lasts four seconds: the path moves, then the completed state pauses so you can read it. The sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![SSO: reuse provider login, keep application sessions explicit](../assets/animations/single-sign-on.gif)

## Read the same sequence without motion

1. **Open the first application.** Payroll redirects the browser to the trusted identity provider.
   - **Why it matters:** An application relies on an agreed identity protocol, not another appâ€™s password store.
   - **Notice:** App access rules remain local; Validate redirect handling.
2. **Authenticate once.** The employee signs in at the provider and receives a provider session.
   - **Why it matters:** The provider session is separate from application sessions.
   - **Notice:** The provider authenticates U; No payroll password copy needed.
3. **Establish payroll access.** Payroll validates the result and creates its own session.
   - **Why it matters:** Authenticated identity still needs payroll permission.
   - **Notice:** Use stable subject identifiers; Signed-in does not mean admin.
4. **Open another application.** Email redirects through the same provider.
   - **Why it matters:** The provider can recognize its existing session instead of demanding a new password.
   - **Notice:** Provider session reuse is policy-based; Extra authentication may be required.
5. **Create a second app session.** Email validates its result and establishes an independent session.
   - **Why it matters:** One sign-in can produce multiple independent application sessions.
   - **Notice:** Each app controls its own session; Their expiration times may differ.
6. **Log out of payroll only.** Payroll invalidates its session after the employee selects logout.
   - **Why it matters:** Local logout is not universal logout unless that policy is implemented.
   - **Notice:** Provider session can remain active; Email session can remain active.
7. **Email still works.** The browser accesses email using its still-valid email session.
   - **Why it matters:** This follows independent session boundaries, not a failure of SSO.
   - **Notice:** Provider may still be signed in; Payroll may sign in again on reopening.
8. **Design global revocation.** Organization-wide sign-out needs explicit provider and application-session rules.
   - **Why it matters:** Disabling an account does not inherently end every already-established application session immediately.
   - **Notice:** Define revocation propagation; Balance reuse and revocation delay.

**Design tradeoff:** Central sign-in improves reuse, but application permissions, session lifetimes, and global revocation still need coordination.

[View all states as still images](../assets/animations/single-sign-on-steps.png)

## Related lessons

- [Single Sign-On (SSO)](../curriculum/10-security-and-location/03-single-sign-on-sso.md)
