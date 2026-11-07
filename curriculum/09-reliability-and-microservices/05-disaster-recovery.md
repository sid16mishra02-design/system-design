[← Category](README.md) · [Schedule](../../SCHEDULE.md)

<!-- BEGIN ORIGINAL TOPIC -->
# Disaster recovery

Disaster recovery (DR) is a process of regaining access and functionality of the infrastructure after events like a natural disaster, cyber attack, or even business disruptions.

Disaster recovery relies upon the replication of data and computer processing in an off-premises location not affected by the disaster. When servers go down because of a disaster, a business needs to recover lost data from a second location where the data is backed up. Ideally, an organization can transfer its computer processing to that remote location as well in order to continue operations.

_Disaster Recovery is often not actively discussed during system design interviews but it's important to have some basic understanding of this topic. You can learn more about disaster recovery from [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-for-disaster-recovery-dr.html)._

## Why is disaster recovery important?

Disaster recovery can have the following benefits:

- Minimize interruption and downtime
- Limit damages
- Fast restoration
- Better customer retention

## Terms

Let's discuss some important terms relevantly for disaster recovery:

![disaster-recovery](https://raw.githubusercontent.com/karanpratapsingh/portfolio/master/public/static/courses/system-design/chapter-IV/disaster-recovery/disaster-recovery.png)

### RTO

Recovery Time Objective (RTO) is the maximum acceptable delay between the interruption of service and restoration of service. This determines what is considered an acceptable time window when service is unavailable.

### RPO

Recovery Point Objective (RPO) is the maximum acceptable amount of time since the last data recovery point. This determines what is considered an acceptable loss of data between the last recovery point and the interruption of service.

## Strategies

A variety of disaster recovery (DR) strategies can be part of a disaster recovery plan.

### Back-up

This is the simplest type of disaster recovery and involves storing data off-site or on a removable drive.

### Cold Site

In this type of disaster recovery, an organization sets up basic infrastructure in a second site.

### Hot site

A hot site maintains up-to-date copies of data at all times. Hot sites are time-consuming to set up and more expensive than cold sites, but they dramatically reduce downtime.
<!-- END ORIGINAL TOPIC -->

## Make it concrete

### Test recovery, not just backup creation

With successful hourly backups and no newer recoverable log, possible data loss is roughly an hour: RPO. Restoring service within two hours concerns RTO.

Choose targets from business loss tolerance. Rehearse restoring data, application configuration, credentials, and traffic routing in an isolated recovery exercise. Measure when users can work again, not when files finish copying. Faster restore automation improves RTO; more frequent recoverable data capture improves RPO. Protect backups from the same accidental deletion or compromise affecting production.

**Check:** can you prove the last backup is restorable?

[Next topic in this category](README.md) · [Credits and license](../../ATTRIBUTION.md)
