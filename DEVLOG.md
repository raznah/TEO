# Commit History

## Commit #1
Date: 2026-07-15

Title:
Initial TEO project foundation

Highlights:
- Project structure
- Vision
- Architecture
- Flask
- First working application

---

## Commit #2

Title:
Refactor Flask application structure

Highlights:
- Jinja templates
- Base template
- CSS support
- Application package finalized
- Template resolution fixed

## Commit #3

### Title

Create initial dashboard experience

### Highlights

- Integrated Bootstrap
- Established TEO visual identity
- Introduced reusable dashboard panels
- Added Recommendation Panel
- Added Festival Panel
- Replaced project status with player-focused content

### Lessons Learned

Bootstrap provides an excellent structural foundation.

TEO's own CSS defines the application's identity.

The dashboard should communicate purpose before functionality.

### Milestone

Implemented the first Knowledge Engine component.

The Festival Engine successfully loads application resources from
`teo/resources/festivals.json`.

This establishes the architectural pattern that future modules will follow.

# Development Log

---

## 2026-07-15

### Commit #4 – Implement Festival Knowledge Engine

Today Scout learned to answer two important questions:

- Is a festival active today?
- If not, which festival comes next?

The Festival dashboard is now driven by Scout's Knowledge Engine instead of placeholder text. Festival and location links now open the Guild Wars 2 Wiki, allowing players to quickly find event details and travel information.

### Reflection

Scout answered his first real question and, for the first time, TEO became driven by knowledge instead of placeholder text.