# DNS: lookup, cache, and a server move

[← Animation index](README.md)

**Problem:** Resolve a service name while understanding cached answers during a destination change.

**Scenario:** Illustrative shop.example moves from 203.0.113.8 to 203.0.113.9.

The full system map stays visible as the highlighted path and component states change. Every stage lasts one second and the sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![DNS: lookup, cache, and a server move](../assets/animations/dns-lookup.gif)

## Read the same sequence without motion

1. **A name but no address.** The browser has shop.example but no cached address. Who should it ask, and who owns the answer? Reason about this scenario before comparing the mechanism and its consequences.
   Who follows DNS referrals?; Which server owns the record?; Does DNS deliver the page?.
2. **Start with a referral.** The resolver asks a root server and receives a referral toward the relevant TLD. The root does not fetch the shop page or run the whole lookup.
   Resolver follows iterative referrals.; Root answers which direction to ask..
3. **Find the zone authority.** The TLD response directs the resolver to the zone's authoritative nameservers. Delegation tells the resolver who holds the relevant record.
   TLD is not the shop's web server.; Resolver continues the lookup..
4. **Read the published record.** Authoritative DNS returns 203.0.113.8 and an illustrative 60-second TTL. The TTL limits normal cache reuse; it is not a page-download timer.
   Address and TTL are separate fields.; This TTL is an illustrative value..
5. **Return the answer.** The resolver supplies the address; the browser can now connect to that endpoint. Resolving a name and reaching its server are separate steps.
   DNS carries the address answer.; Connection setup follows resolution..
6. **Retrieve the page.** The browser uses HTTPS with the old web server, which returns the page. DNS servers do not relay the website's response body.
   HTTP response comes from the server.; An open connection can be reused..
7. **Publish a server move.** The operator changes the authoritative answer to .9, but an existing cache still holds .8. Changing the source record does not purge every cached answer.
   Different resolvers may disagree.; Keep old destination through transition..
8. **A cached lookup stays old.** Before expiry, a later lookup can still return .8 and connect to the old endpoint. Short TTLs reduce cache duration; they do not create instant failover.
   No new authority lookup is needed.; Existing connections need separate care..
9. **Refresh after TTL expiry.** After the story's TTL expires, the resolver asks again and learns the new .9 address. Plan changes ahead of time rather than assuming immediate cache replacement.
   Story time jumps past TTL expiry.; Cached delegation can still be reused..
10. **Use the new endpoint.** The browser connects to the new server and receives a page from .9. Measure DNS answers and server reachability independently during a move.
   Check answer and remaining TTL.; Old connections do not teleport..

**Design tradeoff:** Shorter TTLs can reduce stale routing but increase lookups; existing connections do not instantly migrate.

[View all states as still images](../assets/animations/dns-lookup-steps.png)

## Related lessons

- [Domain Name System (DNS)](../curriculum/02-networking/04-domain-name-system-dns.md)
