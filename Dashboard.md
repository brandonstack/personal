# Dashboard

## Today

`$= "**[[journal/" + dv.date("today").toFormat("yyyy") + "/" + dv.date("today").toFormat("yyyy-MM") + "/" + dv.date("today").toFormat("yyyy-MM-dd") + "|Today's Note]]** | **[[journal/" + dv.date("today").toFormat("yyyy") + "/" + dv.date("today").toFormat("yyyy-MM") + "/W" + dv.date("today").toFormat("WW") + "|This Week]]**"`

---

## Projects

```dataview
TABLE WITHOUT ID
  link(file.path, file.folder) AS "Project",
  file.mtime AS "Last Updated"
FROM "projects"
WHERE file.name = "README"
SORT file.mtime DESC
```

---

## Tasks

> [!todo] Journal
> ```dataview
> TASK
> FROM "journal"
> WHERE !completed
> LIMIT 15
> ```

> [!example]- Areas & Projects
> ```dataview
> TASK
> FROM "areas" OR "projects"
> WHERE !completed
> LIMIT 15
> ```

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
