# Li Xing — Senior Software Engineer

lxxdev@qq.com | 130 530 55531 | 1997-08-16

---

## Summary

7+ years of experience in software engineering, data platform, and cloud infrastructure. Proven track record at Microsoft Bing Shopping building scalable data pipelines, cloud infrastructure, and driving measurable product growth. Strong ownership and technical leadership across cross-functional teams. Promoted from L61 to L63 (Senior SWE) within 4 years; consistently rated Exceeds Expectations.

---

## Skills

- **Cloud & Infrastructure**: Azure (ADF, Synapse, Cosmos DB, Function Apps, Azure Batch, Key Vault, Service Bus, VMSS), PME/Entra ID, Azure Monitor, Geneva, Grafana, IcM
- **Data Engineering**: SCOPE, PySpark, Spark on Cosmos, ETL pipeline design, Power BI, Titan, Data Warehouse
- **Languages**: Java, Python, C#, SQL
- **Backend**: Spring Boot, Spring Cloud, Microservices
- **Security**: RBAC, Managed Identity, Secret management, SFI compliance
- **Databases**: Cosmos DB, MySQL, PostgreSQL, Oracle, Redis, ElasticSearch

---

## Experience

### Microsoft — Senior Software Engineer
**Oct 2021 – Present | Bing Shopping**

---

#### Shopping Catalog Team *(Jun 2024 – Present)*

**Price Accuracy** *(2025 – Present)*
- Optimized troubleshooting pipeline: **5x speed improvement**, near-zero failure rate (previously 10+ hrs runtime, single-failure-kills-all); extracted core API calls to Function App with retry logic
- Built product price tracking baseline via random sampling; fixed cart extraction and PDP source issues; proposed improvements for Copilot and Edge PT accuracy
- Integrated Keepa hourly dump to improve Amazon price timeliness for downstream consumers
- Analyzed IndexNow + IndexProbe + Wrapstar data to extract product/price signals from web index
- Built Cosmos VC utilization dashboard (daily scraping → Data Explorer → dashboard) serving the entire Shopping org

**Catalog Expansion** *(2024 – 2025)*
- Grew Amazon NPC from **96% to 99%** by integrating invalid offer signals (404 from IndexProbe/SFS/active crawling, MMC rejected, Keepa OOS/no-price/non-PDP URLs)
- Built active crawling pipeline with WebDriver + BrightData to proactively ingest offers
- Optimized ingestion pipeline **10x faster** by splitting large files and sorting by country
- Designed Trendy Products V2 scoring system; analyzed Edge Copilot catalog coverage

**Security & Infrastructure** *(2024)*
- Security owner for catalog team: cleared **200+ security items** inherited from 3 teams within tight timeline
- Fixed **43 over-privileged RBAC** issues; disabled local auth on 8 SQL Servers, 5 Cosmos DBs, 100+ Storage Accounts
- Applied ownership to 33 Entra ID apps; remediated app secrets across 40+ Azure Batch and AML instances — zero production disruption
- Helped recommendation team migrate AML workloads to managed identity

---

#### Buy with Microsoft Team *(Oct 2021 – Jun 2024)*

**Infrastructure & Platform**
- Led full PME tenant migration of all production Azure resources over 3+ months — **zero P1 incidents**; designed solution from scratch, resolved dependencies, coordinated with internal and external teams
- Built unified monitoring system (Grafana + Geneva + Kusto/Aria + IcM) covering backend, frontend, data pipelines, and Aether jobs; significantly reduced DSAT
- Introduced **Spark on Cosmos** and **Durable Function Apps** as team-wide standards; both widely adopted for data analysis and production batch workloads

**Data Engineering & Analytics**
- Designed and implemented E2E data warehouse integrating MSN/Bing/SLAPI logs from multiple sources; **improved team analytics productivity by 50%**
- Published data to Titan + Power BI; eliminated 2–3 day report turnaround, enabling self-serve analytics for developers, PMs, and AMs
- Managed 7 daily ETL pipelines; continuously resolved data quality issues across confirmed orders, MSN logs, PDP views, etc.
- Refactored product refresh pipeline to handle **10M feeds in under half a day**

**Growth & Product**
- Drove bi-weekly email campaigns with consistently high open/click/CVR rates; **80 orders on Cyber Monday** alone
- Onboarded **70+ sellers** to Public API; built custom product import pipeline to accelerate seller onboarding
- Grew Amazon NRT mapping rate by **~20%** by ingesting SAN Offer Mapping data to Object Store

**Technical Leadership**
- Mentored 3 teammates to independently own email campaigns, data skills, and seller API workflows
- Helped Qianqian, Shumin, and Haidi ramp up their respective areas, making the team more scalable

---

### iFLYTEK Medical — Java Software Engineer
**Jul 2018 – Apr 2021**

- Backend development for cloud medical platform serving hospitals across China (Spring Boot, Microservices, Oracle, Redis)
- Built IM/RTC integration (RongCloud) and configurable message push service for multi-platform delivery
- Developed Apache NiFi-based data exchange platform with configurable JSON/XML transformation; deployed across 3 hospital sites, significantly reducing integration effort
- Migrated legacy statistical system by introducing Kafka Streams, Apache Druid, and PostgreSQL to handle increasing data throughput

---

## Education

**Wuhan University of Technology** | B.S. Software Engineering | Sep 2014 – Jul 2018

