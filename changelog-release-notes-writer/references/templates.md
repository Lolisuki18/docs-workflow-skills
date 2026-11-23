# Templates

## CHANGELOG.md section (Keep a Changelog)

```markdown
## [1.2.0] - YYYY-MM-DD

### Added
- <User-visible capability> (#123)

### Changed
- <Behavior that is different now>

### Deprecated
- <Thing> will be removed in <version, only if stated by the project>

### Removed
- <Thing removed>

### Fixed
- <Symptom that no longer happens> (#130)

### Security
- <Fixed vulnerability, described without exploit detail>

[1.2.0]: https://<host>/<owner>/<repo>/compare/v1.1.0...v1.2.0
```

Keep an `## [Unreleased]` section at the top for work not yet tagged. Omit empty groups.

## Release notes (for users)

```markdown
# <Product> <version> - <date>

## Highlights
- <1-3 changes that matter most, one sentence each>

## Upgrade notes
- **Breaking:** <what changed>. Before: `<old>`. After: `<new>`.
- **Action required:** <new env var / config key / migration command found in the diff>

## Fixes
- <Symptom, now resolved>

## Known issues
- <Only issues recorded in the tracker or the user's notes; otherwise omit this section>

Full list of changes: <link to the changelog section or compare view, if it exists>
```

## Mapping hints

| Commit signal | Section |
|---|---|
| `feat:` / new route, command or option | Added |
| `fix:` / bug label | Fixed |
| `BREAKING CHANGE:` footer, `!` after type, removed export or route | Changed or Removed, plus Upgrade notes |
| `perf:` with measurable user effect | Changed |
| dependency bump with a security advisory | Security (only when the advisory is named in the source) |
| `docs:`, `test:`, `ci:`, `chore:`, formatting | omit, unless it changes how users install or run |

## Detecting unannounced breaking changes in a diff

- Removed or renamed public functions, classes, routes, CLI flags, config keys, events.
- Changed default values, response shapes, error codes, database columns or constraints.
- Raised minimum runtime or dependency versions.
Mark each as "found in the diff" and ask the user to confirm the wording.
