[← Category](README.md) · [Schedule](../../SCHEDULE.md)

> **Reading note:** some statements in the preserved passage need clarification. Read [Make it concrete](#make-it-concrete) with it.

<!-- BEGIN INQUIRY -->
## Try solving this first

Checkout responds quickly but sometimes returns errors. What counts as success? Which measured percentage would show whether the service meets its promise?
<!-- END INQUIRY -->

<!-- BEGIN ORIGINAL TOPIC -->
# SLA, SLO, SLI

Let's briefly discuss SLA, SLO, and SLI. These are mostly related to the business and site reliability side of things but good to know nonetheless.

## Why are they important?

SLAs, SLOs, and SLIs allow companies to define, track and monitor the promises made for a service to its users. Together, SLAs, SLOs, and SLIs should help teams generate more user trust in their services with an added emphasis on continuous improvement to incident management and response processes.

## SLA

An SLA, or Service Level Agreement, is an agreement made between a company and its users of a given service. The SLA defines the different promises that the company makes to users regarding specific metrics, such as service availability.

_SLAs are often written by a company's business or legal team._

## SLO

An SLO, or Service Level Objective, is the promise that a company makes to users regarding a specific metric such as incident response or uptime. SLOs exist within an SLA as individual promises contained within the full user agreement. The SLO is the specific goal that the service must meet in order to comply with the SLA. SLOs should always be simple, clearly defined, and easily measured to determine whether or not the objective is being fulfilled.

## SLI

An SLI, or Service Level Indicator, is a key metric used to determine whether or not the SLO is being met. It is the measured value of the metric described within the SLO. In order to remain in compliance with the SLA, the SLI's value must always meet or exceed the value determined by the SLO.
<!-- END ORIGINAL TOPIC -->

## Make it concrete

SLI is the measurement; SLO the target; SLA an agreement that may specify consequences.

For checkout, count correct purchases within a latency threshold over a defined window. Ten failures among 10,000 requests means 99.9% success. An error budget is the permitted failure allowance. Prioritize dominant user-visible failures.

In that example, requests that return an error are not rescued by a fast response time. If the success definition also requires completion within a deadline, a correct but excessively late purchase can count as unsuccessful. State which requests are eligible and avoid changing the denominator simply to improve the reported number.

The error budget expresses how much failure the chosen objective allows in its measurement window. It is a planning signal, not permission to harm customers. Teams can use it to decide whether operational reliability needs attention before adding more risky changes.

An SLA may contain contractual consequences; an internal SLO can be stricter or cover additional user journeys. Measure what the user needs rather than assuming every process must be up for every feature to work.

[Next topic in this category](README.md) · [Credits and license](../../ATTRIBUTION.md)
