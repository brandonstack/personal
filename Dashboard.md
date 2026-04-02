# Dashboard

## Today

`$= "**[[journal/daily/" + dv.date("today").toFormat("yyyy-MM-dd") + "|Today's Note]]** | **[[journal/weekly/" + dv.date("today").toFormat("yyyy-'W'WW") + "|This Week]]**"`

---

## Inbox

> [!info] Unprocessed
> ```dataview
> TABLE source, date, tags
> FROM "inbox"
> SORT date DESC
> LIMIT 15
> ```

**Total unprocessed:**
`$= dv.pages('"inbox"').length`

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
