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


# DEVLOG

---

## Commit #7 – Introduce Scout Reasoning Engine

**Status:** Complete

### Summary

This milestone introduces Scout's first reasoning engine, establishing the architecture that transforms knowledge into recommendations.

Rather than placing decision-making inside the dashboard or Flask routes, Scout now relies on a dedicated reasoning layer that consumes structured knowledge and returns recommendation objects.

This commit establishes the core pipeline that future recommendation modules (festivals, trading, Wizard's Vault, activities, etc.) will use.

---

### New Components

#### Reasoning Engine

- Added `reasoning/engine.py`
- Introduced a central engine responsible for collecting recommendations from reasoning modules.
- Recommendations are prioritized before being returned to Scout.

#### Fishing Reasoning

- Added `reasoning/fishing.py`
- Implemented the first reasoning module.
- Uses the Daily Catch rotation and fish knowledge to produce today's fishing recommendation.

#### Scout

- Added `reasoning/scout.py`
- Scout now acts as the presentation layer for recommendations instead of making decisions itself.

---

### Knowledge Layer

Standardized the knowledge modules used by the reasoning engine.

Implemented:

- loader.py
- fish_species.py
- fishing_pools.py
- daily_rotation.py

---

### Architecture

Established the first complete reasoning pipeline.


This architecture separates:

- knowledge
- reasoning
- presentation

allowing new recommendation modules to be added without modifying the engine.

---

### Testing

Successfully verified:

- Flask application starts successfully.
- Knowledge loads correctly.
- Daily Catch is read correctly.
- Scout generates a recommendation.
- Recommendation reaches the dashboard.
- Invalid knowledge returns gracefully without crashing.

---

### Technical Cleanup

- Removed temporary debugging output.
- Standardized knowledge loading.
- Improved module separation.

---

### Next Milestone

Commit #8

**Enrich Fishing Recommendations**

Goals:

- Complete fish knowledge database.
- Resolve fishing pool references.
- Display fishing location, bait, time of day and preparation.
- Produce richer recommendation objects.
- Improve dashboard presentation.

## Project Milestones

- ✅ Project structure established
- ✅ Flask application created
- ✅ Knowledge layer introduced
- ✅ Scout reasoning engine implemented
- ⏳ Rich recommendation system
- ⏳ Knowledge importer
- ⏳ Trading engine
- ⏳ Festival reasoning
- ⏳ Market analysis