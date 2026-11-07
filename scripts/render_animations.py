"""Author and render deterministic instructional animations, not simulations."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import math,json,textwrap,sys,hashlib
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'assets/animations';DEST.mkdir(parents=True,exist_ok=True)
FONT=next((p for p in ['C:/Windows/Fonts/segoeui.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'] if Path(p).exists()),'DejaVuSans.ttf')
BOLD=next((p for p in ['C:/Windows/Fonts/seguisb.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'] if Path(p).exists()),FONT)
def f(size,bold=False):return ImageFont.truetype(BOLD if bold else FONT,size)
INK='#172B46';MUTED='#52647A';BLUE='#1769C2';RED='#BA3442';BG='#F2F6FB';GREEN='#176A50'
W,H=960,600
stories=[]
def S(key,title,nodes,steps,topics,kind='flow'):
    stories.append(dict(id=key,title=title,nodes=[dict(id=k,label=v) for k,v in nodes],steps=[dict(caption=s[0],edge=s[1],updates=s[2],blocked=s[3] if len(s)>3 else False) for s in steps],topics=topics,kind=kind))

S('request-latency','Find the slow part of a request',[('c','Client'),('a','Application'),('d','Database')],[
 ('A request begins. Its response time includes each sequential stage.',('c','a'),{'c':'Waiting','a':'30 ms network'}),
 ('Application work adds 70 ms before the database call.',('a','d'),{'a':'70 ms own work','d':'Query: 100 ms'}),
 ('Sequential total: 30 + 70 + 100 = 200 ms. This is one request latency.',('d','c'),{'c':'Response: 200 ms'}),
 ('A suitable index reduces only the query stage: 100 ms becomes 25 ms.',('a','d'),{'d':'Query: 25 ms'}),
 ('New total: 125 ms. More completed requests per second is a separate measure.',('d','c'),{'c':'Response: 125 ms'})
],['Latency vs Throughput vs Bandwidth','Distributed Tracing'])
S('dns-lookup','DNS: a name becomes an address',[('b','Browser'),('r','Resolver'),('n','Authoritative DNS'),('s','Web server')],[
 ('The browser needs the address for shop.example.',('b','r'),{'b':'shop.example','r':'Cache miss'}),
 ('On a miss, the resolver follows DNS delegation to the responsible server.',('r','n'),{'n':'Address: 203.0.113.8'}),
 ('The resolver returns the address and caches it for its TTL.',('n','r'),{'r':'Cached address + TTL'}),
 ('The browser can now connect to the web server. DNS did not carry the page.',('b','s'),{'s':'Serve HTTP response'}),
 ('A later lookup may use the cached answer until its TTL expires.',('b','r'),{'r':'Cache hit'})
],['Domain Name System (DNS)'])
S('tcp-udp','Lost data: transport choices',[('t','TCP sender'),('r','TCP receiver'),('u','UDP sender'),('v','UDP receiver')],[
 ('TCP presents an ordered byte stream; a lost segment can delay delivery.',('t','r'),{'t':'Bytes 1-3','r':'Bytes 1, then gap'},True),
 ('TCP detects loss and retransmits; later bytes wait for the missing data.',('t','r'),{'r':'Bytes 1, 2, 3 in order'}),
 ('UDP sends datagrams without a built-in delivery or ordering guarantee.',('u','v'),{'u':'Datagrams A, B, C','v':'A arrives; B lost'},True),
 ('Datagram C can arrive without transport waiting for B.',('u','v'),{'v':'A and C available'}),
 ('The UDP application chooses whether to recover, ignore, or reorder data.',None,{'v':'Application policy'})
],['TCP and UDP'])
S('load-balancer','Scale a service without losing sessions',[('c','Client'),('l','Load balancer'),('a','App A'),('b','App B'),('s','Shared session store')],[
 ('The client sends a request to the service entry point.',('c','l'),{'c':'Request 1','l':'Select healthy instance'}),
 ('The load balancer routes the first request to App A.',('l','a'),{'a':'Handle request 1'}),
 ('App A keeps session state outside its own process.',('a','s'),{'s':'Session for user 7'}),
 ('A later request can be routed to App B.',('l','b'),{'b':'Handle request 2'}),
 ('App B retrieves the session instead of relying on App A memory.',('b','s'),{'b':'Same session available'}),
 ('More app instances do not remove shared-store bottlenecks or failures.',None,{'s':'Shared dependency'})
],['Scalability','Load Balancing','Clustering'])
S('cache-aside','Cache-aside: hit, miss, and update',[('a','Application'),('c','Cache'),('d','Database')],[
 ('The application checks the cache for product 42.',('a','c'),{'c':'Missing','d':'Price: 500'}),
 ('On a miss, the application reads the authoritative database.',('a','d'),{'a':'Loaded price: 500'}),
 ('The application fills the cache for later reads.',('a','c'),{'c':'Price: 500'}),
 ('A write changes the database to 550; the cached copy is now old.',('a','d'),{'d':'Price: 550','c':'Price: 500 (stale)'}),
 ('Invalidate the old entry, then reload on a later miss. Races still need a policy.',('a','c'),{'c':'Invalidated'})
],['Caching','Caching Strategies','Distributed Caching'])
S('replication','Replication is copying, not partitioning',[('w','Writer'),('p','Primary'),('r','Replica'),('c','Reader')],[
 ('Both copies initially show address V1.',None,{'p':'Address V1','r':'Address V1'}),
 ('A write commits V2 on the primary.',('w','p'),{'p':'Address V2','r':'Address V1'}),
 ('Before replication applies, a replica read can still return V1.',('c','r'),{'c':'Reads older V1'}),
 ('The replication stream applies the update on the replica.',('p','r'),{'r':'Address V2'}),
 ('Both now show V2. Deletions can replicate too; replication is not a backup.',('c','r'),{'c':'Reads V2'})
],['Database Replication','SQL vs NoSQL databases'])
S('atomic-stock','Two buyers, one remaining ticket',[('a','Buyer A'),('b','Buyer B'),('d','Stock row')],[
 ('There is one unit of product 42. Both buyers want it.',None,{'d':'product 42: quantity 1'}),
 ('A performs an atomic update WHERE product_id = 42 AND quantity > 0.',('a','d'),{'d':'quantity 0','a':'1 row changed'}),
 ('B executes the same conditional update after A.',('b','d'),{'b':'0 rows changed'}),
 ('Only A may confirm a reservation from these results.',('d','a'),{'a':'Reserved','b':'Not reserved'}),
 ('Related changes need a suitable transaction; external payment is another boundary.',None,{'d':'Preserve the invariant'})
],['Transactions','ACID and BASE consistency models'])
S('normalization','An address update and duplicated data',[('c','Customer record'),('o','Current-order view'),('h','Historical order')],[
 ('A normalized current view refers to the customer rather than copying every field.',('o','c'),{'c':'Current address: A','o':'Customer ID: 7'}),
 ('An order can also retain the delivery address used at purchase time.',('c','h'),{'h':'Purchase snapshot: A'}),
 ('The customer changes their current address to B.',None,{'c':'Current address: B'}),
 ('A live join sees B; the past delivery snapshot should still show A.',('o','c'),{'o':'Joined current: B','h':'Purchase snapshot: A'}),
 ('Choose duplication by meaning and access pattern, not a universal rule.',None,{'h':'History remains intact'})
],['Normalization and Denormalization'])
S('sharding','Sharding divides ownership of data',[('r','Router'),('a','Shard A'),('b','Shard B'),('ar','Replica of A')],[
 ('Choose a shard from the customer identifier.',None,{'a':'Customers 1-1000','b':'Customers 1001-2000'}),
 ('Customer 42 is routed to A.',('r','a'),{'a':'Owns customer 42'}),
 ('Customer 1500 is routed to B, not to a duplicate of A.',('r','b'),{'b':'Owns customer 1500'}),
 ('A replica of A copies A data, not B data.',('a','ar'),{'ar':'Copy of customers 1-1000'}),
 ('A query across both customer ranges needs deliberate coordination.',None,{'r':'Cross-shard query cost'})
],['Sharding','Database Federation'])
S('consistent-hash','Consistent hashing: a node joins',[('a','Node A'),('b','Node B'),('c','Node C'),('d','New node D')],[
 ('Keys go clockwise to the next node. Key K at 170 maps to C at 260.',None,{'a':'20 degrees','b':'140 degrees','c':'260 degrees','d':'Not yet a member'}),
 ('K is owned by C before the new node joins.',('b','c'),{'c':'Owns key K'}),
 ('D joins at 200 degrees, between B and C.',None,{'d':'200 degrees: joined'}),
 ('K at 170 now meets D first. Move the affected range from C to D.',('c','d'),{'d':'Now owns key K','c':'Other ranges remain'}),
 ('A key at 80 still maps to B. Not every key needs to move.',None,{'b':'Key at 80 unchanged'})
],['Consistent Hashing'],kind='ring')
S('bloom-filter','Bloom filter: no, or maybe',[('q','Lookup'),('f','Bloom filter'),('s','Authoritative store')],[
 ('Insert A with illustrative hash positions 1, 4, and 8.',('q','f'),{'f':'Set bits 1, 4, 8'}),
 ('A query needing bit 2 finds zero: definitely absent from the represented set.',('q','f'),{'q':'Needs bits 2, 6, 10','f':'Bit 2 is zero'}),
 ('A different key X can map to bits 1, 4, and 8 too.',('q','f'),{'q':'X needs bits 1, 4, 8','f':'All set: MAYBE'}),
 ('Verify a positive result in real storage; a collision can mean X is absent.',('q','s'),{'s':'X does not exist'}),
 ('The filter saves absent-key reads, but is not the final membership authority.',None,{'f':'No / maybe; not yes'})
],['Bloom Filters'],kind='bloom')
S('cap-partition','CAP: a choice during a partition',[('a','Replica A'),('n','Network link'),('b','Replica B'),('r','Client at B')],[
 ('Both replicas initially know that a ticket is available.',None,{'a':'Available','b':'Available','n':'Connected'}),
 ('A records sold, then communication to B is unavailable.',('a','b'),{'a':'Sold','b':'Last known: available','n':'PARTITION'},True),
 ('A request reaches non-failing B, which cannot confirm the current state at A.',('r','b'),{'r':'Is the ticket available?'}),
 ('Choice 1: answer without the latest write; consistency may be sacrificed.',('b','r'),{'r':'Potentially stale answer'}),
 ('Choice 2: refuse or wait; CAP availability is sacrificed for this request.',('b','r'),{'r':'Cannot confirm now'})
],['CAP Theorem'])
S('pacelc','PACELC: normal operation also matters',[('c','Client'),('a','Local replica'),('b','Distant replica')],[
 ('Normal operation: waiting for distant coordination can cost latency.',('a','b'),{'a':'Write pending','b':'Round-trip wait'}),
 ('Coordinated completion can provide the chosen stronger guarantee.',('b','a'),{'a':'Acknowledge after rule'}),
 ('An asynchronous path can respond sooner while the remote copy lags.',('a','c'),{'c':'Earlier acknowledgement','b':'Older state possible'}),
 ('During a partition, availability versus consistency becomes a separate choice.',('a','b'),{'a':'Partition policy','b':'Unreachable'},True)
],['PACELC Theorem'])
S('saga','A saga compensates a completed step',[('o','Order service'),('p','Payment service'),('s','Stock service'),('j','Recovery state')],[
 ('Record a pending order and a recoverable step identifier.',('o','j'),{'o':'Pending','j':'Saga started'}),
 ('A local payment operation commits successfully.',('o','p'),{'p':'Charged once'}),
 ('Stock reservation fails. Earlier committed work did not vanish.',('o','s'),{'s':'Reservation failed'},True),
 ('The saga issues a compensating refund with safe retry behavior.',('o','p'),{'p':'Refund requested'}),
 ('Record completion after confirmation; compensation can take time or fail too.',('o','j'),{'j':'Compensation tracked'})
],['Distributed Transactions'])
S('cache-eviction','LRU and FIFO make different choices',[('i','Access sequence'),('l','LRU cache'),('f','FIFO cache')],[
 ('Insert A, B, and C into caches with room for three equal-size entries.',None,{'l':'Oldest: A, B, C','f':'Oldest: A, B, C'}),
 ('Read A. LRU updates recency; FIFO keeps insertion order.',('i','l'),{'l':'Oldest: B, C, A','f':'Oldest: A, B, C'}),
 ('Insert D. LRU evicts B, the least recently used entry.',('i','l'),{'l':'C, A, D; B evicted'}),
 ('FIFO evicts A, the earliest inserted entry.',('i','f'),{'f':'B, C, D; A evicted'}),
 ('Eviction frees memory. It does not establish that a cached price is current.',None,{'i':'Freshness is separate'})
],['Cache Eviction Policies'])
S('idempotency','A lost response must not mean two charges',[('c','Client'),('a','Payment API'),('d','Durable operation record')],[
 ('The client sends one payment attempt with idempotency key K.',('c','a'),{'c':'Attempt K','a':'Validate request'}),
 ('Atomically associate K with one payment operation and its recoverable result.',('a','d'),{'d':'K -> one operation'}),
 ('The response is lost after the operation succeeds.',('a','c'),{'d':'K -> succeeded'},True),
 ('The client retries using K and the same request body.',('c','a'),{'a':'Same logical attempt'}),
 ('Return or resume the recorded result, rather than create a second charge.',('d','a'),{'a':'Reuse result for K'})
],['Idempotency','Webhooks'])
S('token-bucket','Token bucket: bursts have a limit',[('c','Incoming requests'),('b','Token bucket'),('s','Service')],[
 ('This illustrative bucket holds three tokens and refills at one token/second.',None,{'b':'Tokens: 3'}),
 ('Request 1 consumes a token and is allowed.',('c','s'),{'b':'Tokens: 2'}),
 ('Two more requests consume the remaining tokens.',('c','s'),{'b':'Tokens: 0'}),
 ('A new immediate request is rejected or delayed by the chosen policy.',('c','b'),{'c':'No token available'},True),
 ('After one second, one token is available again, up to the bucket capacity.',('b','s'),{'b':'One token refilled'})
],['Rate Limiting'])
S('realtime-protocols','Which way do live updates travel?',[('c','Browser'),('s','Server')],[
 ('Long polling: browser sends a request; the server may hold its response.',('c','s'),{'c':'Waiting request','s':'Response held'}),
 ('A response arrives; the browser starts another request for later updates.',('s','c'),{'c':'Issue next long poll'}),
 ('Separate SSE example: server events arrive over a streaming HTTP response.',('s','c'),{'s':'HTTP event stream','c':'Receives one-way events'}),
 ('Separate WebSocket example: after setup, the browser can send a message.',('c','s'),{'c':'Two-way channel','s':'WebSocket ready'}),
 ('The server can send messages back on the same WebSocket connection.',('s','c'),{'s':'Two-way channel'})
],['Long polling, WebSockets, Server-Sent Events (SSE)'])
S('work-queue','A work queue can redeliver a job',[('p','Producer'),('q','Work queue'),('a','Worker A'),('b','Worker B')],[
 ('One logical job enters a queue shared by competing workers.',('p','q'),{'q':'Job J waiting'}),
 ('Worker A receives J and writes the result.',('q','a'),{'a':'Result written'}),
 ('A crashes before acknowledging. The queue may redeliver J.',('a','q'),{'q':'J available again'},True),
 ('Worker B receives J and checks the durable result or deduplication rule.',('q','b'),{'b':'Recognize repeated J'}),
 ('Safe repeated processing avoids a duplicate business effect.',('b','q'),{'q':'J acknowledged'})
],['Message Brokers','Message Queues'])
S('pub-sub','Independent subscribers need their own copy',[('p','Order publisher'),('t','Topic / broker'),('b','Billing subscription'),('s','Shipping subscription')],[
 ('Publish OrderPlaced once to a topic.',('p','t'),{'t':'Event E'}),
 ('The billing subscription receives its own logical delivery.',('t','b'),{'b':'Bill order'}),
 ('The shipping subscription receives its own logical delivery.',('t','s'),{'s':'Prepare shipment'}),
 ('Workers within one subscription may compete; independent subscriptions do not.',None,{'b':'Own progress / retry','s':'Own progress / retry'}),
 ('Timing and delivery guarantees depend on the broker and configuration.',None,{'t':'Push or pull varies'})
],['Publish-Subscribe','Event-Driven Architecture (EDA)','Enterprise Service Bus (ESB)'])
S('cdc','CDC: a committed change reaches a read view',[('d','Source database'),('c','CDC connector'),('q','Change stream'),('s','Search index')],[
 ('A database transaction commits a product price change.',None,{'d':'Product 42: price 550'}),
 ('The connector reads the corresponding durable-log position.',('d','c'),{'c':'Read committed change'}),
 ('A change record reaches the stream; downstream work can lag.',('c','q'),{'q':'Change E waiting','s':'Old price 500'}),
 ('The consumer applies the change using an appropriate id/version rule.',('q','s'),{'s':'Price 550'}),
 ('Recovery may replay records. Consumers must handle duplicates safely.',('q','s'),{'s':'Repeat E: safe update'})
],['Change Data Capture (CDC)'])
S('event-sourcing','Event sourcing: replay builds state',[('c','Commands'),('l','Event history'),('v','Account view')],[
 ('Append Deposited(100) to the durable event history.',('c','l'),{'l':'Deposited 100'}),
 ('Apply the event to the derived balance.',('l','v'),{'v':'Balance 100'}),
 ('Append Withdrawn(30), then update the view.',('c','l'),{'l':'Deposit 100; withdraw 30'}),
 ('The current balance is 70.',('l','v'),{'v':'Balance 70'}),
 ('Replay rebuilds the view; avoid repeating external side effects such as email.',('l','v'),{'v':'Rebuilt balance 70'})
],['Event Sourcing'])
S('cqrs','CQRS: a read view can lag behind a write',[('c','Create-order command'),('w','Write model'),('e','Update event'),('r','Order-list view')],[
 ('A command creates order 42 in the write model.',('c','w'),{'w':'Order 42 committed'}),
 ('An update event waits for processing.',('w','e'),{'e':'Update queued','r':'Order 42 not yet shown'}),
 ('A list read can temporarily show the old view.',None,{'r':'Read view is behind'}),
 ('The projector applies the update to the read view.',('e','r'),{'r':'Order 42 now listed'}),
 ('CQRS separates read and write responsibilities; event sourcing is optional.',None,{'w':'Write responsibility','r':'Read responsibility'})
],['Command and Query Responsibility Segregation (CQRS)'])
S('circuit-breaker','Circuit breaker: closed, open, half-open',[('a','Caller'),('b','Circuit breaker'),('s','Slow dependency')],[
 ('Closed: calls reach the dependency and failures are measured.',('a','s'),{'b':'CLOSED','s':'Repeated failures'}),
 ('The configured failure rule opens the circuit.',('a','b'),{'b':'OPEN: reject fast'},True),
 ('During the open interval, new calls use a safe fallback or fail explicitly.',('a','b'),{'a':'No unsafe success claim'},True),
 ('After a delay, half-open allows limited probe calls.',('b','s'),{'b':'HALF-OPEN: probes'}),
 ('Successful probes can close it; failing probes can open it again.',('s','b'),{'b':'CLOSED after success'})
],['Circuit breaker'])
S('discovery-heartbeat','Discovery data can become stale',[('c','Caller'),('r','Service registry'),('a','Orders instance A'),('b','Orders instance B')],[
 ('A and B register reachable endpoints; health information is refreshed.',('a','r'),{'r':'A and B registered'}),
 ('The caller discovers candidate orders endpoints.',('c','r'),{'c':'Candidates: A, B'}),
 ('A fails after discovery; a previously returned endpoint can now be stale.',('c','a'),{'a':'Unavailable'},True),
 ('A health timeout marks A suspect; the registry can stop advertising it.',('r','a'),{'r':'A suspect; B remains'},True),
 ('A retry to B must respect the operation retry/idempotency policy.',('c','b'),{'b':'Handle safe retry'})
],['Service Discovery','HeartBeats'])
S('recovery-objectives','Recovery time and data-loss targets differ',[('b','Last backup'),('f','Failure'),('r','Restore'),('s','Service restored')],[
 ('A recoverable backup exists at 10:00.',None,{'b':'Data through 10:00'}),
 ('The service fails at 10:20; newer data may need another recoverable log.',('b','f'),{'f':'Failure at 10:20'}),
 ('Without newer recoverable data, this scenario loses up to 20 minutes.',None,{'b':'Recovery point: 10:00'}),
 ('Restore and validation take until 11:00.',('f','r'),{'r':'Restore + validate'}),
 ('Observed recovery took 40 minutes. RPO/RTO are targets, not these observations.',('r','s'),{'s':'Available at 11:00'})
],['Disaster recovery','SLA, SLO, SLI'])
S('oauth-oidc','OAuth / OIDC: code, tokens, and audiences',[('u','User browser'),('a','Client application'),('i','Identity provider'),('p','Protected API')],[
 ('The browser signs in at the provider; the client does not receive that password.',('u','i'),{'i':'User authentication'}),
 ('An authorization-code flow returns a code to the client redirect.',('i','a'),{'a':'Authorization code'}),
 ('The client exchanges the code with the required checks, such as PKCE.',('a','i'),{'i':'Validate exchange'}),
 ('With OIDC, the client can receive an ID token; an access token targets an API.',('i','a'),{'a':'ID token / access token'}),
 ('The API validates the access token and enforces authorization.',('a','p'),{'p':'Check access + ownership'})
],['OAuth 2.0 and OpenID Connect (OIDC)'])
S('single-sign-on','SSO does not mean one universal app session',[('u','Browser'),('i','Identity provider'),('a','Payroll app'),('b','Email app')],[
 ('The user authenticates at the identity provider.',('u','i'),{'i':'Provider session exists'}),
 ('Payroll establishes its own application session using the sign-in result.',('i','a'),{'a':'Payroll session'}),
 ('Email can reuse the provider session for sign-in, then create its own session.',('i','b'),{'b':'Email session'}),
 ('Logging out of payroll may end only the payroll session.',('u','a'),{'a':'Logged out','b':'Still signed in'}),
 ('Global logout needs an explicit plan for provider and application sessions.',None,{'i':'Separate logout policy'})
],['Single Sign-On (SSO)'])
S('tls-mtls','TLS identity is separate from authorization',[('c','Client'),('s','Server'),('z','Authorization rules')],[
 ('During TLS setup, the client validates the server certificate and identity.',('s','c'),{'c':'Verify server identity'}),
 ('The protected connection carries application traffic.',('c','s'),{'s':'Encrypted in transit'}),
 ('With mTLS, the server also validates a client certificate.',('c','s'),{'s':'Verify client identity'}),
 ('An authenticated client still needs permission for the requested operation.',('s','z'),{'z':'May this user read order 42?'}),
 ('Valid identity does not grant unlimited access to every record.',('z','s'),{'s':'Enforce operation policy'})
],['SSL, TLS, mTLS','HTTP/HTTPS'])
S('nearby-search','Nearby search must cross cell boundaries',[('u','Rider'),('a','Cell A'),('b','Neighbor cell B'),('d','Nearby driver')],[
 ('A rider is close to the edge of cell A.',None,{'u':'Near boundary','a':'Rider cell'}),
 ('The nearest driver is across the boundary in cell B.',None,{'b':'Adjacent cell','d':'Close, but in B'}),
 ('Searching only A misses that driver.',('u','a'),{'a':'No matching driver'}),
 ('Search intersecting neighbor cells, then filter by actual distance.',('u','b'),{'b':'Candidate driver found'}),
 ('Grid prefixes and quadtrees are candidate indexes, not exact distance tests.',('b','d'),{'d':'Validate distance + availability'})
],['Geohashing and Quadtrees'],kind='grid')
S('raft-majority','Raft: minority isolation stops safe progress',[('a','Voter A'),('b','Voter B'),('c','Voter C')],[
 ('A is leader in this illustrative three-voter crash-fault group.',None,{'a':'Leader: term 1','b':'Follower','c':'Follower'}),
 ('Raft replicates and commits entries using its log, term, and majority rules.',('a','b'),{'a':'Entry X committed','b':'Entry X stored'}),
 ('A becomes isolated. A alone cannot commit conflicting new decisions.',('a','c'),{'a':'Isolated minority'},True),
 ('B and C can elect a leader when protocol and timing conditions permit.',('b','c'),{'b':'Leader: later term','c':'Majority participant'}),
 ('Only the communicating majority can progress under the protocol rules.',('b','c'),{'b':'Commit rule enforced'})
],['Consensus Algorithms'])
S('fencing-token','Lease expiry does not stop the old worker',[('a','Worker A'),('b','Worker B'),('l','Lease authority'),('s','Protected store')],[
 ('A receives ownership token 10, then pauses.',('l','a'),{'a':'Token 10; paused'}),
 ('A lease expires; B acquires a newer token 11.',('l','b'),{'b':'Token 11'}),
 ('The store accepts B and records the newer fencing token.',('b','s'),{'s':'Newest accepted: 11'}),
 ('A resumes and sends a stale write carrying token 10.',('a','s'),{'a':'Old worker resumed'},True),
 ('The store rejects 10 because it enforces fencing. Issuing tokens alone is not enough.',('s','a'),{'a':'Stale write rejected'})
],['Distributed Locking'])
S('gossip-spread','Gossip spreads knowledge gradually',[('a','Node A'),('b','Node B'),('c','Node C'),('d','Node D')],[
 ('A learns a new membership observation, version V2.',None,{'a':'Knows V2','b':'Knows V1','c':'Knows V1','d':'Knows V1'}),
 ('A exchanges information with B.',('a','b'),{'b':'Knows V2'}),
 ('B later exchanges with C; D may still have old information.',('b','c'),{'c':'Knows V2'}),
 ('A reachable peer exchange eventually reaches D under convergence assumptions.',('c','d'),{'d':'Knows V2'}),
 ('Spreading observations is not consensus on one committed transaction history.',None,{'a':'Temporary disagreement allowed'})
],['Gossip Protocol'])

S('availability-failover','A replacement helps only if traffic reaches it',[('u','User'),('r','Request router'),('a','App A'),('b','App B')],[
 ('Two app instances can handle the same request contract.',None,{'a':'Healthy','b':'Healthy standby'}),
 ('The router initially selects A.',('r','a'),{'a':'Handles request'}),
 ('A stops responding. A second box alone does not redirect traffic.',('r','a'),{'a':'Unavailable'},True),
 ('A configured health and routing policy switches suitable traffic to B.',('r','b'),{'b':'Handles new requests'}),
 ('Test shared dependencies too. Both apps can fail if their common database fails.',('b','u'),{'u':'Response restored'})
],['Availability'])
S('index-lookup','An index narrows the records to examine',[('q','Query'),('t','Table rows'),('i','Customer-ID index'),('r','Matching rows')],[
 ('Find orders for customer 7 in a hypothetical table with one million rows.',None,{'q':'WHERE customer_id = 7','t':'1,000,000 orders'}),
 ('Without a useful access path, the engine may inspect the full table.',('q','t'),{'t':'Scan many rows'}),
 ('A suitable index maps customer 7 to candidate records.',('q','i'),{'i':'7 -> row IDs 12, 81, 99'}),
 ('Read or validate the matching records as required by the execution plan.',('i','r'),{'r':'3 candidate records'}),
 ('The index costs storage and write maintenance; measure the actual query plan.',None,{'i':'Maintain on writes'})
],['Indexes'])
S('cdn-edge','CDN: origin miss, then nearby reuse',[('u','Viewer'),('e','Nearby CDN edge'),('o','Origin server')],[
 ('A viewer requests a public video segment from the nearby edge.',('u','e'),{'e':'Segment not cached'}),
 ('On a miss, the edge obtains the allowed content from the origin.',('e','o'),{'o':'Public segment V1'}),
 ('The edge stores the response according to its caching policy.',('o','e'),{'e':'Cached segment V1'}),
 ('A later viewer request can be served without another origin fetch.',('e','u'),{'u':'Nearby cached response'}),
 ('Versions, expiry, and access rules still matter. Private files need protection.',None,{'e':'Freshness + access policy'})
],['Content Delivery Network (CDN)'])
S('p2p-pieces','Peers share verified pieces and may leave',[('o','File origin'),('a','Peer A'),('b','Peer B'),('c','Peer C')],[
 ('A trusted file description identifies the pieces and their expected digests.',('o','a'),{'a':'Pieces 1, 2','b':'Piece 3','c':'No pieces yet'}),
 ('C downloads a useful piece from A and verifies it.',('a','c'),{'c':'Verified piece 1'}),
 ('C obtains another useful piece from B.',('b','c'),{'c':'Verified pieces 1, 3'}),
 ('A leaves before sending piece 2. Discovery must locate another source.',('a','c'),{'a':'Disconnected','c':'Still needs piece 2'},True),
 ('Peers reduce origin traffic only when useful sources remain reachable.',('o','c'),{'c':'Fallback source for piece 2'})
],['Peer-to-Peer (P2P) Architecture'])

# One concrete reliability example is the combination of safe retries and recovery.
for story in stories:
    if story['id'] in ['idempotency','saga']:story['topics'].append('Reliability')
    if story['id']=='pub-sub':story['topics'].remove('Enterprise Service Bus (ESB)')
    if story['id']=='replication':story['topics'].remove('SQL vs NoSQL databases')
    if story['id']=='recovery-objectives':story['topics'].remove('SLA, SLO, SLI')

S('case-url-shortener','Design example: create and resolve a short URL',[('c','Client'),('a','Short-link service'),('d','Mapping database'),('k','Lookup cache'),('t','Destination site')],[
 ('Creation: validate the destination and allocate a short key with a collision policy.',('c','a'),{'c':'Create short link','a':'Allocate key K'}),
 ('Persist K -> destination under a uniqueness rule before confirming creation.',('a','d'),{'d':'K -> destination saved'}),
 ('Resolution: a later request for K checks the fast lookup cache.',('a','k'),{'k':'Miss for K'}),
 ('On a miss, retrieve the mapping and fill the cache using a freshness policy.',('d','k'),{'k':'K -> destination cached'}),
 ('The service returns an HTTP redirect; the client requests the destination.',('c','t'),{'c':'Follow validated redirect','t':'Serve destination'}),
 ('Later cache hits reduce mapping reads; expiry, deletion, and abuse still need policies.',('k','a'),{'a':'Resolve hit for K'})
],['URL Shortener'])
S('case-whatsapp','Design example: accepted is not yet delivered',[('s','Sender'),('a','Chat service'),('d','Message store'),('q','Delivery work'),('r','Recipient')],[
 ('The sender submits one logical message using a stable message identifier.',('s','a'),{'s':'Message M42'}),
 ('Persist the message and recovery state before promising durable acceptance.',('a','d'),{'d':'M42 persisted'}),
 ('Acknowledge acceptance, which is different from recipient delivery.',('a','s'),{'s':'Accepted by service'}),
 ('Use a recoverable handoff for delivery work; do not lose work between stores.',('d','q'),{'q':'Deliver M42'}),
 ('An online recipient receives M42; offline clients need later retrieval.',('q','r'),{'r':'M42 received'}),
 ('A retry or reconnect can repeat M42. Deduplicate at the durable/client boundary.',('q','r'),{'r':'Repeated M42 recognized'})
],['WhatsApp'])
S('case-twitter','Design example: fanout makes feeds fast, at a cost',[('w','Post writer'),('p','Post store'),('q','Fanout work'),('t','Follower timelines'),('a','Feed service'),('r','Feed reader')],[
 ('Persist a new post with its author and stable identifier.',('w','p'),{'p':'Post P recorded'}),
 ('Schedule recoverable fanout work rather than blocking on every follower.',('p','q'),{'q':'Distribute references to P'}),
 ('Fanout updates follower timelines, which can temporarily lag.',('q','t'),{'t':'Post references ready'}),
 ('A reader asks the feed service for a bounded page.',('r','a'),{'r':'Read next feed page'}),
 ('Read prepared timeline references, then retrieve authorized post content.',('a','t'),{'a':'Serve prepared page'}),
 ('Very large authors may need another fanout policy; a hybrid trades write work for read work.',('p','a'),{'a':'Merge selected read-time posts'})
],['Twitter'])
S('case-netflix','Design example: prepare video, then serve nearby',[('s','Object storage'),('e','Encoding work'),('o','Origin service'),('c','CDN edge'),('v','Viewer')],[
 ('An uploaded video is kept in durable object storage.',None,{'s':'Original video stored'}),
 ('Encoding work creates suitable versions and segments; retries must be safe.',('s','e'),{'e':'Encode versions'}),
 ('Prepared segments become available to the origin delivery path.',('e','o'),{'o':'Versioned segments ready'}),
 ('A viewer requests a segment from the CDN edge.',('v','c'),{'c':'Segment miss'}),
 ('On a miss, the edge fetches allowed content from the origin.',('o','c'),{'c':'Segment cached'}),
 ('Nearby reuse reduces origin delivery load; cold caches and access control still matter.',('c','v'),{'v':'Play segment'})
],['Netflix'])
S('case-uber','Design example: near a rider does not mean available',[('r','Rider'),('a','Dispatch service'),('g','Location index'),('s','Assignment store'),('d','Driver')],[
 ('The rider requests a trip with a pickup location.',('r','a'),{'a':'Find nearby candidates'}),
 ('Search intersecting spatial cells and filter by actual distance and freshness.',('a','g'),{'g':'Candidate driver D'}),
 ('Check current availability and conditionally claim the driver.',('a','s'),{'s':'D claimed for trip T'}),
 ('Notify the selected driver and track acceptance or timeout.',('a','d'),{'d':'Trip offer T'}),
 ('Another request must not also claim D. Stale location data is not an assignment guarantee.',('r','s'),{'s':'Conflicting claim rejected'}),
 ('Expired offers need an explicit release/retry policy before another assignment.',('a','s'),{'s':'Transition by trip state'})
],['Uber'])

S('concurrency-parallelism','Interleaving is different from simultaneous execution',[('q','Tasks'),('s','One execution unit'),('a','Execution unit A'),('b','Execution unit B')],[
 ('One execution unit starts A. Both tasks need two model time units of CPU work.',None,{}),
 ('The same execution unit switches to B. Task lifetimes overlap, but work is interleaved.',None,{}),
 ('It resumes A, which finishes after its second unit of work.',None,{}),
 ('It resumes B. Both tasks finish after four model time units.',None,{}),
 ('Separate alternative: two available execution units run A and B at the same time.',None,{}),
 ('Both finish after two model units in this idealized CPU-only example.',None,{})
],['Concurrency vs parallelism','Latency vs throughput'],kind='workers')
S('batch-stream','Batch and streaming organize the same arrivals differently',[('e','Incoming records'),('b','Batch buffer'),('w','Batch processor'),('s','Stream processor')],[
 ('Compare two alternatives for the same arriving records.',None,{'b':'Empty','s':'Waiting for arrivals'}),
 ('E1 waits for a batch boundary; a streaming path can begin E1 now.',('e','b'),{'b':'E1 waiting','s':'Process E1'}),
 ('E2 joins the buffer; the streaming path can handle it as it arrives.',('e','s'),{'b':'E1, E2 waiting','s':'Process E2'}),
 ('At its boundary, the batch processor receives the accumulated group.',('b','w'),{'w':'Process E1 + E2'}),
 ('Batching amortizes overhead but adds waiting. Streaming still has processing delay.',None,{'b':'Start next batch','s':'Continue processing'})
],['Batch vs stream processing'])
S('read-write-through','Read-through and write-through can be combined',[('a','Application'),('c','Cache layer'),('d','Backing database')],[
 ('Read-through: the application asks the cache layer for a missing value.',('a','c'),{'c':'Read miss'}),
 ('The cache layer loads it from the backing database.',('c','d'),{'d':'Authoritative value V1'}),
 ('The layer caches V1 and returns it to the application.',('d','c'),{'c':'Cache contains V1'}),
 ('Write-through: the application sends a new value through that layer.',('a','c'),{'c':'Write V2 pending'}),
 ('The layer synchronously persists the write according to its write policy.',('c','d'),{'d':'Persisted V2'}),
 ('After the required writes succeed, acknowledge. Failure ordering still needs a policy.',('c','a'),{'c':'Cache V2','a':'Write acknowledged'})
],['Read-through vs write-through cache'])
S('push-pull','Who initiates the update: sender or receiver?',[('p','Provider: push'),('r','Push receiver'),('q','Polling receiver'),('s','Provider: pull')],[
 ('Both alternatives begin with the receiver knowing version V1.',None,{'p':'Current V1','r':'Knows V1','q':'Knows V1','s':'Current V1'}),
 ('The provider records V2 and initiates a push notification.',('p','r'),{'p':'Current V2','r':'Receives V2','s':'Current V2'}),
 ('The polling receiver can remain on V1 until its next check.',None,{'q':'Still knows V1'}),
 ('The polling receiver initiates a request asking for updates.',('q','s'),{'q':'Request latest version'}),
 ('The pull response now supplies V2. Poll interval and retry behavior affect delay.',('s','q'),{'q':'Receives V2'})
],['Push vs pull'])
S('sync-async','An order response can precede email completion',[('c','Client'),('a','Order API'),('d','Order database'),('q','Delivery queue'),('w','Email worker')],[
 ('A client submits an order request.',('c','a'),{'a':'Validate order'}),
 ('Persist the order and recoverable email work record under the required atomic rule.',('a','d'),{'d':'Order + work saved'}),
 ('Asynchronous choice: acknowledge order creation, not email completion.',('a','c'),{'c':'Order created'}),
 ('A recoverable handoff queues email work.',('d','q'),{'q':'Email work waiting'}),
 ('The worker can finish the email later and must tolerate retries.',('q','w'),{'w':'Email processed'}),
 ('Separate synchronous choice: the caller waits for required downstream work.',('a','w'),{'a':'Waiting for email result'}),
 ('That response is delayed by the downstream result and its failure behavior.',('a','c'),{'c':'Later synchronous response'})
],['Synchronous vs asynchronous communication'])

# Related comparison labels must survive asset regeneration.
aliases={'request-latency':['Latency vs throughput'],'load-balancer':['Stateful vs stateless design'],'realtime-protocols':['Long polling vs WebSockets'],'replication':['Strong vs eventual consistency'],'cap-partition':['Strong vs eventual consistency']}
for story in stories:
    for label in aliases.get(story['id'],[]):
        if label not in story['topics']:story['topics'].append(label)

# Renderer: text stays readable; each state has a hold as well as moving data.
def wrapped(draw,text,font,width):
    lines=[];line=''
    for word in text.split():
        trial=(line+' '+word).strip()
        if draw.textlength(trial,font=font)>width and line:lines.append(line);line=word
        else:line=trial
    if line:lines.append(line)
    return lines

def textblock(draw,xy,text,font,width,fill=INK,lineheight=27,maxlines=4):
    lines=wrapped(draw,text,font,width)
    assert len(lines)<=maxlines,(text,lines)
    for i,line in enumerate(lines):draw.text((xy[0],xy[1]+lineheight*i),line,font=font,fill=fill)
    return len(lines)*lineheight

def positions(n):
    if n==2:return [(250,250),(710,250)]
    if n==3:return [(170,250),(480,250),(790,250)]
    if n==4:return [(210,190),(750,190),(210,355),(750,355)]
    if n==5:return [(160,190),(480,190),(800,190),(320,355),(640,355)]
    if n==6:return [(160,190),(480,190),(800,190),(160,355),(480,355),(800,355)]
    raise ValueError(n)

def path_points(a,b):
    dx=b[0]-a[0];dy=b[1]-a[1]
    t=min(104/abs(dx) if dx else 1e9,53/abs(dy) if dy else 1e9)
    return (a[0]+dx*t,a[1]+dy*t),(b[0]-dx*t,b[1]-dy*t)

def frame(story,step_i,phase,previous,updated):
    im=Image.new('RGB',(W,H),BG);d=ImageDraw.Draw(im)
    d.rectangle((0,0,W,106),fill=INK)
    textblock(d,(30,18),story['title'],f(29,True),885,'white',34,2)
    d.text((32,114),f'STEP {step_i+1} / {len(story["steps"])}',font=f(17,True),fill=BLUE)
    step=story['steps'][step_i];nodes=story['nodes']
    state=updated if phase>=.85 else previous
    pts=dict(zip([x['id'] for x in nodes],positions(len(nodes))))
    if story['kind']=='workers':
        x0=190;cw=155
        d.text((30,158),'One unit',font=f(20,True),fill=INK)
        d.text((30,280),'Two units',font=f(20,True),fill=INK)
        single=min(step_i+1,4)
        parallel=0 if step_i<4 else step_i-3
        for i in range(4):
            x=x0+i*cw
            d.rectangle((x,185,x+cw-5,239),fill='#DEE5EF')
            if i<single:
                name='A' if i%2==0 else 'B'
                d.rectangle((x,185,x+cw-5,239),fill=BLUE if name=='A' else GREEN)
                d.text((x+63,196),name,font=f(24,True),fill='white')
            for j,name in enumerate(['A','B']):
                y=310+j*58
                d.rectangle((x,y,x+cw-5,y+48),fill='#DEE5EF')
                if i<parallel:
                    d.rectangle((x,y,x+cw-5,y+48),fill=BLUE if name=='A' else GREEN)
                    d.text((x+63,y+7),name,font=f(24,True),fill='white')
            d.text((x+58,423),str(i+1),font=f(16),fill=MUTED)
        d.text((190,150),'Equal CPU tasks; cells are model time units',font=f(17),fill=MUTED)
        d.text((30,422),'Time unit:',font=f(16),fill=MUTED)
    elif story['kind']=='ring':
        center=(480,278);rad=133
        pts={k:(center[0]+rad*math.sin(math.radians(a)),center[1]-rad*math.cos(math.radians(a))) for k,a in [('a',20),('b',140),('c',260),('d',200)]}
        # Ring geometry uses compact labels, keeping states outside the circle.
        d.ellipse((347,145,613,411),outline='#AAB9CC',width=3)
        for key,angle in [('K:170',170),('key:80',80)]:
            x=center[0]+rad*math.sin(math.radians(angle));y=center[1]-rad*math.cos(math.radians(angle))
            d.ellipse((x-6,y-6,x+6,y+6),fill='#BF7107')
            d.text((x+9,y-10),key,font=f(16),fill=INK)
        d.text((35,190),'Clockwise owner',font=f(17,True),fill=INK)
        for i,node in enumerate(nodes):
            val=state.get(node['id'],'')
            textblock(d,(35,220+i*43),node['label']+': '+val,f(16),285,lineheight=19,maxlines=2)
        for node in nodes:
            if node['id']=='d' and not (step_i>2 or step_i==2 and phase>=.85):
                continue
            x,y=pts[node['id']];active=node['id'] in (step['edge'] or ())
            d.ellipse((x-21,y-21,x+21,y+21),fill=BLUE if active else INK)
            d.text((x-7,y-13),node['id'].upper(),font=f(20,True),fill='white')
        if step_i in [1,4]:
            start,end=(170,260) if step_i==1 else (80,140)
            angle=math.radians(start+(end-start)*phase)
            x=center[0]+rad*math.sin(angle);y=center[1]-rad*math.cos(angle)
            d.ellipse((x-7,y-7,x+7,y+7),fill='#BF7107')
        elif step['edge']:
            a,b=[pts[k] for k in step['edge']];t=phase
            x=a[0]+(b[0]-a[0])*t;y=a[1]+(b[1]-a[1])*t
            d.ellipse((x-7,y-7,x+7,y+7),fill='#BF7107')
    elif story['kind']=='grid':
        left,top,cw,ch=105,162,150,68
        for x in range(6):d.line((left+x*cw,top,left+x*cw,top+4*ch),fill='#CBD7E6',width=2)
        for y in range(5):d.line((left,top+y*ch,left+5*cw,top+y*ch),fill='#CBD7E6',width=2)
        if step_i>=2:
            d.rectangle((left+2*cw,top+ch,left+3*cw,top+2*ch),fill='#DCEBFE',outline=BLUE,width=3)
        if step_i>=3:
            d.rectangle((left+3*cw,top+ch,left+4*cw,top+2*ch),fill='#DFF0E9',outline=GREEN,width=3)
        rider=(left+3*cw-18,top+1.5*ch);driver=(left+3*cw+18,top+1.5*ch)
        for (x,y),label,color,offset in [(rider,'Rider',BLUE,-93),(driver,'Driver',GREEN,20)]:
            d.ellipse((x-9,y-9,x+9,y+9),fill=color)
            d.text((x+offset,y+14),label,font=f(18,True),fill=INK)
        d.text((left+2*cw+12,top+ch-28),'Cell A',font=f(18,True),fill=INK)
        d.text((left+3*cw+12,top+ch-28),'Cell B',font=f(18,True),fill=INK)
        if step_i>=3:d.line((rider,driver),fill=GREEN,width=4)
    else:
        # Show only meaningful links present in the storyboard, rather than a complete graph.
        edges={tuple(s['edge']) for s in story['steps'] if s['edge']}
        for a,b in edges:
            p,q=path_points(pts[a],pts[b]);d.line((p,q),fill='#CCD7E5',width=2)
        edge=step['edge']
        if edge:
            p,q=path_points(pts[edge[0]],pts[edge[1]])
            color=RED if step['blocked'] else BLUE
            d.line((p,q),fill=color,width=4)
            t=min(phase,.52) if step['blocked'] else phase
            x=p[0]+(q[0]-p[0])*t;y=p[1]+(q[1]-p[1])*t
            d.ellipse((x-8,y-8,x+8,y+8),fill=color)
            if step['blocked']:
                mx=(p[0]+q[0])/2;my=(p[1]+q[1])/2
                d.line((mx-9,my-9,mx+9,my+9),fill=RED,width=4);d.line((mx-9,my+9,mx+9,my-9),fill=RED,width=4)
            else:
                angle=math.atan2(q[1]-p[1],q[0]-p[0]);v=12
                d.polygon([q,(q[0]-v*math.cos(angle-.45),q[1]-v*math.sin(angle-.45)),(q[0]-v*math.cos(angle+.45),q[1]-v*math.sin(angle+.45))],fill=BLUE)
        for node in nodes:
            x,y=pts[node['id']];active=node['id'] in (edge or ())
            d.rounded_rectangle((x-104,y-53,x+104,y+53),radius=13,fill='white',outline=BLUE if active else '#B9C8DC',width=3 if active else 2)
            textblock(d,(x-91,y-43),node['label'],f(19,True),182,lineheight=22,maxlines=2)
            textblock(d,(x-91,y+5),state.get(node['id'],'Ready'),f(16),182,fill=MUTED,lineheight=19,maxlines=2)
        if story['kind']=='bloom':
            bits=[0]*12
            if step_i>=1 or phase>=.85:
                for b in [1,4,8]:bits[b]=1
            for i,bit in enumerate(bits):
                x=142+i*57
                d.rectangle((x,378,x+43,412),fill=BLUE if bit else 'white',outline='#B9C8DC')
                d.text((x+15,382),str(bit),font=f(19,True),fill='white' if bit else INK)
                d.text((x+15,414),str(i),font=f(13),fill=MUTED)
    d.rounded_rectangle((24,460,936,568),radius=13,fill='white')
    textblock(d,(44,477),step['caption'],f(23),870,lineheight=29,maxlines=3)
    d.text((32,576),'Illustrative sequence; the lesson explains assumptions and tradeoffs.',font=f(14),fill=MUTED)
    return im

manifest=[]
existing={s['id']:s for s in json.loads((ROOT/'metadata/animations.json').read_text(encoding='utf-8'))} if (ROOT/'metadata/animations.json').exists() else {}
for story in stories:
    if '--only' in sys.argv and story['id']!=sys.argv[sys.argv.index('--only')+1]:
        if story['id'] in existing:manifest.append(existing[story['id']])
        continue
    if '--missing' in sys.argv and story['id'] in existing:
        manifest.append({**existing[story['id']], 'topics':story['topics']})
        continue
    frames=[];durations=[];states={n['id']:'Ready' for n in story['nodes']};stills=[]
    for i,step in enumerate(story['steps']):
        updated={**states,**step['updates']}
        for phase in [0,.2,.4,.6,.8,1.0]:
            im=frame(story,i,phase,states,updated)
            frames.append(im.quantize(colors=96,method=Image.Quantize.FASTOCTREE));durations.append(100 if phase<1 else 7000)
        stills.append(im)
        states=updated
    path=DEST/(story['id']+'.gif')
    frames[0].save(path,save_all=True,append_images=frames[1:],duration=durations,loop=0,optimize=True,disposal=2)
    # The complete still storyboard is accessible without any animation playback.
    scale=.62;tilew=int(W*scale);tileh=int(H*scale)
    board=Image.new('RGB',(tilew*2,tileh*math.ceil(len(stills)/2)),'white')
    for i,im in enumerate(stills):board.paste(im.resize((tilew,tileh),Image.Resampling.LANCZOS),((i%2)*tilew,(i//2)*tileh))
    board.save(DEST/(story['id']+'-steps.png'),optimize=True)
    static=DEST/(story['id']+'-steps.png')
    with Image.open(path) as encoded:
        encoded_count=encoded.n_frames
    word_count=lambda t:len(__import__('re').findall(r"\b[\w]+(?:['’-][\w]+)*\b",t))
    manifest.append({**story,'gif':f'assets/animations/{story["id"]}.gif','static':f'assets/animations/{story["id"]}-steps.png','duration_ms':sum(durations),'frame_count':len(frames),'encoded_frame_count':encoded_count,'gif_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'static_sha256':hashlib.sha256(static.read_bytes()).hexdigest(),'caption_words':sum(word_count(s['caption']) for s in story['steps'])})
    print(story['id'],path.stat().st_size,flush=True)
(ROOT/'metadata/animations.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print('Rendered',len(manifest),'instructional animations with still storyboards.')
