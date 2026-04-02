# Dashboard

## Today

**[[journal/daily/<% tp.date.now("YYYY-MM-DD") %>|Today's Note]]** | [[journal/weekly/<% tp.date.now("YYYY-[W]ww") %>|This Week]]

---

## Inbox

> [!info] Unprocessed
> ```dataview
> TABLE source, date, tags
> FROM "inbox"
> WHERE status = "raw"
> SORT date DESC
> LIMIT 15
> ```

**Total unprocessed:**
```dataview
LIST length(rows) AS "count"
FROM "inbox"
WHERE status = "raw"
GROUP BY true
```

---

## Projects

```dataview
TABLE WITHOUT ID
  link(file.path, file.name) AS "Project",
  file.mtime AS "Last Updated"
FROM "projects"
WHERE file.name = "README"
SORT file.mtime DESC
```

---

## Tasks

```dataview
TASK
FROM "areas" OR "projects" OR "journal"
WHERE !completed
LIMIT 20
```

---

## Recent Changes

```dataview
TABLE WITHOUT ID
  link(file.path, file.name) AS "File",
  file.folder AS "Folder",
  file.mtime AS "Modified"
FROM ""
WHERE file.name != "Dashboard"
SORT file.mtime DESC
LIMIT 10
```
