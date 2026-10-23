# Learning journal

## Week 1 (Oct 12-17): Docker foundations
- Built a FastAPI service with a /health endpoint.
- Dockerfile: multi-stage build, non-root user, .dockerignore.
- docker-compose with PostgreSQL and MongoDB; secrets in .env (not in Git).
- Blockers: GitHub authentication (solved with gh), port 5432 already in use (solved by using 5433).
- What I learned: ...

## Week 2 (Oct 19-25): HBase and AWS theory

### Memory measurement of the stack (at rest, Oct 23)

| Service | Memory |
|---|---|
| HBase | 542.6 MiB |
| MongoDB | 299.4 MiB |
| config-service | 36.5 MiB |
| PostgreSQL | 32.3 MiB |

Total: 910.8 MiB. HBase is about 60% of the total.
Conclusion: HBase is the heaviest service (JVM, 326 PIDs), so it will need the
largest memory request in Kubernetes (phase 5). To measure again on Saturday,after writing data.


### HBase persistence test
After `docker compose down` / `up`, `list` returned no table at first.
Cause: HBase answers before it has finished recovering (about 1-2 minutes).
Checked: the volume was mounted on /data and hbase.rootdir pointed to it.
Rule: wait (or check readiness) before reading from HBase after a start.




