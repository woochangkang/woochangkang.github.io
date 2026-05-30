# scripts/

## sync_publications.py
Incrementally adds the author's Zotero journal articles that are **not yet**
in `_publications/`. Existing files are never modified.

```bash
python scripts/sync_publications.py --dry-run   # preview new papers
python scripts/sync_publications.py             # write new _publications files
```

- Identifies the author by creator name (`Woo Chang Kang` / `강우창`).
- Maps Zotero fields → front matter (title, authors with own name bolded,
  venue, volume/issue/pages, year, DOI/URL, `language` → English/Korean,
  abstract → body for Korean, `English Title:` in Zotero **Extra** → `title_en`).
- New files get `tags: []` — add topic tags by hand, then they show under the
  Publications topic filter.

Credentials: `ZOTERO_USER_ID` / `ZOTERO_API_KEY` from env (or `~/.claude/settings.json`).

Automation: `.github/workflows/sync-publications.yml` runs this weekly /
on-demand. Add `ZOTERO_USER_ID` and `ZOTERO_API_KEY` as repository secrets.
